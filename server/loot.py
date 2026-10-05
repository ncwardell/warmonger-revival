"""Loot: what a monster drops when it dies, and getting it into the bag.

The client has NO ground-item object: no S->C opcode spawns an item in the world,
no C->S opcode picks one up, and no drop/loot/field-item class exists in the binary
(see out/spec/monsters.md, "Loot"). What it does have is the acquisition path:

  - 0x427 single slot update with reason 0x46 into container 1 (bag), extra = own uid.
    FUN_00478d54 stores the 16-byte item at bag slot +0x14, highlights the slot,
    pops the ItemPickupMessage panel (0x3e) with "You acquired <name>" /
    "<name> x N" (StringAll Item_pickup / Item_pickup2; N = new count - old count
    when the slot already held the same code) and, because reason != 0, also
    prints system message 70 StrDef_GetItem ("You acquired an <item>").
  - 0x428 field 2 = gold (char+0x283): +0x10 u16 reason 0, +0x12 u16 2,
    +0x14 u32 new total. No popup (reason 6 is the nation-pay text).
  - 0x41b system message 36 StrDef_InventoryIsFull when the bag has no room.

So "ground" drops live only on the server: on_kill() rolls the drop table and
lays the items at the corpse; anything within KILL_PICKUP_RADIUS of the player is
collected at once (auto-loot, which is what the player sees), the rest (bag full,
killed from far away) stays for DESPAWN_SECONDS and is picked up by walking
within WALK_PICKUP_RADIUS (tick) or by a 0x451 interact on the corpse.

The quest drops are client data: Quest.cdb kill-and-collect objectives
{type 1, unit, count, rate %, item} (quest 631: 3 x Slime 604 -> 100 % 2550
Slime Mucus; 632: 5 x Bee 731 -> 2552 Bee Needle, 5 x Cobra 732 -> 2551 Snake
Leather). Gold and the extra materials are server data the client never had;
EXTRA_DROPS below is our choice, with real Item_Base codes.

handlers.py wires this in:
  - GAME_REPLIES.update(loot.REPLIES)   (0x451; returns None unless it is a corpse with loot)
  - tick(): out += loot.tick(time.monotonic())
world.deaths() calls on_kill(unit) for each kill.
"""
import pathlib

import paths
import sessions
import random
import struct
import sys
import time

import skills
from proto import build


def log(*args):
    print(time.strftime("%H:%M:%S"), "[loot]", *args, flush=True)


clock = time.monotonic  # replaced by the self-test

GOLD = 1003  # Item_Base "Gold" pseudo-item: a ground drop of this code is money
REASON_GET_ITEM = 0x46  # 0x427 reason: pickup popup + system message 70 StrDef_GetItem
MSG_INVENTORY_FULL = 36  # system_msg.cdb StrDef_InventoryIsFull
FIELD_GOLD = 2  # 0x428 field: char+0x283
STACK_MAX = 99  # item +4 is a signed char; the client shows count only for stackable types

KILL_PICKUP_RADIUS = 12.0  # auto-loot on kill: ranged weapons reach 7 units
WALK_PICKUP_RADIUS = 3.0  # walking over leftovers
INTERACT_RADIUS = 15.0  # 0x451 on a corpse; loose on purpose
DESPAWN_SECONDS = 60.0
SCATTER = 0.8  # drops land up to this far from the corpse

# Quest kill-and-collect objectives from Quest.cdb: unit -> [(item, rate %, count)].
# This fallback is what the loader finds for the tutorial; load_quest_drops() adds the rest.
QUEST_DROPS = {
    604: [(2550, 100, 3)],  # Slime -> Slime Mucus (quest 631 "The Slime is mine")
    731: [(2552, 100, 5)],  # Bee -> Bee Needle (quest 632)
    732: [(2551, 100, 5)],  # Cobra -> Snake Leather (quest 632)
}

# Ours: unit -> (gold min, gold max, [(item, chance 0..1, min, max)]).
EXTRA_DROPS = {
    604: (2, 5, [(839, 0.10, 1, 1)]),  # Slime: Wild herb
    732: (3, 8, [(611, 0.05, 1, 1), (839, 0.10, 1, 1)]),  # Cobra: Red Passion Fragments [D]
    731: (4, 10, [(601, 0.05, 1, 1), (839, 0.10, 1, 1)]),  # Bee: Blue Passion Fragments [D]
    605: (20, 40, [(2550, 1.0, 2, 3), (692, 0.25, 1, 1),  # Great Slime: Mucus, Gem Stone: Blue,
                   (601, 0.15, 1, 1), (611, 0.15, 1, 1)]),  # Blue/Red Passion Fragments [D]
}
NO_STACK = {692}  # gem stones: one per slot to be safe
DEFAULT_GOLD = (1, 3)  # any other monster


def load_quest_drops(path=paths.SETTING / "Quest.cdb"):
    """Add every Quest.cdb kill-and-collect objective to QUEST_DROPS.

    Each objective is 10 fields before its Quest_QuickText key:
    type, unit, count, rate %, item, 0, map x3, 0. Type 1 with an item is a drop.
    """
    try:
        tokens = path.read_bytes().split(b"\0")
    except OSError:
        return
    n = int(tokens[0])
    width = (len(tokens) - 4) // n
    for i in range(n):
        row = [t.decode("latin1") for t in tokens[2 + i * width:2 + (i + 1) * width]]
        for j, field in enumerate(row):
            if not field.startswith("Quest_QuickText") or j < 10:
                continue
            kind, unit, count, rate, code = row[j - 10:j - 5]
            if kind == "1" and code.isdigit() and int(code) and int(rate) > 0:
                drops = QUEST_DROPS.setdefault(int(unit), [])
                entry = (int(code), int(rate), int(count))
                # 26xx rows repeat 25xx objectives for another quest line; keep one.
                if all(d[0] not in (entry[0], entry[0] - 100) for d in drops):
                    drops.append(entry)


load_quest_drops()


class Drop:
    """An item (or gold) lying where a monster died. Server-side only."""

    def __init__(self, uid, code, count, x, z, source, expires):
        self.uid, self.code, self.count = uid, code, count
        self.x, self.z, self.source, self.expires = x, z, source, expires
        self.warned = False  # bag-full message sent once

    def __repr__(self):
        return f"<drop 0x{self.uid:x} {self.code} x{self.count} ({self.x:.0f},{self.z:.0f})>"


GROUND = globals().get("GROUND", {})  # fallback drop uid -> Drop
STATE = globals().get("STATE", {"gold": 0, "next_uid": 0x3000})


def state():
    session = sessions.current()
    return session.loot if session is not None else STATE


def ground():
    session = sessions.current()
    return session.drops if session is not None else GROUND


def set_gold(amount):
    """The player's current gold (slot record +0x80 = char+0x283); call on enter world."""
    state()["gold"] = amount


# ---------------------------------------------------------------- rolling


def quest_cap(code):
    """How many of a quest item are worth holding (largest objective count), else None."""
    caps = [c for drops in QUEST_DROPS.values() for i, _, c in drops if i == code]
    return max(caps) if caps else None


def held(code):
    bag, counts = skills.state()["bag"], skills.state().setdefault("count", [0] * skills.BAG_SLOTS)
    return sum((counts[s] or 1) for s, c in enumerate(bag) if c == code)


def roll(unit_id, rng=random):
    """[(code, count)] one kill of `unit_id` drops; gold as (GOLD, amount)."""
    out = []
    for code, rate, _ in QUEST_DROPS.get(unit_id, ()):
        cap = quest_cap(code)
        if rng.random() * 100 < rate and (cap is None or held(code) < cap):
            out.append((code, 1))
    lo, hi, extras = EXTRA_DROPS.get(unit_id, (*DEFAULT_GOLD, []))
    for code, chance, n_min, n_max in extras:
        if rng.random() < chance:
            out.append((code, rng.randint(n_min, n_max)))
    if hi:
        out.append((GOLD, rng.randint(lo, hi)))
    return out


# ---------------------------------------------------------------- packets


def player_uid():
    if sessions.current() is not None:
        return sessions.current().uid
    world = sys.modules.get("world")
    return getattr(world, "PLAYER", {}).get("uid", 1) if world else 1


def player_pos():
    """(x, z) of the player from handlers.PLAYER, or None when unknown."""
    session = sessions.current()
    handlers = sys.modules.get("handlers")
    p = session.player if session is not None else getattr(handlers, "PLAYER", None)
    if not p or not p.get("in_world"):
        return None
    return p["x"], p["z"]


def slot_update(slot, reason=REASON_GET_ITEM):
    """0x427 (0x28 bytes, extra = own uid): +0x10 u16 reason | +0x12 u16 container 1 |
    +0x14 u16 slot | +0x18 16-byte item (+0 u16 code, +4 u8 count)."""
    code = skills.state()["bag"][slot]
    count = skills.state()["count"][slot] or 1
    payload = struct.pack("<HHHH", reason, skills.BAG, slot, 0) + skills.item(code, count)
    return build(0x427, payload, extra=player_uid())


def gold_update():
    """0x428 (0x1c bytes, extra = own uid): +0x10 u16 reason 0 | +0x12 u16 field 2 (gold) |
    +0x14 u32 new total | +0x18 u32 0."""
    return build(0x428, struct.pack("<HHII", 0, FIELD_GOLD, state()["gold"], 0), extra=player_uid())


def system_message(msg_id, param=0):
    """0x41b (0x18 bytes): +0x10 u32 system_msg.cdb id | +0x14 u32 parameter."""
    return build(0x41B, struct.pack("<II", msg_id, param), extra=player_uid())


def add_to_bag(code, count):
    """Put `count` x `code` into the bag (stacks first, then empty slots).

    Returns (slots touched, count left over); a partial fit stores what fits.
    """
    bag, counts = skills.state()["bag"], skills.state().setdefault("count", [0] * skills.BAG_SLOTS)
    cap = 1 if code in NO_STACK else STACK_MAX
    touched = []
    for slot, held_code in enumerate(bag):
        if count and held_code == code and (counts[slot] or 1) < cap:
            room = cap - (counts[slot] or 1)
            n = min(room, count)
            counts[slot] = (counts[slot] or 1) + n
            count -= n
            touched.append(slot)
    for slot, held_code in enumerate(bag):
        if count and not held_code:
            n = min(cap, count)
            bag[slot], counts[slot] = code, n
            count -= n
            touched.append(slot)
    return touched, count


def collect(drop):
    """Move one drop into the player's bag / purse. Returns packets; removes it when done."""
    if drop.code == GOLD:
        state()["gold"] += drop.count
        del ground()[drop.uid]
        log(f"picked up {drop.count} gold (now {state()['gold']})")
        return gold_update()
    touched, left = add_to_bag(drop.code, drop.count)
    out = b"".join(slot_update(s) for s in touched)
    if left:
        drop.count = left
        if not drop.warned:
            drop.warned = True
            log(f"bag full: {drop} stays on the ground")
            out += system_message(MSG_INVENTORY_FULL)
    else:
        del ground()[drop.uid]
        log(f"picked up {drop.code} x{drop.count} into slot(s) {touched}")
    return out


def near(drop, pos, radius):
    return pos is None or (drop.x - pos[0]) ** 2 + (drop.z - pos[1]) ** 2 <= radius * radius


def collect_near(pos, radius, source=None):
    out = b""
    for drop in list(ground().values()):
        if (source is None or drop.source == source) and near(drop, pos, radius):
            out += collect(drop)
    return out


# ---------------------------------------------------------------- entry points


def on_kill(unit, rng=random):
    """Roll `unit`'s drops onto the ground at its corpse; auto-loot what is in reach.

    Returns the 0x427 / 0x428 packets for what the player collected (b"" if none).
    """
    now = clock()
    for code, count in roll(unit.unit_id, rng):
        uid = state()["next_uid"]
        state()["next_uid"] = 0x3000 + (uid - 0x3000 + 1) % 0x1000
        x = unit.x + rng.uniform(-SCATTER, SCATTER)
        z = unit.z + rng.uniform(-SCATTER, SCATTER)
        ground()[uid] = Drop(uid, code, count, x, z, unit.uid, now + DESPAWN_SECONDS)
        log(f"{unit.name} 0x{unit.uid:x} dropped {ground()[uid]}")
    return collect_near(player_pos(), KILL_PICKUP_RADIUS, source=unit.uid)


def tick(now=None):
    """Despawn drops past their time; pick up what the player walks over. Bytes (maybe b"")."""
    now = clock() if now is None else now
    for drop in list(ground().values()):
        if now >= drop.expires:
            log(f"despawned {drop}")
            del ground()[drop.uid]
    pos = player_pos()
    if pos is None or not ground():
        return b""
    return collect_near(pos, WALK_PICKUP_RADIUS)


def interact(packet):
    """C->S 0x451 (0x18 bytes): +0x10 u16 target, +0x12 u16 kind (2 = unit), +0x14 u16 state.

    Interacting with a corpse that still has loot picks it all up. Anything else is not
    ours: None (no ack is needed for 0x451).
    """
    if len(packet) < 0x18:
        return None
    target, kind, state = struct.unpack_from("<HHH", packet, 0x10)
    if kind != 2 or state != 1 or not any(d.source == target for d in ground().values()):
        return None
    return collect_near(player_pos(), INTERACT_RADIUS, source=target) or None


REPLIES = {
    0x0451: interact,
}


# ---------------------------------------------------------------- self-test

if __name__ == "__main__":
    from proto import HEADER, split

    class FakeUnit:
        def __init__(self, uid, unit_id, name, x=100.0, z=100.0):
            self.uid, self.unit_id, self.name, self.x, self.z = uid, unit_id, name, x, z

    def ops(data):
        packets, rest = split(data)
        assert not rest
        for p in packets:
            assert 16 < len(p) == struct.unpack_from("<H", p)[0]
        return [(struct.unpack_from("<H", p, 4)[0], p) for p in packets]

    now = [500.0]
    clock = lambda: now[0]  # noqa: E731
    rng = random.Random(7)

    # Data: the tutorial objectives come from Quest.cdb (or the fallback).
    assert (2550, 100, 3) in QUEST_DROPS[604] and (2551, 100, 5) in QUEST_DROPS[732]
    assert (2552, 100, 5) in QUEST_DROPS[731]
    assert quest_cap(2550) >= 3

    skills.STATE["bag"][:] = [0] * skills.BAG_SLOTS
    skills.STATE["count"] = [0] * skills.BAG_SLOTS
    skills.STATE["bag"][0] = 10011  # a weapon already in slot 0

    # A slime dies next to the (unknown-position) player: everything is auto-looted.
    out = ops(on_kill(FakeUnit(0x400, 604, "Slime"), rng))
    codes = [op for op, _ in out]
    assert 0x427 in codes and codes[-1] == 0x428, codes
    p = [q for op, q in out if op == 0x427][0]  # quest item first
    reason, container, slot = struct.unpack_from("<HHH", p, 0x10)
    assert (reason, container, slot) == (0x46, 1, 1)
    assert struct.unpack_from("<HxxB", p, 0x18) == (2550, 1) and len(p) == 0x28
    g = dict(out)[0x428]
    assert len(g) == 0x1C and struct.unpack_from("<HHI", g, 0x10) == (0, 2, STATE["gold"]) and STATE["gold"] >= 2
    assert not GROUND

    # Second slime: Mucus stacks onto slot 1 (count 2, the popup shows "x 1").
    out = ops(on_kill(FakeUnit(0x401, 604, "Slime"), rng))
    p = [q for op, q in out if op == 0x427 and struct.unpack_from("<H", q, 0x18)[0] == 2550][0]
    assert struct.unpack_from("<H", p, 0x14)[0] == 1 and p[0x1C] == 2
    on_kill(FakeUnit(0x402, 604, "Slime"), rng)
    assert held(2550) == 3
    # Quest cap reached (3): a fourth slime drops no more Mucus.
    on_kill(FakeUnit(0x400, 604, "Slime"), rng)
    assert held(2550) == 3

    # Player known and far away: drops stay, walking over them collects them.
    sys.modules["handlers"] = type(sys)("handlers")
    sys.modules["handlers"].PLAYER = {"uid": 1, "x": 0.0, "z": 0.0, "in_world": True}
    assert on_kill(FakeUnit(0x403, 732, "Cobra"), rng) == b""
    assert GROUND and all(d.source == 0x403 for d in GROUND.values())
    assert tick(now[0]) == b""
    sys.modules["handlers"].PLAYER.update(x=100.0, z=100.0)
    out = ops(tick(now[0]))
    assert 0x428 in [op for op, _ in out] and held(2551) == 1 and not GROUND

    # 0x451 interact on a corpse with loot picks it up; on anything else -> None.
    sys.modules["handlers"].PLAYER.update(x=113.0, z=100.0)  # 13 units: past auto-loot, inside interact
    on_kill(FakeUnit(0x404, 731, "Bee"), rng)
    assert GROUND and tick(now[0]) == b""
    req = HEADER.pack(0x18, 0xA53C, 0x451, 1, 0, 0) + struct.pack("<HHHH", 0x404, 2, 1, 0)
    assert 0x427 in [op for op, _ in ops(interact(req))] and not GROUND and held(2552) == 1
    assert interact(req) is None
    assert interact(HEADER.pack(0x18, 0xA53C, 0x451, 1, 0, 0) + struct.pack("<HHHH", 7, 1, 1, 5)) is None

    # Bag full: the leftover stays on the ground with one 0x41b 36, then despawns.
    skills.STATE["bag"][:] = [9999] * skills.BAG_SLOTS
    sys.modules["handlers"].PLAYER.update(x=100.0, z=100.0)
    out = ops(on_kill(FakeUnit(0x405, 605, "Great Slime"), rng))
    msgs = [q for op, q in out if op == 0x41B]
    assert len(msgs) >= 1 and struct.unpack_from("<I", msgs[0], 0x10)[0] == 36
    assert GROUND and all(d.code != GOLD for d in GROUND.values())  # gold always fits
    assert tick(now[0]) == b""  # still full: no repeat of the message
    now[0] += DESPAWN_SECONDS
    tick(now[0])
    assert not GROUND

    # Drop-rate sanity over many kills (quest cap lifted by emptying the bag each time).
    skills.STATE["bag"][:] = [0] * skills.BAG_SLOTS
    tally = {}
    for _ in range(2000):
        for code, n in roll(731, rng):
            tally[code] = tally.get(code, 0) + 1
    assert tally[2552] == 2000 and tally[GOLD] == 2000 and 40 < tally.get(601, 0) < 180
    print("ok:", {k: v for k, v in sorted(tally.items())}, "gold", STATE["gold"])

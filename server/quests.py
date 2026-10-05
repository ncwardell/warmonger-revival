"""Small tutorial quest experiment, using the player's own Quest.cdb.

Packet evidence: contract/quests.yaml (0x48e..0x492, FUN_00599ab2).
Only rows 1..4 and their talk/kill/collect objectives and NPC handoff are enabled. Unknown
quests or objective/reward types are rejected, never silently completed.
"""
import copy
import math
import struct

import loot
import paths
import sessions
import world
from proto import build


def rows(name):
    try:
        tokens = (paths.SETTING / name).read_bytes().split(b"\0")
    except FileNotFoundError:
        return []
    count = int(tokens[0])
    if not count or (len(tokens) - 4) % count:
        raise ValueError(f"invalid table shape: {name}")
    width = (len(tokens) - 4) // count
    return [tokens[2 + i * width:2 + (i + 1) * width] for i in range(count)]


def definitions():
    result = {}
    for row in rows("Quest.cdb"):
        qid = int(row[0])
        if qid not in (1, 2, 3, 4):
            continue
        objectives = [tuple(int(v) for v in row[i:i + 5]) for i in range(56, 111, 11)]
        rewards = [tuple(int(v) for v in row[i:i + 4]) for i in range(111, 141, 6)]
        if any(o[0] not in (0, 1, 4) for o in objectives) or any(r[0] not in (0, 1, 2, 4) for r in rewards):
            continue
        result[qid] = {"id": qid, "bit": int(row[5]), "prerequisite": int(row[3]),
                       "exclusion": int(row[4]), "maps": tuple(map(int, row[7:10])),
                       "giver": int(row[10]), "receiver": int(row[17]),
                       # Row 13 -> definition +0x11 (loader 0x43e7f0).
                       # No receiver NPC/gadget means the client cannot offer a
                       # turn-in marker (0x59925d..0x5992ab). Treat this flag as
                       # automatic completion for the supported tutorial slice.
                       "automatic": bool(int(row[13])) and not int(row[17]) and not int(row[18]),
                       "stages": tuple(map(int, row[51:56])), "objectives": objectives,
                       "rewards": rewards}
    return result


DEFINITIONS = definitions()
LEVELS = {int(row[0]): int(row[1]) for row in rows("Level_Table.cdb")}


def level_for_experience(experience, current_level=1):
    """Row L is the total XP needed to leave level L, not to enter it.

    Client XP display 0x57d223..0x57d28e uses rows L-1 and L as the
    lower/upper bounds. Keep earned XP intact and tolerate absent game data.
    """
    level = current_level
    cap = min(30, max(LEVELS, default=current_level))
    while level < cap and level in LEVELS and experience >= LEVELS[level]:
        level += 1
    return level


def refresh_level():
    """Repair an older session's level once, without granting additional XP."""
    s = sessions.current()
    level = level_for_experience(s.experience, s.level)
    if level == s.level:
        return b""
    s.level = level
    return build(0x422, struct.pack("<BBHI", level, 1, 0, s.experience), extra=s.uid)


def near_npc(template):
    p = sessions.current().player
    return any(u.unit_id == template and math.hypot(p["x"] - u.x, p["z"] - u.z) <= 15
               for u in world.UNITS.values() if not world.is_monster(u))


def allowed(q):
    s = sessions.current()
    # Prototype nation is 1; other nations need their own map/scene setup.
    return s.player["alive"] and q["maps"][0] in (0, s.player["map"])


def apply_to_world(packet):
    s = sessions.current()
    packet[0x524:0x68C] = b"".join(s.quest_slots)
    packet[0x68C:0x6B4] = s.quest_flags.to_bytes(40, "little")


def update(slot, notify=0):
    s = sessions.current()
    packet = bytearray(0x5C)
    packet[0x10], packet[0x11] = slot, notify
    packet[0x14:0x3C] = s.quest_flags.to_bytes(40, "little")
    packet[0x44:0x5C] = s.quest_slots[slot]
    return build(0x491, bytes(packet[16:]), extra=s.uid)


def active(q, record):
    first = next((i for i in range(5) if not record[8 + i]), 5)
    return q["stages"][first] if first < 5 else 5


def ready(q, record):
    record[2] = 2 if all(not o[0] or record[8 + i] for i, o in enumerate(q["objectives"])) else 0


def accept_or_abandon(packet):
    s = sessions.current()
    notice, action, slot, qid = struct.unpack_from("<HhHH", packet, 0x10)
    q = DEFINITIONS.get(qid)
    if not q or notice or not allowed(q):
        return None
    if action == 2:
        if slot < 15 and struct.unpack_from("<H", s.quest_slots[slot])[0] == qid:
            s.quest_slots[slot] = bytes(24)
            return update(slot)
        return None
    if action != 1 or not near_npc(q["giver"]):
        return None
    flags = s.quest_flags
    if (flags & (1 << q["bit"]) or (q["prerequisite"] and not flags & (1 << q["prerequisite"]))
            or (q["exclusion"] and flags & (1 << q["exclusion"]))
            or any(struct.unpack_from("<H", r)[0] == qid for r in s.quest_slots)):
        return None
    slot = next((i for i, r in enumerate(s.quest_slots) if not any(r)), None)
    if slot is None:
        return None
    record = bytearray(24)
    struct.pack_into("<H", record, 0, qid)
    ready(q, record)
    s.quest_slots[slot] = bytes(record)
    return update(slot) + collect_progress()


def objective_report(packet):
    s = sessions.current()
    slot, qid, target, index, kind = struct.unpack_from("<HHHhi", packet, 0x10)
    q = DEFINITIONS.get(qid)
    if not q or not allowed(q) or not 0 <= slot < 15 or not 0 <= index < 5:
        return None
    record = bytearray(s.quest_slots[slot])
    if struct.unpack_from("<H", record)[0] != qid or record[8 + index] or index >= active(q, record):
        return None
    objective = q["objectives"][index]
    if kind != 4 or objective[0:2] != (4, target) or not near_npc(target):
        return None
    record[8 + index] = 1
    struct.pack_into("<h", record, 14 + index * 2, 1)
    ready(q, record)
    s.quest_slots[slot] = bytes(record)
    return update(slot) + finish_automatic()


def collect_progress(killed_unit=None):
    """Count authoritative kills or held quest items; never trust a client kill report."""
    s = sessions.current()
    if s is None:
        return b""
    out = b""
    for slot, old in enumerate(s.quest_slots):
        q = DEFINITIONS.get(struct.unpack_from("<H", old)[0])
        if not q or not allowed(q):
            continue
        record = bytearray(old)
        for i in range(active(q, record)):
            kind, unit, required, rate, item = q["objectives"][i]
            if kind != 1:
                continue
            value = struct.unpack_from("<h", record, 14 + i * 2)[0]
            value = loot.held(item) if item else value + int(unit == killed_unit)
            value = min(value, required, 32767)
            record[8 + i] = int(value >= required)
            struct.pack_into("<h", record, 14 + i * 2, value)
        ready(q, record)
        if record != old:
            s.quest_slots[slot] = bytes(record)
            out += update(slot)
    return out


def finish_automatic():
    """Finish earned zero-receiver quests, including an older saved ready state.

    Never infer a conversation just from being near the NPC: the objective must
    already have been validated and persisted as ready. Only enabled definitions
    with the automatic flag and no receiver can take this path.
    """
    s = sessions.current()
    out = b""
    for slot, record in enumerate(s.quest_slots):
        q = DEFINITIONS.get(struct.unpack_from("<H", record)[0])
        if (q and q.get("automatic", False) and not q["receiver"]
                and allowed(q) and record[2] == 2):
            out += finish(slot, q) or b""
    return out


def turn_in(packet):
    s = sessions.current()
    qid, slot, choice = struct.unpack_from("<HHh", packet, 0x10)
    q = DEFINITIONS.get(qid)
    if (not q or not allowed(q) or slot >= 15 or choice != 0
            or not q["receiver"] or not near_npc(q["receiver"])):
        return None
    before = collect_progress()
    return before + (finish(slot, q) or b"") or None


def finish(slot, q):
    """One reward transaction shared by explicit and automatic completion."""
    s = sessions.current()
    record = s.quest_slots[slot]
    if struct.unpack_from("<H", record)[0] != q["id"] or record[2] != 2 or s.quest_flags & (1 << q["bit"]):
        return None
    # Test the complete inventory transaction before changing live state.
    original = s.inventory
    s.inventory = copy.deepcopy(original)
    touched = set()
    success = False
    try:
        for kind, unit, required, rate, item in q["objectives"]:
            if kind == 1 and item:
                remaining = required
                for i, code in enumerate(s.inventory["bag"]):
                    if code == item and remaining:
                        count = s.inventory["count"][i] or 1
                        taken = min(count, remaining)
                        remaining -= taken
                        s.inventory["count"][i] = count - taken
                        if count == taken:
                            s.inventory["bag"][i] = 0
                        touched.add(i)
                if remaining:
                    return None
        exp, gold = 0, 0
        for kind, a, b, c in q["rewards"]:
            if kind == 1:
                if a:  # selectable/class-dependent rewards are outside this slice
                    return None
                changed, left = loot.add_to_bag(b, c)
                if left:
                    return loot.system_message(loot.MSG_INVENTORY_FULL)
                touched.update(changed)
            elif kind == 2:
                exp += a
            elif kind == 4:
                gold += a
        if s.experience + exp > 0xFFFFFFFF or s.loot["gold"] + gold > 0xFFFFFFFF:
            return None
        s.experience += exp
        s.loot["gold"] += gold
        old_level = s.level
        s.level = level_for_experience(s.experience, s.level)
        s.quest_flags |= 1 << q["bit"]
        s.quest_slots[slot] = bytes(24)
        success = True
        return (b"".join(loot.slot_update(i, reason=0) for i in sorted(touched))
                + loot.gold_update() + build(0x422, struct.pack("<BBHI", s.level, int(s.level > old_level), 0, s.experience), extra=s.uid)
                + update(slot, notify=1))
    finally:
        if not success:
            s.inventory = original


REPLIES = {0x48E: accept_or_abandon, 0x48F: turn_in, 0x492: objective_report}

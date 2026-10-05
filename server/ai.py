"""Monster AI: idle at home, aggro, chase, basic-attack the player, leash back.

handlers.py calls tick_world(now, sessions) once about every 200 ms. Each monster
targets one living player and shared updates reach all players in that scene.
Player HP/alive state is scoped through sessions.use(); tick(now, player) remains
available for standalone single-player experiments and self-tests.

Packets (all key 0, see out/spec/monsters.md section 6):
  - walk: S->C 0x416 (0x20 bytes, extra = monster uid) {u8 heading, u8 type, u8 stance,
    u8 0, u16 speed (x0.01 units/s), u16 0, f32 x, f32 z}. The client path-finds and
    walks the unit to x/z at that speed; type 2 = move, type 0 = move then stop.
  - attack: S->C 0x411 (0x64 bytes, extra = monster uid), skill 0 = basic attack:
    +0x10 monster uid, +0x16 motion, +0x18 flags (0x4 crit), +0x1a lethal mask,
    +0x1c/+0x20 monster x/z, +0x24/+0x28 player x/z, +0x2c/+0x30 monster HP/MP
    (HP must be > 0 or the monster dies), +0x34 {u16 player uid, s16 damage}.
    The client subtracts the damage from the player at once and plays the swing.
  - player death: 0x420 {HP 0, MP} for the player (the lethal bit already kills).
  - player revive after PLAYER_REVIVE_SECONDS: 0x421 {HP, MP, max HP, max MP}
    (HP > 0 on a dead unit revives it in place), then 0x416 type 1 = snap to spawn.
  - leash home: 0x416 type 0 at LEASH_SPEED; on arrival 0x420 with full HP.
  - respawns: world.due_respawns() (0x804) now come from the timer too.
"""
import math
import random
import struct
import time

import world
import sessions
from proto import build

AGGRO_RANGE = 8.0  # player within this of a monster -> it chases
ATTACK_RANGE = 2.5  # monster swings when the player is this close (centre to centre)
CHASE_STOP = 1.6  # chase destination: this far short of the player
LEASH_RANGE = 25.0  # player (or monster) this far from the monster's home -> go home
ATTACK_INTERVAL = 1.5  # seconds between swings
FIRST_SWING = 0.5  # delay between arriving in range and the first swing
CHASE_RESEND = 0.5  # seconds between chase 0x416s
CHASE_RETARGET = 1.0  # resend early if the player moved this far from the last aim
CHASE_SPEED = world.MONSTER_SPEED  # x0.01 units/s (the player runs 450)
LEASH_SPEED = 600  # running home, x0.01 units/s
MONSTER_DAMAGE = 40  # level-1 basic hit, before the 0.8..1.2 roll
DAMAGE_PER_LEVEL = 15
MONSTER_CRIT = 0.05  # chance of a double-damage hit (flag 0x4)
ATTACK_MOTION = 0  # 0x411 +0x16 swing animation index
PLAYER_REVIVE_SECONDS = world.PLAYER_REVIVE_SECONDS

MOVE, STOP, SNAP = 2, 0, 1  # 0x416 +0x11 types


def log(*args):
    print(time.strftime("%H:%M:%S"), "[ai]", *args, flush=True)


def dist(ax, az, bx, bz):
    return math.hypot(bx - ax, bz - az)


def heading(dx, dz):
    """u8 heading for a direction: atan2(x, z) scaled to 256 (FUN_005106ab); medium confidence."""
    if not dx and not dz:
        return 0
    return round(math.atan2(dx, dz) / (2 * math.pi) * 256) & 0xFF


# ---------------------------------------------------------------- packets


def move(u, x, z, kind=MOVE, speed=CHASE_SPEED, face=None):
    """S->C 0x416 for monster u: walk to (x, z). Starts the server-side walk too."""
    fx, fz = face if face else (x, z)
    u.heading = heading(fx - u.x, fz - u.z)
    u.dest = (x, z) if dist(u.x, u.z, x, z) > 0.01 else None
    u.move_speed = speed * 0.01
    return build(0x416, struct.pack("<BBBBHHff", u.heading, kind, 0, 0, speed, 0, x, z), extra=u.uid)


def monster_damage(u):
    """(amount, flags) for one monster swing."""
    amount = (MONSTER_DAMAGE + DAMAGE_PER_LEVEL * (u.level - 1)) * random.uniform(0.8, 1.2)
    flags = 0
    if random.random() < MONSTER_CRIT:
        amount, flags = amount * 2, world.FLAG_CRIT
    return min(int(amount), 0x7FFF), flags


def attack(u, player):
    """S->C 0x411 basic attack from monster u on the player; lowers the player's HP."""
    P = world.player()
    amount, flags = monster_damage(u)
    P["hp"] = max(P["hp"] - amount, 0)
    lethal = 1 if P["hp"] == 0 else 0
    p = bytearray(0x64)
    struct.pack_into("<HHhHHH", p, 0x10, u.uid, 0, 0, ATTACK_MOTION, flags, lethal)
    struct.pack_into("<ffff", p, 0x1C, u.x, u.z, player["x"], player["z"])
    struct.pack_into("<II", p, 0x2C, max(u.hp, 1), u.mp)
    struct.pack_into("<Hh", p, 0x34, P["uid"], amount)
    log(f"{u.name} 0x{u.uid:x} hits player for {amount}{' (crit)' if flags else ''}: {P['hp']}/{P['max_hp']}")
    out = build(0x411, bytes(p[16:]), extra=u.uid)
    if lethal:
        out += player_died()
    return out


def player_died():
    P = world.player()
    P["alive"] = False
    P["revive_at"] = world.clock() + PLAYER_REVIVE_SECONDS
    log(f"player died; revive in {PLAYER_REVIVE_SECONDS} s")
    return build(0x420, struct.pack("<II", 0, P["mp"]), extra=P["uid"])


def player_revive():
    """0x421 full HP/MP (revives the dead avatar in place), then 0x416 type 1: snap to spawn."""
    P = world.player()
    P.update(alive=True, revive_at=None, hp=P["max_hp"], mp=P["max_mp"])
    x, z = P["spawn"]
    log(f"player revived at ({x:.1f}, {z:.1f})")
    return (build(0x421, struct.pack("<IIII", P["hp"], P["mp"], P["max_hp"], P["max_mp"]), extra=P["uid"])
            + build(0x416, struct.pack("<BBBBHHff", 0, SNAP, 0, 0, 0, 0, x, z), extra=P["uid"]))


# ---------------------------------------------------------------- state machine


def walk(u, dt):
    """Advance u along its current walk (the client walks it the same way)."""
    if u.dest is None:
        return
    tx, tz = u.dest
    d = dist(u.x, u.z, tx, tz)
    step = u.move_speed * dt
    if d <= step:
        u.x, u.z, u.dest = tx, tz, None
    else:
        u.x += (tx - u.x) * step / d
        u.z += (tz - u.z) * step / d


def go_home(u, now):
    u.state, u.aimed_at = "leash", None
    log(f"{u.name} 0x{u.uid:x} leashes home")
    u.last_move = now
    return move(u, *u.home, kind=STOP, speed=LEASH_SPEED)


def think(u, now, player, alive):
    """One monster's decision for this tick -> packets."""
    hx, hz = u.home
    px, pz = player["x"], player["z"]
    d = dist(u.x, u.z, px, pz)

    if u.state == "leash":
        if u.dest is None:  # home
            u.state = "idle"
            if u.hp < u.max_hp:
                u.hp = u.max_hp
                return world.hp_update(u)
        return b""

    if u.state == "idle":
        provoked = u.hp < u.max_hp and dist(hx, hz, px, pz) <= LEASH_RANGE
        if alive and (d <= AGGRO_RANGE or provoked):
            u.state = "chase"
            log(f"{u.name} 0x{u.uid:x} aggro at {d:.1f}")
        else:
            return b""

    # chase / attack
    if not alive or dist(hx, hz, px, pz) > LEASH_RANGE or dist(hx, hz, u.x, u.z) > LEASH_RANGE:
        return go_home(u, now)

    if d <= ATTACK_RANGE:
        out = b""
        if u.state != "attack":
            u.state = "attack"
            u.next_attack = max(u.next_attack, now + FIRST_SWING)
            u.last_move, u.aimed_at = now, None
            out += move(u, u.x, u.z, kind=STOP, face=(px, pz))  # stop, face the player
        if now >= u.next_attack:
            u.next_attack = now + ATTACK_INTERVAL
            out += attack(u, player)
        return out

    # out of reach: (re)aim at a point just short of the player
    u.state = "chase"
    moved = u.aimed_at is None or dist(*u.aimed_at, px, pz) > CHASE_RETARGET
    if now - u.last_move < CHASE_RESEND or (not moved and u.dest is not None):
        return b""
    k = max(d - CHASE_STOP, 0) / d
    u.last_move, u.aimed_at = now, (px, pz)
    return move(u, u.x + (px - u.x) * k, u.z + (pz - u.z) * k)


_last = globals().get("_last", {"now": None})


def tick(now, player):
    """Run every monster once; returns the bytes to send (b"" if nothing).

    now: seconds (time.monotonic(), the same clock as world.clock).
    player: {"uid", "x", "z", ...}; "hp"/"alive" are written back from world.player().
    """
    P = world.player()
    dt = 0.0 if _last["now"] is None else min(max(now - _last["now"], 0.0), 1.0)
    _last["now"] = now
    out = b""

    if not P["alive"] and P["revive_at"] is not None and now >= P["revive_at"]:
        out += player_revive()
        player["x"], player["z"] = P["spawn"]  # until the client's next 0x416
    alive = P["alive"] and P["hp"] > 0

    for u in list(world.UNITS.values()):
        if not world.is_monster(u):
            continue
        if u.dead_until is not None:
            u.state, u.dest, u.aimed_at = "idle", None, None
            continue
        walk(u, dt)
        out += think(u, now, player, alive)

    out += world.due_respawns()
    player["hp"], player["alive"] = P["hp"], P["alive"]
    return out


def tick_world(now, players):
    """Advance shared monsters once; target a nearby living player.

    Nearest-player aggro and killer-only loot are test-server design choices.
    Wire layouts remain the same as the single-player packet experiments above.
    """
    dt = 0.0 if _last["now"] is None else min(max(now - _last["now"], 0.0), 1.0)
    _last["now"] = now
    for session in players:
        p = session.player
        if not p["alive"] and p["revive_at"] is not None and now >= p["revive_at"]:
            with sessions.use(session):
                out = player_revive()
            p["x"], p["z"] = p["spawn"]
            sessions.broadcast(session, out, include_self=True)
    out = b""
    for u in list(world.UNITS.values()):
        if not world.is_monster(u):
            continue
        if u.dead_until is not None:
            u.state, u.dest, u.aimed_at = "idle", None, None
            u.target_uid = None
            continue
        walk(u, dt)
        eligible = [s for s in players if s.player["alive"] and s.player["hp"] > 0
                    and (s.player["map"], s.player["scene"]) == (117, 87)
                    and dist(*u.home, s.player["x"], s.player["z"]) <= LEASH_RANGE]
        target = next((s for s in eligible if s.uid == getattr(u, "target_uid", None)), None)
        if target is None:
            target = min(eligible, key=lambda s: dist(u.x, u.z, s.player["x"], s.player["z"]), default=None)
        if target is not None:
            u.target_uid = target.uid
            with sessions.use(target):
                out += think(u, now, target.player, True)
        else:
            u.target_uid = None
            out += think(u, now, {"x": u.home[0], "z": u.home[1]}, False)
    out += world.due_respawns()
    if out:
        for session in players:
            if (session.player["map"], session.player["scene"]) == (117, 87):
                session.send(out)


# ---------------------------------------------------------------- self-test

if __name__ == "__main__":
    from proto import split

    random.seed(2)
    clock = [5000.0]
    world.clock = lambda: clock[0]

    world.spawn_all(1)
    slime = world.UNITS[world.MONSTER_UID_BASE]
    hx, hz = slime.home
    player = {"uid": 1, "x": hx + 30.0, "z": hz, "hp": 1000, "alive": True}
    seen = {}

    def run(seconds, step=0.2):
        got = []
        end = clock[0] + seconds
        while clock[0] < end:
            clock[0] += step
            data = tick(clock[0], player)
            packets, rest = split(data)
            assert not rest
            for p in packets:
                op, extra = struct.unpack_from("<HH", p, 4)
                size = {0x416: 0x20, 0x411: 0x64, 0x420: 0x18, 0x421: 0x20, 0x804: 0xBC}[op]
                assert len(p) == size, (hex(op), len(p))
                got.append((op, extra, p))
                seen[op] = seen.get(op, 0) + 1
        return got

    # Far away: nothing happens.
    assert run(2) == [] and slime.state == "idle"

    # Walk to 6 units from the slime: it aggroes and chases with 0x416 type 2.
    player["x"] = hx + 6.0
    got = run(0.4)
    moves = [p for op, extra, p in got if op == 0x416 and extra == slime.uid]
    assert slime.state == "chase" and moves and moves[0][0x11] == MOVE
    assert struct.unpack_from("<H", moves[0], 0x14)[0] == CHASE_SPEED
    tx, tz = struct.unpack_from("<ff", moves[0], 0x18)
    assert abs(dist(tx, tz, player["x"], player["z"]) - CHASE_STOP) < 0.01
    assert heading(-1, 0) == 192 and moves[0][0x10] == heading(1, 0) and heading(0, 1) == 0

    # It reaches the player, stops (type 0) and swings every ATTACK_INTERVAL.
    got = run(6)
    assert slime.state == "attack" and dist(slime.x, slime.z, player["x"], player["z"]) <= ATTACK_RANGE
    hits = [(extra, p) for op, extra, p in got if op == 0x411 and extra == slime.uid]
    assert 3 <= len(hits) <= 5, len(hits)
    extra, p = hits[0]
    assert extra == slime.uid and struct.unpack_from("<Hhh", p, 0x10) == (slime.uid, 0, 0)
    assert struct.unpack_from("<II", p, 0x2C) == (slime.hp, 0)
    uid, amount = struct.unpack_from("<Hh", p, 0x34)
    assert uid == 1 and 30 <= amount <= 100 and player["hp"] < 1000 and player["hp"] == world.PLAYER["hp"]
    print(f"slime hit {len(hits)} times, player at {player['hp']}")

    # Kite past the leash: the slime runs home (type 0, leash speed) and heals.
    slime.hp = 10
    player["x"] = hx + 30.0
    got = run(0.2)
    home = [p for op, extra, p in got if op == 0x416 and extra == slime.uid]
    assert slime.state == "leash" and home[0][0x11] == STOP
    assert struct.unpack_from("<Hxxff", home[0], 0x14) == (LEASH_SPEED, world.f32(hx), world.f32(hz))
    got = run(3)
    assert slime.state == "idle" and (slime.x, slime.z) == (hx, hz) and slime.hp == slime.max_hp
    assert [op for op, extra, _ in got if extra == slime.uid] == [0x420]

    # Stand among the slimes until dead: lethal bit, 0x420 HP 0, then revive + snap.
    player["x"], player["z"] = hx - 1.0, hz
    world.PLAYER["hp"] = 90
    got = run(8)
    lethal = [p for op, _, p in got if op == 0x411 and struct.unpack_from("<H", p, 0x1A)[0] == 1]
    assert len(lethal) == 1
    ops = [(op, extra) for op, extra, _ in got]
    assert (0x420, 1) in ops and (0x421, 1) in ops and (0x416, 1) in ops
    assert ops.index((0x420, 1)) < ops.index((0x421, 1)) < ops.index((0x416, 1))
    snap = next(p for op, extra, p in got if (op, extra) == (0x416, 1))
    assert snap[0x11] == SNAP and struct.unpack_from("<ff", snap, 0x18) == tuple(map(world.f32, world.PLAYER["spawn"]))
    after = ops.index((0x420, 1))
    assert all(op != 0x411 for op, _ in ops[after:ops.index((0x421, 1))])  # nobody hits a corpse
    assert player["alive"] and (player["x"], player["z"]) == world.PLAYER["spawn"]

    # A dead monster stops thinking and comes back through the timer.
    bee = world.UNITS[world.MONSTER_UID_BASE + 5]
    bee.hp, bee.dead_until = 0, clock[0] + 1.0
    got = run(1.4)
    assert [(op, len(p)) for op, extra, p in got if extra == bee.uid] == [(0x804, 0xBC)]
    assert bee.dead_until is None and bee.state == "idle"

    # NPCs never move.
    npc = world.UNITS[world.NPC_UID_BASE]
    assert npc.state == "idle" and (npc.x, npc.z) == npc.home
    print("ok:", ", ".join(f"0x{op:x} x{n}" for op, n in sorted(seen.items())))

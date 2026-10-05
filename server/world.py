"""Monsters and NPCs in the tutorial zone: spawn, take hits, die, respawn.

handlers.py uses join() for shared monsters and spawn_player() for peers.
The shared AI timer advances monsters and broadcasts respawns once, while
packet handlers select a player's state through sessions.use().

The client decides hits (out/spec/combat.md): it sends 0x411/0x412 with every
damage slot 0, and the server fills in damage, the lethal mask and the
attacker's HP/MP and sends the packet back. Unit ids come from UnitDB.cdb
(data/tables/UnitDB.tsv); HP and level are server-side, chosen here.
Monster state survives hot reloads of this module. PLAYER is fallback state
for standalone experiments and self-tests.
"""
import math
import random
import os
import struct
import sys
import time
import sessions

from proto import build, split

try:
    import loot  # drops on kill (loot.py); optional
except ImportError:
    loot = None


def log(*args):
    print(time.strftime("%H:%M:%S"), "[world]", *args, flush=True)


clock = time.monotonic  # replaced by the self-test

# Tutorial zone tutorial_map_01 (map 117, ZoneDB 1344..1503 x 352..479). Spawns are
# offsets from CENTRE so the whole group moves when a walkable point is found.
CENTRE = globals().get("CENTRE", (1424.0, 416.0))
QUEST_TEST = os.environ.get("WARMONGER_QUEST_TEST") == "1"
# One stable scene per supported map. Coordinates choose the terrain in this
# client. NPC estimates and portal arrivals: docs/gameplay/npc-locations.md.
SITES = {117: (87, 1427.0, 429.0), 89: (89, 419.0, 3661.0),
         88: (88, 325.8, 3438.9)}
MAP_ID = 89 if QUEST_TEST else 117
SCENE_ID, SPAWN_X, SPAWN_Z = SITES[MAP_ID]

# Teams: the client's friend/foe test (FUN_00486179, target = +0x655 team byte)
# treats team 0 as friendly to everyone, 1..3 as nations, and 4+ as hostile to
# everyone. Monsters must be 4+ or the client never sends the attack.
MONSTER_TEAM = 4
NPC_TEAM = 0

RESPAWN_SECONDS = 10.0
MONSTER_SPEED = 300  # stats +0x36, x0.01 units/s
SPAWN_FX = 0  # 0x803 +0x33: 1..3 play the "appear" action
CONFIRM_DEATH = True  # also send 0x420 HP 0 when a hit is lethal (the 0x411 alone kills)

# (UnitDB id, name, level, max HP, dx, dz). Tutorial quests: 631 "The Slime is mine"
# (kill 3 x 604), 632 (5 x 732 Cobra), Bee 731 (5 x); 605 Great Slime as a tougher one.
MONSTERS = [
    # Offsets checked against the navmesh around the tutorial spawn (1427, 429):
    # each is walkable and >= 2 units from a mesh edge (tools/navmesh.py).
    (604, "Slime", 1, 80, 10.3, -1.0),
    (604, "Slime", 1, 80, 9.0, 8.0),
    (604, "Slime", 1, 80, 13.0, -7.0),
    (732, "Cobra", 2, 120, -11.0, 10.0),
    (732, "Cobra", 2, 120, -13.0, 3.0),
    (731, "Bee", 3, 150, 5.0, -13.0),
    (731, "Bee", 3, 150, 2.7, -13.0),
    (605, "Great Slime", 4, 400, -5.8, 20.4),
]
# NPCs: friendly (team 0), never take damage. Shaia (201) uses ObjectList model
# 275, Guide_wisp, in the original client data; her ghostlike form is expected.
NPCS = [
    (201, "Shaia", 10, 1000, 6.0, 3.0),
    (239, "Floyd", 10, 1000, 9.0, 3.0),
]

MONSTER_UID_BASE = 0x400  # monsters/NPCs are uid 0x3F7..0x2B05
NPC_UID_BASE = 0x3F8

# Damage: base x (0.75..1.25), 10 % crits for double. Skill hits hit harder.
BASIC_DAMAGE = 30
SKILL_DAMAGE = 45
CRIT_CHANCE = 0.10
FLAG_CRIT = 0x0004

# Fallback player state. The attacker's HP/MP go into every hit reply (+0x2c/+0x30);
# 0 would kill it, so hp must track the real value: ai.py lowers it when monsters hit.
# spawn_all() resets it; handlers.py may overwrite any field.
PLAYER = globals().get("PLAYER", {"uid": 1, "hp": 1000, "mp": 500, "max_hp": 1000,
          "max_mp": 500, "speed": 450, "alive": True, "revive_at": None, "spawn": CENTRE})


def player():
    session = sessions.current()
    return session.player if session is not None else PLAYER

# Stat block (0x5c bytes, char+0x443; carried by 0x41f at +0x10 and 0x804 at +0x28).
# Basic attacks need +0x1e: the client's basic-attack range is that s16 x 0.01
# (FUN_0058641a, online path). 0 means range 0, so the avatar never gets in range,
# never swings and never sends the skill-0 0x411. Skills have their own range (Skill_Base +0x41).
STAT_ATTACK_SPEED = 0x1C  # s16, x0.002; players are clamped to 200..1000 (FUN_004b8b5f)
STAT_ATTACK_RANGE = 0x1E  # s16, x0.01 world units
STAT_SPEED = 0x36  # u16 move speed, x0.01 units/s
STAT_REVIVE_DELAY = 0x40  # s16 seconds the client counts down after death
ATTACK_SPEED = 500  # 1.0
MELEE_RANGE = 200  # 2.0 units: the offline default (_DAT_00722c18)
RANGED_RANGE = 700  # 7.0 units: a guess for guns, bows, wands and cannons
RANGED_WEAPONS = {10001, 10002, 10011, 15004, 20021}
PLAYER_REVIVE_SECONDS = 5


class Unit:
    """A server-side monster or NPC."""

    def __init__(self, uid, unit_id, name, level, max_hp, x, z, team, map_id=None, scene=None):
        self.uid, self.unit_id, self.name, self.level = uid, unit_id, name, level
        self.map_id = MAP_ID if map_id is None else map_id
        self.scene = SITES[self.map_id][0] if scene is None else scene
        self.max_hp = self.hp = max_hp
        self.max_mp = self.mp = 0
        self.home = (x, z)
        self.x, self.z = x, z
        self.team = team
        self.heading = 0
        self.dead_until = None  # clock() time to respawn, None while alive
        # AI state (ai.py): idle / chase / attack / leash
        self.state = "idle"
        self.dest = None  # (x, z) it is walking to, None when standing
        self.move_speed = 0.0  # units/s while walking to dest
        self.last_move = 0.0  # clock() of the last 0x416 sent
        self.next_attack = 0.0
        self.aimed_at = None  # player (x, z) the last chase packet aimed at

    def __repr__(self):
        state = "dead" if self.dead_until is not None else f"{self.hp}/{self.max_hp}"
        return f"<{self.name} uid=0x{self.uid:x} id={self.unit_id} ({self.x:.0f},{self.z:.0f}) {state}>"


UNITS = globals().get("UNITS", {})
INITIALIZED = globals().get("INITIALIZED", False)


def reset():
    """(Re)create every unit at full HP at its home position."""
    UNITS.clear()
    cx, cz = CENTRE
    for i, (unit_id, name, level, hp, dx, dz) in enumerate(MONSTERS):
        u = Unit(MONSTER_UID_BASE + i, unit_id, name, level, hp, cx + dx, cz + dz, MONSTER_TEAM)
        UNITS[u.uid] = u
    for i, (unit_id, name, level, hp, dx, dz) in enumerate(NPCS if QUEST_TEST else NPCS[:1]):
        u = Unit(NPC_UID_BASE + i, unit_id, name, level, hp, cx + dx, cz + dz, NPC_TEAM)
        UNITS[u.uid] = u
    if QUEST_TEST:
        # Monster placement is a test layout, checked on the original navmesh;
        # HP, damage and respawn timing remain prototype choices.
        points = ((429.3, 3660), (427, 3654), (432, 3654), (408, 3671),
                  (406, 3664), (424, 3648), (421.7, 3648), (410, 3664))
        for i, point in enumerate(points):
            u = UNITS[MONSTER_UID_BASE + i]
            u.home = point
            u.x, u.z = point
        for i, point in enumerate(((423.9, 3664.8), (370.5, 3660.6))):
            u = UNITS[NPC_UID_BASE + i]
            u.home = point
            u.x, u.z = point
        # The video's Frei estimate (358.8, 3469.1) is off the walkable mesh.
        # This nearby point has >2 units of clearance; exact placement pending.
        u = Unit(NPC_UID_BASE + 2, 198, "Frei", 10, 1000,
                 360.8, 3466.1, NPC_TEAM, map_id=88)
        UNITS[u.uid] = u


def visible(u, session=None):
    """Unit visibility, combat and NPC interactions use the same map boundary."""
    session = session or sessions.current()
    return u is not None and (session is None or
        (session.player["map"], session.player["scene"]) ==
        (getattr(u, "map_id", MAP_ID), getattr(u, "scene", SCENE_ID)))


def is_monster(u):
    return u is not None and u.team == MONSTER_TEAM


# ---------------------------------------------------------------- S->C packets


def spawn(u):
    """0x803 spawn unit, monster/NPC branch (FUN_00477d13), 0x1c0 bytes, extra = uid.

    +0x10 u16 UnitDB id (required, else ignored) | +0x12 u8 level |
    +0x13 u8 category (0 = UnitDB +0x8a) | +0x14 f32 x | +0x18 f32 z |
    +0x1c u32 status flags | +0x20 u32 HP (0 spawns a corpse) | +0x24 u32 max HP |
    +0x28 u32 MP | +0x2c u32 max MP | +0x30 u16 | +0x32 u8 heading | +0x33 u8 spawnFx |
    +0x34 i8 team | +0x36 u16 battle side | +0x38 i16 guild | +0x3a u16 | +0x3c u32 buff mask
    """
    p = bytearray(0x1C0)
    struct.pack_into("<HBB", p, 0x10, u.unit_id, u.level, 0)
    struct.pack_into("<ffI", p, 0x14, u.x, u.z, 0)
    struct.pack_into("<IIII", p, 0x20, max(u.hp, 1), u.max_hp, u.mp, u.max_mp)
    struct.pack_into("<BBb", p, 0x32, u.heading, SPAWN_FX, u.team)
    return build(0x803, bytes(p[16:]), extra=u.uid)


def spawn_compact(u):
    """0x805 spawn unit, compact (FUN_0047858b), monster branch, 0x38 bytes, extra = uid.

    +0x10 f32 x | +0x14 f32 z | +0x18 u8 heading | +0x19 u8 category (0) | +0x1a u8 level |
    +0x1b i8 team | +0x1c u16 battle side | +0x1e u16 UnitDB id | +0x22 i16 guild |
    +0x24 u32 status flags | +0x28 u32 HP | +0x2c u32 max HP | +0x30 u32 MP | +0x34 u32 max MP
    """
    p = bytearray(0x38)
    struct.pack_into("<ffBBBbHH", p, 0x10, u.x, u.z, u.heading, 0, u.level, u.team, 0, u.unit_id)
    struct.pack_into("<IIII", p, 0x28, max(u.hp, 1), u.max_hp, u.mp, u.max_mp)
    return build(0x805, bytes(p[16:]), extra=u.uid)


def refresh(u):
    """0x804 full refresh / respawn (FUN_00472f4d), 0xbc bytes, extra = uid.

    Revives a dead unit when HP > 0 and snaps it to x/z if more than 5 units away.
    +0x10 f32 x | +0x14 f32 z | +0x18 u8 heading | +0x19 i8 team | +0x1a u16 battle side |
    +0x1c u32 status flags | +0x23 u8 level | +0x28 0x5c-byte stats block
    (+0x28 HP, +0x2c MP, +0x30 max HP, +0x34 max MP, +0x5e i16 speed) |
    +0xb4 u16 | +0xb8 u32 buff mask (+0xbc packed buffs)
    """
    p = bytearray(0xBC)
    struct.pack_into("<ffBbHI", p, 0x10, u.x, u.z, u.heading, u.team, 0, 0)
    p[0x23] = u.level
    struct.pack_into("<IIII", p, 0x28, u.hp, u.mp, u.max_hp, u.max_mp)
    struct.pack_into("<hh", p, 0x28 + STAT_ATTACK_SPEED, ATTACK_SPEED, MELEE_RANGE)
    struct.pack_into("<h", p, 0x5E, MONSTER_SPEED)
    return build(0x804, bytes(p[16:]), extra=u.uid)


def player_weapon():
    """The current player's equipped main weapon item code, 0 if unknown."""
    skills = sys.modules.get("skills")
    try:
        return skills.state()["equip"][0]
    except (AttributeError, KeyError, IndexError, TypeError):
        return 0


def player_stats():
    """0x41f full stat block for the player (0x6c bytes, extra = player uid).

    As handlers.stat_block() (HP, MP, maxes, speed) plus what basic attacks need:
    +0x2c attack speed, +0x2e basic-attack range, +0x50 revive delay (block +0x1c/+0x1e/+0x40).
    """
    stats = bytearray(0x5C)
    struct.pack_into("<IIII", stats, 0, player()["hp"], player()["mp"], player()["max_hp"], player()["max_mp"])
    rng = RANGED_RANGE if player_weapon() in RANGED_WEAPONS else MELEE_RANGE
    struct.pack_into("<hh", stats, STAT_ATTACK_SPEED, ATTACK_SPEED, rng)
    struct.pack_into("<H", stats, STAT_SPEED, player()["speed"])
    struct.pack_into("<h", stats, STAT_REVIVE_DELAY, PLAYER_REVIVE_SECONDS)
    return build(0x41F, bytes(stats), extra=player()["uid"])


def hp_update(u):
    """0x420 HP/MP (FUN_00472079), 0x18 bytes, extra = uid. HP < 1 kills, HP > 0 revives.

    +0x10 u32 HP | +0x14 u32 MP
    """
    return build(0x420, struct.pack("<II", u.hp, u.mp), extra=u.uid)


def remove(uid, mode=2):
    """0x806 remove/kill unit (FUN_00470223), 0x14 bytes, extra = uid.

    +0x10 u32 mode: 1 die then fade, 2 remove now, 5 die in place (corpse stays)
    """
    return build(0x806, struct.pack("<I", mode), extra=uid)


def spawn_all(player_uid):
    """Every unit at full HP, sent right after entering the world.

    First a 0x41f for the player that sets the basic-attack range (handlers' stat
    block leaves it 0), then 0x803 for each unit and 0x804 to give monsters a move
    speed (0x803 has none).
    """
    handlers = sys.modules.get("handlers")
    player().update(uid=player_uid, alive=True, revive_at=None, spawn=CENTRE)
    for key, name in (("max_hp", "MAX_HP"), ("max_mp", "MAX_MP"), ("speed", "SPEED")):
        player()[key] = getattr(handlers, name, player()[key])
    player()["hp"], player()["mp"] = player()["max_hp"], player()["max_mp"]
    reset()
    log(f"spawning {len(UNITS)} units around {CENTRE}")
    return player_stats() + b"".join(spawn(u) + refresh(u) for u in UNITS.values())


def join(centre):
    """Snapshot the shared monsters without resetting another player's fight."""
    global CENTRE, INITIALIZED
    if not INITIALIZED:
        CENTRE = centre
        reset()
        INITIALIZED = True
    return player_stats() + b"".join(
        spawn(u) + (hp_update(u) if u.dead_until is not None else refresh(u))
        for u in UNITS.values() if visible(u))


def spawn_player(session):
    """0x803 player branch, 0x270 bytes; FUN_00477d13 at 0x477d56..0x477f89.

    +0x10 name[40], +0x38 x/z, +0x40 class, +0x46 heading, +0x49 level,
    +0x4a team, +0x54 appearance[8], +0x60 stats[0x5c], +0xbc equipment[0x30].
    Evidence: docs/spec/world.md, section 1. Never send this to the own uid.
    """
    import skills
    record, p = session.record, session.player
    out = bytearray(0x270)
    out[0x10:0x38] = record[8:0x30]
    struct.pack_into("<ffH", out, 0x38, p["x"], p["z"], struct.unpack_from("<H", record, 0x36)[0])
    out[0x44:0x46] = record[0x7C:0x7E]
    out[0x46], out[0x49], out[0x4A] = p["heading"], session.level, p["team"]
    out[0x54:0x5C] = record[0x38:0x40]
    with sessions.use(session):
        out[0x60:0xBC] = player_stats()[16:]
        out[0xBC:0xDC] = b"".join(skills.item(code) for code in session.inventory["equip"])
    out[0xDC:0xEC] = record[0x60:0x70]
    return build(0x803, bytes(out[16:]), extra=session.uid)


def due_respawns():
    """0x804 for every dead monster whose respawn time has passed (b"" if none)."""
    if sessions.current() is not None:
        # A private query must not consume a shared respawn before the timer
        # broadcasts it. Standalone experiments still run without a session.
        return b""
    out = b""
    now = clock()
    for u in UNITS.values():
        if u.dead_until is not None and now >= u.dead_until:
            u.dead_until = None
            u.hp, u.mp = u.max_hp, u.max_mp
            u.x, u.z = u.home
            log(f"respawn {u}")
            out += refresh(u)
    return out


# ---------------------------------------------------------------- C->S replies


def damage(skill_id):
    """(amount, flags) for one hit: base x 0.75..1.25, CRIT_CHANCE for double."""
    amount = (SKILL_DAMAGE if skill_id else BASIC_DAMAGE) * random.uniform(0.75, 1.25)
    flags = 0
    if random.random() < CRIT_CHANCE:
        amount, flags = amount * 2, FLAG_CRIT
    return min(int(amount), 0x7FFF), flags


def apply_hits(reply, slots):
    """Fill damage for `slots` target slots at +0x34 (u16 uid, s16 amount) of a 0x411/0x412.

    Sets +0x18 crit flag, +0x1a lethal mask and +0x2c/+0x30 attacker HP/MP.
    Returns the units this hit killed.
    """
    (skill_id,) = struct.unpack_from("<h", reply, 0x14)
    lethal, flags, killed = 0, 0, []
    for i in range(slots):
        (uid,) = struct.unpack_from("<H", reply, 0x34 + 4 * i)
        u = UNITS.get(uid)
        if not is_monster(u) or not visible(u) or u.dead_until is not None:
            struct.pack_into("<h", reply, 0x36 + 4 * i, 0)
            if not visible(u):
                struct.pack_into("<H", reply, 0x34 + 4 * i, 0)
            continue
        amount, crit = damage(skill_id)
        flags |= crit
        u.hp = max(u.hp - amount, 0)
        struct.pack_into("<h", reply, 0x36 + 4 * i, amount)
        if u.hp == 0:
            lethal |= 1 << i
            u.dead_until = clock() + RESPAWN_SECONDS
            killed.append(u)
        log(f"skill {skill_id} hits {u} for {amount}{' (crit)' if crit else ''}")
    (old_flags,) = struct.unpack_from("<H", reply, 0x18)
    struct.pack_into("<HH", reply, 0x18, old_flags | flags, lethal)
    struct.pack_into("<II", reply, 0x2C, player()["hp"], player()["mp"])
    return killed


def deaths(killed):
    """0x420 HP 0 for each unit a hit killed (CONFIRM_DEATH), then its loot
    (loot.on_kill: 0x427 bag slots / 0x428 gold for what the player picks up)."""
    for u in killed:
        log(f"killed {u}; respawn in {RESPAWN_SECONDS:.0f} s")
    out = b"".join(hp_update(u) for u in killed) if CONFIRM_DEATH else b""
    if loot is not None:
        for u in killed:
            out += loot.on_kill(u)
            if sessions.current() is not None:
                import quests
                out += quests.collect_progress(u.unit_id)
    return out


def hit(packet):
    """C->S 0x411 hit report (0x64 bytes) -> the same packet with damage filled in.

    +0x10 u16 attacker | +0x12 u16 display skill | +0x14 s16 skill (0 basic) |
    +0x16 u16 motion | +0x18 u16 flags | +0x1a u16 lethal mask | +0x1c/+0x20 f32 attacker x,z |
    +0x24/+0x28 f32 target point | +0x2c u32 attacker HP | +0x30 u32 attacker MP |
    +0x34 12 x {u16 target uid, s16 amount}
    Sent back to the attacker (extra = attacker): its damage numbers appear only then.
    """
    if len(packet) < 0x64:
        return due_respawns() or None
    reply = bytearray(packet[:0x64])
    (attacker,) = struct.unpack_from("<H", reply, 0x10)
    if attacker != player()["uid"] or not player()["alive"]:
        return due_respawns() or None
    killed = apply_hits(reply, 12)
    return build(0x411, bytes(reply[16:]), extra=attacker) + deaths(killed) + due_respawns()


def hit_push(packet):
    """C->S 0x412 hit with displacement (0x88 bytes) -> the same packet, damage filled in.

    As 0x411, but +0x34 holds 7 targets, +0x1a has 7 lethal bits, and
    +0x50 7 x f32 x / +0x6c 7 x f32 z are where the client pushed each target (0,0 = not moved).
    """
    if len(packet) < 0x88:
        return due_respawns() or None
    reply = bytearray(packet[:0x88])
    (attacker,) = struct.unpack_from("<H", reply, 0x10)
    if attacker != player()["uid"] or not player()["alive"]:
        return due_respawns() or None
    if not all(math.isfinite(v) for v in struct.unpack_from("<14f", reply, 0x50)):
        return None
    for i in range(7):
        (uid,) = struct.unpack_from("<H", reply, 0x34 + 4 * i)
        x, z = struct.unpack_from("<f", reply, 0x50 + 4 * i)[0], struct.unpack_from("<f", reply, 0x6C + 4 * i)[0]
        u = UNITS.get(uid)
        if is_monster(u) and visible(u) and u.dead_until is None and (x or z):
            u.x, u.z = x, z
        else:
            struct.pack_into("<f", reply, 0x50 + 4 * i, 0)
            struct.pack_into("<f", reply, 0x6C + 4 * i, 0)
    killed = apply_hits(reply, 7)
    return build(0x412, bytes(reply[16:]), extra=attacker) + deaths(killed) + due_respawns()


def cast(packet):
    """C->S 0x40f precast (+0x10 u32 skill) / 0x410 cast announce (0x38 bytes).

    Both only go to other observers; alone in the world nothing is sent back,
    apart from respawns that are due.
    """
    return due_respawns() or None


def unknown_unit(packet):
    """C->S 0x4ca unknown-unit query (0x18 bytes): +0x10 u32 uid.

    The client sends it when a 0x411 names an attacker it has not spawned.
    Reply: that unit's 0x803 (+0x804 for its speed), or 0x806 mode 2 if it is gone.
    """
    (uid,) = struct.unpack_from("<I", packet, 0x10)
    u = UNITS.get(uid & 0xFFFF)
    if not visible(u):
        return remove(uid & 0xFFFF, 2) + due_respawns()
    if u.dead_until is not None:
        return spawn(u) + hp_update(u) + due_respawns()  # recreate, then lay it down
    return spawn(u) + refresh(u) + due_respawns()


def camera(packet):
    """C->S 0x417 camera report (0x1c bytes): +0x10 f32 x, +0x14 f32 z, +0x18 u8 1 = free camera.

    Sent by the camera object (DAT_0084a7b0; FUN_00450acd/00450caf/004512cd) when the
    camera is unlocked from the avatar (key toggles of camera+0xcc bits 4/8/0x10/0x40)
    and while it pans (arrow keys / screen edge), all-zero when it locks back on.
    Nothing to do with targeting or attacks; no reply exists. Presumably the original
    server used it for area-of-interest.
    """
    return due_respawns() or None


REPLIES = {
    0x040F: cast,
    0x0410: cast,
    0x0411: hit,
    0x0412: hit_push,
    0x0417: camera,
    0x04CA: unknown_unit,
}

if not UNITS:
    reset()


# ---------------------------------------------------------------- self-test


def f32(v):
    """v as it reads back from a packet's f32 field."""
    return struct.unpack("<f", struct.pack("<f", v))[0]


def _client_hit(target, opcode=0x411, skill=0):
    """A C->S 0x411/0x412 as the client builds it (damage 0), header key 0."""
    size = 0x64 if opcode == 0x411 else 0x88
    p = bytearray(size)
    struct.pack_into("<HHHHII", p, 0, size, 0xA53C, opcode, player()["uid"], 0, 0)
    struct.pack_into("<HHhHH", p, 0x10, player()["uid"], skill, skill, 1, 0)
    struct.pack_into("<ff", p, 0x1C, *CENTRE)
    struct.pack_into("<H", p, 0x34, target)
    if opcode == 0x412:
        struct.pack_into("<f", p, 0x50, target and CENTRE[0] + 20)
        struct.pack_into("<f", p, 0x6C, target and CENTRE[1])
    return bytes(p)


def _ops(data):
    packets, rest = split(data)
    assert not rest
    for p in packets:
        assert len(p) > 16 and len(p) <= 0x1010, len(p)
    return [(struct.unpack_from("<H", p, 4)[0], len(p), p) for p in packets]


if __name__ == "__main__":
    random.seed(1)
    now = [1000.0]
    clock = lambda: now[0]  # noqa: E731

    burst = _ops(spawn_all(1))
    stats = burst.pop(0)
    assert (stats[0], stats[1]) == (0x41F, 0x6C)
    assert struct.unpack_from("<IIII", stats[2], 0x10) == (1000, 500, 1000, 500)
    assert struct.unpack_from("<hh", stats[2], 0x2C) == (ATTACK_SPEED, MELEE_RANGE)
    assert struct.unpack_from("<H", stats[2], 0x46)[0] == 450
    assert struct.unpack_from("<h", stats[2], 0x50)[0] == PLAYER_REVIVE_SECONDS
    assert [(op, n) for op, n, _ in burst[:2]] == [(0x803, 0x1C0), (0x804, 0xBC)]
    assert struct.unpack_from("<hh", burst[1][2], 0x44) == (ATTACK_SPEED, MELEE_RANGE)
    assert len(burst) == 2 * (len(MONSTERS) + (3 if QUEST_TEST else 1))
    assert all(len(p) == 0x38 for _, _, p in [(0, 0, spawn_compact(u)) for u in UNITS.values()])
    slime = UNITS[MONSTER_UID_BASE]
    first = burst[0][2]
    assert struct.unpack_from("<HBBffI", first, 0x10)[:5] == (604, 1, 0, f32(slime.x), f32(slime.z))
    assert struct.unpack_from("<II", first, 0x20) == (80, 80) and first[0x34] == MONSTER_TEAM
    assert len(remove(slime.uid)) == 0x14 and len(hp_update(slime)) == 0x18

    # 0x417 camera reports get no reply.
    assert camera(bytes(0x1C)) is None

    # A basic attack (skill 0) on a monster does damage.
    cobra = UNITS[MONSTER_UID_BASE + 3]
    op, n, p = _ops(hit(_client_hit(cobra.uid)))[0]
    assert (op, n) == (0x411, 0x64) and struct.unpack_from("<h", p, 0x14)[0] == 0
    assert 0 < struct.unpack_from("<h", p, 0x36)[0] and cobra.hp < cobra.max_hp

    # Hit the slime until it dies.
    hits = 0
    while slime.dead_until is None:
        out = _ops(hit(_client_hit(slime.uid)))
        hits += 1
        op, n, p = out[0]
        assert (op, n) == (0x411, 0x64)
        amount, = struct.unpack_from("<h", p, 0x36)
        assert amount > 0 and struct.unpack_from("<II", p, 0x2C) == (1000, 500)
    lethal = struct.unpack_from("<H", p, 0x1A)[0]
    assert lethal == 1 and [o[0] for o in out][:2] == [0x411, 0x420]
    assert struct.unpack_from("<I", out[1][2], 0x10)[0] == 0
    if loot is not None:  # the slime's loot follows: Slime Mucus (0x427) and gold (0x428)
        assert {o[0] for o in out[2:]} <= {0x427, 0x428, 0x41B} and out[-1][0] == 0x428
    print(f"slime died after {hits} hits")

    # Dead: further hits do nothing; no respawn before the time.
    p = _ops(hit(_client_hit(slime.uid)))[0][2]
    assert struct.unpack_from("<hH", p, 0x36)[0] == 0
    assert due_respawns() == b"" and cast(b"") is None
    now[0] += RESPAWN_SECONDS
    out = _ops(cast(b""))
    assert [(o[0], o[1]) for o in out] == [(0x804, 0xBC)] and slime.hp == slime.max_hp
    assert struct.unpack_from("<I", out[0][2], 0x28)[0] == 80

    # NPCs and unknown uids take no damage.
    npc = UNITS[NPC_UID_BASE]
    p = _ops(hit(_client_hit(npc.uid)))[0][2]
    assert struct.unpack_from("<h", p, 0x36)[0] == 0 and npc.hp == npc.max_hp

    # 0x412 with a push: damage filled, position taken.
    bee = UNITS[MONSTER_UID_BASE + 5]
    out = _ops(hit_push(_client_hit(bee.uid, 0x412, skill=1)))
    assert (out[0][0], out[0][1]) == (0x412, 0x88) and bee.hp < bee.max_hp and bee.x == CENTRE[0] + 20

    # 0x4ca: known -> 0x803 + 0x804; unknown -> 0x806 mode 2.
    q = bytearray(0x18)
    struct.pack_into("<HHHHII", q, 0, 0x18, 0xA53C, 0x4CA, 1, 0, 0)
    struct.pack_into("<I", q, 0x10, bee.uid)
    assert [o[0] for o in _ops(unknown_unit(bytes(q)))] == [0x803, 0x804]
    struct.pack_into("<I", q, 0x10, 0x2000)
    out = _ops(unknown_unit(bytes(q)))
    assert [(o[0], o[1]) for o in out] == [(0x806, 0x14)] and struct.unpack_from("<I", out[0][2], 0x10)[0] == 2

    print("ok:", ", ".join(repr(u) for u in UNITS.values()))

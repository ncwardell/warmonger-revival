"""Packet and web handlers for the stub server.

stub.py reloads this module whenever it changes, so handlers can be edited
while the client stays connected.
"""
import json
import pathlib
import struct
import time

from proto import build

import importlib
import loot
import skills
import world as units

# stub.py only reloads this module; pick up edits to the helper modules too.
importlib.reload(skills)
importlib.reload(loot)
importlib.reload(units)

try:
    import ai  # monster AI; optional until it exists

    importlib.reload(ai)
except ImportError:
    ai = None


def log(*args):
    print(time.strftime("%H:%M:%S"), *args, flush=True)


ACCOUNT_ID = 1
ACCOUNT_NAME = b"player"

# Session tag the client echoes in header +6 of character-select packets (0x2001 extra).
SESSION_TAG = 1
# The player's in-world unit id (0x2000 extra); players are below 0x3F7.
PLAYER_UID = 1
# Account nation/faction (0x2001 +0xB74; 0 = not chosen yet) and team index (0x2000 +0x24, 0..3).
NATION = 1
TEAM = 0

# Where entering the world puts you. Field names from StringAll_Eng.cdb:
# 87/91/95 Village, 88/92/96 Training Camp, 117 Beginner's Training Ground, 120 Fortress.
# Places (x, z) from the extracted map/zone tables (docs/spec/navmesh.md).
VILLAGE = (87, 2688.8, 382.9)  # Village, segment ZP10_01 (Teleport_List.cdb)
TUTORIAL = (117, 1427.0, 429.0)  # tutorial_map_01, on the navmesh (tools/navmesh.py check); ZP05_01

SPAWN_MAP, SPAWN_X, SPAWN_Z = TUTORIAL
# Any value works as long as later warps reuse it; a different one forces a full reload.
SPAWN_SCENE = 87

# Live state of the connected player, kept from their packets (used by the monster AI).
PLAYER = {"uid": PLAYER_UID, "x": 0.0, "z": 0.0, "hp": 0, "alive": True}

# Echo the player's own 0x416 moves back to them (experiment: movement hops without it).
ECHO_MOVES = False

# A warp to perform on the player's next movement packet (map, x, z), or None.
PENDING_WARP = TUTORIAL

HP = MAX_HP = 1000
MP = MAX_MP = 500
SPEED = 450  # 4.5 units/s, the client's default; 0 leaves the avatar unable to move


def login_ok(_packet):
    """0x4201 login reply (FUN_00470032).

    +0x10 u32 result (0-2 ok, >=3 error code) | +0x14 u16 server index |
    +0x18 u32, +0x1c u32 account/session ids | +0x20 char[32] account name
    """
    payload = struct.pack("<IHHII", 0, 0, 0, ACCOUNT_ID, ACCOUNT_ID)
    payload += ACCOUNT_NAME.ljust(32, b"\0")
    return build(0x4201, payload)


CHARACTER_SLOTS = 5
SLOT_SIZE = 0x240
CHARACTERS = pathlib.Path(__file__).with_name("characters.json")


def load_characters():
    """Slot index -> 0x240-byte character record (u64 id @0, name char[] @8)."""
    if not CHARACTERS.exists():
        return {}
    return {int(k): bytes.fromhex(v) for k, v in json.loads(CHARACTERS.read_text()).items()}


def save_characters(chars):
    CHARACTERS.write_text(json.dumps({k: v.hex() for k, v in chars.items()}, indent=1))


def character_list(_packet):
    """0x2001 character list (FUN_004760b2); sends the login scene to character select.

    +0x10 5 x 0x240-byte slots (all-zero slot = empty; name at slot+8) |
    +0xb50 u32 | +0xb74 u8 | +0xb78 u32 | +0xb7c u32 | +0xb80 u32 time? |
    +0xb84 u8 | +0xb88 u32
    """
    packet = bytearray(0xB8C)
    for slot, record in load_characters().items():
        record = bytearray(record)
        record[0x34] = max(record[0x34], 1)  # level; 0 breaks the avatar
        packet[0x10 + slot * SLOT_SIZE:0x10 + (slot + 1) * SLOT_SIZE] = record
    struct.pack_into("<I", packet, 0xB50, ACCOUNT_ID)
    packet[0xB74] = NATION
    struct.pack_into("<I", packet, 0xB80, int(time.time()))
    return build(0x2001, bytes(packet[16:]), extra=SESSION_TAG)


def enter_world(packet):
    """0x406 enter world with the selected character -> 0x2000 + initial state.

    0x2000 (FUN_00472272, 0x704 bytes) is ignored unless +0x10 is a char id
    from the 0x2001 list; its extra becomes the player's unit id. The client
    builds its own avatar from the slot record, so no self-spawn is needed.
    """
    (char_id,) = struct.unpack_from("<Q", packet, 0x10)
    record = next((r for r in load_characters().values() if struct.unpack_from("<Q", r)[0] == char_id), None)
    if record is None:
        log(f"enter world: unknown char id {char_id}")
        record = bytes(SLOT_SIZE)
    (class_id,) = struct.unpack_from("<H", record, 0x36)
    level = max(record[0x34], 1)
    world = bytearray(0x704)
    struct.pack_into("<Q", world, 0x10, char_id)
    struct.pack_into("<hhff", world, 0x18, SPAWN_SCENE, SPAWN_MAP, SPAWN_X, SPAWN_Z)
    world[0x24] = TEAM
    world[0x25] = 0xFF  # mapfort -1: no fort
    struct.pack_into("<I", world, 0x6F8, int(time.time()))
    weapon = skills.weapon_of(record)
    skills.apply_to_world(world, class_id, level, weapon=weapon)
    log(f"enter world: char {char_id} -> map {SPAWN_MAP} scene {SPAWN_SCENE} at ({SPAWN_X}, {SPAWN_Z})")
    PLAYER.update(x=SPAWN_X, z=SPAWN_Z, hp=HP, alive=True, in_world=True)
    loot.set_gold(struct.unpack_from("<I", record, 0x80)[0])
    units.PLAYER["spawn"] = (SPAWN_X, SPAWN_Z)
    # Monsters sit around wherever the player spawns until the tutorial spot is walkable.
    units.CENTRE = (SPAWN_X, SPAWN_Z)
    return (
        build(0x2000, bytes(world[16:]), extra=PLAYER_UID)
        + stat_block()
        + build(0x421, struct.pack("<IIII", HP, MP, MAX_HP, MAX_MP), extra=PLAYER_UID)
        # Equipping the weapon in-game is what loads its skills onto the bar.
        + skills.after_enter_world(PLAYER_UID, class_id, level, weapon=weapon)
        + units.spawn_all(PLAYER_UID)
    )


def move(packet):
    """0x416 movement; also flushes monster respawns that have come due."""
    return (_move(packet) or b"") + units.due_respawns() or None


def _move(packet):
    """0x416 movement (0x20 bytes, both directions; header +6 = mover uid).

    +0x10 u8 heading | +0x11 u8 type (2 move, 0x20 alt, 0 stop, 1 resync request,
    4 clock-drift report) | +0x12 u8 stance | +0x14 u16 speed | +0x18 f32 x | +0x1c f32 z
    The client moves on its own; it only needs an answer to a resync request,
    which is a 0x416 of type 1 that snaps it to a position.
    """
    global PENDING_WARP
    _, kind = packet[0x10], packet[0x11]
    x, z = struct.unpack_from("<ff", packet, 0x18)
    if kind in (0, 2, 0x20):
        PLAYER["x"], PLAYER["z"] = x, z
    if PENDING_WARP:
        (map_id, wx, wz), PENDING_WARP = PENDING_WARP, None
        PLAYER["x"], PLAYER["z"] = wx, wz
        # Bring the monsters along: drop the old ones, respawn around the new spot.
        gone = b"".join(units.remove(uid) for uid in list(units.UNITS))
        units.CENTRE = (wx, wz)
        units.PLAYER["spawn"] = (wx, wz)
        return warp(map_id, wx, wz) + gone + units.spawn_all(PLAYER_UID)
    if kind == 1:
        log(f"resync request at ({x:.1f}, {z:.1f}); snapping to spawn")
        return build(0x416, struct.pack("<BBBBHHff", 0, 1, 0, 0, 0, 0, SPAWN_X, SPAWN_Z), extra=PLAYER_UID)
    if kind == 4:
        log("client reported clock drift (anti-cheat)")
        return None
    if ECHO_MOVES and kind in (0, 2, 0x10, 0x20):
        # The client's 0x416 handler also processes moves for its own unit;
        # echoing them back may be what the original server did.
        return build(0x416, packet[16:0x20], extra=PLAYER_UID)
    return None


def warp(map_id, x, z):
    """0x44e warp (0x2c bytes, extra = player uid).

    +0x10 u16 mapid | +0x12 u16 sceneidx | +0x14 f32 x | +0x18 f32 z |
    +0x1e i8 mapfort (-1 none) | +0x20 u32 mapGuild. Same sceneidx = in-place move.
    """
    log(f"warp to map {map_id} at ({x}, {z})")
    payload = bytearray(0x2C - 16)
    struct.pack_into("<HHff", payload, 0, map_id, SPAWN_SCENE, x, z)
    payload[0x1E - 0x10] = 0xFF
    return build(0x44E, bytes(payload), extra=PLAYER_UID)


def tick():
    """Called by stub.py every TICK_SECONDS per game connection: monster AI and respawns.

    Idle until the player has entered the world, so the AI never acts on a stale position.
    """
    if not PLAYER.get("in_world"):
        return None
    now = time.monotonic()
    out = ai.tick(now, PLAYER) if ai is not None else units.due_respawns()
    return (out or b"") + loot.tick(now) or None


def stat_block():
    """0x41f full stat block (0x5c bytes), sent after 0x2000.

    The client builds the avatar dead (HP 0) with speed 0; this revives it.
    +0x10 HP, +0x14 MP, +0x18 max HP, +0x1c max MP, +0x46 i16 speed, rest stats.
    """
    stats = bytearray(0x5C)
    struct.pack_into("<IIII", stats, 0, HP, MP, MAX_HP, MAX_MP)
    struct.pack_into("<h", stats, 0x46 - 0x10, SPEED)
    return build(0x41F, bytes(stats), extra=PLAYER_UID)


def create_character(packet):
    """0x407 create character; the reply echoes the request with an id (FUN_00477a62).

    +0x10 u32 slot | +0x18 u8 flag | +0x20 0x240-byte record (u64 id must be non-zero)
    """
    reply = bytearray(packet[:0x260])
    (slot,) = struct.unpack_from("<I", reply, 0x10)
    chars = load_characters()
    char_id = max((struct.unpack_from("<Q", r)[0] for r in chars.values()), default=0) + 1
    struct.pack_into("<Q", reply, 0x20, char_id)
    record = bytes(reply[0x20:0x20 + SLOT_SIZE])
    chars[slot] = record
    save_characters(chars)
    name = record[8:40].split(b"\0")[0].decode(errors="replace")
    log(f"created character {char_id} '{name}' in slot {slot}")
    return build(0x407, bytes(reply[16:]))


LOGIN_REPLIES = {
    0x4200: login_ok,  # ID/password login
    0x4207: login_ok,  # token (OAuth/Steam) login
}

GAME_REPLIES = {
    0x4200: character_list,  # game-server login carrying the account ids from 0x4201
    0x0407: create_character,
    0x0406: enter_world,
    0x0416: move,
    **{op: fn for op, fn in skills.REPLIES.items()},
    **{op: fn for op, fn in units.REPLIES.items()},
    **{op: fn for op, fn in loot.REPLIES.items()},
}


def log(*args):
    print(time.strftime("%H:%M:%S"), *args, flush=True)


def world_channel(form):
    """/JoyImpact/WorldChannel.asp (parsed by FUN_0042a92f).

    One row per world: WORLD must equal the world index from serverlist.sof;
    WORLD_STATE is stored per world; CH_01..CH_05 are per-channel values
    (player counts, presumably) and each listed channel is marked available.
    """
    world = form.get("world", "1")
    channels = "".join(f"<CH_0{i}>0</CH_0{i}>" for i in range(1, 6))
    return (
        '<?xml version="1.0" encoding="utf-8"?>'
        f"<ROOT><ROW><WORLD>{world}</WORLD><WORLD_STATE>1</WORLD_STATE>"
        "<NatBlock1>0</NatBlock1><NatBlock2>0</NatBlock2><NatBlock3>0</NatBlock3>"
        f"{channels}<NEWBIE_CHANNEL>0</NEWBIE_CHANNEL></ROW></ROOT>"
    )


WEB_PAGES = {
    # world_channel() is parsed by the client, but with it the client never
    # attempts the TCP login; an empty reply lets login proceed. Off until the
    # WORLD_STATE / channel semantics are understood.
    # "/JoyImpact/WorldChannel.asp": world_channel,
}

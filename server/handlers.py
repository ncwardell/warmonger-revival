"""Reloadable packet experiments with per-connection state in sessions.py."""
import importlib
import json
import math
import re
import secrets
import struct
import time

import sessions
import persistence
from proto import build, split
import skills
import loot
import world as units
import ai
import quests

# State lives in sessions.py; shared units and AI clocks survive these reloads.
for module in (skills, loot, units, ai, quests):
    importlib.reload(module)

NATION, TEAM = 1, 0
VILLAGE = (87, 2688.8, 382.9)
TUTORIAL = (117, 1427.0, 429.0)
SPAWN_MAP = units.MAP_ID
_, SPAWN_X, SPAWN_Z = TUTORIAL
SPAWN_SCENE = units.SCENE_ID
HP = MAX_HP = 1000
MP = MAX_MP = 500
SPEED = 450
CHARACTER_SLOTS, SLOT_SIZE = 5, 0x240


def log(*args):
    print(time.strftime("%H:%M:%S"), *args, flush=True)


def login_ok(packet):
    """0x4201: +0x18/+0x1c tickets, +0x20 account[32] (FUN_00470032).

    Token at 0x4207 +0x14 comes from -ologin=NAME; empty tokens use 'player'.
    Evidence: contract/session.yaml, token_login and game_server_login.
    """
    opcode = struct.unpack_from("<H", packet, 4)[0]
    token = packet[0x14:0x94] if opcode == 0x4207 else packet[0x10:0x30]
    account, ticket = sessions.issue_ticket(token.split(b"\0")[0])
    payload = struct.pack("<IHHII", 0, 0, 0, *ticket)
    return build(0x4201, payload + account.encode().ljust(32, b"\0"))


def game_login(packet):
    """0x4200 +0x10 account[32], +0x50/+0x54 tickets -> 0x2001."""
    session = sessions.current()
    account = packet[0x10:0x30].split(b"\0")[0].decode("ascii")
    sessions.authenticate(session, account, struct.unpack_from("<II", packet, 0x50))
    return character_list()


def character_list(_packet=None):
    """0x2001: +0x10 five 0x240-byte records; extra = this connection's uid.

    FUN_004760b2: +0xb50 account id, +0xb74 nation, +0xb80 Unix time.
    """
    session = sessions.current()
    packet = bytearray(0xB8C)
    for slot, record in sessions.load_characters(session.account).items():
        record = bytearray(persistence.character_view(session.account, record))
        record[0x34] = max(record[0x34], 1)
        packet[0x10 + slot * SLOT_SIZE:0x10 + (slot + 1) * SLOT_SIZE] = record
    struct.pack_into("<I", packet, 0xB50, session.uid)
    packet[0xB74] = NATION
    struct.pack_into("<I", packet, 0xB80, int(time.time()))
    return build(0x2001, bytes(packet[16:]), extra=session.uid)


def create_character(packet):
    """0x407: +0x10 slot, +0x20 record; echo with a new id (FUN_00477a62)."""
    session = sessions.current()
    slot = struct.unpack_from("<I", packet, 0x10)[0]
    chars = sessions.load_characters(session.account)
    if not 0 <= slot < CHARACTER_SLOTS or slot in chars:
        raise ValueError("character slot is invalid or occupied")
    record = bytearray(packet[0x20:0x260])
    name = record[8:0x30].split(b"\0")[0]
    class_id = struct.unpack_from("<H", record, 0x36)[0]
    weapon = skills.weapon_of(record)
    if not re.fullmatch(rb"[A-Za-z0-9]{1,16}", name):
        raise ValueError("character name must contain 1-16 letters or digits")
    if class_id not in skills.CLASS_WEAPONS or weapon not in skills.CLASS_WEAPONS[class_id]:
        raise ValueError("invalid starting class or weapon")
    if any(r[8:0x30].split(b"\0")[0].lower() == name.lower() for r in chars.values()):
        raise ValueError("character name is already used on this account")
    char_id = secrets.randbits(63) or 1
    struct.pack_into("<Q", record, 0, char_id)
    record[0x34] = 1
    chars[slot] = bytes(record)
    sessions.save_characters(session.account, chars)
    reply = bytearray(packet[:0x260])
    reply[0x20:0x260] = record
    log(f"created character {char_id} '{name.decode()}' in slot {slot}")
    return build(0x407, bytes(reply[16:]), extra=session.uid)


def enter_world(packet):
    """0x406 +0x10 char id -> 0x2000 and mutual player spawns.

    Own avatar: FUN_00472272 (0x704 bytes); peers: FUN_00477d13 (0x803).
    See docs/spec/world.md and contract/session.yaml.
    """
    session = sessions.current()
    char_id = struct.unpack_from("<Q", packet, 0x10)[0]
    record = next((r for r in sessions.load_characters(session.account).values()
                   if struct.unpack_from("<Q", r)[0] == char_id), None)
    if record is None:
        return character_list()
    session.record = record
    session.reset_player()
    persistence.restore_progress(session)
    session.level = quests.level_for_experience(session.experience, session.level)
    session.record = persistence.character_view(session.account, record)
    session.drops.clear()
    p = session.player
    p.update(x=SPAWN_X, z=SPAWN_Z, spawn=(SPAWN_X, SPAWN_Z), map=SPAWN_MAP,
             scene=SPAWN_SCENE, team=TEAM, hp=HP, mp=MP, max_hp=MAX_HP, max_mp=MAX_MP, speed=SPEED)
    class_id = struct.unpack_from("<H", record, 0x36)[0]
    level = session.level
    weapon = session.inventory["equip"][0] if session.inventory["initialized"] else skills.weapon_of(record)
    packet = bytearray(0x704)
    struct.pack_into("<Qhhff", packet, 0x10, char_id, SPAWN_SCENE, SPAWN_MAP, SPAWN_X, SPAWN_Z)
    packet[0x24], packet[0x25] = TEAM, 0xFF
    struct.pack_into("<I", packet, 0x6F8, int(time.time()))
    skills.apply_to_world(packet, class_id, level, weapon=weapon)
    quests.apply_to_world(packet)
    out = build(0x2000, bytes(packet[16:]), extra=session.uid)
    out += skills.after_enter_world(session.uid, class_id, level, weapon=weapon)
    out += units.join((SPAWN_X, SPAWN_Z))
    out += build(0x422, struct.pack("<BBHI", session.level, 0, 0, session.experience), extra=session.uid)
    out += loot.gold_update()
    p["in_world"] = True
    for other in sessions.CONNECTED.values():
        if other is not session and sessions.same_scene(session, other):
            out += units.spawn_player(other)
            other.send(units.spawn_player(session))
    log(f"uid {session.uid} entered map {SPAWN_MAP} at ({SPAWN_X}, {SPAWN_Z})")
    return out


def move(packet):
    """0x416: +0x10 heading, +0x11 type, +0x14 speed, +0x18/+0x1c x/z.

    See docs/spec/world.md: relay to observers, never echo normal own movement.
    Type 1 requests an authoritative position correction.
    """
    session = sessions.current()
    p = session.player
    heading, kind = packet[0x10:0x12]
    if not p["alive"]:
        return None  # movement would revive this corpse on other clients
    if kind == 1:
        return build(0x416, struct.pack("<BBBBHHff", p["heading"], 1, 0, 0, p["speed"], 0, p["x"], p["z"]), extra=session.uid)
    if kind not in (0, 2, 0x20):
        return None
    x, z = struct.unpack_from("<ff", packet, 0x18)
    if not math.isfinite(x) or not math.isfinite(z):
        raise ValueError("movement coordinates must be finite")
    p.update(x=x, z=z, heading=heading)
    sessions.broadcast(session, build(0x416, packet[16:0x20], extra=session.uid))


def leave_world(session):
    if session.player["in_world"]:
        try:
            persistence.save_progress(session)
        finally:
            sessions.broadcast(session, units.remove(session.uid))
            session.player["in_world"] = False
            session.drops.clear()


def leave_game(packet):
    """0x409 +0x10 mode: 0 -> 0x2001 on the same socket, 1 -> exit.

    FUN_0048d666 / FUN_004760b2; keep the old wire key after character select.
    """
    mode = struct.unpack_from("<I", packet, 0x10)[0]
    if mode not in (0, 1):
        raise ValueError("unknown leave-game mode")
    leave_world(sessions.current())
    return character_list() if mode == 0 else None


def disconnect(session):
    try:
        leave_world(session)
    finally:
        sessions.CONNECTED.pop(session.uid, None)


def unknown_unit(packet):
    """0x4ca +0x10 uid: return a visible player or the existing monster path."""
    uid = struct.unpack_from("<I", packet, 0x10)[0]
    session = sessions.current()
    if uid < 0x3F7:
        other = sessions.CONNECTED.get(uid)
        if other is session:
            return None
        return units.spawn_player(other) if other and sessions.same_scene(session, other) else units.remove(uid)
    return units.unknown_unit(packet)


def cast(packet):
    session = sessions.current()
    if session.player["alive"]:
        opcode = struct.unpack_from("<H", packet, 4)[0]
        sessions.broadcast(session, build(opcode, packet[16:], extra=session.uid))


def tick():
    """One shared AI tick, followed by private per-player loot collection."""
    now = time.monotonic()
    active = [s for s in sessions.CONNECTED.values() if s.player["in_world"]]
    ai.tick_world(now, active)
    for session in active:
        with sessions.use(session):
            old_level = session.level
            # Resume zero-receiver quests left ready by the earlier handler,
            # and finish newly earned automatic quests without a client turn-in.
            out = quests.refresh_level() + quests.finish_automatic() + loot.tick(now)
            if out:
                out += quests.collect_progress()
                persistence.save_progress(session)
                session.send(out)
                if session.level != old_level:
                    sessions.broadcast(session, units.spawn_player(session))


LOGIN_REPLIES = {0x4200: login_ok, 0x4207: login_ok}
GAME_REPLIES = {
    0x4200: game_login, 0x407: create_character, 0x406: enter_world,
    0x409: leave_game, 0x416: move,
    **skills.REPLIES, **units.REPLIES, **loot.REPLIES, **quests.REPLIES,
    0x4CA: unknown_unit, 0x40F: cast, 0x410: cast,
}
MIN_SIZE = {0x4207: 0x9C, 0x4200: 0x60, 0x407: 0x260, 0x406: 0x20,
            0x409: 0x14, 0x416: 0x20, 0x417: 0x1C, 0x411: 0x64,
            0x412: 0x88, 0x40F: 0x14, 0x410: 0x38, 0x4CA: 0x18,
            0x42A: 0x18, 0x494: 0x28, 0x451: 0x18,
            0x48E: 0x18, 0x48F: 0x18, 0x492: 0x1C}


def dispatch(table, packet, session=None):
    opcode, extra = struct.unpack_from("<HH", packet, 4)
    if len(packet) < MIN_SIZE.get(opcode, 16):
        raise ValueError(f"short packet for 0x{opcode:04x}")
    reply = globals()[table].get(opcode)
    if reply is None:
        return None
    if session is not None and opcode != 0x4200:
        if not session.account or extra != session.uid:
            raise ValueError("packet does not belong to this session")
        selecting = opcode in (0x406, 0x407)
        if selecting == session.player["in_world"]:
            raise ValueError("packet is not valid in this scene")
    with sessions.use(session):
        out = reply(packet)
        if session is not None and opcode in (0x411, 0x412) and out:
            # Loot and bag/gold updates belong only to the player who killed it.
            packets, _ = split(out)
            shared = b"".join(p for p in packets if struct.unpack_from("<H", p, 4)[0] in (0x411, 0x412, 0x420, 0x804))
            sessions.broadcast(session, shared)
        if session is not None and opcode == 0x42A:
            out = (out or b"") + units.player_stats()
            sessions.broadcast(session, units.spawn_player(session))
        if session is not None and session.player["in_world"]:
            if opcode in (0x42A, 0x451):
                out = (out or b"") + quests.collect_progress()
            persistence.save_progress(session)
            if opcode == 0x48F and out:
                sessions.broadcast(session, units.spawn_player(session))
        return out


def channel_status(form):
    """One available channel as JSON (FUN_0042a92f calls Json::Reader::parse).

    WORLD echoes the serverlist index requested by the client. Other channels
    are unavailable. This is a local test-server policy, not a population model.
    """
    try:
        world = int(form.get("world", "1"))
    except ValueError:
        return ""
    fields = {"WORLD": world, "WORLD_STATE": 1, "NatBlock1": 0, "NatBlock2": 0,
              "NatBlock3": 0, "CH_01": len(sessions.CONNECTED), "CH_02": -1,
              "CH_03": -1, "CH_04": -1, "CH_05": -1, "NEWBIE_CHANNEL": 0}
    return json.dumps([fields])


WEB_PAGES = {"/JoyImpact/WorldChannel.asp": channel_status,
             "/JoyImpact/ChannelList.asp": channel_status}

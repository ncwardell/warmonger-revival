"""Class skills: they come from the equipped weapon, not from a skill list.

The client has no skill-list packet. Each weapon item carries a WeaponBase id
(Item_Base option type 200), and WeaponBase.cdb gives that id 8 Skill_Base ids;
the first 4 fill the skill bar ("SoulWeaponSkillSlot0-3" for equip slot 0,
"SubSoulWeaponSkillSlot0-3" for slot 1). Equipment is container 3: two 16-byte
items at slot record +0x40/+0x50 (char+0x243). The client copies a weapon's
skills into its skill controller (FUN_005848d5) only when container 3 changes
in game (0x427, 0x426 or 0x804). Building the avatar from 0x2000 does not, so
the bar stays empty until the server sends a 0x427 for the equipped weapon.

Skills are not gated by level, Mastery or Skill_TP; quick slots (0x2000 +0x50c)
hold items only. See docs/spec/skills.md.
"""
import struct

import paths
import sessions

from proto import build

# Starting weapons per class (Create_Char.cdb), first = the default.
CLASS_WEAPONS = {
    1: (10017, 10011, 10001, 10002),  # Saint: blade, dual gun, thunder wand, life wand
    4: (15007, 15004),  # Punisher: dagger, bow
    5: (20001, 20021, 20003),  # Gardian: demolition hammer, cannon, crush hammer
}

# Weapon item -> (WeaponBase id, skill bar ids), from Item_Base.cdb and WeaponBase.cdb.
WEAPON_SKILLS = {
    10017: (18, (5022, 5023, 5024, 5025)),  # Blade storm, Wings of fair wind, Blink like wind, Wrath of the West
    10011: (12, (5102, 5103, 5104, 5105)),  # Ankle Aim, Rapid Reload, Entangling Bullet, Suppressing Fire
    10001: (2, (5004, 5005, 5006, 5007)),  # Thunderbolt, Lightning Strike, Ball of Lighting, Might of Thunder God
    10002: (64, (5277, 5279, 5280, 5281)),  # Mother Nature's Blessing .. Savior's Gift
    15007: (29, (5026, 5027, 5028, 5029)),  # Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art
    15004: (26, (5112, 5113, 5114, 5115)),  # Sharp Edges, Potential Power, Hail of Arrows, Spinning Whirlwind
    20001: (43, (5036, 5038, 5040, 5041)),  # Soul Infestation, Aura of Demise, Severe Blow, Dark Transformation
    20021: (63, (5107, 5109, 5110, 5111)),  # Nimble Pursuit, Firm Hand, Buckshot, Explosive Mortar
    20003: (45, (5067, 5068, 5069, 5070)),  # Crushing Blow, Head Butt, Howl of Victory, Unyielding Will
}

# Containers (FUN_004dfe59): 1 bag (70), 2 (8), 3 equipment (2: main, sub weapon).
BAG, EQUIPMENT = 1, 3
BAG_SLOTS = 70
ITEM_SIZE = 0x10

# Fallback state for standalone packet experiments and self-tests.
# "count" parallels "bag": the stack size at item +4 (0 = a single item).
STATE = globals().get("STATE", sessions.new_inventory())


def state():
    session = sessions.current()
    return session.inventory if session is not None else STATE


def item(code, count=1):
    """16-byte item: +0 u16 item code, +4 u8 count (ignored for weapons), rest 0."""
    raw = bytearray(ITEM_SIZE)
    if code:
        struct.pack_into("<HxxB", raw, 0, code, count)
    return bytes(raw)


def skills_of(code):
    """Skill bar ids a weapon item gives (empty for non-weapons)."""
    return WEAPON_SKILLS.get(code, (0, ()))[1]


def class_skills(class_id):
    """{weapon item: skill ids} for every starting weapon of the class."""
    return {code: skills_of(code) for code in CLASS_WEAPONS.get(class_id, ())}


def apply_to_world(world: bytearray, class_id: int, level: int, weapon=None) -> None:
    """Fill the 0x2000 profile block (0x704-byte buffer, offsets from packet start).

    +0xac 70 x 16-byte bag (= 0x424 payload): the class's other starting weapons,
    so the player can swap skill sets. +0x50c u16[8] quick-slot codes and
    +0x51c u8[8] types (0 item, 1 skill): whatever the client last saved (0x494).
    The equipped weapon itself is not here; it is in the slot record (+0x40).
    Level does not gate weapon skills, so it is unused.
    """
    weapon = weapon or default_weapon(class_id)
    spares = [c for c in CLASS_WEAPONS.get(class_id, ()) if c != weapon]
    bag = state()["bag"]
    if not any(bag):
        bag[:len(spares)] = spares
    counts = state().setdefault("count", [0] * BAG_SLOTS)
    for slot, code in enumerate(bag):
        world[0xAC + slot * ITEM_SIZE:0xAC + (slot + 1) * ITEM_SIZE] = item(code, counts[slot] or 1)
    quick = state()["quick"]
    world[0x51C:0x524] = quick[:8]
    world[0x50C:0x51C] = quick[8:]


def default_weapon(class_id):
    """The class's first Create_Char weapon, or 0 for classes without one."""
    return CLASS_WEAPONS.get(class_id, (0,))[0]


def equip(uid, slot, code):
    """0x427 single item slot update for container 3 (0x28 bytes, extra = uid).

    +0x10 u16 reason (0 = no message) | +0x12 u16 container 3 | +0x14 u16 slot |
    +0x18 16-byte item. FUN_00478d54 stores it at char+0x243+slot*16, redraws the
    avatar, then FUN_005848d5(slot) loads the weapon's 4 skills and FUN_005849b2
    fires UI event 0x18, which refills the skill bar.
    """
    state()["equip"][slot] = code
    payload = struct.pack("<HHHH", 0, EQUIPMENT, slot, 0) + item(code)
    return build(0x427, payload, extra=uid)


def after_enter_world(uid: int, class_id: int, level: int, weapon=None) -> bytes:
    """Packets to send right after 0x2000 (+ 0x41f): re-equip the weapon so the
    skill bar fills. `weapon` is the item code at slot record +0x40 (0 or None =
    the class default). A sub weapon in state()["equip"][1] gets its own 0x427.
    """
    weapon = weapon or default_weapon(class_id)
    if not weapon:
        return b""
    out = equip(uid, 0, weapon)
    if state()["equip"][1]:
        out += equip(uid, 1, state()["equip"][1])
    return out


def weapon_of(record):
    """Item code of the main weapon in a 0x240-byte slot record (+0x40)."""
    return struct.unpack_from("<H", record, 0x40)[0]


def save_quick_slots(packet):
    """C->S 0x494 (0x28 bytes): +0x10 u8[8] types (0 item, 1 skill), +0x18 u16[8] codes.

    No reply; kept so the next 0x2000 returns the same bar (+0x51c/+0x50c).
    """
    state()["quick"] = bytes(packet[0x10:0x28])
    return None


def container(kind):
    return state()["bag"] if kind == BAG else state()["equip"] if kind == EQUIPMENT else None


def move_item(packet):
    """C->S 0x42a move/swap (0x18 bytes): +0x10 u8 dst container, +0x11 dst slot,
    +0x12 src container, +0x13 src slot.

    The echo (extra = player uid) makes the client swap the two slots
    (FUN_004e1357), but that never reloads skills, so a weapon moved into or out
    of container 3 is followed by a 0x427 for that equipment slot.
    """
    uid = struct.unpack_from("<H", packet, 6)[0]
    dst_kind, dst_slot, src_kind, src_slot = packet[0x10:0x14]
    dst, src = container(dst_kind), container(src_kind)
    if dst is None or src is None or dst_slot >= len(dst) or src_slot >= len(src):
        return build(0x42A, bytes(packet[0x10:0x18]), extra=uid)
    dst[dst_slot], src[src_slot] = src[src_slot], dst[dst_slot]
    counts = state().setdefault("count", [0] * BAG_SLOTS)
    if dst_kind == src_kind == BAG:
        counts[dst_slot], counts[src_slot] = counts[src_slot], counts[dst_slot]
    else:  # a weapon to/from equipment: the bag side holds a single item
        for kind, slot in ((dst_kind, dst_slot), (src_kind, src_slot)):
            if kind == BAG:
                counts[slot] = 0
    out = build(0x42A, bytes(packet[0x10:0x18]), extra=uid)
    for kind, slot in ((dst_kind, dst_slot), (src_kind, src_slot)):
        if kind == EQUIPMENT:
            out += equip(uid, slot, state()["equip"][slot])
    return out


def tp_skill(packet):
    """C->S 0x4b4 TP skill pick: +0x10 u16 slot/group, +0x12 u16 skill id (match TP
    skills, Skill_TP.cdb). Reply unknown; ignored."""
    return None


REPLIES = {
    0x0494: save_quick_slots,
    0x042A: move_item,
    0x04B4: tp_skill,
}


if __name__ == "__main__":
    import pathlib
    from proto import HEADER, split

    world = bytearray(0x704)
    apply_to_world(world, 1, 1, weapon=10017)
    assert len(world) == 0x704
    bag = [struct.unpack_from("<H", world, 0xAC + i * 16)[0] for i in range(4)]
    assert bag == [10011, 10001, 10002, 0], bag
    out = after_enter_world(1, 1, 1, weapon=10017)
    packets, rest = split(out)
    assert len(packets) == 1 and not rest
    length, _, opcode, extra, _, _ = HEADER.unpack_from(packets[0])
    assert (length, opcode, extra) == (0x28, 0x427, 1)
    assert struct.unpack_from("<HHH", packets[0], 0x10) == (0, 3, 0)
    assert struct.unpack_from("<H", packets[0], 0x18)[0] == 10017
    assert skills_of(10017) == (5022, 5023, 5024, 5025)

    # Swap the dual gun (bag 0) into the main weapon slot.
    request = HEADER.pack(0x18, 0xA53C, 0x42A, 1, 0, 0) + bytes([3, 0, 1, 0]) + bytes(4)
    packets, _ = split(move_item(request))
    assert [struct.unpack_from("<H", p, 4)[0] for p in packets] == [0x42A, 0x427]
    assert STATE["equip"][0] == 10011 and STATE["bag"][0] == 10017
    assert save_quick_slots(bytes(0x28)) is None

    # Cross-check the tables against the game data when it is available.
    setting = paths.SETTING
    if setting.exists():
        def rows(name):
            t = (setting / name).read_bytes().split(b"\0")
            n = int(t[0])
            c = (len(t) - 4) // n  # header column counts are unreliable
            return [[x.decode("latin1") for x in t[2 + i * c:2 + (i + 1) * c]] for i in range(n)]
        items = {int(r[0]): r for r in rows("Item_Base.cdb")}
        bases = {int(r[0]): r for r in rows("WeaponBase.cdb")}
        for r in rows("Create_Char.cdb"):
            assert tuple(int(w) for w in r[5:13:2] if w) == CLASS_WEAPONS.get(int(r[0]), ()), r[0]
        for code, (base, skills) in WEAPON_SKILLS.items():
            options = items[code][19:39]
            assert ("200", str(base)) in zip(options[::2], options[1::2]), code
            assert tuple(int(s) for s in bases[base][5:9]) == skills, code
    print("ok")

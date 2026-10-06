"""Quest experiment, using the committed game wiki.

Packet evidence: contract/quests.yaml (0x48e..0x492, FUN_00599ab2).
Every wiki quest whose objectives (report, talk, kill, collect), rewards (exp,
gold, fixed/chosen/class items), NPC endpoints, level range and class limit are
supported is enabled; quests 1..7 must be. Others are skipped (SKIPPED gives the
reason) and their packets rejected, never silently completed.
"""
import copy
import gamedata
import math
import struct

import loot
import maps
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


REQUIRED = range(1, 8)  # the tested tutorial chain must always load
CLASSES = {"Saint": 1, "Punisher": 4, "Guardian": 5}  # Create_Char class ids
CLASS_REWARD = 0x100  # reward pick code: 0x100 | class id
LEVEL, CLASS = 4, 1  # prerequisite rows the generator reads as level range / class mask


class Unsupported(ValueError):
    pass


def compile_quest(qid, page):
    """One wiki quest page -> the fixed-size protocol record this server runs.

    Reward `amount` is authoritative; `shown` is historical UI evidence only.
    """
    number = gamedata.integer
    if page.get("type") != "quest" or "bit" not in page or "stages" not in page:
        raise Unsupported("no completion bit or stages")
    # objectives_client / rewards_client hold rows only the client tracks; the
    # server cannot verify them, so it never completes those quests.
    for key in ("unused", "periodic", "board", "owned_field", "objectives_client", "rewards_client"):
        if page.get(key):
            raise Unsupported(key)
    for pre in page.get("prerequisites") or []:
        if pre.get("type") not in (LEVEL, CLASS) or (pre["type"] == LEVEL and "min" not in pre and "max" not in pre):
            raise Unsupported(f"prerequisite {pre}")
    objectives = [(0,) * 5] * 5
    occupied = set()
    for o in page.get("objectives") or []:
        index = number(o["n"], 1, 5) - 1
        kind = o["type"]
        if kind not in (0, 1, 4):
            raise Unsupported(f"objective type {kind}")
        if index in occupied:
            raise ValueError(f"quest {qid}: duplicate objective")
        occupied.add(index)
        target = number(o.get("npc", o.get("unit", 0)), 0, 65535)
        item = number(o.get("item", 0), 0, 65535)
        count = number(o.get("count", 0), 1 if kind == 1 else 0, 32767)
        if kind and target not in gamedata.pages("npcs" if kind == 4 else "monsters"):
            raise Unsupported(f"objective target {target} has no wiki page")
        if item:
            gamedata.entity("items", item)
        objectives[index] = (kind, target, count, number(o.get("rate", 0), 0, 100), item)
    rewards = []
    for r in page.get("rewards") or []:
        kind, pick = r["type"], r.get("pick")
        if kind == 1 and pick in ("fixed", "choose", "class"):
            item = number(r["item"], 1, 65535)
            gamedata.entity("items", item)
            code = {"fixed": 0, "choose": 11}.get(pick)
            if pick == "class":
                if r.get("class") not in CLASSES:
                    raise Unsupported(f"reward class {r.get('class')}")
                code = CLASS_REWARD | CLASSES[r["class"]]
            rewards.append((1, code, item, number(r["count"], 1, 65535)))
        elif kind in (2, 4):
            rewards.append((kind, number(r["amount"], 0, 0xFFFFFFFF), 0, 0))
        else:
            raise Unsupported(f"reward {r}")
    giver, receiver = page["giver"], page["turn_in"]
    placed = {unit for unit, *_ in maps.NPCS}
    for endpoint in (giver, receiver):
        if set(endpoint) == {"npc"}:
            gamedata.entity("npcs", number(endpoint["npc"], 1, 65535))
            if endpoint["npc"] not in placed:
                raise Unsupported(f"NPC {endpoint['npc']} has no wiki position on an enabled map")
        elif endpoint != {"auto": True}:
            raise Unsupported(f"NPC endpoint {endpoint}")
    maps_ = tuple(number(m, 0, 65535) for m in page.get("offer_maps", [0] * 3))
    receiving = tuple(number(m, 0, 65535) for m in page.get("turn_in_maps", maps_))
    stages = tuple(number(n, 1, 5) for n in page["stages"])
    if len(maps_) != 3 or len(receiving) != 3 or len(stages) != 5:
        raise ValueError(f"quest {qid}: expected three nation maps and five stages")
    prerequisite = number(page.get("requires_bit", 0), 0, 319)
    if giver.get("auto") and not prerequisite:
        raise Unsupported("automatic assignment needs an explicit prerequisite")
    if page.get("automatic") and not any(o[0] for o in objectives):
        raise Unsupported("automatic completion without a server-verified objective")
    level = page.get("level") or {}
    classes = page.get("classes")
    if classes is not None and any(c not in CLASSES for c in classes):
        raise Unsupported(f"classes {classes}")
    return {"id": qid, "bit": number(page["bit"], 1, 319),
            "prerequisite": prerequisite,
            "exclusion": number(page.get("excludes_bit", 0), 0, 319),
            "maps": maps_, "receiver_maps": receiving,
            "giver": giver.get("npc", 0), "receiver": receiver.get("npc", 0),
            "auto_accept": giver.get("auto", False),
            "automatic": page.get("automatic", False) and receiver.get("auto", False),
            "level": (number(level.get("min", 1), 1, 255), number(level.get("max", 255), 1, 255)),
            "classes": None if classes is None else frozenset(CLASSES[c] for c in classes),
            "stages": stages, "objectives": objectives, "rewards": rewards}


SKIPPED = {}


def definitions():
    """Compile every supported wiki quest; record why the others are skipped."""
    result = {}
    SKIPPED.clear()
    for qid, page in sorted(gamedata.pages("quests").items()):
        try:
            result[qid] = compile_quest(qid, page)
        except (ValueError, KeyError, TypeError) as e:
            if qid in REQUIRED:
                raise ValueError(f"quest {qid}: {e}") from e
            SKIPPED[qid] = str(e)
    for qid in REQUIRED:
        if qid not in result:
            raise ValueError(f"expected one wiki/quests page for id {qid}")
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
               for u in world.UNITS.values() if not world.is_monster(u) and world.visible(u))


def allowed(q, receiving=False):
    s = sessions.current()
    # Prototype nation is 1; other nations need their own map/scene setup.
    maps = q.get("receiver_maps", q["maps"]) if receiving else q["maps"]
    return s.player["alive"] and maps[0] in (0, s.player["map"])


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


def class_id():
    record = sessions.current().record
    return struct.unpack_from("<H", record, 0x36)[0] if len(record) >= 0x38 else 0


def eligible(q):
    s = sessions.current()
    flags = s.quest_flags
    low, high = q.get("level", (1, 255))
    classes = q.get("classes")
    return not (flags & (1 << q["bit"])
                or not low <= s.level <= high
                or (classes is not None and class_id() not in classes)
                or (q["prerequisite"] and not flags & (1 << q["prerequisite"]))
                or (q["exclusion"] and flags & (1 << q["exclusion"]))
                or any(struct.unpack_from("<H", r)[0] == q["id"] for r in s.quest_slots))


def assign(q):
    s = sessions.current()
    if not allowed(q) or not eligible(q):
        return b""
    slot = next((i for i, r in enumerate(s.quest_slots) if not any(r)), None)
    if slot is None:
        return b""
    record = bytearray(24)
    struct.pack_into("<H", record, 0, q["id"])
    ready(q, record)
    s.quest_slots[slot] = bytes(record)
    return update(slot) + collect_progress()


def start_automatic():
    """Recover giver-less chain quests, including reconnects/full-log retries.

    Assignment never counts as a conversation; a validated 0x492 is still needed.
    Only explicitly enabled wiki definitions with a prerequisite can be assigned.
    """
    return b"".join(assign(q) for q in DEFINITIONS.values() if q.get("auto_accept"))


def accept_or_abandon(packet):
    s = sessions.current()
    notice, action, slot, qid = struct.unpack_from("<HhHH", packet, 0x10)
    q = DEFINITIONS.get(qid)
    if not q or notice or not s.player["alive"]:
        return None
    if action == 2:
        if slot < 15 and struct.unpack_from("<H", s.quest_slots[slot])[0] == qid:
            s.quest_slots[slot] = bytes(24)
            return update(slot)
        return None
    if action != 1 or q.get("auto_accept") or not near_npc(q["giver"]):
        return None
    return assign(q) or None


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
    if (not q or not allowed(q, receiving=True) or slot >= 15
            or not q["receiver"] or not near_npc(q["receiver"])):
        return None
    before = collect_progress()
    return before + (finish(slot, q, choice) or b"") or None


def finish(slot, q, choice=0):
    """One reward transaction shared by explicit and automatic completion."""
    s = sessions.current()
    record = s.quest_slots[slot]
    if struct.unpack_from("<H", record)[0] != q["id"] or record[2] != 2 or s.quest_flags & (1 << q["bit"]):
        return None
    choices = [r for r in q["rewards"] if r[0:2] == (1, 11)]
    if (choices and not 0 <= choice < len(choices)) or (not choices and choice != 0):
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
        selected = 0
        for kind, a, b, c in q["rewards"]:
            if kind == 1:
                if a == 11:
                    selected += 1
                    if selected - 1 != choice:
                        continue
                elif a & CLASS_REWARD:
                    if a & 0xFF != class_id():
                        continue
                elif a:
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
                + update(slot, notify=1) + start_automatic())
    finally:
        if not success:
            s.inventory = original


REPLIES = {0x48E: accept_or_abandon, 0x48F: turn_in, 0x492: objective_report}

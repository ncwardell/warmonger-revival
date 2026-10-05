"""Atomic, versioned character progress; creation records remain untouched."""
import hashlib
import json
import os
import struct

import sessions


def progress_path(account, char_id):
    return sessions.STATE_DIR / "progress" / hashlib.sha256(account.encode()).hexdigest() / f"{char_id}.json"


def read_progress(account, record):
    """Malformed saves fail closed instead of silently resetting a character."""
    path = progress_path(account, struct.unpack_from("<Q", record)[0])
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("version") != 1:
        raise ValueError(f"unsupported progress save: {path}")
    def numbers(values, length, maximum):
        return (isinstance(values, list) and len(values) == length
                and all(type(n) is int and 0 <= n <= maximum for n in values))
    inv = data["inventory"]
    if not (numbers(inv["bag"], 70, 65535) and numbers(inv["count"], 70, 99)
            and numbers(inv["equip"], 2, 65535) and inv["initialized"] is True
            and len(bytes.fromhex(inv["quick"])) == 24
            and type(data["gold"]) is int and 0 <= data["gold"] <= 0xFFFFFFFF
            and type(data["experience"]) is int and 0 <= data["experience"] <= 0xFFFFFFFF
            and type(data["level"]) is int and 1 <= data["level"] <= 30
            and type(data["quest_flags"]) is int and 0 <= data["quest_flags"] < (1 << 320)
            and (data.get("checkpoint_map") is None or
                 (type(data["checkpoint_map"]) is int and data["checkpoint_map"] in (117, 89, 88)))
            and isinstance(data["quest_slots"], list) and len(data["quest_slots"]) == 15
            and all(len(bytes.fromhex(s)) == 24 for s in data["quest_slots"])):
        raise ValueError(f"invalid progress save: {path}")
    return data


def restore_progress(session):
    data = read_progress(session.account, session.record)
    session.inventory = {**sessions.new_inventory(), "initialized": False}
    session.loot = {"gold": struct.unpack_from("<I", session.record, 0x80)[0], "next_uid": 0x3000}
    session.level = max(session.record[0x34], 1)
    session.experience = struct.unpack_from("<I", session.record, 0x30)[0]
    session.quest_slots = [bytes(24) for _ in range(15)]
    session.quest_flags = 0
    session.checkpoint_map = None
    session.saved_progress = ""
    if data is not None:
        session.inventory = {**data["inventory"], "quick": bytes.fromhex(data["inventory"]["quick"])}
        session.loot["gold"] = data["gold"]
        session.level, session.experience = data["level"], data["experience"]
        session.quest_slots = [bytes.fromhex(s) for s in data["quest_slots"]]
        session.quest_flags = data["quest_flags"]
        session.checkpoint_map = data.get("checkpoint_map")


def save_progress(session):
    """Checkpoint durable state before acknowledging it to the client.

    Same-directory replacement is atomic. Keep the previous valid checkpoint as
    .bak. Map checkpoints persist; exact position, HP and drops remain transient.
    """
    if not session.record or not session.inventory.get("initialized"):
        return
    data = {"version": 1, "inventory": {**session.inventory, "quick": session.inventory["quick"].hex()},
            "gold": session.loot["gold"], "level": session.level, "experience": session.experience,
            "quest_slots": [s.hex() for s in session.quest_slots], "quest_flags": session.quest_flags,
            "checkpoint_map": session.checkpoint_map}
    encoded = json.dumps(data, sort_keys=True, indent=1)
    if encoded == session.saved_progress:
        return
    path = progress_path(session.account, struct.unpack_from("<Q", session.record)[0])
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        read_progress(session.account, session.record)
        backup = path.with_suffix(".json.bak")
        backup_tmp = backup.with_suffix(".bak.tmp")
        backup_tmp.write_bytes(path.read_bytes())
        backup_tmp.replace(backup)
    temporary = path.with_suffix(".json.tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        handle.write(encoded)
        handle.flush()
        os.fsync(handle.fileno())
    temporary.replace(path)
    session.saved_progress = encoded


def character_view(account, record):
    """Overlay saved equipment/exp/gold on the original creation record."""
    data = read_progress(account, record)
    if data is None:
        return record
    result = bytearray(record)
    struct.pack_into("<I", result, 0x30, data["experience"])
    result[0x34] = data["level"]
    struct.pack_into("<I", result, 0x80, data["gold"])
    for slot, code in enumerate(data["inventory"]["equip"]):
        result[0x40 + slot * 16:0x50 + slot * 16] = struct.pack("<H", code) + bytes(14)
    return bytes(result)

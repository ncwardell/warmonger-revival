"""Connection state for the Python test server (kept across handler reloads).

Packet functions stay synchronous. A ContextVar selects the connection's state
while a handler runs; monster state is shared and advanced by one server timer.
Named -ologin tokens are development identities, not authenticated accounts.
"""
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field
import hashlib
import json
import os
import pathlib
import secrets
import time


STATE_DIR = pathlib.Path(os.environ.get("WARMONGER_STATE", pathlib.Path(__file__).parent))
CURRENT = ContextVar("warmonger_session", default=None)
CONNECTED = {}
TICKETS = {}


def new_inventory():
    return {"bag": [0] * 70, "count": [0] * 70, "equip": [0, 0], "quick": bytes(0x18)}


@dataclass
class Session:
    uid: int
    send: object
    account: str = ""
    record: bytes = b""
    player: dict = field(default_factory=dict)
    inventory: dict = field(default_factory=new_inventory)
    loot: dict = field(default_factory=lambda: {"gold": 0, "next_uid": 0x3000})
    drops: dict = field(default_factory=dict)
    # Keep each character's experimental progress when returning to selection.
    characters: dict = field(default_factory=dict)

    def __post_init__(self):
        self.reset_player()

    def reset_player(self):
        self.player = {"uid": self.uid, "x": 0.0, "z": 0.0, "heading": 0,
                       "hp": 1000, "mp": 500, "max_hp": 1000, "max_mp": 500,
                       "speed": 450, "alive": True, "revive_at": None,
                       "spawn": (0.0, 0.0), "in_world": False,
                       "map": 117, "scene": 87, "team": 0}


def current():
    return CURRENT.get()


@contextmanager
def use(session):
    token = CURRENT.set(session)
    try:
        yield session
    finally:
        CURRENT.reset(token)


def connect(send):
    # Client FUN_00477d13 branches to player spawn only below 0x3f7.
    uid = next((n for n in range(1, 0x3F7) if n not in CONNECTED), None)
    if uid is None:
        raise ValueError("all player ids are in use")
    session = Session(uid, send)
    CONNECTED[uid] = session
    return session


def same_scene(a, b):
    return (a.player["in_world"] and b.player["in_world"]
            and (a.player["map"], a.player["scene"]) == (b.player["map"], b.player["scene"]))


def broadcast(source, data, include_self=False):
    if not data:
        return
    for other in tuple(CONNECTED.values()):
        if same_scene(source, other) and (include_self or other is not source):
            other.send(data)


def issue_ticket(token):
    # Empty tokens and the launcher's default keep using old characters.json.
    # Other tokens get stable ASCII account names without reflecting token data.
    account = "player" if token in (b"", b"player") else "test-" + hashlib.sha256(token).hexdigest()[:24]
    now = time.monotonic()
    for ticket, (_, expiry) in list(TICKETS.items()):
        if expiry < now:
            del TICKETS[ticket]
    ticket = (secrets.randbits(32), secrets.randbits(32))
    TICKETS[ticket] = (account, now + 120)
    return account, ticket


def authenticate(session, account, ticket):
    if session.account:
        raise ValueError("game connection is already logged in")
    claim = TICKETS.get(ticket)
    if not claim or claim[0] != account or claim[1] < time.monotonic():
        raise ValueError("invalid or expired login ticket")
    if any(s is not session and s.account == account for s in CONNECTED.values()):
        raise ValueError("account already connected; use distinct -ologin names for two clients")
    del TICKETS[ticket]
    session.account = account


def character_path(account):
    if account == "player":
        return STATE_DIR / "characters.json"
    return STATE_DIR / "accounts" / (hashlib.sha256(account.encode()).hexdigest() + ".json")


def load_characters(account):
    path = character_path(account)
    if not path.exists():
        return {}
    records = {int(k): bytes.fromhex(v) for k, v in json.loads(path.read_text()).items()}
    if any(not 0 <= slot < 5 or len(record) != 0x240 for slot, record in records.items()):
        raise ValueError("invalid saved character slots")
    return records


def save_characters(account, records):
    path = character_path(account)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps({k: v.hex() for k, v in records.items()}, indent=1))
    temporary.replace(path)

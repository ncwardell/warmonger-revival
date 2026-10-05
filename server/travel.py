"""Training Ground <-> Camp portal experiment; nation 1, quest-test mode only.

Wire layout: contract/world.yaml, FUN_0048796a / FUN_00473548. The portal
destination is a Teleport_List gate id, not a map id: deviceTrigger records in
ZP01_14 send 1202, and ZP01_13 sends 1203. See docs/testing.md for limits.
"""
import math
import struct

import persistence
import sessions
import world
from proto import build

# Destination gate -> (source map, source arrival anchor, target map, arrival).
# The source trigger is further out than its arrival anchor. A 25-unit radius
# accommodates it; this tolerance and the quest-4 gate are prototype policies.
PORTALS = {1202: (89, (451.64, 3629.45), 88, (325.8, 3438.9)),
           1203: (88, (325.8, 3438.9), 89, (451.64, 3629.45))}
PORTAL_RADIUS = 25.0


def warp(packet):
    """C2S 0x44e (0x28) -> S2C 0x44e (0x2c), never a second 0x2000.

    +0x10 u16 NPC, +0x14 u32 gate, +0x18 dungeon, +0x1c cost,
    +0x20 party, +0x24 world-map flag. Only free, ordinary map portals work.
    """
    s = sessions.current()
    p = s.player
    npc, destination, dungeon, cost, party, worldmap = (
        struct.unpack_from("<H", packet, 0x10)[0],
        *struct.unpack_from("<IIi", packet, 0x14),
        struct.unpack_from("<H", packet, 0x20)[0],
        struct.unpack_from("<H", packet, 0x24)[0])
    route = PORTALS.get(destination)
    if (not world.QUEST_TEST or not p["alive"] or not route
            or npc or dungeon or cost or party or worldmap
            or not s.quest_flags & (1 << 4)):
        return None
    source, anchor, target, arrival = route
    if ((p["map"], p["scene"]) != (source, world.SITES[source][0])
            or not math.isfinite(p["x"]) or not math.isfinite(p["z"])
            or math.hypot(p["x"] - anchor[0], p["z"] - anchor[1]) > PORTAL_RADIUS):
        return None
    old_player = p.copy()
    old_checkpoint = s.checkpoint_map
    old_viewers = [o for o in sessions.CONNECTED.values()
                   if o is not s and sessions.same_scene(s, o)]
    p.update(map=target, scene=world.SITES[target][0], x=arrival[0], z=arrival[1],
             spawn=world.SITES[target][1:])
    s.checkpoint_map = target
    try:
        persistence.save_progress(s)
    except (OSError, ValueError):
        p.clear()
        p.update(old_player)
        s.checkpoint_map = old_checkpoint
        raise
    # Drops are private and transient. Never collect a previous map's loot here.
    s.drops.clear()
    for other in old_viewers:
        other.send(world.remove(s.uid))
    reply = bytearray(0x2C)
    struct.pack_into("<HHff", reply, 0x10, target, p["scene"], *arrival)
    reply[0x1E] = 0xFF
    out = build(0x44E, bytes(reply[16:]), extra=s.uid)
    out += world.join((world.SPAWN_X, world.SPAWN_Z))
    for other in sessions.CONNECTED.values():
        if other is not s and sessions.same_scene(s, other):
            out += world.spawn_player(other)
            other.send(world.spawn_player(s))
    return out


def route_state(_packet):
    """0x445 -> 0x446 (0x7dc) releases the auto-travel wait after a warp.

    FUN_00474eb1 resumes FUN_00598a5f. Empty field/resource records mean no
    active wars in this prototype; no historical land ownership is inferred.
    """
    if not world.QUEST_TEST:
        return None
    packet = bytearray(0x7DC)
    struct.pack_into("<I", packet, 0x10, 1)  # the prototype account's nation
    return build(0x446, bytes(packet[16:]))


REPLIES = {0x44E: warp, 0x445: route_state}

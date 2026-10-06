"""Map portals between the wiki's enabled fields; quest-test mode only.

Wire layout: contract/world.yaml, FUN_0048796a / FUN_00473548. The portal
destination is a Teleport_List gate id in the target field, not a map id:
deviceTrigger records in ZP01_14 send 1202, and ZP01_13 sends 1203. Every
gate pair on the field pages follows that rule (maps.route). NPC teleporters,
dungeon entry and world-map warps are not enabled. See docs/testing.md.
"""
import math
import struct

import maps
import persistence
import sessions
import world
from proto import build

# A trigger sits further out than its gate's arrival point; a 25-unit radius
# accommodates it. The radius and per-gate quest requirements are test policies.
PORTAL_RADIUS = 25.0
# destination gate -> completion bit required (leave Training Ground after quest 4)
REQUIRES_BIT = {1202: 4}


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
    route = maps.route(destination, p["map"]) if p["map"] in world.SITES else None
    bit = REQUIRES_BIT.get(destination)
    if (not world.QUEST_TEST or not p["alive"] or not route
            or npc or dungeon or cost or party or worldmap
            or (bit and not s.quest_flags & (1 << bit))):
        if world.QUEST_TEST and not route:
            world.log(f"portal: no route to gate {destination} from map {p['map']}")
        return None
    sources, target, *arrival = route
    if (p["scene"] != world.SITES[p["map"]][0]
            or not math.isfinite(p["x"]) or not math.isfinite(p["z"])
            or min(math.hypot(p["x"] - x, p["z"] - z) for x, z in sources) > PORTAL_RADIUS):
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

"""Maps, gates and town NPCs for quest-test mode, read from the committed wiki.

Terrain is chosen by x/z alone and sceneidx is a server instance id
(docs/spec/loading.md section 4), so every enabled field uses its field id as
its scene. Gates are the client's Teleport_List rows on each field page: a map
portal trigger sends the gate in the *destination* field whose link points back
to the sender's field (contract/world.yaml 0x44e; FUN_0048796a). Town NPC
positions are video/image measurements in docs/gameplay, copied onto NPC pages.
"""
import gamedata

NATION = "Arslan"  # the prototype account's nation (handlers.NATION 1)
# Dungeons, arenas and event maps need their own entry flow; other nations'
# home maps are closed to this nation. Both are test-server policies.
KINDS = ("town", "field", "land")
# Spawn points checked on the original navmesh (tools/navmesh.py). Other maps
# use their lowest client gate arrival; reconnecting there is a server policy.
CHECKED_SPAWNS = {89: (419.0, 3661.0), 88: (325.8, 3438.9)}


def _fields():
    return {fid: page for fid, page in gamedata.pages("fields").items()
            if page.get("kind") in KINDS and page.get("nation") in (None, NATION)}


def _gates():
    """gate id -> (field, x, z, linked field) for every client gate."""
    gates = {}
    for fid, page in gamedata.pages("fields").items():
        for gate in page.get("gates") or []:
            gid = gamedata.integer(gate["gate"], 0, 0xFFFF)
            if not gid:
                continue  # field 87's placeholder row
            if gid in gates:
                raise ValueError(f"gate {gid} is listed on two field pages")
            gates[gid] = (fid, gamedata.number(gate["x"]), gamedata.number(gate["z"]),
                          gamedata.integer(gate["to_field"], 0, 0xFFFF))
    return gates


def _sites(fields, gates):
    sites = {}
    for fid in fields:
        if fid in CHECKED_SPAWNS:
            sites[fid] = (fid, *CHECKED_SPAWNS[fid])
            continue
        own = sorted(g for g, row in gates.items() if row[0] == fid)
        if own:
            sites[fid] = (fid, gates[own[0]][1], gates[own[0]][2])
    return sites


def _npcs(sites):
    """(unit id, name, map, x, z) for NPC pages placed on an enabled map."""
    placed = []
    for uid, page in sorted(gamedata.pages("npcs").items()):
        if page.get("map") in sites and page.get("x") is not None and page.get("z") is not None:
            placed.append((uid, page["title"], page["map"],
                           gamedata.number(page["x"]), gamedata.number(page["z"])))
    return placed


FIELDS = _fields()
GATES = _gates()
SITES = _sites(FIELDS, GATES)
NPCS = _npcs(SITES)


def route(destination, field):
    """Validate a map-portal destination gate sent from `field`.

    Returns (source gate positions, target field, arrival x, z) or None. The
    destination must be an enabled field's gate linked back to `field`, and
    `field` must have a gate linked to the destination's field.
    """
    row = GATES.get(destination)
    if row is None:
        return None
    target, x, z, back = row
    if target == field or back != field or target not in SITES:
        return None
    sources = [(gx, gz) for gfield, gx, gz, to in GATES.values() if gfield == field and to == target]
    return (sources, target, x, z) if sources else None

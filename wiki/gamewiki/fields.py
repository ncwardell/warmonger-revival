"""Fields: one page per field (SceneList / FieldNames id) -- a map a player can
be in: Gaia lands, towns, home areas, abyss fields, dungeons, the arena.

Shared data and the meaning of every client column: maps.py.

Front matter the server loads (beyond the bookkeeping keys):
  kind            town | land | dungeon | arena | field | event_dungeon
                  (SceneList type 1/2/3/4/5/6; names *inferred*)
  max_users, group, scene_c4, neighbours   SceneList columns
  nation, nation_copies  {"Arslan": id, "Erion": id, "Armia": id}
  zones, segments        ZoneDB rectangles and the ZPxx_zz terrain segments
  worldmap_rect          WorldmapData (UI pixels on the world-map panel)
  gates           every Teleport_List row of the field: where a player
                  arrives when sent to that gate, and where it leads
  connections     REQUIRED. [{"to": field, "gate": id, "to_gate": id}]; an
                  exit gate of a dungeon has "to": null ("back where you came
                  from"). Hand-added rows are kept.
  npcs            REQUIRED (towns, lands, fields). UnitDB ids of the NPCs that
                  stand here. From quests (start NPC, talk targets in this
                  field), docs/gameplay/npc-locations.md tables and npc pages.
  monsters        REQUIRED (not towns/arena). UnitDB ids. From quest kill
                  objectives in this field, dungeon bosses
                  (docs/gameplay/maps-and-dungeons.md) and monster pages.
  spawn_points    REQUIRED (lands, fields, dungeons). Where monsters spawn:
                  [{"unit": id, "x": .., "z": .., "count": n, "radius": r,
                  "respawn_s": s}]. Not in the client (the server spawned
                  them): copied from monster pages' 'spawns' that carry x/z,
                  otherwise entered by hand.
  triggers        client-placed objects (Trigger.cdb): talk devices and
                  gathering nodes, with positions; loaded as they are.
"""
from . import common, maps
from .common import Page, table_md

TYPE = "fields"
KIND = "field"
LABEL = "Field"
PLURAL = "Fields (maps)"
DESCRIPTION = ("Every field (map) in the client's `SceneList` / `FieldNames` tables: the Gaia lands, "
               "the towns and home areas of each nation, the abyss fields, the dungeons and the arena. "
               "Each page lists the gates in and out, the NPCs, monsters and gathering nodes, the "
               "terrain zones and navmesh segments. See also [[wiki/zones/index|Zones]] and "
               "[[wiki/dungeons/index|Dungeons]].")
REQUIRED = ["spawn_points", "monsters", "npcs", "connections"]
UNION_KEYS = ["connections", "npcs", "monsters", "spawn_points"]

# Which REQUIRED keys apply to which kind of field. A town has no monsters,
# a dungeon no NPCs to place, the arena only its gates.
REQUIRED_BY_KIND = {
    "town": ["npcs", "connections"],
    "land": ["spawn_points", "monsters", "connections"],
    "field": ["spawn_points", "monsters", "npcs", "connections"],
    "dungeon": ["spawn_points", "monsters", "connections"],
    "event_dungeon": ["spawn_points", "monsters", "connections"],
    "arena": [],          # entered from the UI; gates 1401/1402 are team starts
}


def gate_kind(field, g, dungeon=False):
    """gate (to another field) | exit (dungeon entrance: leaving returns the
    player to where they came from) | portal (pair inside the field) |
    spawn (links to itself: an arrival point only)."""
    if dungeon and (g.get("label") or "").startswith("FieldName_") and g["to_field"] in (0, field):
        return "exit"
    if g["to_field"] == field and g["to_gate"] == g["gate"]:
        return "spawn"
    if g["to_field"] == field or (g["label"] == "FiledPortal" and g["to_field"] in (0, field)):
        return "portal"
    if g["to_field"] == 0:
        return "exit"
    return "gate"


def build(ctx):
    ix = maps.index(ctx)
    for fid in ix.field_ids:
        sc = ix.scenes.get(fid)
        f = {}
        sources = []
        if sc is not None:
            sources.append("client: SceneList.cdb id %d" % fid)
            f["name_key"] = sc.str("nameKey")
            f["kind"] = maps.SCENE_KINDS.get(sc.int("type"), "type %d" % sc.int("type"))
            f["scene_type"] = sc.int("type")
            f["max_users"] = sc.int("maxUsers")
            f["group"] = sc.int("group")
            if sc.int("c4"):
                f["scene_c4"] = sc.int("c4")
            if sc.int("c10"):
                f["scene_c10"] = sc.int("c10")
            nb = [sc.int("link%d" % n) for n in (1, 2, 3) if sc.int("link%d" % n)]
            if nb:
                f["neighbours"] = nb
        else:
            sources.append("client: FieldNames.cdb id %d (no SceneList row)" % fid)
            f["name_key"] = "FieldName_%d" % fid if ctx.s("FieldName_%d" % fid) else None
            f["kind"] = None
        kind = f.get("kind")
        if fid in ix.copies:
            trip, src = ix.copies[fid]
            f["nation"] = maps.nation_of(ix, fid)
            f["nation_copies"] = {maps.NATIONS[i + 1]: trip[i] for i in range(3)}
            if src not in sources:
                sources.append(src)
        zs = ix.field_zones.get(fid, [])
        if zs:
            f["zones"] = zs
            segs = []
            for z in zs:
                for s in ix.segments(z):
                    if maps.seg_name(*s) not in segs:
                        segs.append(maps.seg_name(*s))
            f["segments"] = segs
            src = ix.zone_source.get(fid)
            if src and src not in sources:
                sources.append(src)
        if fid in ix.worldmap:
            f["worldmap_rect"] = ix.worldmap[fid]
        gates = ix.gates.get(fid, [])
        if gates:
            sources.append("client: Teleport_List.cdb field %d" % fid)
            f["gates"] = [{k: v for k, v in g.items() if k != "field" and not (k in ("x2", "z2", "x3", "z3") and v in (0, g[k[0]]))}
                          for g in gates]
        conns = []
        is_dungeon = kind in ("dungeon", "event_dungeon")
        for g in gates:
            k = gate_kind(fid, g, is_dungeon)
            if k == "gate":
                c = {"to": g["to_field"], "gate": g["gate"], "to_gate": maps.paired_gate(ix, fid, g)}
                if not g["to_gate"] and c["to_gate"]:
                    c["paired"] = True       # linked gate 0: the target's gate back here
                conns.append(c)
            elif k == "exit":
                conns.append({"to": None, "gate": g["gate"], "kind": "exit"})
        f["connections"] = conns
        # NPCs
        pnpcs, pmons, pspawns = ix.page_units(ctx, fid)
        npcs = []
        for u in sorted(ix.quest_npcs.get(fid, {})):
            npcs.append(u)
        if ix.quest_npcs.get(fid) or ix.quest_kills.get(fid):
            sources.append("client: Quest.cdb (quests and objectives in field %d)" % fid)
        for u, sec in sorted(ix.doc_npcs.get(fid, {}).items()):
            if u not in npcs:
                npcs.append(u)
            s = "doc: gameplay/npc-locations § %s" % sec
            if s not in sources:
                sources.append(s)
        for u in sorted(pnpcs):
            if u not in npcs:
                npcs.append(u)
        f["npcs"] = [u for u in npcs if ctx.unit_type(u) != "monsters"] + \
            [u for u in npcs if ctx.unit_type(u) == "monsters" and u not in ix.quest_kills.get(fid, {})]
        # monsters
        mons = [u for u in sorted(ix.quest_kills.get(fid, {}))]
        boss = ix.doc_boss.get(fid)
        if boss:
            for u in boss[0]:
                if u not in mons:
                    mons.append(u)
            sources.append("doc: gameplay/maps-and-dungeons § %s (boss)" % boss[2])
        for u in sorted(pmons):
            if u not in mons:
                mons.append(u)
        f["monsters"] = mons
        f["spawn_points"] = pspawns
        trig = ix.triggers.get(fid, [])
        if trig:
            sources.append("client: Trigger.cdb field %d" % fid)
            f["triggers"] = [trigger_entry(r) for r in trig]
        if fid in ix.dungeon_ids:
            f["dungeon"] = fid
        req = REQUIRED_BY_KIND.get(kind, REQUIRED)
        yield Page(TYPE, fid, ctx.title(TYPE, fid), fields=f, sources=sources, body=body, required=req)


def trigger_entry(r):
    e = {"id": r.int("id"), "type": r.int("type"), "shape": r.int("shape"),
         "x": maps.num(r.get("x")), "z": maps.num(r.get("z")), "name_key": r.str("name_key")}
    if r.int("item_or_quest"):
        e["item"] = r.int("item_or_quest")
    if r.int("model"):
        e["model"] = r.int("model")
    return e


# ------------------------------------------------------------------ rendering

def unit_cell(ctx, u):
    if ctx.table("UnitDB").get(u) is None:
        return "unit %d (not in UnitDB)" % u
    return ctx.unit_link(u)


def field_cell(ctx, f):
    return ctx.link(TYPE, f) if f else "—"


def body(ctx, page):
    ix = maps.index(ctx)
    fm, fid = page.fm, page.id
    L = []
    info = []
    zs = [z for z in fm.get("zones") or [] if isinstance(z, int)]
    img = None
    if fid in ix.dungeon_ids and ctx.image("dungeons", fid):
        img = ctx.image("dungeons", fid)
    for z in zs[:1]:
        if ctx.image("zones", z):
            info.append(("", "![minimap of zone %d](%s)" % (z, ctx.image("zones", z))))
    if img:
        info.append(("", "![%s](%s)" % (common.link_text(page.title), img)))
    info.append(("Field id", "`%d`" % fid))
    if fm.get("kind"):
        info.append(("Kind", "%s (SceneList type %s; name *inferred*)" % (fm["kind"].replace("_", " "), fm.get("scene_type", "?"))))
    if fm.get("max_users"):
        info.append(("Max users", "%s (SceneList, column meaning *guessed*)" % fm["max_users"]))
    if fm.get("group") is not None and fm.get("scene_type") is not None:
        info.append(("Region group", "%s (SceneList last column)" % fm["group"]))
    if fm.get("nation"):
        info.append(("Nation", fm["nation"]))
    nc = fm.get("nation_copies")
    if isinstance(nc, dict):
        info.append(("Nation copies", ", ".join("%s %s" % (k, ctx.link(TYPE, v, "%s (%d)" % (k, v)) if v != fid else "**%d**" % v)
                                                for k, v in nc.items())))
    if zs:
        info.append(("Zones", ", ".join(ctx.link("zones", z) for z in zs)))
    if fm.get("segments"):
        info.append(("Terrain segments", ", ".join("`%s`" % s for s in fm["segments"])))
    if fm.get("worldmap_rect"):
        info.append(("World-map rectangle", "`%s` (WorldmapData, panel pixels)" % fm["worldmap_rect"]))
    if fm.get("dungeon"):
        info.append(("Dungeon", ctx.link("dungeons", fid, "dungeon page")))
    if fm.get("name_key"):
        info.append(("Name key", "`%s`" % fm["name_key"]))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))
    if fm.get("kind") == "land":
        L += ["A land of Gaia. Who owns it (Arslan, Erion, Armia or monsters) changes in play and is "
              "server state; see [[gameplay/maps-and-dungeons|Maps and dungeons]] §1 and §4.", ""]

    # connections
    gates = [g for g in (fm.get("gates") or []) if isinstance(g, dict)]
    rows = []
    for g in gates:
        k = gate_kind(fid, {"to_field": g.get("to_field", 0), "to_gate": g.get("to_gate", 0),
                            "gate": g.get("gate"), "label": g.get("label", "")},
                      fm.get("kind") in ("dungeon", "event_dungeon"))
        to = {"gate": field_cell(ctx, g.get("to_field")), "exit": "entrance / exit (leaving returns you to the field you came from)",
              "portal": "portal to gate %s in this field" % g.get("to_gate"), "spawn": "arrival / spawn point only"}[k]
        arr = g.get("to_gate") or "—"
        if not g.get("to_gate") and k == "gate":
            pg = maps.paired_gate(ix, fid, {"to_gate": 0, "to_field": g.get("to_field", 0)})
            arr = "%s (paired, *inferred*)" % pg if pg else "—"
        at = maps.pos(g.get("x", 0), g.get("z", 0)) if g.get("x") or g.get("z") else "no position (0, 0)"
        rows.append((g.get("gate"), at, to, arr, g.get("label", "")))
    L += ["### Gates and connections", ""]
    if rows:
        L += ["`Teleport_List` rows of this field. A player sent to a gate id arrives at that "
              "gate's position (`server/travel.py`); the gate's own trigger is the portal object "
              "a little further out (*client*).", "", table_md(["gate", "at (x, z)", "leads to", "arrives at gate", "label"], rows)]
    else:
        L += ["No `Teleport_List` row: the client places no gate here.", ""]
    hand_conns = [c for c in (fm.get("connections") or []) if isinstance(c, dict)
                  and not any(c.get("gate") == g.get("gate") for g in gates)]
    if hand_conns:
        L += ["Other connections (hand-entered): " + "; ".join(
            ", ".join("%s %s" % kv for kv in c.items()) for c in hand_conns), ""]
    inbound = ix.gates_in.get(fid, [])
    if inbound:
        L += ["Entered from: " + ", ".join("%s (gate %d → %s)" % (ctx.link(TYPE, g["field"]), g["gate"], maps.paired_gate(ix, g["field"], g) or "?")
                                         for g in inbound), ""]
    if fm.get("neighbours"):
        L += ["Neighbouring lands (`SceneList` link columns): " +
              ", ".join(ctx.link(TYPE, n) for n in fm["neighbours"] if isinstance(n, int)), ""]

    # NPCs
    npcs = [u for u in fm.get("npcs") or [] if isinstance(u, int)]
    pnpcs, pmons, _sp = ix.page_units(ctx, fid)
    L += ["### NPCs", ""]
    if npcs:
        rows = []
        for u in npcs:
            why = []
            qs = ix.quest_npcs.get(fid, {}).get(u)
            if qs:
                why.append("quests " + ", ".join(ctx.link("quests", q, str(q)) for q in qs[:5]) + (" …" if len(qs) > 5 else ""))
            if u in ix.doc_npcs.get(fid, {}):
                sec = ix.doc_npcs[fid][u]
                why.append("[[gameplay/npc-locations#%s|NPC locations § %s]]" % (maps.section_anchor(sec), common.link_text(sec)))
            npc_fm = ctx.pages("npcs").get(u) or {}
            where = ""
            for p in [npc_fm] + [p for p in npc_fm.get("positions") or [] if isinstance(p, dict)]:
                if p.get("field", p.get("map")) == fid and isinstance(p.get("x"), (int, float)) \
                        and isinstance(p.get("z"), (int, float)):
                    where = maps.pos(p["x"], p["z"])
                    break
            if u in pnpcs:
                why.append("NPC page (`map` / `positions`)")
            if not why:
                why.append("hand-entered")
            rows.append((unit_cell(ctx, u), u, where, "; ".join(why)))
        L += ["Positions come from the NPC's own page (`x`, `z`). The client does not place town "
              "NPCs; the server spawns them ([[gameplay/npc-locations|NPC locations]] §1).", "",
              table_md(["NPC", "unit", "position", "why it is listed"], rows)]
    else:
        L += ["None known yet.", ""]

    # monsters
    mons = [u for u in fm.get("monsters") or [] if isinstance(u, int)]
    L += ["### Monsters", ""]
    if mons:
        rows = []
        boss = ix.doc_boss.get(fid)
        for u in mons:
            why = []
            qs = ix.quest_kills.get(fid, {}).get(u)
            if qs:
                grp = ix.group_of.get((fid, u))
                why.append("kill objective of quest " + ", ".join(ctx.link("quests", q, str(q)) for q in qs[:5]) +
                           (" (kill group %d, UnitDB i32@80)" % grp if grp else ""))
            if boss and u in boss[0]:
                why.append("boss ([[gameplay/maps-and-dungeons#%s|Maps and dungeons]])" % maps.section_anchor(boss[2]))
            if u in pmons:
                why.append("monster page (`spawns` / `spawn_fields`)")
            rows.append((unit_cell(ctx, u), u, "; ".join(why) or "hand-entered"))
        L += [table_md(["monster", "unit", "why it is listed"], rows)]
    else:
        L += ["None known yet.", ""]

    # spawn points
    sp = [s for s in fm.get("spawn_points") or [] if isinstance(s, dict)]
    L += ["### Spawn points", ""]
    if sp:
        keys = []
        for s in sp:
            for k in s:
                if k not in keys:
                    keys.append(k)
        L += [table_md(keys, [[s.get(k, "") if k != "unit" else unit_cell(ctx, s[k]) if isinstance(s.get(k), int) else s.get(k)
                               for k in keys] for s in sp])]
    else:
        L += ["Monster spawn positions are not in the client data (`map.jpk` has no spawn files; "
              "[[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, "
              "`z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).", ""]
    srv = server_site(fid)
    if srv:
        L += [srv, ""]

    # triggers
    trig = [t for t in fm.get("triggers") or [] if isinstance(t, dict)]
    if trig:
        L += ["### Client-placed objects (`Trigger`)", "",
              "Talk devices (shape 4) and gathering nodes (type 0, shape 5: the item is what gathering "
              "gives). The server can load these as they are; the video check in "
              "[[gameplay/video-dungeon-run|Nas Village dungeon run]] §5 matched them within 5 units.", ""]
        rows = []
        for t in trig:
            nm = ctx.s(t.get("name_key")) or t.get("name_key") or ""
            what = ctx.link("items", t["item"]) if t.get("item") else ""
            rows.append((ctx.link("nodes", t["id"], str(t["id"])) if isinstance(t.get("id"), int) else t.get("id"),
                         "node" if t.get("shape") == 5 else "talk/device", nm, what,
                         maps.pos(t.get("x", 0), t.get("z", 0)), t.get("type"), t.get("model", "")))
        L.append(table_md(["trigger", "kind", "name", "gives", "at (x, z)", "type", "model"], rows))
        away = ix.trigger_elsewhere.get(fid)
        if away:
            same = sorted({f for z in away for f in ix.zone_fields.get(z, []) if f != fid})
            L += ["> [!warning] Trigger positions outside this field",
                  "> Some `Trigger` rows of this field lie in %s, not in the zone of its gates. %s"
                  "The server should not use these positions as they are (*client data; cause unknown*)." % (
                      ", ".join(ctx.link("zones", z) for z in away),
                      ("That zone belongs to %s; the rows look copied from it without moving them. " %
                       ", ".join(ctx.link(TYPE, f) for f in same)) if same else ""), ""]

    # quests
    qs = ix.quest_fields.get(fid, [])
    if qs:
        L += ["### Quests in this field", "",
              ", ".join(ctx.link("quests", q) for q in qs[:40]) + (" and %d more" % (len(qs) - 40) if len(qs) > 40 else ""), ""]

    # dungeon / events
    if fid in ix.dungeon_ids:
        L += ["### Dungeon", "", "Entry cost, rewards, boss and schedule: %s." % ctx.link("dungeons", fid), ""]

    # navmesh
    segs = fm.get("segments") or []
    if segs:
        rows = []
        for s in segs:
            nav = ix.has("map/navi/%s_00.nav" % s)
            zp = ix.has("map/%s_00.zp" % s)
            rows.append((s, {True: "yes", False: "no", None: "?"}[nav], {True: "yes", False: "no", None: "?"}[zp]))
        L += ["### Navmesh", "",
              "Segments covered by this field's zones (256 × 256 units each). Check a point with "
              "`tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).", "",
              table_md(["segment", "navmesh (.nav)", "terrain (.zp)"], rows)]

    refs = maps.doc_refs(ctx).get(("fields", fid), [])
    ment = [m for m in ctx.mentions(page.title) if not any(m[0] == r[0] for r in refs)]
    if refs or ment:
        L += ["### Mentioned in", ""] + maps.ref_lines(refs)
        L += ["- [[%s|%s]] (by name)" % m for m in ment[:8]]
        L.append("")
    return "\n".join(L)


def server_site(fid):
    """What server/world.py does with this field today (our choice, not
    original data)."""
    import ast
    try:
        tree = ast.parse((common.REPO / "server" / "world.py").read_text(encoding="utf-8"))
    except (OSError, SyntaxError):
        return None
    sites, mons = {}, []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            names = [getattr(t, "id", "") for t in node.targets]
            try:
                if "SITES" in names:
                    sites = ast.literal_eval(node.value)
                elif "MONSTERS" in names:
                    mons = ast.literal_eval(node.value)
            except ValueError:
                pass
    if fid not in sites:
        return None
    scene, x, z = sites[fid]
    txt = "Current server (`server/world.py`, our choice, not original data): players appear at (%s) in scene %s." % (
        maps.pos(x, z), scene)
    if fid == 117 and mons:
        txt += " The tutorial monsters are placed around it: " + ", ".join(
            "%s (%d) at offset %s" % (m[1], m[0], maps.pos(m[4], m[5])) for m in mons) + "."
    return txt

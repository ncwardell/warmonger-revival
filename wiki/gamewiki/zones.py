"""Zones: one page per ZoneDB row -- a rectangle of world terrain with its own
minimap (map/minimap/minimap_z<zone>_00.dds; docs/wiki/assets/zones/<id>.png).

ZoneDB (CP949 CSV, loader FUN_0046028a): id, Korean name, x0 z0 x1 z1
(world units, inclusive), terrain name (also the Setting/weather/<name>.dat
lighting file). The page title is an English gloss of the Korean name
(maps.GLOSS); the original is kept as name_kr. Which fields lie in a zone
is worked out in maps.py (gate and trigger positions inside the rectangle).

The minimap texture covers the rectangle x0..x1+1, z0..z1+1 with z up; for a
non-square zone it is the square of the long side, centred
(docs/gameplay/npc-locations §2, video-dungeon-run §5).

REQUIRED: fields (empty for zones no field uses: tests, leftovers). Zones
that are UI scenes (login, character select, logo) require nothing.
"""
from . import common, maps
from .common import Page, table_md

TYPE = "zones"
KIND = "zone"
LABEL = "Zone"
DESCRIPTION = ("Every terrain zone in the client's `ZoneDB` table, with its minimap: the world "
               "rectangle, the terrain segments and navmesh, and the [[wiki/fields/index|fields]] "
               "that use it. Names are English glosses of the Korean ZoneDB names.")
REQUIRED = ["fields"]


def name(ctx, id_):
    ix = maps.index(ctx)
    z = ix.zones.get(id_)
    if not z:
        return None
    g = maps.gloss(z["name_kr"])
    fl = ix.zone_fields.get(id_, [])
    fname = common.clean_name(ctx.name("fields", fl[0]) or "") if fl else None
    if g and fname and fname.lower() not in g.lower():
        g = "%s (%s)" % (g, fname)
    return g or None


def build(ctx):
    ix = maps.index(ctx)
    for zid, z in sorted(ix.zones.items()):
        f = {"name_kr": z["name_kr"], "terrain": z["map"],
             "bounds": {"x0": z["x0"], "z0": z["z0"], "x1": z["x1"], "z1": z["z1"]}}
        if z["x1"] > z["x0"]:
            f["size"] = [z["x1"] - z["x0"] + 1, z["z1"] - z["z0"] + 1]
        f["segments"] = [maps.seg_name(*s) for s in ix.segments(zid)]
        f["fields"] = sorted(ix.zone_fields.get(zid, []))
        f["minimap"] = "map/minimap/minimap_z%d_00.dds" % zid if ix.has("map/minimap/minimap_z%d_00.dds" % zid) else None
        sources = ["client: ZoneDB.cdb id %d" % zid]
        if f["fields"]:
            srcs = {ix.zone_source.get(fid) for fid in f["fields"]} - {None}
            sources += sorted(srcs)
        req = [] if z["name_kr"] in maps.UI_ZONES else REQUIRED
        yield Page(TYPE, zid, ctx.title(TYPE, zid), fields=f, sources=sources, body=body, required=req)


def body(ctx, page):
    ix = maps.index(ctx)
    fm, zid = page.fm, page.id
    z = ix.zones.get(zid, {})
    L, info = [], []
    img = ctx.image(TYPE, zid)
    if img:
        info.append(("", "![minimap of %s](%s)" % (common.link_text(page.title), img)))
    info.append(("Zone id", "`%d`" % zid))
    info.append(("ZoneDB name", "%s (English gloss: %s)" % (z.get("name_kr"), page.title)))
    info.append(("Terrain name", "`%s`" % z.get("map")))
    b = fm.get("bounds") or {}
    if isinstance(b, dict) and b.get("x1", 0) > b.get("x0", 0):
        info.append(("Rectangle", "x %s–%s, z %s–%s (%s × %s units)" % (
            b.get("x0"), b.get("x1"), b.get("z0"), b.get("z1"),
            b.get("x1", 0) - b.get("x0", 0) + 1, b.get("z1", 0) - b.get("z0", 0) + 1)))
    else:
        info.append(("Rectangle", "empty (all zero)"))
    fl = [f for f in fm.get("fields") or [] if isinstance(f, int)]
    if fl:
        info.append(("Fields", ", ".join(ctx.link("fields", f) for f in fl)))
    if fm.get("minimap"):
        info.append(("Minimap", "`%s`" % fm["minimap"]))
    fog = ix.has("map/fogmap/Fog_z%d.dds" % zid)
    if fog:
        info.append(("Fog map", "`map/fogmap/Fog_z%d.dds`" % zid))
    if z.get("map") in ix.weather:
        info.append(("Lighting", "`Setting/weather/%s.dat`" % z.get("map")))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))
    if not fl:
        L += ["No field is known to use this zone: no gate or trigger lies inside it. It may be a test, "
              "a UI scene or a leftover. Add `fields:` if you know better.", ""]

    segs = fm.get("segments") or []
    if segs:
        rows = []
        for s in segs:
            nav = ix.has("map/navi/%s_00.nav" % s)
            zp = ix.has("map/%s_00.zp" % s)
            rows.append((s, {True: "yes", False: "no", None: "?"}[nav], {True: "yes", False: "no", None: "?"}[zp]))
        L += ["### Segments", "",
              "Terrain segments `ZPxx_zz` (x = column, z = row; 256 × 256 units) the rectangle "
              "touches. Navmesh format and the walkability check: [[spec/navmesh|Navmesh]].", "",
              table_md(["segment", "navmesh (.nav)", "terrain (.zp)"], rows)]

    others = []
    for oid, o in sorted(ix.zones.items()):
        if oid == zid or o["x1"] <= o["x0"] or not b or b.get("x1", 0) <= b.get("x0", 0):
            continue
        if o["x0"] <= b["x1"] and b["x0"] <= o["x1"] and o["z0"] <= b["z1"] and b["z0"] <= o["z1"]:
            others.append(oid)
    if others:
        L += ["### Overlapping zones", "", ", ".join(ctx.link(TYPE, o) for o in others), ""]

    refs = maps.doc_refs(ctx).get(("zones", zid), [])
    if refs:
        L += ["### Mentioned in", ""] + maps.ref_lines(refs) + [""]
    return "\n".join(L)

"""Shared data for the map-type pages: fields (fields.py), zones (zones.py) and
dungeons (dungeons.py). This module has no build(), so it is not an entity
type itself; build the three with

  python3 -m wiki.gamewiki build fields zones dungeons

What the words mean here
========================

* **field** = a scene the server puts a player in (SceneList / FieldNames id,
  the "map id" of 0x2000 and 0x44e). Several fields can share one piece of
  terrain (the three nation copies of the Training Camp are three fields on
  three zones; the Fortress is one field, 120, on three zones).
* **zone** = a ZoneDB rectangle of world terrain with its own minimap
  (map/minimap/minimap_z<zone>_00.dds). Zones are geometry: world x/z, 256
  units per terrain segment ZPxx_zz (x = segment column, z = segment row).
* **dungeon** = a field you enter through the dungeon panel
  (DungeonAdmission / Dungeon / Event_Dungeon); its page id is the field id.

Client sources (data/tables/*.tsv; docs/spec/data-tables.md)
-------------------------------------------------------------
  SceneList      field id, name key, type (1 town, 2 land, 3 dungeon, 4 arena,
                 5 field, 6 event dungeon -- meanings *inferred* from the
                 rows), c4, max users, 3 neighbour links, region group
  FieldNames     id -> English name (also ids 102/112/116/118/119 that have no
                 SceneList row)
  Teleport_List  gates: id, field, x/z (three copies x/z, x2/z2, x3/z3),
                 linked gate + field, label ('FiledPortal' = a portal pair
                 inside the field). A gate's x/z is where a player arrives
                 when a portal sends them to that gate id (server/travel.py).
  Trigger        client-placed objects per field: quest/talk devices (shape 4)
                 and gathering nodes (type 0, shape 5, item_or_quest = item)
  ZoneDB         zone rectangles (x0 z0 x1 z1 inclusive) + terrain name
  WorldmapData   a field's rectangle on the world-map panel (UI pixels)
  Quest          map1..3 / obj*_map1..3 = the Arslan / Erion / Armia copies of
                 the field a quest or objective is in; start NPC, talk targets
                 (obj type 4) and kill targets (obj type 1) per field
  map.jpk        which segments have a navmesh (map/navi/ZPxx_zz_00.nav),
                 terrain (.zp) and fog map; read with tools/jpk.py
  weather        Setting/weather/<terrain>.dat per terrain name

Hand-written sources pulled in (docs/gameplay)
----------------------------------------------
  npc-locations.md     tables "Unit id" per section "(field N)" / "(fields
                       a / b / c)" -> the field's npcs; "Field ids (Arslan /
                       Erion / Armia)" -> nation copies
  maps-and-dungeons.md the border-area table (Field id, Boss (UnitDB id),
                       Gear tier) -> dungeon boss and gear tier
  every page           lines that name a field ("field 124", "fields 88 / 92 /
                       96", "FieldNames 88-98") or a zone ("ZoneDB 126") are
                       listed under "Mentioned in", with the first video
                       timestamp on the line
FACTS (below) holds the few other numbers copied from docs/gameplay, each
with its source.

Other wiki pages read (front matter, written by other modules or people)
------------------------------------------------------------------------
  monsters  'spawns': [{"field": id, "x", "z", ...}] or [field ids], 'spawn_fields'
            -> the field's monsters and spawn_points
  npcs      'map', 'x', 'z', 'positions': [{"field", "x", "z"}] -> the field's npcs
"""
import re

from . import common

NATIONS = {1: "Arslan", 2: "Erion", 3: "Armia"}
SCENE_KINDS = {1: "town", 2: "land", 3: "dungeon", 4: "arena", 5: "field", 6: "event_dungeon"}

# Field -> zones the client data cannot place (no gate or trigger in the
# field). Each with its source.
ZONE_HINTS = {
    117: ([2], "doc: spec/navmesh (tutorial spawn in ZoneDB 2 tutorial_map_01)"),
    120: ([103, 104, 105], "doc: gameplay/npc-locations §2 (Fortress = ZoneDB 103-105, one per nation)"),
    133: ([126], "doc: gameplay/video-dungeon-run §1 (Nas Village Entrance geometry = ZoneDB 126; guess)"),
}

# Korean ZoneDB names -> English gloss (title of zone pages).
GLOSS = [
    ("케릭터 선택창", "Character select"), ("C마을_더미상점가", "Town C dummy shop street"),
    ("전장 튜토리얼", "Battlefield tutorial"), ("튜토리얼맵", "Tutorial map"),
    ("튜토리얼존", "Tutorial zone"), ("배틀아레나", "Battle arena"), ("필드던전", "Field dungeon"),
    ("이벤트던전", "Event dungeon"), ("운명의탑_지하", "Tower of Fate basement"),
    ("탑지하", "Tower basement"), ("해골묘지", "Skull cemetery"), ("경계지역", "border area"),
    ("언더월드", "Underworld"), ("대도시", " Castle (big city)"), ("캠핑장", "Training Camp"),
    ("훈련장", "Training Ground"), ("어비스", "Abyss"), ("코어실", "Room of Core"),
    ("신장실", "Room of the Fortress Keeper"), ("요새", "Fortress"), ("마을", "Town "),
    ("필드", "Field "), ("인던", "Instance dungeon "), ("던전", "Dungeon"), ("사용안함", "unused"),
    ("신규", "new"), ("기본", "default"), ("로그인", "login"), ("테스트", "test"),
    ("데몬", "demon"), ("리자드맨", "lizardman"), ("유령", "ghost"), ("오크", "orc"),
    ("드래곤", "dragon"),
]
UI_ZONES = {"Logo", "Create", "login", "로그인", "케릭터 선택창"}


def gloss(kr):
    s = kr or ""
    for k, v in GLOSS:
        s = s.replace(k, v)
    s = re.sub(r"\s+", " ", s.replace("_", " ")).strip()
    s = re.sub(r"\s+\)", ")", s)
    return s[:1].upper() + s[1:] if s else s


def num(v):
    try:
        f = float(v)
    except (TypeError, ValueError):
        return 0
    return int(f) if f.is_integer() else round(f, 2)


def seg_name(sx, sz):
    return "ZP%02d_%02d" % (sx, sz)


# --------------------------------------------------------------- doc scanning

FIELD_REF = re.compile(
    r"\b(?:client\s+)?fields?\s*\*{0,2}\s*(\d{1,3})\*{0,2}((?:\s*(?:/|,|and|or|–|-)\s*\*{0,2}\d{1,3}\*{0,2})*)",
    re.I)
FIELDNAMES_REF = re.compile(r"\bFieldNames?\s+(\d{1,3})\s*[–-]\s*(\d{1,3})")
ZONE_REF = re.compile(r"\bZoneDB\s+(\d{1,3})((?:\s*(?:/|,|and|–|-)\s*\d{1,3})*)")
TIME_LINK = re.compile(r"\[(\d{1,2}:\d{2}(?::\d{2})?)\]\((https?://[^)\s]+)\)")


def _expand(first, rest):
    """'88', ' / 92 / 96' -> [88, 92, 96]; '99', '–101' -> [99, 100, 101]."""
    out = [int(first)]
    for sep, n in re.findall(r"(/|,|and|or|–|-)\s*\*{0,2}(\d{1,3})", rest or ""):
        n = int(n)
        if sep in ("–", "-") and out and out[-1] < n <= out[-1] + 30:
            out += list(range(out[-1] + 1, n + 1))
        else:
            out.append(n)
    return out


def md_tables(text):
    """[(heading path, header cells, [row cells])] of the Markdown tables."""
    out, heading, lines = [], "", text.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"(#{2,4})\s+(.*)", ln)
        if m:
            heading = m.group(2).strip()
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"\|\s*:?-", lines[i + 1]):
            head = [c.strip() for c in ln.strip().strip("|").split("|")]
            rows = []
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append((heading, head, rows))
            continue
        i += 1
    return out


def section_anchor(heading):
    return common.link_text(heading).replace("#", "")


def doc_refs(ctx):
    """{("fields"|"zones", id): [(page path, page title, section, time link)]}
    from docs/gameplay lines that name a field or zone id."""
    if getattr(ctx, "_map_doc_refs", None) is not None:
        return ctx._map_doc_refs
    refs = {}
    for f in sorted((common.DOCS / "gameplay").glob("*.md")):
        fm, body = common.parse_front_matter(f.read_text(encoding="utf-8"))
        title = fm.get("title") or f.stem
        heading = ""
        for ln in body.split("\n"):
            m = re.match(r"#{1,4}\s+(.*)", ln)
            if m:
                heading = m.group(1).strip()
            hits = set()
            for m in FIELD_REF.finditer(ln):
                hits |= {("fields", n) for n in _expand(m.group(1), m.group(2))}
            for m in FIELDNAMES_REF.finditer(ln):
                a, b = int(m.group(1)), int(m.group(2))
                if 0 < b - a <= 30:
                    hits |= {("fields", n) for n in range(a, b + 1)}
            for m in ZONE_REF.finditer(ln):
                hits |= {("zones", n) for n in _expand(m.group(1), m.group(2))}
            if not hits:
                continue
            t = TIME_LINK.search(ln)
            when = "[%s](%s)" % (t.group(1), t.group(2)) if t else None
            for h in hits:
                lst = refs.setdefault(h, [])
                key = ("gameplay/" + f.stem, heading)
                if any((p, s) == key for p, _t, s, _w in lst):
                    if when:
                        for k, (p, tt, s, w) in enumerate(lst):
                            if (p, s) == key and not w:
                                lst[k] = (p, tt, s, when)
                    continue
                lst.append(("gameplay/" + f.stem, title, heading, when))
    ctx._map_doc_refs = refs
    return refs


def ref_lines(refs, limit=15):
    out = []
    for path, title, section, when in refs[:limit]:
        target = path + ("#" + section_anchor(section) if section else "")
        txt = common.link_text(title + (" § " + section if section else ""))
        out.append("- [[%s|%s]]%s" % (target, txt, " — at " + when if when else ""))
    if len(refs) > limit:
        out.append("- … and %d more sections" % (len(refs) - limit))
    return out


# ---------------------------------------------------------------------- index

class MapIndex:
    def __init__(self, ctx):
        t = ctx.table
        self.ctx = ctx
        self.scenes = {r.int("id"): r for r in t("SceneList")}
        self.fieldnames = {r.int("id"): r.get("c1") for r in t("FieldNames")}
        self.field_ids = sorted(set(self.scenes) | set(self.fieldnames))
        # gates
        self.gates, self.gates_in = {}, {}
        self.gate_rows = {}
        for r in t("Teleport_List"):
            g = {"gate": r.int("id"), "field": r.int("c1"), "x": num(r.get("c2")), "z": num(r.get("c3")),
                 "x2": num(r.get("c4")), "z2": num(r.get("c5")), "x3": num(r.get("c6")), "z3": num(r.get("c7")),
                 "to_gate": r.int("c8"), "to_field": r.int("c9"), "label": (r.get("c10") or "").strip()}
            self.gates.setdefault(g["field"], []).append(g)
            self.gate_rows.setdefault(g["gate"], g)
        for f, gs in self.gates.items():
            for g in gs:
                if g["to_field"] and g["to_field"] != f:
                    self.gates_in.setdefault(g["to_field"], []).append(g)
        # triggers
        self.triggers = {}
        for r in t("Trigger"):
            self.triggers.setdefault(r.int("field"), []).append(r)
        # zones
        self.zones = {}
        for r in t("ZoneDB"):
            self.zones[r.int("id")] = {
                "name_kr": (r.get("c1") or "").strip(), "x0": r.int("c2"), "z0": r.int("c3"),
                "x1": r.int("c4"), "z1": r.int("c5"), "map": (r.get("c6") or "").strip()}
        self.worldmap = {r.int("field_id"): [r.int("x0"), r.int("y0"), r.int("x1"), r.int("y1")]
                         for r in t("WorldmapData")}
        try:
            self.weather = {(r.get("scene") or "").strip() for r in t("weather")}
        except OSError:
            self.weather = set()
        self._archive_checked = False
        self._map_arc = None
        self._quests(ctx)
        self._docs(ctx)
        self._field_zones()
        self._dungeons(ctx)

    # -- nation copies, quest NPCs / monsters
    def _quests(self, ctx):
        triples = {}
        self.quest_fields = {}           # field -> [quest ids]
        self.quest_npcs = {}             # field -> {unit: [quest ids]}
        self.quest_kills = {}            # field -> {unit: [quest ids]}

        def add(d, field, unit, qid):
            if field and unit:
                d.setdefault(field, {}).setdefault(unit, [])
                if qid not in d[field][unit]:
                    d[field][unit].append(qid)

        # kill groups: objective unit ids >= 9999 match UnitDB i32@80
        # (docs/gameplay/precept-shop.md; quests.py)
        self.kill_groups = {}
        units = ctx.table("UnitDB").by()
        for u in ctx.table("UnitDB"):
            if u.int("i32@80"):
                self.kill_groups.setdefault(u.int("i32@80"), []).append(u.int("id"))
        self.group_of = {}               # (field, unit) -> kill group id

        for q in ctx.table("Quest"):
            qid = q.int("id")
            maps = [q.int("map1"), q.int("map2"), q.int("map3")]
            trip = tuple(maps)
            if len(set(trip)) == 3 and all(trip):
                triples[trip] = triples.get(trip, 0) + 1
            for m in set(maps) - {0}:
                self.quest_fields.setdefault(m, []).append(qid)
                add(self.quest_npcs, m, q.int("start_npc"), qid)
            for n in range(1, 6):
                typ, a = q.int("obj%d_type" % n), q.int("obj%d_a" % n)
                omaps = {q.int("obj%d_map%d" % (n, k)) for k in (1, 2, 3)} - {0}
                otrip = tuple(q.int("obj%d_map%d" % (n, k)) for k in (1, 2, 3))
                if len(set(otrip)) == 3 and all(otrip):
                    triples[otrip] = triples.get(otrip, 0) + 1
                for m in omaps:
                    if typ == 4:
                        add(self.quest_npcs, m, a, qid)
                    elif typ == 1:
                        if a in units:
                            add(self.quest_kills, m, a, qid)
                        for u in self.kill_groups.get(a, []) if a >= 9999 else []:
                            add(self.quest_kills, m, u, qid)
                            self.group_of[(m, u)] = a
        self.copies = {}                 # field -> (arslan, erion, armia), source
        for trip, n in triples.items():
            if n >= 2:                   # one-off triples are typos (99, 100, 96)
                for f in trip:
                    self.copies.setdefault(f, (list(trip), "client: Quest.cdb map1..3"))

    def _docs(self, ctx):
        """npc-locations / maps-and-dungeons tables."""
        self.doc_npcs = {}               # field -> {unit: section}
        self.doc_boss = {}               # field -> (units, tier, section)
        gp = common.DOCS / "gameplay"
        try:
            text = (gp / "npc-locations.md").read_text(encoding="utf-8")
        except OSError:
            text = ""
        for heading, head, rows in md_tables(text):
            low = [h.lower() for h in head]
            if any("field ids" in h for h in low):
                ci = next(i for i, h in enumerate(low) if "field ids" in h)
                for r in rows:
                    ids = [int(x) for x in re.findall(r"\d+", r[ci] if ci < len(r) else "")]
                    if len(ids) == 3:
                        for f in ids:
                            if f not in self.copies:
                                self.copies[f] = (ids, "doc: gameplay/npc-locations §2")
            if "unit id" not in low:
                continue
            fields = []
            for m in FIELD_REF.finditer(heading):
                fields += _expand(m.group(1), m.group(2))
            ci = low.index("unit id")
            for r in rows:
                cellv = r[ci] if ci < len(r) else ""
                if re.fullmatch(r"\d+", cellv):
                    for f in fields:
                        self.doc_npcs.setdefault(f, {}).setdefault(int(cellv), heading)
        try:
            text = (gp / "maps-and-dungeons.md").read_text(encoding="utf-8")
        except OSError:
            text = ""
        for heading, head, rows in md_tables(text):
            low = [h.lower() for h in head]
            fi = next((i for i, h in enumerate(low) if h == "field id"), None)
            bi = next((i for i, h in enumerate(low) if h.startswith("boss")), None)
            ti = next((i for i, h in enumerate(low) if "tier" in h), None)
            if fi is None or bi is None:
                continue
            for r in rows:
                if fi >= len(r) or not re.fullmatch(r"\d+", r[fi]):
                    continue
                paren = re.search(r"\(([^)]*)\)", r[bi]) if bi < len(r) else None
                units = [int(x) for x in re.findall(r"\d+", paren.group(1))] if paren else []
                tier = r[ti] if ti is not None and ti < len(r) and r[ti] not in ("?", "") else None
                if units:
                    self.doc_boss[int(r[fi])] = (units, tier, heading)

    # -- geometry
    def points(self, field):
        pts = [(g["x"], g["z"]) for g in self.gates.get(field, []) if g["x"] or g["z"]]
        pts += [(r.float("x"), r.float("z")) for r in self.triggers.get(field, [])]
        return pts

    def _zone_at(self, field, x, z):
        """The zone a point lies in. Overlapping rectangles: the one named
        after the land (필드_NN) first, unused/test zones last, then the
        smallest."""
        inside = [zid for zid, zr in self.zones.items()
                  if zr["x1"] > zr["x0"] and zr["x0"] <= x <= zr["x1"] + 1 and zr["z0"] <= z <= zr["z1"] + 1]
        named = "필드_%02d" % field
        unused = lambda n: n == "사용안함" or "test" in n.lower() or "테스트" in n
        inside.sort(key=lambda zid: (self.zones[zid]["name_kr"] != named, unused(self.zones[zid]["name_kr"]),
                                     (self.zones[zid]["x1"] - self.zones[zid]["x0"]) *
                                     (self.zones[zid]["z1"] - self.zones[zid]["z0"])))
        return inside[0] if inside else None

    def _field_zones(self):
        """Zones of a field: those holding its gates; when it has no gate,
        those holding its triggers. Triggers outside the gates' zones are
        recorded in trigger_elsewhere (field 142's nodes sit at field 125's
        coordinates)."""
        self.field_zones = {}            # field -> [zone ids]
        self.zone_source = {}
        self.trigger_elsewhere = {}      # field -> [zone ids]
        for f in self.field_ids:
            gz, tz = [], []
            for g in self.gates.get(f, []):
                if g["x"] or g["z"]:
                    zid = self._zone_at(f, g["x"], g["z"])
                    if zid is not None and zid not in gz:
                        gz.append(zid)
            for r in self.triggers.get(f, []):
                zid = self._zone_at(f, r.float("x"), r.float("z"))
                if zid is not None and zid not in tz:
                    tz.append(zid)
            zs = gz or tz
            if gz and [z for z in tz if z not in gz]:
                self.trigger_elsewhere[f] = [z for z in tz if z not in gz]
            if zs:
                self.zone_source[f] = "client: Teleport_List / Trigger positions inside ZoneDB rectangles"
            if not zs:
                # abyss zones carry their field id in the name (어비스_LV2_102);
                # every abyss zone that a gate also places agrees
                for zid, zr in self.zones.items():
                    m = re.fullmatch(r"어비스_LV\d+_(\d+)", zr["name_kr"])
                    if m and int(m.group(1)) == f:
                        zs.append(zid)
                        self.zone_source[f] = "client: ZoneDB name %s (abyss zones are named after their field)" % zr["name_kr"]
            if f in ZONE_HINTS:
                for z in ZONE_HINTS[f][0]:
                    if z not in zs:
                        zs.append(z)
                self.zone_source[f] = ZONE_HINTS[f][1]
            if zs:
                self.field_zones[f] = sorted(zs)
        self.zone_fields = {}
        for f, zs in self.field_zones.items():
            for z in zs:
                self.zone_fields.setdefault(z, []).append(f)

    def segments(self, zid):
        z = self.zones.get(zid)
        if not z or z["x1"] <= z["x0"]:
            return []
        out = []
        for sz in range(z["z0"] // 256, z["z1"] // 256 + 1):
            for sx in range(z["x0"] // 256, z["x1"] // 256 + 1):
                out.append((sx, sz))
        return out

    def map_archive(self):
        if not self._archive_checked:
            self._archive_checked = True
            try:
                from .assets import Client
                self._map_arc = Client().archive("map")
            except Exception:       # no client, or tools/jpk.py missing
                self._map_arc = None
        return self._map_arc

    def has(self, path):
        """True/False if map.jpk has the file, None if the archive is absent."""
        arc = self.map_archive()
        if arc is None:
            return None
        return arc.lookup(path.replace("/", "\\")) is not None

    # -- dungeons
    def _dungeons(self, ctx):
        self.admission = {r.int("field"): r for r in ctx.table("DungeonAdmission")}
        self.groups = {}                 # field -> [(group id, slot)]
        for r in ctx.table("Dungeon"):
            for n in range(1, 16):
                f = r.int("field%d" % n)
                if f:
                    self.groups.setdefault(f, []).append((r.int("id"), n))
        self.events = {}                 # target field -> [rows]
        for r in ctx.table("Event_Dungeon"):
            self.events.setdefault(r.int("target_field"), []).append(r)
        self.dungeon_ids = sorted(set(self.admission) | set(self.groups) | set(self.events))

    # -- other pages
    def page_units(self, ctx, field):
        """(npcs {unit: source}, monsters {unit: source}, spawn points)
        from npc and monster pages' front matter (npcs: 'map', 'positions';
        monsters: 'spawns', 'spawn_fields')."""
        npcs, mons, spawns = {}, {}, []
        for uid, fm in ctx.pages("npcs").items():
            where = [fm.get("map")]
            for p in fm.get("positions") or []:
                if isinstance(p, dict):
                    where.append(p.get("field"))
            if field in where:
                npcs[uid] = "npc page"
        for uid, fm in ctx.pages("monsters").items():
            sf = fm.get("spawn_fields")
            if isinstance(sf, list) and field in sf:
                mons[uid] = "monster page"
            sp = fm.get("spawns")
            if not isinstance(sp, list):
                continue
            for s in sp:
                if isinstance(s, int) and s == field:
                    mons[uid] = "monster page"
                elif isinstance(s, dict) and field in (s.get("field"), s.get("map")):
                    mons[uid] = "monster page"
                    if "x" in s and "z" in s:
                        e = {"unit": uid}
                        e.update({k: v for k, v in s.items() if k not in ("field", "map")})
                        spawns.append(e)
        return npcs, mons, spawns


def index(ctx):
    if getattr(ctx, "_map_index", None) is None:
        ctx._map_index = MapIndex(ctx)
    return ctx._map_index


def scene_kind(ix, field):
    r = ix.scenes.get(field)
    return SCENE_KINDS.get(r.int("type")) if r is not None else None


def nation_of(ix, field):
    c = ix.copies.get(field)
    if not c or c[0].count(field) != 1:
        return None
    return NATIONS[c[0].index(field) + 1]


def _coord(v):
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v)


def pos(x, z):
    return "%s, %s" % (_coord(x), _coord(z))


def paired_gate(ix, field, g):
    """A gate with linked gate 0 leads to the gate of the target field that
    links back to this field (inferred; server/travel.py: 89 -> 1202 in 88)."""
    if g["to_gate"] or not g["to_field"] or g["to_field"] == field:
        return g["to_gate"] or None
    back = [b["gate"] for b in ix.gates.get(g["to_field"], []) if b["to_field"] == field]
    return back[0] if len(back) == 1 else None

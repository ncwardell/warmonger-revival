"""NPCs: one page per non-hostile unit (UnitDB rows that ctx.unit_type()
classes as "npcs": category 4 / 50, or any unit with a shop or a portrait).

Client sources (data/tables/*.tsv, see docs/spec/data-tables.md, monsters.md):
  UnitDB      name_key@04 (TitleName_<n> = the NPC's own name for named NPCs),
              str@40 = title key (UnitName_<n>: "Oracle of Knowledge",
              "Merchant" ...), category@8a, class_mask@7c, model@ac, scale@a4,
              u8@8c/@8d/@8e = the three NPC menu functions, u16@a2 = shop id
              (Npc_Carry), str@110 = dialogue portrait, str@114 = greeting key,
              7 {a, skill} pairs.
  Npc_Carry   shop stock (shop id = UnitDB u16@a2)
  Quest       giver start_npc?@18 (fields map1..3 per nation), receiver
              c18@2c (fields map4..6), objective type 4 = talk to unit a
              (contract/quests.yaml)
  QuestTalk   quest dialogue rows (quest_id = Quest_Title_<n> number,
              speaker_unit_key = the unit's title or name key)

The menu functions are *client*: FUN_0056ea03 reads the three bytes at UnitDB
+0x8c..+0x8e (unit+0x3a4 -> row) and FUN_0056c8fd turns each code into a menu
entry with an NpcFunc_* label (FUNCTIONS below; codes it skips get no entry).

Positions are NOT in the client for town NPCs (npc-locations.md section 1).
They come from the hand-measured tables in docs/gameplay/*.md: every Markdown
table with a unit-id column and x / z columns is read, with the field from a
field column or the section heading ("(fields 88 / 92 / 96)"). The first
position from npc-locations.md wins (it is the curated list); others are kept
in ``positions``. Nation copies are derived from npc-locations.md section 2
(local position + the other copy's segment origin) and marked as derived.
"""
import ast
import re
from collections import Counter

from . import common
from .common import Page, fmt_num, quote, table_md

TYPE = "npcs"
KIND = "npc"
LABEL = "NPC"
PLURAL = "NPCs"
DESCRIPTION = ("Every non-hostile unit in the client's `UnitDB`: town NPCs, shopkeepers, "
               "quest givers, guards, teleporters, bots and the mail box. Town NPC positions "
               "are not in the client; they come from video and screenshot measurements in "
               "[[gameplay/npc-locations|NPC locations]]. Gathering nodes and the quest NPCs "
               "the client places itself are under [[wiki/nodes/index|Nodes]].")
REQUIRED = ["map", "x", "z", "role"]       # + "shop" (shop function), "teleport_to" (teleport)
# positions is not a union key: a union keeps stale generated rows when the docs change;
# a hand edit to positions marks it manual instead.

# NpcFunc label per menu code (FUN_0056c8fd, *client*). Codes 5, 7-10, 13, 22-25
# and 71 produce no menu entry (quest-only NPCs, the mail box ...).
FUNCTIONS = {
    1: ("shop", "NpcFunc_Shop"), 2: ("mock_battle", "NpcFunc_WarRoom"), 3: ("craft", "NpcFunc_MakeItem"),
    4: ("teleport", "NpcFunc_Tel"), 6: ("legion_create", "NpcFunc_GuildCreate"),
    11: ("legion_stock", "NpcFunc_GuildStock"), 12: ("fort_donate", "NpcFunc_FortDonate"),
    14: ("change_nation", "NpcFunc_MoveNation"), 15: ("warehouse", "NpcFunc_Cargo"),
    16: ("fort_info", "NpcFunc_FortInfo"), 17: ("auction", "NpcFunc_Auction"),
    18: ("craft", "NpcFunc_MakeItem"), 19: ("craft", "NpcFunc_MakeItem"), 20: ("craft", "NpcFunc_MakeItem"),
    21: ("craft", "NpcFunc_MakeItem"), 26: ("crush", "NpcFunc_Crush"),
    27: ("channel_move", "NpcFunc_MoveChannel"), 28: ("legion_warehouse", "NpcFunc_Cargo"),
    29: ("guild_war_request", "GUI_GuildWarReq_Ok"), 30: ("costume_lock", "NpcFunc_CostumeLock"),
    31: ("legion_core", "NpcFunc_MakeGCore"), 32: ("craft", "NpcFunc_MakeItem"),
    33: ("weapon_alchemy", "NpcFunc_CombineWeaopn"), 34: ("craft", "NpcFunc_MakeItem"),
    35: ("rune_socket", "NpcFunc_SocketOpen"), 36: ("rune_bind", "NpcFunc_JewelBind"),
    38: ("hero_bind", "NpcFunc_HeroBind"), 39: ("move_to_temple", "NpcFunc_TownToHoly"),
    40: ("move_to_castle", "NpcFunc_HolyToTown"), 41: ("auction_premium", "NpcFunc_AuctionPrem"),
}
NO_MENU = {5, 7, 8, 9, 10, 13, 22, 23, 24, 25, 71}
CATEGORIES = {4: "NPC (category 4: bots, training assistants)", 50: "NPC (category 50)"}


# ------------------------------------------------------- hand-written sources

TS_RE = re.compile(r"\[(\d{1,2}:\d{2}(?::\d{2})?)\]\((https?://[^)\s]+)\)")
NUM_RE = re.compile(r"^-?\d+(?:\.\d+)?$")


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _ints(text):
    return [int(x) for x in re.findall(r"\d+", text or "")]


def gameplay_docs():
    """[(stem, title, text)] of docs/gameplay/*.md, npc-locations first."""
    out = []
    for f in sorted((common.DOCS / "gameplay").glob("*.md"), key=lambda p: (p.stem != "npc-locations", p.stem)):
        text = f.read_text(encoding="utf-8")
        fm, body = common.parse_front_matter(text)
        out.append((f.stem, fm.get("title") or f.stem, body))
    return out


def doc_tables(docs):
    """Yield (stem, title, heading, header cells, row cells) for every
    Markdown table row in the gameplay docs."""
    for stem, title, body in docs:
        lines = body.split("\n")
        heading = ""
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith("#"):
                heading = line.lstrip("#").strip()
            if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?\s*$", lines[i + 1]):
                header = [h.lower() for h in _cells(line)]
                i += 2
                while i < len(lines) and lines[i].startswith("|"):
                    yield stem, title, heading, header, _cells(lines[i])
                    i += 1
                continue
            i += 1


def _col(header, *names, contains=None):
    for n in names:
        if n in header:
            return header.index(n)
    if contains:
        for k, h in enumerate(header):
            if contains in h:
                return k
    return None


def doc_positions(docs):
    """{unit id: [position dict]} from gameplay tables with unit, x and z columns."""
    out = {}
    for stem, title, heading, header, row in doc_tables(docs):
        cu, cx, cz = _col(header, "unit id", "unit"), _col(header, "x"), _col(header, "z")
        if cu is None or len(row) < len(header) or not re.fullmatch(r"\d+", row[cu]):
            continue
        if cx is not None and cz is not None:
            xs, zs = row[cx], row[cz]
        else:       # one 'World x, z' column
            cxz = next((k for k, h in enumerate(header) if h.endswith("x, z") and "local" not in h), None)
            if cxz is None or row[cxz].count(",") != 1:
                continue
            xs, zs = (v.strip() for v in row[cxz].split(","))
        if not NUM_RE.match(xs) or not NUM_RE.match(zs):
            continue
        cf = _col(header, "field", "map (field)", contains="field")
        field = None
        if cf is not None:
            m = re.search(r"\((\d+)", row[cf]) or re.search(r"\d+", row[cf])
            field = int(m.group(1) if m.groups() else m.group(0)) if m else None
        if field is None:
            m = re.search(r"\(fields? (\d+)", heading)
            field = int(m.group(1)) if m else None
        if field is None:
            continue
        cs = _col(header, "source", "sightings", "time")
        cc = _col(header, "confidence")
        cr = _col(header, "role")
        times = TS_RE.findall(row[cs]) if cs is not None else []
        sec = re.match(r"(\d+)\.", heading)
        p = {"field": field, "x": float(xs), "z": float(zs),
             "source": "gameplay/%s%s" % (stem, " §%s" % sec.group(1) if sec else ""),
             "confidence": (row[cc] if cc is not None else "video").strip("* ")}
        if times:
            p["seen"] = [t for t, _u in times[:4]]
        out.setdefault(int(row[cu]), []).append(
            (p, row[0], row[cr] if cr is not None else None, [(t, u) for t, u in times], (stem, title)))
    return out


def copy_origins(docs):
    """npc-locations §2 table -> {field: (fields, origins)} for the three
    nation copies of each home map."""
    out = {}
    for stem, title, heading, header, row in doc_tables(docs):
        if stem != "npc-locations" or not header or not header[0].startswith("map") or len(row) < 3:
            continue
        fields = _ints(row[1].split("(")[0]) if "one id" not in row[1] else _ints(row[1])[:1] * 3
        origins = [tuple(float(v) for v in m) for m in re.findall(r"\((\d+(?:\.\d+)?), (\d+(?:\.\d+)?)\)", row[2])]
        if len(fields) == 3 and len(origins) == 3:
            for f in set(fields):
                out.setdefault(f, (fields, origins))
    return out


def derive_copies(pos, copies):
    if pos["field"] not in copies:
        return []
    fields, origins = copies[pos["field"]]
    i = fields.index(pos["field"])
    lx, lz = pos["x"] - origins[i][0], pos["z"] - origins[i][1]
    out = []
    for j, (f, o) in enumerate(zip(fields, origins)):
        if j == i:
            continue
        out.append({"field": f, "x": round(o[0] + lx, 2), "z": round(o[1] + lz, 2),
                    "source": "derived: %s + copy origin (gameplay/npc-locations §2)" % pos["source"],
                    "confidence": "derived"})
    return out


def sightings(docs, name, ids, unique_name):
    """{(stem, title): [(heading, [timestamps])]} of gameplay lines that name
    the unit (and its id, unless the name is unique among NPCs)."""
    if not name:
        return {}
    name_re = re.compile(r"(?<!\w)%s(?!\w)" % re.escape(name), re.I)
    id_re = re.compile(r"(?<![\w=.:/#-])(?:%s)(?![\w.:%%])" % "|".join(str(i) for i in ids))
    out = {}
    for stem, title, body in docs:
        heading = ""
        for line in body.split("\n"):
            if line.startswith("#"):
                heading = line.lstrip("#").strip()
                continue
            if not name_re.search(line):
                continue
            plain = TS_RE.sub("", line)
            if not unique_name and not id_re.search(plain):
                continue
            out.setdefault((stem, title), []).append((heading, near_times(line, name_re)))
    return out


def near_times(line, pattern):
    """Timestamps in the parts of a line that match ``pattern``: the whole row
    of a table, else the sentences that contain it (so a list of other NPCs
    on the same line does not lend its timestamps)."""
    if line.lstrip().startswith("|"):
        parts = [line]
    else:
        parts = [p for p in re.split(r"(?<=[.;!?])\s+(?=[A-Z*\[(])", line) if pattern.search(TS_RE.sub("", p))]
    out = []
    for p in parts:
        out += [t for t, _u in TS_RE.findall(p) if t not in out]
    return out


def server_npcs():
    """Unit ids spawned by server/world.py (NPCS list + explicit Unit(...) NPCs)."""
    out = {}
    try:
        src = (common.REPO / "server" / "world.py").read_text(encoding="utf-8")
    except OSError:
        return out
    try:
        tree = ast.parse(src)
        for node in tree.body:
            if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "NPCS" for t in node.targets):
                for unit, nm, *_ in ast.literal_eval(node.value):
                    out[unit] = "listed in `NPCS`"
    except (SyntaxError, ValueError):
        pass
    for m in re.finditer(r"Unit\(NPC_UID_BASE \+ \d+, (\d+), \"[^\"]*\",[^,]*,[^,]*,\s*([\d.]+), ([\d.]+), NPC_TEAM, map_id=(\d+)", src):
        out[int(m.group(1))] = "placed at (%s, %s) in map %s" % (m.group(2), m.group(3), m.group(4))
    return out


# --------------------------------------------------------------- client index

class Index:
    def __init__(self, ctx):
        t = ctx.table
        self.given, self.received, self.talk = {}, {}, {}
        self.quest_title_no = {}
        for q in t("Quest"):
            qid = q.int("id")
            m = re.search(r"(\d+)", q.get("title_key") or "")
            if m:
                self.quest_title_no.setdefault(int(m.group(1)), []).append(qid)
            if q.int("start_npc"):
                self.given.setdefault(q.int("start_npc"), []).append(
                    (qid, [q.int("map%d" % n) for n in (1, 2, 3)]))
            if q.int("c18@2c"):
                self.received.setdefault(q.int("c18@2c"), []).append(
                    (qid, [q.int("map%d" % n) for n in (4, 5, 6)]))
            for n in range(1, 6):
                if q.int("obj%d_type" % n) == 4 and q.int("obj%d_a" % n):
                    self.talk.setdefault(q.int("obj%d_a" % n), []).append(
                        (qid, n, ctx.s(q.get("obj%d_text_key" % n))))
        self.talks = {}
        for r in t("QuestTalk"):
            for qid in self.quest_title_no.get(r.int("quest_id"), []):
                self.talks.setdefault(qid, []).append(r)
        self.shops = {r.int("shop_id"): r for r in t("Npc_Carry")}
        self.docs = gameplay_docs()
        self.positions = doc_positions(self.docs)
        self.copies = copy_origins(self.docs)
        self.server = server_npcs()


def npc_ids(ctx):
    return [r.int("id") for r in ctx.table("UnitDB") if ctx.unit_type(r.int("id")) == TYPE]


def functions_of(ctx, row):
    out = []
    for col in ("u8@8c", "u8@8d", "u8@8e"):
        code = row.int(col)
        if not code:
            continue
        fn = FUNCTIONS.get(code)
        e = {"code": code}
        if fn:
            e["function"] = fn[0]
            e["label"] = ctx.s(fn[1])
        else:
            e["function"] = "none" if code in NO_MENU else "unknown"
        out.append(e)
    return out


def build(ctx):
    ix = Index(ctx)
    ctx.npcs_index = ix
    u = ctx.table("UnitDB")
    ids = npc_ids(ctx)
    names = Counter(ctx.name(TYPE, i) for i in ids)
    for id_ in ids:
        r = u.get(id_)
        f = {}
        sources = ["client: UnitDB.cdb id %d" % id_]
        nm = ctx.name(TYPE, id_)
        f["name_key"] = r.str("name_key")
        title_key = r.str("str@40")
        if title_key:
            f["title_key"] = title_key
            f["npc_title"] = ctx.s(title_key)
        f["category"] = r.int("category@8a")
        f["class_mask"] = r.int("class_mask@7c")
        f["model"] = r.int("model@ac")
        f["scale"] = r.float("scale@a4")
        fns = functions_of(ctx, r)
        if fns:
            f["functions"] = fns
        # role: client title, else menu functions, else the hand-written table
        role, role_src = None, None
        if f.get("npc_title"):
            role = f["npc_title"]
        elif any(e.get("label") for e in fns):
            role = ", ".join(e["label"] for e in fns if e.get("label"))
        doc = ix.positions.get(id_, [])
        doc_roles = [(p, rl) for p, _n, rl, _t, _d in doc if rl and _name_ok(_n, nm)]
        if role is None and doc_roles:
            # the table's role column, up to the first comment ("Guide, gives ..." -> "Guide")
            role = re.split(r"\s*[,(;]", doc_roles[0][1].replace("`", ""), 1)[0].strip() or None
            role_src = doc_roles[0][0]["source"]
            sources.append(role_src + " (role)")
        f["role"] = role
        if r.int("u16@a2"):
            f["shop"] = r.int("u16@a2")
        if r.str("str@114"):
            f["talk_key"] = r.str("str@114")
        if r.str("str@110") and r.str("str@110").lower().startswith("ui/"):
            f["portrait"] = r.str("str@110")
        skills = [s for s in (r.int("skill@%x" % (0xd0 + 8 * k)) for k in range(7)) if s]
        if skills:
            f["skills"] = skills
        given = [q for q, _m in ix.given.get(id_, [])]
        received = [q for q, _m in ix.received.get(id_, [])]
        talk = sorted({q for q, _n, _t in ix.talk.get(id_, [])})
        quests = {}
        if given:
            quests["gives"] = given
        if received:
            quests["receives"] = received
        if talk:
            quests["talk_objective"] = talk
        if quests:
            f["quests"] = quests
            sources.append("client: Quest.cdb start_npc@18 / c18@2c / objective type 4")
        qfields = Counter()
        for _q, maps in ix.given.get(id_, []) + ix.received.get(id_, []):
            for m in maps:
                if m:
                    qfields[m] += 1
        if qfields:
            f["quest_fields"] = sorted(qfields)
        # positions from the hand-measured tables
        positions = []
        for p, rowname, _rl, _t, _d in doc:
            if not _name_ok(rowname, nm):
                continue
            positions.append(p)
            if p["source"] not in sources:
                sources.append(p["source"])
        if positions:
            prim = positions[0]
            f["map"], f["x"], f["z"] = prim["field"], prim["x"], prim["z"]
            for c in derive_copies(prim, ix.copies):
                if not any(c["field"] == q["field"] and abs(c["x"] - q["x"]) < 0.01 for q in positions):
                    positions.append(c)
            f["positions"] = positions
        elif qfields:
            # the field the client's quests put the NPC in (Arslan copy first)
            firsts = Counter()
            for _q, maps in ix.given.get(id_, []) + ix.received.get(id_, []):
                if maps and maps[0]:
                    firsts[maps[0]] += 1
            if firsts:
                f["map"] = firsts.most_common(1)[0][0]
                sources.append("client: Quest.cdb giver/receiver field (map only; no position)")
        else:
            f["map"] = None
        f.setdefault("x", None)
        f.setdefault("z", None)
        req = list(REQUIRED)
        if any(e.get("function") == "shop" for e in fns):
            req.append("shop")
        if any(e.get("function") == "teleport" for e in fns):
            req.append("teleport_to")
            f.setdefault("teleport_to", None)
        page = Page(TYPE, id_, ctx.title(TYPE, id_), fields=f, sources=sources, body=body, required=req)
        page._unique = names[nm] == 1
        yield page


def _name_ok(rowname, name):
    """A table row names this unit (tables write 'Hadrian?', 'Mail box' ...)."""
    if not name:
        return True
    a = re.sub(r"[^a-z]", "", rowname.lower())
    b = re.sub(r"[^a-z]", "", name.lower())
    return not a or b in a or a in b or a.startswith("(")


# ------------------------------------------------------------------ rendering

def field_link(ctx, f):
    return ctx.link("fields", f) if f else "?"


def body(ctx, page):
    ix = ctx.npcs_index
    fm, id_ = page.fm, page.id
    row = ctx.table("UnitDB").get(id_)
    L = []
    info = []
    img = ctx.image(TYPE, id_)
    if img:
        info.append(("", "![%s](%s)" % (common.link_text(page.title), img)))
    info.append(("Unit id", "`%d`" % id_))
    if fm.get("npc_title"):
        info.append(("Title", fm["npc_title"]))
    if fm.get("role") and fm.get("role") != fm.get("npc_title"):
        info.append(("Role", fm["role"]))
    info.append(("Category", CATEGORIES.get(fm.get("category"), "category %s" % fm.get("category"))))
    fns = [e for e in (fm.get("functions") or []) if isinstance(e, dict)]
    if fns:
        info.append(("Menu", ", ".join(
            "%s (`%s`)" % (e["label"], e.get("code")) if e.get("label") else
            "no menu entry (code `%s`)" % e.get("code") for e in fns)))
    if fm.get("shop"):
        info.append(("Shop", ctx.link("shops", fm["shop"])))
    if fm.get("map"):
        where = field_link(ctx, fm["map"])
        if fm.get("x") is not None and fm.get("z") is not None:
            where += " at (%s, %s)" % (fm["x"], fm["z"])
        else:
            where += " (position unknown)"
        info.append(("Stands in", where))
    info.append(("Model", "ObjectList `%s`, scale %s" % (fm.get("model"), fm.get("scale"))))
    if fm.get("portrait"):
        info.append(("Portrait", "`%s`" % fm["portrait"]))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))

    greet = ctx.s(fm.get("talk_key"))
    if greet:
        L += ["### Greeting", "", quote(greet)]

    # position
    pos = [p for p in (fm.get("positions") or []) if isinstance(p, dict)]
    if pos:
        L += ["### Where it stands", "",
              "Town NPC positions are not in the client data; these were measured from video "
              "and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the "
              "method). Rows marked *derived* place the same spot in the other nations' copies "
              "of the map.", "",
              table_md(["field", "x", "z", "confidence", "source"], [
                  (field_link(ctx, p.get("field")), p.get("x"), p.get("z"), p.get("confidence", ""),
                   _src_link(p.get("source", "")) + (" at " + ", ".join(p["seen"]) if p.get("seen") else ""))
                  for p in pos])]
    elif fm.get("quest_fields"):
        L += ["### Where it stands", "",
              "No measured position yet. The client's quests put this NPC in %s (giver/receiver "
              "fields, one per nation)." % ", ".join(field_link(ctx, f) for f in fm["quest_fields"]), ""]
    if id_ in ix.server:
        L += ["Current server: `server/world.py` spawns this NPC (%s)." % ix.server[id_], ""]

    # shop stock
    shop = ix.shops.get(fm.get("shop") or 0)
    if shop is not None:
        stock = [c for c, *_x in common.repeat(shop, "item%d_code", "item%d_p1", "item%d_count", "item%d_p2")]
        L += ["### Shop", "",
              "Sells %d items (`Npc_Carry` row %d; full list on %s): %s." % (
                  len(stock), fm["shop"], ctx.link("shops", fm["shop"]),
                  ", ".join(ctx.link("items", c) for c in stock[:12]) + (" …" if len(stock) > 12 else "")), ""]

    # quests
    q = fm.get("quests") if isinstance(fm.get("quests"), dict) else {}
    if q:
        L += ["### Quests", ""]
        for key, text in (("gives", "Gives"), ("receives", "Takes the turn-in of"),
                          ("talk_objective", "Must be talked to in")):
            if q.get(key):
                L.append("- **%s:** %s" % (text, ", ".join(ctx.link("quests", x) for x in q[key])))
        L.append("")
        keys = {k for k in (fm.get("name_key"), fm.get("title_key")) if k}
        rows = []
        for qid in sorted(set(sum((v for v in q.values() if isinstance(v, list)), []))):
            for t in ix.talks.get(qid, []):
                if t.get("speaker_unit_key") in keys or t.get("speaker_key") in keys:
                    first = next((ctx.s(t.get("line%d_text_key" % n)) for n in range(1, 11)
                                  if ctx.s(t.get("line%d_text_key" % n))), None)
                    rows.append((ctx.link("quests", qid), t.get("quest_id"),
                                 ctx.s(t.get("speaker_key")) or "",
                                 common.clean_text(first or "")[:120].replace("\n", " ")))
        if rows:
            L += ["Dialogue rows (`QuestTalk`; full text on the quest pages):", "",
                  table_md(["quest", "QuestTalk", "speaker", "first line"], rows)]

    if fm.get("skills"):
        L += ["### Skills", "", ", ".join(ctx.link("skills", s) for s in fm["skills"]), ""]

    # namesakes
    same = [i for i in npc_ids(ctx) if i != id_ and ctx.name(TYPE, i) == ctx.name(TYPE, id_) and ctx.name(TYPE, i)]
    if same:
        L += ["### Other units with this name", "",
              "The client has one unit row per placement or variant: " +
              ", ".join(ctx.link(TYPE, i, "%s (%d)" % (ctx.title(TYPE, i), i)) for i in same) + ".", ""]

    # where the hand-written pages mention it
    seen = sightings(ix.docs, ctx.name(TYPE, id_), [id_], getattr(page, "_unique", False))
    if seen:
        L += ["### Seen in", ""]
        for (stem, title), hits in seen.items():
            ts = sorted({x for _h, t in hits for x in t}, key=_seconds)
            heads = []
            for h, _t in hits:
                if h and h not in heads:
                    heads.append(h)
            L.append("- [[gameplay/%s|%s]]%s%s" % (
                stem, common.link_text(title),
                " at " + ", ".join(ts[:8]) + (" …" if len(ts) > 8 else "") if ts else "",
                " (%s)" % "; ".join(heads[:3]) if heads else ""))
        L.append("")
    return "\n".join(L)


def _seconds(ts):
    v = 0
    for part in ts.split(":"):
        v = v * 60 + int(part)
    return v


def _src_link(src):
    m = re.match(r"gameplay/([\w-]+)(.*)", src)
    return "[[gameplay/%s|%s]]%s" % (m.group(1), m.group(1), m.group(2)) if m else src

"""Skills: one page per Skill_Base row (weapon, hero, TP, item and dev skills).

Client sources (data/tables/*.tsv, see docs/spec/data-tables.md, docs/spec/skills.md
and docs/spec/combat.md section 5):
  Skill_Base   name/description keys, kind, targeting, cost, range, area,
               cast/channel/cooldown ms, 2 requirement slots, 4 effect slots
               {type, value, rate}, visual, required weapon type, icon
  WeaponBase   8 skill ids per weapon base (1-4 = Q/W/E/R, 5-8 = hero set);
               Item_Base option 200 -> WeaponBase id gives the weapons
  HeroData     10 skill ids per hero transform
  Skill_TP     war "TP" skills: TP cost, cooldown (s), need flags. Skill_TP has
               no names or data of its own (every row points at a Skill_Base
               id), so TP skills are not a type of their own: the TP row is shown
               on the skill's page (``tp:``).
  Item_Base    option 210 = skill cast when the item is used
  Policy       buff_or_skill (nation policies; server-only table)
  skillVisual  visual set name (Skill_Base visual@bd)
  StringAll    SkillComment_<id> tooltips. Their value tags carry numbers the
               client shows: <EF_STATIC n> = n, <EF_R_DAM n> = n % of Attack,
               <EF_R_MDAM n> = n % of Ability Power, ... (FUN_004c2f58 area,
               string list at decompiled.c 187035). They are copied into
               ``tooltip_formula``.

UnitDB's 7 unit skill slots (skill@d0..@100) hold ids like 4040001 or 3000014
that are not Skill_Base rows (monster/basic-attack skills, server data), so no
skill page lists units.

Effect slot types (``effects``) are not decoded in the client (it never reads
damage). What is known from the data: 330 = base amount, 101 = % of Attack,
102 = % of Ability Power -- these match the tooltip tags in about 80 % of the
skills that have both (*inferred*); the 3xx types listed in BUFF_TYPES always
hold a Skill_Buff id (*inferred*); other codes below 300 look like ItemOption
stat codes. ``damage_or_effect`` summarises only those readings.

Hand-written knowledge: lines of docs/gameplay/*.md that name a skill (with
any video timestamps on the line) are linked under "Mentioned in"; rows of
gameplay tables with Skill + Cooldown/Mana/TP columns are copied into the
``observed`` front-matter key with their source.
"""
import re

from . import common
from .common import Page, fmt_num, quote, repeat, table_md

TYPE = "skills"
KIND = "skill"
LABEL = "Skill"
DESCRIPTION = ("Every skill in the client's `Skill_Base` table: weapon skills (Q/W/E/R and "
               "the hero set), hero transform skills, war TP skills, skills cast by items, "
               "and unused developer rows. Damage numbers are not in the client: the "
               "effect slots and the tooltip formula are the best evidence of what a skill "
               "did.")
REQUIRED = ["damage_or_effect", "cooldown", "cost", "range"]    # actives
PASSIVE_REQUIRED = ["damage_or_effect"]                         # kind 2
UNION_KEYS = ["used_by", "observed"]

KINDS = {1: "active", 2: "passive", 4: "ground"}
TARGET_TYPES = {1: "unit", 2: "ground", 3: "self"}
RELATIONS = [(1, "self"), (2, "ally"), (4, "enemy"), (8, "party")]
UNIT_CLASSES = [(1, "monster"), (2, "NPC"), (4, "player"), (8, "structure"), (0x20, "untargetable"),
                (64, "misc")]
COST_TYPES = {4: "HP %", 5: "MP", 6: "EXP", 14: "TP", 20: "cost type 20 (unknown)"}
MOVEMENT = {1: "blink / teleport", 2: "dash"}
DELIVERY = {0: "instant", 1: "projectile / SFX", 4: "projectile / SFX (4)", 5: "ground field (ticks)"}
EFFECT_KINDS = {0: "none / other", 1: "damage (physical?)", 2: "damage (magic?)",
                0x1f: "heal HP", 0x21: "restore MP", 0x2d: "drain MP"}
AREA_SHAPES = {1: "circle", 2: "line / rectangle?", 3: "cone?", 4: "area 4 (unknown)"}
SLOT_KEYS = {1: "Q", 2: "W", 3: "E", 4: "R"}
# Effect types whose value is always a Skill_Buff id (checked over all 675 rows).
BUFF_TYPES = {300, 301, 302, 303, 304, 305, 307, 308, 314, 317, 321, 331, 365, 366, 452, 453, 460}
EFFECT_TEXT = {330: "base amount (tooltip `EF_STATIC`)", 101: "% of Attack (tooltip `EF_R_DAM`)",
               102: "% of Ability Power (tooltip `EF_R_MDAM`)", 331: "transform: applies buff",
               327: "summon? (item option 327 = summon unit)", 328: "summon? (unknown)",
               129: "% of the target's missing HP? (5025 tooltip: 30 = '30% of the enemy's lost stamina')"}
TAGS = {"EF_STATIC": ("base", ""), "EF_R_DAM": ("attack_pct", "% Attack"),
        "EF_R_MDAM": ("ability_pct", "% Ability Power"), "EF_R_MANA": ("mana_pct", "% Mana"),
        "EF_R_MAXMANA": ("max_mana_pct", "% max Mana"), "EF_R_DEF": ("armor_pct", "% Armor"),
        "EF_R_DEF_MAGIC": ("magic_resist_pct", "% Magic Resist"),
        "EF_R_MOVEMENT": ("movement_pct", "% Movement"), "EF_R_HP": ("hp_pct", "% HP"),
        "EF_R_MAXHP": ("max_hp_pct", "% max HP")}


def bits(value, table):
    return [n for b, n in table if value & b]


def effect_text(ctx, type_, value):
    if type_ in EFFECT_TEXT:
        return EFFECT_TEXT[type_]
    if type_ in BUFF_TYPES:
        return "applies buff (variant %d)" % type_
    opt = index(ctx).options.get(type_)
    if opt is not None:
        return "stat? %s" % (opt.get("name") or "").strip()
    return "unknown"


class Index:
    """Reverse lookups over the client tables, built once per run."""

    def __init__(self, ctx):
        t = ctx.table
        self.options = {r.int("code"): r for r in t("ItemOption")}
        self.buffs = t("Skill_Buff").by()
        self.weapon_items = {}          # WeaponBase id -> [item ids]
        self.item_use = {}              # skill id -> [item ids] (option 210)
        for r in t("Item_Base"):
            for slot in range(1, 11):
                code, value = r.int("opt%d_type" % slot), r.int("opt%d_value" % slot)
                if code == 200:
                    self.weapon_items.setdefault(value, []).append(r.int("id"))
                elif code == 210:
                    self.item_use.setdefault(value, []).append(r.int("id"))
        self.weapon = {}                # skill id -> [(WeaponBase id, slot)]
        for w in t("WeaponBase"):
            for n, (s,) in enumerate(repeat(w, "skill%d", skip_zero=False), 1):
                if s:
                    self.weapon.setdefault(s, []).append((w.int("id"), n))
        self.hero = {}                  # skill id -> [(hero id, slot)]
        for h in t("HeroData"):
            for n, (s,) in enumerate(repeat(h, "skill%d", skip_zero=False), 1):
                if s:
                    self.hero.setdefault(s, []).append((h.int("id"), n))
        self.tp = {}
        for r in t("Skill_TP"):
            self.tp.setdefault(r.int("skill_id"), r)
        self.policy = {}
        try:
            for r in t("Policy"):
                self.policy.setdefault(r.int("buff_or_skill"), []).append(r)
        except OSError:
            pass
        self.visual = {}
        try:
            for r in t("skillVisual"):
                self.visual[r.int("c1")] = (r.get("c2") or "").strip()
        except OSError:
            pass
        self.server = server_skills()


def index(ctx):
    if getattr(ctx, "skills_index", None) is None:
        ctx.skills_index = Index(ctx)
    return ctx.skills_index


def server_skills():
    """{skill id: [(weapon item, slot)]} from server/skills.py WEAPON_SKILLS
    (read with ast; the module is not imported)."""
    import ast
    out = {}
    try:
        tree = ast.parse((common.REPO / "server" / "skills.py").read_text(encoding="utf-8"))
    except (OSError, SyntaxError):
        return out
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "WEAPON_SKILLS" for t in node.targets):
            try:
                table = ast.literal_eval(node.value)
            except ValueError:
                return out
            for item, (_wb, ids) in table.items():
                for n, s in enumerate(ids, 1):
                    out.setdefault(s, []).append((item, n))
    return out


# ------------------------------------------------------- hand-written knowledge

TIME_RE = re.compile(r"(?<![\d:.,])(\d{1,2}:\d{2}(?::\d{2})?)(?![\d:])")


def gameplay_docs(ctx):
    """[(wikilink path, title, [(line no, heading, line)])] of docs/gameplay."""
    if getattr(ctx, "_gameplay_docs", None) is None:
        docs = []
        for f in sorted((common.DOCS / "gameplay").glob("*.md")):
            text = f.read_text(encoding="utf-8")
            fm, body = common.parse_front_matter(text)
            offset = text[:len(text) - len(body)].count("\n")
            lines, heading = [], ""
            for n, line in enumerate(body.split("\n"), offset + 1):
                if line.startswith("#"):
                    heading = line.lstrip("#").strip()
                lines.append((n, heading, line))
            docs.append(("gameplay/" + f.stem, fm.get("title") or f.stem, lines))
        ctx._gameplay_docs = docs
    return ctx._gameplay_docs


def name_ids(ctx, type_, table):
    """{lower-case display name: [ids]} for a type."""
    out = {}
    for r in ctx.table(table):
        n = ctx.name(type_, r.int("id"))
        if n:
            out.setdefault(n.lower(), []).append(r.int("id"))
    return out


def _cells(line):
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return None
    return [c.strip() for c in s.strip("|").split("|")]


def _plain(text):
    return re.sub(r"[*`]|\[\[[^|\]]*\||\]\]|\[([^\]]*)\]\([^)]*\)|\[([^\]]*)\]\[[^\]]*\]", r"\1\2", text).strip()


def find_mentions(ctx, type_, table, id_column=None):
    """{id: [(path, title, line no, heading, excerpt, [timestamps])]}. A name
    with two or more words matches anywhere (whole words); a one-word name
    only when the line also has the id, or the name is a whole table cell or
    set in *italics* / **bold** / quotes. When a line names ids explicitly,
    a name shared by several ids is credited only to the ids on the line.
    With ``id_column`` (e.g. "buff"), numbers in a table column whose header
    contains that word ("Buff", "Buff ids") count as mentions of those ids."""
    valid = set(ctx.table(table).by())
    names = name_ids(ctx, type_, table)
    multi = {n: ids for n, ids in names.items() if " " in n and len(n) >= 6}
    single = {n: ids for n, ids in names.items() if " " not in n and len(n) >= 4}
    words_of = {nm: common._words(nm) for nm in names}
    out = {}
    for path, title, lines in gameplay_docs(ctx):
        header = None
        for n, heading, line in lines:
            cl = _cells(line)
            if cl is None:
                header = None
            elif header is None:
                header = [c.lower() for c in cl]
            if not line.strip() or line.lstrip().startswith("["):     # link reference lines
                continue
            words = common._words(line)
            # ids named on the line (not parts of times, versions or decimals;
            # ids below 100 are too common as plain numbers to count)
            nums = {int(x) for x in re.findall(r"(?<![\w:.,])\d{3,6}(?![\w:])", line)}
            cells = [c.lower() for c in (_cells(line) or [])]
            hits = set()
            for nm in multi:
                if words_of[nm] in words:
                    hits.add(nm)
            for nm, ids in single.items():
                if words_of[nm] not in words:
                    continue
                emph = re.search(r"(\*\*?|\"|')%s(\*\*?|\"|')" % re.escape(nm), line, re.I)
                if nums & set(ids) or nm in [_plain(c).lower() for c in cells] or emph:
                    hits.add(nm)
            # drop names contained in a longer hit ("Remote Bomb" in "Nexus Remote Bomb")
            hits = {h for h in hits if not any(h != o and words_of[h] in words_of[o] for o in hits)}
            col_ids = set()
            if id_column and header and cl and header != [c.lower() for c in cl]:
                for i, h in enumerate(header):
                    if id_column in h and i < len(cl):
                        col_ids |= {int(x) for x in re.findall(r"\b\d{1,6}\b", cl[i])} & valid
            if not hits and not col_ids:
                continue
            excerpt = _plain(line.strip().strip("|").strip())
            excerpt = re.sub(r"\s+", " ", excerpt.replace(" | ", " · "))
            if len(excerpt) > 160:
                excerpt = excerpt[:157].rstrip() + "..."
            times = TIME_RE.findall(line)
            done = set()
            for nm in hits:
                ids = names[nm]
                named = [i for i in ids if i in nums]
                done |= set(named or ids)
            for i in sorted(done | col_ids):
                out.setdefault(i, []).append((path, title, n, heading, excerpt, times))
    return out


def mentions(ctx):
    if getattr(ctx, "_skill_mentions", None) is None:
        ctx._skill_mentions = find_mentions(ctx, TYPE, "Skill_Base")
    return ctx._skill_mentions


def _num(text):
    m = re.search(r"-?\d[\d,]*(?:\.\d+)?", text or "")
    if not m:
        return None
    v = m.group(0).replace(",", "")
    return float(v) if "." in v else int(v)


def observed(ctx):
    """{skill id: [entry]} from gameplay tables with a Skill column and a
    Cooldown, Mana or TP column. Rows whose skill cell names ids use them;
    otherwise the name must be unique."""
    if getattr(ctx, "_skill_observed", None) is not None:
        return ctx._skill_observed
    names = name_ids(ctx, TYPE, "Skill_Base")
    known = set(ctx.table("Skill_Base").by())
    out = {}
    for path, title, lines in gameplay_docs(ctx):
        header = None
        for n, heading, line in lines:
            cells = _cells(line)
            if cells is None:
                header = None
                continue
            if header is None:
                header = [c.lower() for c in cells]
                continue
            if all(re.fullmatch(r":?-+:?", c) for c in cells):
                continue
            sk = next((i for i, h in enumerate(header) if h.startswith("skill")), None)
            cols = {}
            for i, h in enumerate(header):
                if h.startswith("cooldown") and "client" not in h:
                    cols.setdefault("cooldown_s", i)
                elif h in ("mana", "mp", "mana cost"):
                    cols["mana"] = i
                elif h == "tp":
                    cols["tp"] = i
                elif h.startswith("effect"):
                    cols["effect"] = i
            if sk is None or not ({"cooldown_s", "mana", "tp"} & set(cols)) or sk >= len(cells):
                continue
            cell = cells[sk]
            ids = [int(x) for x in re.findall(r"\b\d{3,6}\b", cell) if int(x) in known]
            if not ids:
                cand = names.get(_plain(cell).lower(), [])
                ids = cand if len(cand) == 1 else []
            if not ids:
                continue
            e = {}
            for k, i in cols.items():
                if i < len(cells) and cells[i]:
                    v = _plain(cells[i]) if k == "effect" else _num(cells[i])
                    if v not in (None, ""):
                        e[k] = v
            if not e:
                continue
            e["source"] = "%s line %d" % (path, n)
            for i in ids:
                out.setdefault(i, []).append(e)
    ctx._skill_observed = out
    return out


def code_mentions(ctx, id_, word):
    """[(file, line no, line)] in contract/*.yaml and server/*.py naming the
    id on a line that also says ``word`` (skill / buff)."""
    cache = getattr(ctx, "_code_lines", None)
    if cache is None:
        cache = ctx._code_lines = {}
    if word not in cache:
        by_num = {}
        for pat in ("contract/*.yaml", "server/*.py"):
            for f in sorted(common.REPO.glob(pat)):
                if f.name.startswith("test_"):
                    continue
                rel = f.relative_to(common.REPO).as_posix()
                for n, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
                    if word not in line.lower():
                        continue
                    for num in set(re.findall(r"(?<![\w.+])(\d{3,6})(?![\w.])", line)):
                        by_num.setdefault(int(num), []).append((rel, n, line.strip()))
        cache[word] = by_num
    return cache[word].get(id_, [])


# ------------------------------------------------------------------ build

def tooltip_formula(text):
    """[{"tag": "EF_STATIC", "value": 80}, ...] from a tooltip's value tags."""
    return [{"tag": t, "value": int(v)} for t, v in re.findall(r"<(EF_\w+) (-?\d+)>", text or "")]


def summarise(ctx, ix, effects, effect_kind):
    """damage_or_effect: the readable part of the effect slots."""
    out = {}
    if effect_kind in EFFECT_KINDS and effect_kind:
        out["kind"] = EFFECT_KINDS[effect_kind]
    elif effect_kind:
        out["kind"] = "effect kind %d" % effect_kind
    for e in effects:
        t, v = e["type"], e["value"]
        if t == 330:
            out["base"] = v
        elif t == 101:
            out["attack_pct"] = v
        elif t == 102:
            out["ability_pct"] = v
        elif t in BUFF_TYPES and v in ix.buffs:
            out.setdefault("buffs", []).append({"buff": v, "rate": e.get("rate", 0)})
        elif t in ix.options:
            out.setdefault("stats", []).append({"code": t, "value": v})
    # only the effect kind with no slot behind it says nothing a server can use
    return out if set(out) - {"kind"} else {}


def build(ctx):
    ix = index(ctx)
    obs = observed(ctx)
    for r in ctx.table("Skill_Base"):
        id_ = r.int("id")
        kind = r.int("kind")
        f = {}
        f["name_key"] = r.str("name_key")
        f["desc_key"] = r.str("desc_key")
        f["kind"] = kind
        f["kind_name"] = KINDS.get(kind, "kind %d" % kind)
        tt = r.int("target_type")
        f["target"] = {"type": tt, "type_name": TARGET_TYPES.get(tt, "none" if not tt else "type %d" % tt),
                       "relation": bits(r.int("relation"), RELATIONS),
                       "unit_classes": bits(r.int("target_class_mask"), UNIT_CLASSES),
                       "max_targets": r.int("max_targets")}
        f["range"] = r.int("range")
        if r.int("aoe"):
            f["area"] = {"shape": r.int("aoe"), "shape_name": AREA_SHAPES.get(r.int("aoe"), "?"),
                         "radius": r.float("aoe_radius"), "width_or_angle": r.float("c38")}
            if r.str("indicator_tex"):
                f["area"]["indicator"] = r.str("indicator_tex")
        cost_type = r.int("cost_type")
        tp = ix.tp.get(id_)
        if cost_type:
            f["cost"] = {"type": cost_type, "type_name": COST_TYPES.get(cost_type, "type %d" % cost_type),
                         "amount": r.int("cost")}
        elif tp is not None:
            f["cost"] = {"type": 14, "type_name": "TP", "amount": tp.int("tp_cost"), "from": "Skill_TP"}
        else:
            f["cost"] = None
        cd = r.int("cooldown_ms")
        if cd:
            f["cooldown"] = {"ms": cd, "group": r.int("cd_group")}
        elif tp is not None and tp.int("cooldown_s"):
            f["cooldown"] = {"ms": tp.int("cooldown_s") * 1000, "group": 0, "from": "Skill_TP"}
        else:
            f["cooldown"] = None
        if r.int("cast_ms"):
            f["cast_ms"] = r.int("cast_ms")
        if r.int("channel_ms"):
            f["channel"] = {"ms": r.int("channel_ms"), "tick_ms": r.int("channel_tick_ms")}
        if r.int("movement"):
            f["movement"] = MOVEMENT.get(r.int("movement"), r.int("movement"))
        if r.int("delivery"):
            f["delivery"] = {"type": r.int("delivery"), "field_tick": r.float("field_tick")}
        f["effect_kind"] = r.int("effect_kind")
        effects = []
        for n in range(1, 5):
            t = r.int("eff%d_type" % n)
            if t:
                effects.append({"slot": n, "type": t, "value": r.int("eff%d_value" % n),
                                "rate": r.int("eff%d_rate" % n)})
        f["effects"] = effects
        f["damage_or_effect"] = summarise(ctx, ix, effects, r.int("effect_kind"))
        tip = ctx.s(r.get("desc_key"))
        if tooltip_formula(tip):
            f["tooltip_formula"] = tooltip_formula(tip)
        reqs = []
        for n in (1, 2):
            t = r.int("req%d_type" % n)
            if t:
                reqs.append({"type": t, "a": r.int("req%d_a" % n), "b": r.int("req%d_b" % n)})
        if reqs:
            f["requirements"] = reqs
        if r.int("weapon_type"):
            f["weapon_type"] = r.int("weapon_type")
        if r.int("visual"):
            f["visual"] = r.int("visual")
        f["icon"] = {"file": r.str("icon_file"), "index": r.int("icon_idx")} if r.str("icon_file") else None
        used = []
        for wb, slot in ix.weapon.get(id_, []):
            used.append({"weapon_base": wb, "slot": slot, "items": ix.weapon_items.get(wb, [])})
        for hero, slot in ix.hero.get(id_, []):
            used.append({"hero": hero, "slot": slot})
        for item in ix.item_use.get(id_, []):
            used.append({"item_use": item})
        f["used_by"] = used
        if tp is not None:
            f["tp"] = {"row": tp.int("id"), "tp_cost": tp.int("tp_cost"), "cooldown_s": tp.int("cooldown_s"),
                       "need_flags": tp.int("need_flags"), "c7": tp.int("c7")}
        sources = ["client: Skill_Base.cdb id %d" % id_]
        if tp is not None:
            sources.append("client: Skill_TP.cdb row %d" % tp.int("id"))
        if tip and f.get("tooltip_formula"):
            sources.append("client: StringAll_Eng %s (tooltip value tags)" % r.get("desc_key"))
        if id_ in obs:
            f["observed"] = obs[id_]
            for e in obs[id_]:
                s = "gameplay: [[%s]]" % e["source"].split(" line ")[0]
                if s not in sources:
                    sources.append(s)
        req = PASSIVE_REQUIRED if kind == 2 else REQUIRED
        yield Page(TYPE, id_, ctx.title(TYPE, id_), fields=f, sources=sources, body=body, required=req)


# ------------------------------------------------------------------ rendering

def fmt_ms(ms):
    return "%s s" % fmt_num(ms / 1000.0) if ms % 1000 else "%d s" % (ms // 1000)


def formula_text(formula):
    parts = []
    for e in formula or []:
        if not isinstance(e, dict):
            continue
        key, unit = TAGS.get(e.get("tag"), (None, " " + str(e.get("tag"))))
        parts.append("%s%s" % (e.get("value"), unit))
    return " + ".join(parts)


def buff_cell(ctx, ix, value):
    return ctx.link("buffs", value) if value in ix.buffs else str(value)


def body(ctx, page):
    ix = index(ctx)
    fm, id_ = page.fm, page.id
    row = ctx.table("Skill_Base").get(id_)
    L, info = [], []
    img = ctx.image(TYPE, id_)
    if img:
        info.append(("", "![%s](%s)" % (common.link_text(page.title), img)))
    info.append(("Skill id", "`%d`" % id_))
    info.append(("Kind", "%s (%s)" % (fm.get("kind_name"), fm.get("kind"))))
    tg = fm.get("target") if isinstance(fm.get("target"), dict) else {}
    if tg:
        bits_ = ", ".join(tg.get("relation") or []) or "-"
        info.append(("Target", "%s; %s; units: %s; up to %s" % (
            tg.get("type_name"), bits_, ", ".join(tg.get("unit_classes") or []) or "-", tg.get("max_targets"))))
    if fm.get("range") is not None:
        info.append(("Range", "%s (world units)" % fm.get("range")))
    ar = fm.get("area")
    if isinstance(ar, dict):
        info.append(("Area", "%s, radius %s, width/angle %s%s" % (
            ar.get("shape_name"), fmt_num(ar.get("radius")), fmt_num(ar.get("width_or_angle")),
            " (indicator `%s`)" % ar["indicator"] if ar.get("indicator") else "")))
    cost = fm.get("cost")
    if isinstance(cost, dict):
        info.append(("Cost", "%s %s" % (fmt_num(cost.get("amount", 0)), cost.get("type_name"))))
    cd = fm.get("cooldown")
    if isinstance(cd, dict) and cd.get("ms"):
        info.append(("Cooldown", fmt_ms(cd["ms"]) + (" (group %s)" % cd["group"] if cd.get("group") else "")))
    if fm.get("cast_ms"):
        info.append(("Cast time", fmt_ms(fm["cast_ms"])))
    ch = fm.get("channel")
    if isinstance(ch, dict):
        info.append(("Channel", "%s, tick every %s" % (fmt_ms(ch.get("ms", 0)), fmt_ms(ch.get("tick_ms", 0)))))
    if fm.get("movement"):
        info.append(("Movement", fm["movement"]))
    dl = fm.get("delivery")
    if isinstance(dl, dict):
        info.append(("Delivery", "%s%s" % (DELIVERY.get(dl.get("type"), dl.get("type")),
                                           ", tick %s" % fmt_num(dl["field_tick"]) if dl.get("field_tick") else "")))
    if fm.get("effect_kind"):
        info.append(("Effect kind", "%s (%s)" % (EFFECT_KINDS.get(fm["effect_kind"], "?"), fm["effect_kind"])))
    if fm.get("weapon_type"):
        info.append(("Needs weapon type", fm["weapon_type"]))
    if fm.get("visual"):
        info.append(("Visual", "skillVisual %s `%s`" % (fm["visual"], ix.visual.get(fm["visual"], "?"))))
    tp = fm.get("tp")
    if isinstance(tp, dict):
        info.append(("TP skill", "%s TP, %s s cooldown (Skill_TP row %s)" % (
            fmt_num(tp.get("tp_cost", 0)), tp.get("cooldown_s"), tp.get("row"))))
    if isinstance(fm.get("icon"), dict):
        ic = fm["icon"]
        info.append(("Icon", "`ui/icons/%s` cell %s" % (ic.get("file"), ic.get("index"))))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))

    tip = ctx.s(row.get("desc_key")) if row else None
    if tip:
        L += ["### Tooltip", "", quote(tip)]
        ft = formula_text(fm.get("tooltip_formula"))
        if ft:
            L += ["Tooltip formula: **%s** (the client fills these in from the caster's stats)." % ft, ""]

    dmg = fm.get("damage_or_effect")
    effects = [e for e in (fm.get("effects") or []) if isinstance(e, dict)]
    if effects:
        L += ["### Effect slots", "",
              "Raw `Skill_Base` effect slots; the client never applies them, the server does. "
              "Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).", ""]
        rows = []
        for e in effects:
            t, v = e.get("type"), e.get("value")
            shown = buff_cell(ctx, ix, v) if t in BUFF_TYPES else fmt_num(v)
            rows.append((e.get("slot"), t, effect_text(ctx, t, v), shown, e.get("rate")))
        L.append(table_md(["slot", "type", "meaning", "value", "rate"], rows))
    if isinstance(dmg, dict) and dmg:
        parts = []
        if "base" in dmg:
            parts.append(fmt_num(dmg["base"]))
        if "attack_pct" in dmg:
            parts.append("%s%% Attack" % dmg["attack_pct"])
        if "ability_pct" in dmg:
            parts.append("%s%% Ability Power" % dmg["ability_pct"])
        line = []
        if parts:
            line.append("amount **%s**" % " + ".join(parts))
        if dmg.get("kind"):
            line.append(dmg["kind"])
        for b in dmg.get("buffs") or []:
            if isinstance(b, dict):
                line.append("applies %s (%s%%)" % (ctx.link("buffs", b.get("buff")), b.get("rate")))
        if line:
            L += ["**Reading:** " + "; ".join(line) + ".", ""]
        tags = {}
        for e in fm.get("tooltip_formula") or []:
            if isinstance(e, dict) and TAGS.get(e.get("tag"), ("",))[0] in ("base", "attack_pct", "ability_pct"):
                tags[TAGS[e["tag"]][0]] = e.get("value")
        slots = {k: dmg[k] for k in ("base", "attack_pct", "ability_pct") if k in dmg}
        if tags and slots and tags != slots:
            L += ["> [!warning] The tooltip (%s) and the effect slots (%s) disagree; one of them "
                  "was out of date in the shipped client." % (formula_text(fm.get("tooltip_formula")),
                                                             " + ".join(parts)), ""]

    reqs = [q for q in (fm.get("requirements") or []) if isinstance(q, dict)]
    if reqs:
        L += ["### Requirements", "", "`Skill_Base` requirement slots (type 1 = needs a buff or item, "
              "checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):", ""]
        L.append(table_md(["type", "a", "b"], [(q.get("type"), buff_cell(ctx, ix, q.get("a")) if q.get("type") == 1 else q.get("a"), q.get("b")) for q in reqs]))

    use = []
    for u in fm.get("used_by") or []:
        if not isinstance(u, dict):
            continue
        if "weapon_base" in u:
            slot = u.get("slot", 0)
            key = SLOT_KEYS.get(slot, "hero set %d" % (slot - 4) if slot > 4 else str(slot))
            items = u.get("items") or []
            shown = ", ".join(ctx.link("items", i) for i in items[:8])
            if len(items) > 8:
                shown += " and %d more" % (len(items) - 8)
            use.append("Weapon skill **%s** of WeaponBase %s: %s" % (key, u["weapon_base"], shown or "no item uses this base"))
        elif "hero" in u:
            use.append("Hero %s, skill %s" % (ctx.link("heroes", u["hero"]), u.get("slot")))
        elif "item_use" in u:
            use.append("Cast when %s is used (Item_Base option 210)" % ctx.link("items", u["item_use"]))
        else:
            use.append("%s (hand-entered)" % ", ".join("%s %s" % kv for kv in u.items()))
    for p in ix.policy.get(id_, []):
        use.append("Nation policy %s `%s` (Policy.cdb, server-only; buff_or_skill)" % (
            p.int("id"), ctx.s(p.get("name_key")) or p.get("name_key")))
    if use:
        L += ["### Used by", ""] + ["- " + u for u in use] + [""]

    obs = [o for o in (fm.get("observed") or []) if isinstance(o, dict)]
    if obs:
        L += ["### Observed in play", "", "Numbers from the gameplay pages (guides, patch notes, video), "
              "not from the client:", ""]
        rows = []
        for o in obs:
            src = str(o.get("source", ""))
            path = src.split(" line ")[0]
            rows.append((o.get("cooldown_s", ""), o.get("mana", ""), o.get("tp", ""), o.get("effect", ""),
                         "[[%s]]%s" % (path, src[len(path):]) if path.startswith("gameplay/") else src))
        L.append(table_md(["cooldown (s)", "mana", "TP", "effect", "source"], rows))

    srv = ix.server.get(id_, [])
    code = code_mentions(ctx, id_, "skill")
    if srv or code:
        L += ["### Current server", ""]
        for item, slot in srv:
            L.append("- `server/skills.py` WEAPON_SKILLS puts it on slot %s for %s." % (
                SLOT_KEYS.get(slot, slot), ctx.link("items", item)))
        if srv:
            L.append("- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; "
                     "nothing above is used yet.")
        for f, n, l in code:
            if f == "server/skills.py" and srv:
                continue
            L.append("- `%s` line %d: `%s`" % (f, n, l[:140].replace("`", "'")))
        L.append("")

    ment = mentions(ctx).get(id_, [])
    if ment:
        L += ["### Mentioned in", ""] + mention_lines(ment) + [""]
    return "\n".join(L)


def mention_lines(ment):
    out = []
    for path, title, n, heading, excerpt, times in ment[:12]:
        where = "[[%s|%s]]" % (path, common.link_text(str(title)))
        if heading:
            where += " § %s" % common.link_text(heading)
        at = ", at %s" % ", ".join(times) if times else ""
        out.append("- %s (line %d%s): %s" % (where, n, at, excerpt.replace("[[", "").replace("]]", "")))
    if len(ment) > 12:
        out.append("- and %d more lines" % (len(ment) - 12))
    return out

"""Monsters: one page per hostile UnitDB row (ctx.unit_type(id) == "monsters").

Which rows: UnitDB category@8a 1 (monster), 3 (elite / named variants), 6
(dungeon bosses), 8 (field monsters: ogres, trolls, bears, phytons) and 9,
minus units with a shop or a quest-talk portrait (those are NPCs). The split
lives in common.UNIT_TYPES so every module links a unit to the same folder.

What the client has (docs/spec/monsters.md; all *client*):
  UnitDB      name, category, class mask, model (ObjectList id) + scale, second
              scale/radius f32@a8, nameplate height? f32@c0, kill group i32@80,
              projectile? u32@bc, and 7 pairs {a, id}. The spec calls the ids
              "skills", but none of them is a Skill_Base id: 1,772 of 1,838 are
              rows of sound.csv ('Unit/UE4070008.wav'; players: 'voice/UV...'),
              so they are written here as ``sounds``.
  Quest       objective type 1 = kill {a = unit id or kill group, need, drop
              rate %, quest item, 3 map ids}. Ids >= 10000 are not units: they
              equal UnitDB i32@80 of a family of units (10001 = Fragile Tow
              Warrior/Sorcerer ...), so i32@80 is the kill-credit group
              (*inferred*: every group id used by a quest exists in i32@80).
  DungeonAdmission  what a dungeon's entry window advertises (no rates).
  HeroData    hero transforms named after the bosses (portrait = boss art).
There is no HP, level, damage, exp, gold or loot table in the client: those
are the REQUIRED fields people fill in by hand.

Hand-written knowledge used:
  docs/gameplay/dungeon-drops.md and maps-and-dungeons.md (boss -> dungeon
  field, parsed from their tables), video-early-quests.md §5 (HP read off the
  target frame, copied below in SOURCED with the timestamp), every gameplay
  page that names the monster (``Seen in``, with video timestamps).
  server/world.py MONSTERS and server/loot.py EXTRA_DROPS are shown as "current
  server" (our choices), never copied into the front matter.

Front-matter shapes people should use for the missing fields:
  drops:  [{"item": 2550, "rate": 100, "count": [1, 1]}]   (items.py reads this)
  spawns: [{"field": 89, "x": 1434.3, "z": 415.0, "count": 3, "respawn_s": 10}]
"""
import ast
import re

from . import common
from .common import DOCS, Page, clean_name, fmt_num, parse_front_matter, repeat, table_md

TYPE = "monsters"
KIND = "monster"
LABEL = "Monster"
PLURAL = "Monsters"
DESCRIPTION = ("Every hostile unit in the client's `UnitDB` table: field monsters, elites, quest "
               "officers, dungeon bosses, war minions. The client has their names, models and "
               "kill groups; their combat numbers, rewards and spawns were server data and are "
               "filled in by hand.")
REQUIRED = ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed",
            "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
UNION_KEYS = ["spawn_fields"]

CATEGORIES = {1: "monster", 3: "elite / named variant (inferred)", 6: "boss (inferred: every dungeon boss and quest bosses such as Tow Chief)",
              8: "field monster (inferred: ogres, trolls, bears, phytons)", 9: "special (unknown)"}
CLASS_BITS = [(1, "monster"), (2, "NPC"), (4, "player"), (8, "structure/bot"), (16, "16 (?)"),
              (32, "untargetable"), (64, "misc")]

YT = "https://www.youtube.com/watch?v=s04CSN16w1s&t=%ds"
EARLY = "[[gameplay/video-early-quests|Video notes: the first 20 levels]]"
# Hard numbers from docs/gameplay, each with its source. Only rows whose unit id
# is certain: the name is unique, or the page gives the id / the quest group.
SOURCED = {}
for _ids, _hp, _regen, _t, _why in [
        ((702,), 600, 12, 1910, "Elite Skeleton Warrior during quest 101 (kill group 10004 = 702/703)"),
        ((704,), 2000, 0, 2120, "Skeleton Warrior Officer, quest 10's target 704"),
        ((650, 651), 600, None, 3220, "Fragile Lizard Swordsman (both rows carry the name, kill group 10005)"),
        ((826,), 5000, 100, 4200, "Tow Chief 826"),
        ((723, 724), 1400, 28, 5255, "Fragile Elite Tow Warrior / Sorcerer"),
        ((715, 716), 1500, 30, 4900, "Fragile Black / Red Ghost"),
        ((717, 718), 2000, 40, 4995, "Fragile Elite Black / Red Ghost")]:
    for _i in _ids:
        f = {"hp": _hp}
        if _regen is not None:
            f["hp_regen"] = _regen
        SOURCED[_i] = (f, "video: %s §5, target frame at [%d:%02d](%s): HP %d%s (%s)" % (
            EARLY, _t // 60, _t % 60, YT % _t, _hp,
            "" if _regen is None else ", regen +%d/tick (2%% of max)" % _regen, _why))


class Index:
    """Lookups over the client tables and the gameplay docs, built once."""

    def __init__(self, ctx):
        t = ctx.table
        self.units = {r.int("id"): r for r in t("UnitDB")}
        self.ids = [i for i in self.units if ctx.unit_type(i) == TYPE]
        self.groups = {}
        for i, r in self.units.items():
            if r.int("i32@80"):
                self.groups.setdefault(r.int("i32@80"), []).append(i)
        self.by_name = {}
        for i in self.ids:
            n = ctx.name(TYPE, i)
            if n:
                self.by_name.setdefault(n.lower(), []).append(i)
        self.sounds = t("sound").by()
        self.objects = t("ObjectList").by()
        # quests: kill objectives (type 1)
        self.quests = {}
        for q in t("Quest"):
            qid = q.int("id")
            for typ, a, need, rate, item, _e, m1, m2, m3 in repeat(
                    q, "obj%d_type", "obj%d_a", "obj%d_b", "obj%d_c", "obj%d_d", "obj%d_e",
                    "obj%d_map1", "obj%d_map2", "obj%d_map3"):
                if typ != 1 or not a:
                    continue
                maps = sorted({m for m in (m1, m2, m3) if m})
                targets = ([a] if a in self.units else []) + [u for u in self.groups.get(a, []) if u != a]
                for u in targets:
                    self.quests.setdefault(u, []).append({
                        "quest": qid, "target": a, "need": need, "rate": rate, "item": item,
                        "maps": maps, "via_group": u != a})
        self.admission = {r.int("field"): r for r in t("DungeonAdmission")}
        self.bosses = boss_fields(self.units)
        self.heroes = {}
        for h in t("HeroData"):
            n = ctx.s(h.get("name_key"))
            if n:
                self.heroes.setdefault(n.lower(), h.int("id"))
        self.server = server_monsters()
        items = ctx.module("items")
        self.server_drops = {}
        if items is not None and hasattr(items, "server_drops"):
            for item, rows in items.server_drops().items():
                for unit, chance, lo, hi in rows:
                    self.server_drops.setdefault(unit, []).append((item, chance, lo, hi))
        self.seen = Mentions(ctx, self)


def boss_fields(units):
    """{unit: {field: [doc paths]}} from the boss tables of dungeon-drops.md
    (§1: '**121** ...' | 'King Deathhead **672**; Tough King Deathhead 804')
    and maps-and-dungeons.md §2 ('| 121 | King Deathhead (672; ...)')."""
    out = {}
    specs = [("dungeon-drops", 1, 2), ("maps-and-dungeons", 2, 3)]
    for stem, fcol, bcol in specs:
        try:
            text = (DOCS / "gameplay" / (stem + ".md")).read_text(encoding="utf-8")
        except OSError:
            continue
        for line in text.split("\n"):
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) <= bcol:
                continue
            m = re.search(r"\*\*(\d{3})\*\*", cells[fcol]) or re.fullmatch(r"(\d{3})", cells[fcol])
            if not m:
                continue
            field = int(m.group(1))
            for u in re.findall(r"(?<![\d.])(\d{3,4})(?![\d.])", cells[bcol]):
                u = int(u)
                if u in units:
                    out.setdefault(u, {}).setdefault(field, [])
                    if stem not in out[u][field]:
                        out[u][field].append(stem)
    return out


def server_monsters():
    """server/world.py MONSTERS -> {unit: [(level, hp, dx, dz)]} (read with
    ast; our choices, not original data)."""
    out = {}
    try:
        tree = ast.parse((common.REPO / "server" / "world.py").read_text(encoding="utf-8"))
    except (OSError, SyntaxError):
        return out
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "MONSTERS" for t in node.targets):
            try:
                rows = ast.literal_eval(node.value)
            except ValueError:
                return out
            for unit, _name, level, hp, dx, dz in rows:
                out.setdefault(unit, []).append((level, hp, dx, dz))
    return out


# ------------------------------------------------------------- "Seen in" lines

WORD = re.compile(r"\w+(?:'\w+)*")
STAMP = re.compile(r"\[(\d{1,2}:\d{2}(?::\d{2})?)\]\((https?://[^)\s]+)\)")


class Mentions:
    """Lines of docs/gameplay/*.md that name a monster. Names are matched
    longest first (so 'Elite Skeleton Warrior' does not also count as
    'Skeleton Warrior', and item/field names such as 'Slime Mucus' or 'Skull
    Temple' hide the monster word inside them). When the line also carries
    one of the unit ids that share the name, only that id is credited."""

    def __init__(self, ctx, ix):
        vocab = {}                       # lower name -> monster ids ([] = mask only)
        for n, ids in ix.by_name.items():
            vocab[n] = ids
        for r in ctx.table("Item_Base"):
            n = ctx.name("items", r.int("id"))
            if n and len(n) > 3:
                vocab.setdefault(n.lower(), [])
        for k, v in ctx.strings.items():
            if k.startswith(("FieldName_", "UnitName_", "HeroName_")) and v:
                n = clean_name(re.sub(r"^\s*(\[[^\]]*\]|<[^>]*>[^<]*</[^>]*>)\s*", "", v))
                if n and len(n) > 3:
                    vocab.setdefault(n.lower(), [])
        # matched as word n-grams, longest first (a dict lookup per position)
        self.vocab = {}
        for n, ids in vocab.items():
            key = tuple(WORD.findall(n))
            if key:
                self.vocab.setdefault(key, ids)
        self.maxn = max((len(k) for k in self.vocab), default=0)
        self.hits = {}                   # unit -> [(doc, title, heading, stamps, snippet, exact)]
        for f in sorted((DOCS / "gameplay").glob("*.md")):
            text = f.read_text(encoding="utf-8")
            fm, body = parse_front_matter(text)
            self._scan("gameplay/" + f.stem, str(fm.get("title") or f.stem), body)

    def _scan(self, doc, title, body):
        heading = ""
        fence = False
        for line in body.split("\n"):
            if line.startswith("```"):
                fence = not fence
            if fence:
                continue
            if re.match(r"#{1,6} ", line):
                heading = line.lstrip("#").strip()
                continue
            if not line.strip():
                continue
            nums = {int(x) for x in re.findall(r"(?<![\d.,])(\d{3,5})(?![\d.,])", line)}
            stamps = []
            for m in STAMP.finditer(line):
                s = "[%s](%s)" % (m.group(1), m.group(2))
                if s not in stamps:
                    stamps.append(s)
            words = WORD.findall(line)
            low = [w.lower() for w in words]
            credited = {}
            i = 0
            while i < len(words):
                for n in range(min(self.maxn, len(words) - i), 0, -1):
                    ids = self.vocab.get(tuple(low[i:i + n]))
                    if ids is not None:
                        break
                else:
                    i += 1
                    continue
                first = words[i]
                i += n
                if not ids or (n == 1 and len(first) < 6 and not first[:1].isupper()):
                    continue
                exact = [u for u in ids if u in nums]
                for u in exact or ids:
                    credited[u] = credited.get(u, False) or bool(exact)
            for i, exact in credited.items():
                self.hits.setdefault(i, []).append((doc, title, heading, stamps, snippet(line), exact))

    def get(self, unit_id, limit=12):
        rows = self.hits.get(unit_id, [])
        rows = sorted(rows, key=lambda r: (not r[5], not r[3]))  # exact ids, then timestamped
        return rows[:limit], max(0, len(rows) - limit)


def snippet(line, n=160):
    s = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", line)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\[([^\]]*)\]\[[^\]]*\]", r"\1", s)
    s = s.replace("|", " · ").replace("**", "").replace("`", "")
    s = re.sub(r"\s+", " ", s).strip(" ·-")
    s = s.replace("<", "&lt;").replace(">", "&gt;")
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"


# --------------------------------------------------------------------- build

def field_type(ix, field):
    return "dungeons" if field in ix.admission else "fields"


def build(ctx):
    ix = Index(ctx)
    ctx.monsters_index = ix
    for id_ in ix.ids:
        r = ix.units[id_]
        f = {}
        sources = ["client: UnitDB.cdb id %d" % id_]
        f["name_key"] = r.str("name_key")
        f["category"] = r.int("category@8a")
        f["class_mask"] = r.int("class_mask@7c")
        if r.int("i32@80"):
            f["kill_group"] = r.int("i32@80")
        model = r.int("model@ac")
        f["model"] = model
        obj = ix.objects.get(model)
        if obj is not None:
            f["model_name"] = obj.get("name")
            f["model_path"] = obj.get("model path")
        f["scale"] = num(r.float("scale@a4"))
        f["radius"] = num(r.float("f32@a8"))
        if r.int("u32@bc"):
            f["projectile"] = r.int("u32@bc")
        snd = [s for _a, s in pairs(r) if s]
        if snd:
            f["sounds"] = snd
        hero = ix.heroes.get((ctx.name(TYPE, id_) or "").lower())
        if hero is not None:
            f["hero"] = hero
            sources.append("client: HeroData.cdb id %d (hero transform of the same name)" % hero)
        boss = ix.bosses.get(id_, {})
        if boss:
            f["boss_of"] = sorted(boss)
            for doc in sorted({d for docs in boss.values() for d in docs}):
                sources.append("docs: [[gameplay/%s]] (boss of field %s)" % (
                    doc, ", ".join(str(k) for k, v in sorted(boss.items()) if doc in v)))
            rewards = []
            for field in sorted(boss):
                adm = ix.admission.get(field)
                if adm is not None:
                    items = [it for (it,) in repeat(adm, "show_item%d")]
                    if items:
                        rewards.append({"field": field, "items": items})
            if rewards:
                f["dungeon_rewards"] = rewards
                sources.append("client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)")
        qs = ix.quests.get(id_, [])
        if qs:
            f["quest_targets"] = [dict({"quest": q["quest"], "need": q["need"]},
                                       **({"group": q["target"]} if q["via_group"] else {})) for q in qs]
            drops = [{"quest": q["quest"], "item": q["item"], "rate": q["rate"], "need": q["need"]}
                     for q in qs if q["item"]]
            if drops:
                f["quest_drops"] = drops
            sources.append("client: Quest.cdb kill objectives (quests %s)" % ", ".join(
                str(x) for x in sorted({q["quest"] for q in qs})))
        fields = set(boss)
        for q in qs:
            fields.update(q["maps"])
        if fields:
            f["spawn_fields"] = sorted(fields)
        if id_ in SOURCED:
            vals, src = SOURCED[id_]
            f.update(vals)
            sources.append(src)
        yield Page(TYPE, id_, ctx.title(TYPE, id_), fields=f, sources=sources, body=body)


def num(v):
    return int(v) if isinstance(v, float) and v.is_integer() else round(v, 4)


def pairs(r):
    a = [h for h in r if h.startswith("a@")]
    s = [h for h in r if h.startswith("skill@")]
    return [(r.int(x), r.int(y)) for x, y in zip(a, s)]


# ------------------------------------------------------------------ rendering

def body(ctx, page):
    ix = ctx.monsters_index
    fm, id_ = page.fm, page.id
    r = ix.units[id_]
    L = []
    info = []
    img = ctx.image(TYPE, id_)
    if img:
        info.append(("", "![%s](%s)" % (common.link_text(page.title), img)))
    info.append(("Unit id", "`%d`" % id_))
    cat = fm.get("category")
    info.append(("Category", "%s (`category@8a` = %s)" % (CATEGORIES.get(cat, "unknown"), cat)))
    mask = fm.get("class_mask") or 0
    info.append(("Class mask", "%s (%s)" % (mask, ", ".join(n for b, n in CLASS_BITS if mask & b) or "none")))
    if fm.get("kill_group"):
        g = fm["kill_group"]
        mates = [u for u in ix.groups.get(g, []) if u != id_]
        info.append(("Kill group", "`%d`%s" % (g, (" with " + ", ".join(ctx.unit_link(u) for u in mates)) if mates else "")))
    if fm.get("model") is not None:
        info.append(("Model", "ObjectList `%s` %s%s" % (
            fm["model"], fm.get("model_name") or "", (" (`%s`)" % fm["model_path"]) if fm.get("model_path") else "")))
    info.append(("Scale", "%s (second scale / radius %s)" % (fm.get("scale"), fm.get("radius"))))
    if fm.get("projectile"):
        info.append(("Projectile?", "`u32@bc` = %s (archers carry one; meaning *inferred*)" % fm["projectile"]))
    if fm.get("hero"):
        info.append(("Hero transform", ctx.link("heroes", fm["hero"])))
    for field in fm.get("boss_of") or []:
        info.append(("Boss of", ctx.link(field_type(ix, field), field)))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))
    if not img:
        L += ["*No image: the client has no 2-D monster art (only the 3-D model)%s.*" % (
            "" if not fm.get("hero") else "; the hero portrait is used when it is extracted"), ""]

    # the numbers the server needs
    rows = []
    for k in REQUIRED:
        v = fm.get(k)
        if k == "drops":
            shown = "%d entries (below)" % len(v) if isinstance(v, list) and v else ""
        elif k == "spawns":
            shown = "%d entries (below)" % len(v) if isinstance(v, list) and v else ""
        else:
            shown = "" if common.empty(v) else fmt_num(v) if isinstance(v, (int, float)) else str(v)
        rows.append((k, shown or "**missing**"))
    if fm.get("hp_regen") is not None:
        rows.append(("hp_regen", fmt_num(fm["hp_regen"])))
    L += ["### Server stats", "",
          "None of these is in the client; they were server data. Fill them in the front matter "
          "with a source (`drops: [{\"item\": id, \"rate\": %, \"count\": [min, max]}]`, "
          "`spawns: [{\"field\": id, \"x\": .., \"z\": .., \"count\": n, \"respawn_s\": s}]`).", "",
          table_md(["field", "value"], rows)]

    drops = [d for d in (fm.get("drops") or []) if isinstance(d, (dict, int))]
    if drops:
        L += ["### Drops", ""]
        for d in drops:
            d = {"item": d} if isinstance(d, int) else d
            extra = ", ".join("%s %s" % (k, v) for k, v in d.items() if k != "item")
            L.append("- %s%s" % (ctx.link("items", d["item"]) if isinstance(d.get("item"), int) else d.get("item"),
                                 " — " + extra if extra else ""))
        L.append("")
    spawns = [s for s in (fm.get("spawns") or []) if isinstance(s, dict)]
    if spawns:
        L += ["### Spawns", "", table_md(["field", "x", "z", "count", "respawn s"], [
            (ctx.link(field_type(ix, s["field"]), s["field"]) if isinstance(s.get("field"), int) else s.get("field"),
             s.get("x"), s.get("z"), s.get("count"), s.get("respawn_s")) for s in spawns])]

    # quests
    qs = ix.quests.get(id_, [])
    if qs:
        L += ["### Quests", ""]
        for q in qs:
            what = "kill %d" % q["need"]
            if q["item"]:
                what = "collect %d × %s (drops at %s%% while the quest is active)" % (
                    q["need"], ctx.link("items", q["item"]), q["rate"])
            via = (" — via kill group `%d` (*inferred* from UnitDB `i32@80`)" % q["target"]) if q["via_group"] else ""
            where = ", ".join(ctx.link(field_type(ix, m), m) for m in q["maps"])
            L.append("- %s: %s%s%s" % (ctx.link("quests", q["quest"]), what, (" in " + where) if where else "", via))
        L.append("")

    # where it appears
    where = []
    for field in sorted(fm.get("spawn_fields") or []):
        if not isinstance(field, int):
            continue
        why = []
        if field in ix.bosses.get(id_, {}):
            why.append("boss (%s)" % ", ".join("[[gameplay/%s]]" % d for d in ix.bosses[id_][field]))
        qn = sorted({q["quest"] for q in qs if field in q["maps"]})
        if qn:
            why.append("quest map of %s" % ", ".join(ctx.link("quests", x) for x in qn[:6]))
        where.append("- %s — %s" % (ctx.link(field_type(ix, field), field), "; ".join(why) or "hand-entered"))
    if where:
        L += ["### Where it appears", "",
              "Fields the client ties it to (quest objective maps, dungeon boss tables). Positions "
              "and counts are not in the client: add them as `spawns`.", ""] + where + [""]

    rewards = fm.get("dungeon_rewards") or []
    if rewards:
        L += ["### Dungeon rewards (advertised)", "",
              "What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible "
              "rewards of the whole dungeon, not this boss's drop table, and has no rates.", ""]
        for rw in rewards:
            if isinstance(rw, dict):
                L.append("- %s: %s" % (ctx.link("dungeons", rw.get("field")),
                                       ", ".join(ctx.link("items", i) for i in rw.get("items") or [])))
        L.append("")

    same = [u for u in ix.by_name.get((ctx.name(TYPE, id_) or "").lower(), []) if u != id_]
    if same:
        L += ["### Other units with this name", "",
              ", ".join(ctx.unit_link(u, "%s (%d)" % (ctx.title(TYPE, u), u)) for u in same), ""]

    snd = [(a, s) for a, s in pairs(r) if s]
    if snd:
        rows = []
        for n, (a, s) in enumerate(pairs(r), 1):
            if not s:
                continue
            row = ix.sounds.get(s)
            rows.append((n, a, s, "`%s`" % row.get("filename") if row is not None else "not in sound.csv"))
        L += ["### Sounds", "",
              "UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as "
              "skills, but they are `sound.csv` ids (*client*); `a` is unknown.", "",
              table_md(["slot", "a", "sound id", "file"], rows)]

    srv = ix.server.get(id_, [])
    sdrops = ix.server_drops.get(id_, [])
    if srv or sdrops:
        L += ["### Current server", "", "What `server/` does now (our choices, not original data):", ""]
        if srv:
            L.append("- `server/world.py` MONSTERS: %d spawned near the tutorial centre, level %s, HP %s" % (
                len(srv), "/".join(sorted({str(s[0]) for s in srv})), "/".join(sorted({str(s[1]) for s in srv}))))
        if sdrops:
            L.append("- `server/loot.py` EXTRA_DROPS: " + "; ".join(
                "%s %g%% × %d–%d" % (ctx.link("items", it), c * 100, lo, hi) for it, c, lo, hi in sdrops))
        L.append("")

    seen, more = ix.seen.get(id_)
    if seen:
        L += ["### Seen in", ""]
        for doc, title, heading, stamps, snip, exact in seen:
            at = (" at " + ", ".join(stamps[:4])) if stamps else ""
            sec = (" § %s" % common.link_text(heading)) if heading else ""
            tag = "" if exact else " *(name match)*"
            L.append("- [[%s|%s]]%s%s%s: %s" % (doc, common.link_text(title), sec, at, tag, snip))
        if more:
            L.append("- … and %d more lines" % more)
        L.append("")

    raw = [(h, r.get(h)) for h in ("str@40", "i32@84", "u8@8c", "u16@88", "u8@91", "u32@b8", "f32@c0",
                                    "u8@92", "list5@93", "list5@98", "i32@104", "u8@90", "i32@108", "f32@10c")
           if r.get(h) not in (None, "", "0")]
    if raw:
        L += ["### Other client fields", "",
              "Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).", "",
              table_md(["column", "value"], raw)]
    return "\n".join(L)

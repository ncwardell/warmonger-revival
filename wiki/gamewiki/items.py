"""Items: one page per Item_Base row (the reference entity module).

Client sources (data/tables/*.tsv, see docs/spec/data-tables.md):
  Item_Base     name/tooltip keys, kind (ItemKind), price + currency, cost pair,
                fame requirement, bind, class mask, flags, 10 option slots,
                icon (file + cell), period, c41@92 = ItemSancMet id (inferred:
                every equipment row's value is an ItemSancMet id)
  ItemOption    option code -> stat name and display format
  WeaponBase    option 200 -> weapon base row: 4 normal + 4 hero Skill_Base ids
  Item_Jewel    rune stats (server-only table; row id = item id - 7000 via name_key)
  SetBounsItem  set pieces + bonus tiers
  Item_Make     crafting recipes (as result and as material)
  ItemSancMet   reinforcement materials per step
  Npc_Carry     NPC shop stock (shop id = UnitDB u16@a2)
  Quest         reward items (type 1/8) and quest drops (objective type 1)
  RandomBox, Gacha_00..06, PrimiumShop, JewelSocketMake, DungeonAdmission,
  WinAffect     other ways to get or use an item
Other pages: monster pages' ``drops`` front matter ([{"item": id, "rate": %,
"count": [min, max]}]) is listed under "Dropped by" and in obtained_from.
server/loot.py EXTRA_DROPS (what the current server does) is shown, not used.
"""
import ast

from . import common
from .common import Page, fmt_num, quote, repeat, table_md

TYPE = "items"
KIND = "item"
LABEL = "Item"
DESCRIPTION = ("Every item in the client's `Item_Base` table: equipment, weapons, runes, "
               "consumables, materials, quest items and the pseudo-items used for gold, "
               "fame and exp rewards.")
EQUIPMENT_KINDS = {31, 32, 35, 50, 51, 52, 53, 54, 55, 56, 57, 58}
REQUIRED = ["price", "obtained_from"]          # + "stats" for EQUIPMENT_KINDS
UNION_KEYS = ["obtained_from"]

# Item_Base currency codes (contract/items.yaml header).
CURRENCIES = {1: "Gold", 2: "Gold", 17: "Gold (+10%)", 7: "Purple Jewel", 8: "Yellow Jewel",
              10: "Bronze Medal", 11: "Silver Medal", 12: "Gold Medal", 15: "Arena Medal",
              18: "Fame", 9: "currency 9 (unknown)", 16: "currency 16 (unknown)",
              19: "currency 19 (unknown)"}
CLASSES = [(1, "Saint"), (2, "Punisher"), (16, "Guardian")]
BIND = {1: "on_pickup", 2: "on_equip"}
# Non-stat option codes (contract/items.yaml: 0x105 cooldown s, 0x106 cooldown
# group, 0xd2 cast-time item, 0x153 opens UI 8, 200 = WeaponBase id).
SPECIAL = {200: "weapon_base", 210: "use_skill", 261: "cooldown_s", 262: "cooldown_group",
           301: "use_buff", 327: "summon_unit", 339: "opens_ui"}
SPECIAL_TEXT = {200: "WeaponBase row", 201: "Innocence value?", 202: "rune grade?",
                208: "costume/dye value?", 209: "costume value?", 210: "skill cast on use",
                261: "cooldown (s)", 262: "cooldown group", 301: "buff applied on use",
                327: "unit summoned on use", 339: "opens UI 8", 340: "teleport target?"}


# Class name (``classes`` values) -> class page id (= UnitDB unit id, Create_Char).
CLASS_UNITS = {"Saint": 1, "Punisher": 4, "Guardian": 5, "Valkyrie": 7}

# Item category index pages: docs/wiki/items/<slug>.md, written by index.py
# from the item pages' front matter. Weapons are split by ``classes``, the rest
# by ItemKind ``kind``; kinds not listed go to "other-items".
#   (slug, title, kinds, what the page holds)
CATEGORIES = [
    ("weapons-saint", "Saint weapons", [31], "Weapons (kind 31) only the Saint can equip: flying blades, dual guns and wands."),
    ("weapons-punisher", "Punisher weapons", [31], "Weapons (kind 31) only the Punisher can equip: daggers and bows."),
    ("weapons-guardian", "Guardian weapons", [31], "Weapons (kind 31) only the Guardian can equip: maces (hammers) and cannons."),
    ("armor-helmet", "Helmets", [50], "Helmets (kind 50). Every class can wear every armour piece."),
    ("armor-body", "Body armour", [51], "Body armour (kind 51). Every class can wear every armour piece."),
    ("armor-gloves", "Gloves", [52], "Gloves (kind 52). Every class can wear every armour piece."),
    ("armor-shoes", "Shoes", [53], "Shoes (kind 53). Every class can wear every armour piece."),
    ("accessories", "Accessories", [54, 55, 56, 57], "Necklaces, belts, bracelets and rings (kinds 54–57), wearable by every class."),
    ("runes", "Runes and gem stones", [35, 58], "Runes socketed into gear (kind 35) and gem stones (kind 58)."),
    ("costume-items", "Costume items", [32], "Wearable costumes (kind 32), one item per class. Grouped by set in the costumes section."),
    ("hero-items", "Innocence (hero) items", [18, 36], "Innocence items that unlock a hero form (kind 18) and the Innocence pieces they are crafted from (kind 36)."),
    ("consumables", "Consumables", [11, 14, 19, 21, 22, 38, 42, 45, 46, 47],
     "Potions, scrolls, tomes, elixirs, flasks, dyes, transform scrolls, hammers and other items used up from the bag."),
    ("materials", "Materials", [1, 12, 13, 20, 48, 49], "Crafting and reinforcement materials: passion fragments, pieces and patterns, reinforcing stones and adjuvants."),
    ("quest-items", "Quest items", [16, 17, 44], "Quest drops and quest scrolls (kinds 16, 17, 44)."),
    ("boxes-and-packages", "Boxes and packages", [28, 29, 30, 33, 34, 43], "Random boxes, packages and jewel bundles."),
    ("other-items", "Other items", [], "Everything else: fort and legion items (holy things, legion cores, fort establishing), the pseudo-items used for gold, fame and exp rewards, and test rows."),
]
CATEGORY_TITLES = {c[0]: c[1] for c in CATEGORIES}


def category(fm):
    """Category slug of an item page's front matter (see CATEGORIES)."""
    kind = fm.get("kind")
    if kind == 31:
        cls = fm.get("classes")
        if isinstance(cls, list) and len(cls) == 1 and "weapons-" + str(cls[0]).lower() in CATEGORY_TITLES:
            return "weapons-" + str(cls[0]).lower()
        return "other-items"
    for slug, _t, kinds, _d in CATEGORIES:
        if kind in kinds and not slug.startswith("weapons-"):
            return slug
    return "other-items"


def category_link(fm):
    slug = category(fm)
    return "[[wiki/items/%s|%s]]" % (slug, CATEGORY_TITLES[slug])


def class_links(ctx, classes):
    """'all' or class names -> links to the class pages."""
    if classes == "all":
        return "all"
    return ", ".join(ctx.link("classes", CLASS_UNITS[c], c) if c in CLASS_UNITS else str(c)
                     for c in classes or []) or "none"


def name(ctx, id_):
    row = ctx.table("Item_Base").get(id_)
    return (ctx.s(row.get("name_key")) if row else None) or ctx.s("ItemName_%d" % id_)


class Index:
    """Reverse lookups over the client tables, built once per run."""

    def __init__(self, ctx):
        t = ctx.table
        self.options = {r.int("code"): r for r in t("ItemOption")}
        self.kinds = {r.int("kind"): (r.get("name") or "").strip() for r in t("ItemKind")}
        self.jewels = {r.get("name_key"): r for r in t("Item_Jewel")}
        self.sets = {}
        for r in t("SetBounsItem"):
            for (p,) in repeat(r, "piece%d"):
                self.sets.setdefault(p, []).append(r)
        self.made_by, self.used_in = {}, {}
        for r in t("Item_Make"):
            self.made_by.setdefault(r.int("result_item"), []).append(r)
            for it, n, _x in repeat(r, "mat%d_item", "mat%d_count", "mat%d_x"):
                self.used_in.setdefault(it, []).append((r, n))
        self.sanc_mat = {}
        for r in t("ItemSancMet"):
            for step in range(1, 7):
                for it, n in repeat(r, "step%d_mat%%d_item" % step, "step%d_mat%%d_count" % step):
                    self.sanc_mat.setdefault(it, set()).add(r.int("id"))
        self.shops = {}
        for r in t("Npc_Carry"):
            for code, p1, count, p2 in repeat(r, "item%d_code", "item%d_p1", "item%d_count", "item%d_p2"):
                self.shops.setdefault(code, {}).setdefault(r.int("shop_id"), (p1, count))
        self.shop_npcs = {}
        for u in t("UnitDB"):
            if u.int("u16@a2"):
                self.shop_npcs.setdefault(u.int("u16@a2"), []).append(u.int("id"))
        self.quest_rewards, self.quest_drops, self.quest_needs = {}, {}, {}
        for q in t("Quest"):
            qid = q.int("id")
            for typ, a, b, c, d, e in repeat(q, "rew%d_type", "rew%d_a", "rew%d_b", "rew%d_c", "rew%d_d", "rew%d_e"):
                if typ == 1 and b:
                    self.quest_rewards.setdefault(b, []).append((qid, c or 1))
                elif typ == 8 and a:
                    self.quest_rewards.setdefault(a, []).append((qid, b or 1))
            for typ, a, b, c, d, *_ in repeat(q, "obj%d_type", "obj%d_a", "obj%d_b", "obj%d_c", "obj%d_d", "obj%d_e"):
                if typ == 1 and d:
                    self.quest_drops.setdefault(d, []).append((qid, a, b, c))
        self.boxes = {}
        for r in t("RandomBox"):
            for code, count, p in repeat(r, "item%d_code", "item%d_count", "item%d_p"):
                self.boxes.setdefault(code, set()).add(r.int("id"))
        self.gacha = {}
        for n in range(7):
            try:
                for r in t("Gacha_%02d" % n):
                    self.gacha.setdefault(r.int("item"), {})[n] = r.int("grade")
            except OSError:
                pass
        self.premium = {}
        for r in t("PrimiumShop"):
            self.premium.setdefault(r.int("item"), []).append(r)
        self.jewel_make, self.jewel_mat = {}, {}
        for r in t("JewelSocketMake"):
            self.jewel_make.setdefault(r.int("next_item"), []).append(r)
            for it, n in repeat(r, "mat%d_item", "mat%d_count"):
                self.jewel_mat.setdefault(it, []).append(r)
        self.dungeon_show, self.dungeon_cost = {}, {}
        for r in t("DungeonAdmission"):
            for (it,) in repeat(r, "show_item%d"):
                self.dungeon_show.setdefault(it, set()).add(r.int("field"))
            for it, n in repeat(r, "cost%d_item", "cost%d_count"):
                self.dungeon_cost.setdefault(it, {})[r.int("field")] = n
        self.war = {r.int("item"): r.int("id") for r in t("WinAffect") if r.int("item")}
        self.server_drops = server_drops()


def server_drops():
    """server/loot.py EXTRA_DROPS -> {item: [(unit, chance, lo, hi)]}, read
    with ast (the module is not imported)."""
    out = {}
    try:
        tree = ast.parse((common.REPO / "server" / "loot.py").read_text(encoding="utf-8"))
    except OSError:
        return out
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "EXTRA_DROPS" for t in node.targets):
            try:
                table = ast.literal_eval(node.value)
            except ValueError:
                return out
            for unit, (_lo, _hi, extras) in table.items():
                for item, chance, lo, hi in extras:
                    out.setdefault(item, []).append((unit, chance, lo, hi))
    return out


# How the client applies the 10 option slots (FUN_004410d6, item stat sum):
# for weapons (kind 31) and armour (50-57) slots 1-3 are multiplied by
# level = tier * 15 + reinforce (+0..+15, capped at 120), slots 4-6 by the
# tier (only when tier > 0), slots 7-10 are flat. Every other kind: all flat.
SCALE_TEXT = {"level": "× (tier × 15 + reinforce level)", "tier": "× tier", "flat": "flat"}


def scale_of(slot):
    return "level" if slot <= 3 else "tier" if slot <= 6 else "flat"


def stat_text(ix, code, value):
    opt = ix.options.get(code)
    if opt is None:
        return "option %d" % code, "%+d" % value if isinstance(value, int) else str(value)
    fmt = (opt.get("format") or "").strip()
    nm = (opt.get("name") or "").strip()
    if "%" in fmt:
        try:
            shown = fmt.replace("%%", "\0").replace("%+d", "%+d" % value).replace("%d", "%d" % value).replace("\0", "%")
            return nm, shown.replace(nm, "", 1).strip() or shown
        except TypeError:
            pass
    return nm, "%+d" % value


def build(ctx):
    ix = Index(ctx)
    ctx.items_index = ix
    wb = ctx.table("WeaponBase")
    for r in ctx.table("Item_Base"):
        id_ = r.int("id")
        kind = r.int("kind")
        f = {}
        f["name_key"] = r.str("name_key")
        f["kind"] = kind
        f["kind_name"] = ix.kinds.get(kind)
        mask = r.int("req_class")
        f["classes"] = "all" if mask == 255 else [n for b, n in CLASSES if mask & b]
        f["bind"] = BIND.get(r.int("bind"))
        cur = r.int("buy_currency")
        f["price"] = {"currency": cur, "currency_name": CURRENCIES.get(cur, "currency %d" % cur),
                      "buy": r.int("buy_price")}
        pair = [{"currency": c, "amount": a} for c, a in
                ((r.int("sell_currency"), r.int("sell_price")), (r.int("c13"), r.int("c14"))) if c or a]
        if pair:
            f["cost_pair"] = pair
        if r.int("fame_price"):
            f["fame_required"] = r.int("fame_price")
        flags = r.int("c15")
        if flags:
            f["flags"] = flags
            f["no_sell"] = bool(flags & 2)
        if r.int("rarity"):
            f["rarity"] = r.int("rarity")
        if r.int("period"):
            f["period"] = r.int("period")
        stats, options = [], []
        scaled = kind == 31 or 50 <= kind <= 57
        for slot in range(1, 11):
            code, value = r.int("opt%d_type" % slot), r.int("opt%d_value" % slot)
            if not code:
                continue
            if code in SPECIAL or code >= 200 and code not in ix.options:
                options.append({"code": code, "value": value})
                if code in SPECIAL:
                    f[SPECIAL[code]] = value
            else:
                stats.append({"code": code, "stat": stat_text(ix, code, value)[0], "value": value,
                              "scale": scale_of(slot) if scaled else "flat"})
        jewel = ix.jewels.get("ItemName_%d" % id_) if kind == 35 else None
        if jewel is not None and jewel.int("opt_type"):
            stats.append({"code": jewel.int("opt_type"),
                          "stat": stat_text(ix, jewel.int("opt_type"), jewel.int("opt_value"))[0],
                          "value": jewel.int("opt_value"), "scale": "flat", "from": "Item_Jewel"})
            f["rune_level"] = jewel.int("level")
        f["stats"] = stats
        if options:
            f["options"] = options
        if "weapon_base" in f:
            w = wb.get(f["weapon_base"])
            if w is not None:
                f["skills"] = [s for (s,) in repeat(w, "skill%d") if s]
        if id_ in ix.sets:
            f["set"] = ix.sets[id_][0].int("id")
        sanc = r.int("c41")
        if kind in (18, 31, 50, 51, 52, 53, 54, 55, 56, 57) and ctx.table("ItemSancMet").get(sanc):
            f["reinforce"] = sanc
        f["icon"] = {"file": r.str("icon_file"), "index": r.int("icon_idx")} if r.str("icon_file") else None
        f["obtained_from"] = obtained_from(ctx, ix, id_)
        sources = ["client: Item_Base.cdb id %d" % id_]
        if jewel is not None:
            sources.append("client (server-only table): Item_Jewel.cdb id %s" % jewel.get("id"))
        req = REQUIRED + (["stats"] if kind in EQUIPMENT_KINDS else [])
        yield Page(TYPE, id_, ctx.title(TYPE, id_), fields=f, sources=sources, body=body,
                   required=req)


def obtained_from(ctx, ix, id_):
    out = []
    for shop in sorted(ix.shops.get(id_, {})):
        out.append({"how": "shop", "shop": shop})
    for r in ix.made_by.get(id_, []):
        out.append({"how": "craft", "recipe": r.int("id")})
    for qid, n in ix.quest_rewards.get(id_, []):
        out.append({"how": "quest_reward", "quest": qid, "count": n})
    for qid, unit, need, rate in ix.quest_drops.get(id_, []):
        out.append({"how": "quest_drop", "quest": qid, "unit": unit, "rate": rate})
    for box in sorted(ix.boxes.get(id_, ())):
        out.append({"how": "random_box", "box": box})
    for pool in sorted(ix.gacha.get(id_, {})):
        out.append({"how": "gacha", "pool": pool})
    for r in ix.premium.get(id_, []):
        out.append({"how": "premium_shop", "entry": r.int("id")})
    for r in ix.jewel_make.get(id_, []):
        out.append({"how": "jewel_craft", "recipe": r.int("id")})
    for field in sorted(ix.dungeon_show.get(id_, ())):
        out.append({"how": "dungeon", "field": field})
    if id_ in ix.war:
        out.append({"how": "war_reward", "row": ix.war[id_]})
    for unit, d in monster_drops(ctx).get(id_, []):
        e = {"how": "drop", "unit": unit}
        e.update({k: v for k, v in d.items() if k in ("rate", "count")})
        out.append(e)
    return out


def monster_drops(ctx):
    """{item: [(unit id, drop entry)]} from monster pages' front matter."""
    if getattr(ctx, "_monster_drops", None) is None:
        out = {}
        for uid, fm in ctx.pages("monsters").items():
            drops = fm.get("drops")
            if not isinstance(drops, list):
                continue
            for d in drops:
                if isinstance(d, int):
                    d = {"item": d}
                if isinstance(d, dict) and isinstance(d.get("item"), int):
                    out.setdefault(d["item"], []).append((uid, d))
        ctx._monster_drops = out
    return ctx._monster_drops


# ------------------------------------------------------------------ rendering

def body(ctx, page):
    ix = ctx.items_index
    fm, id_ = page.fm, page.id
    row = ctx.table("Item_Base").get(id_)
    L = []
    img = ctx.image(TYPE, id_)
    info = []
    if img:
        info.append(("", "![%s](%s)" % (common.link_text(page.title), img)))
    info.append(("Item id", "`%d`" % id_))
    info.append(("Kind", "%s (%d)" % (fm.get("kind_name") or "?", fm.get("kind", 0))))
    info.append(("Category", category_link(fm)))
    info.append(("Classes", class_links(ctx, fm.get("classes"))))
    hero = [o.get("value") for o in fm.get("options") or [] if isinstance(o, dict) and o.get("code") == 201]
    if hero and fm.get("kind") == 18:
        info.append(("Hero form", ctx.link("heroes", hero[0])))
    if fm.get("kind") == 32:
        from . import costumes
        cid = costumes.set_of(ctx, id_)
        if cid is not None:
            info.append(("Costume set", ctx.link("costumes", cid)))
    if fm.get("bind"):
        info.append(("Bind", fm["bind"].replace("_", " ")))
    price = fm.get("price") or {}
    if price.get("buy") or price.get("currency"):
        info.append(("Buy price", "%s %s" % (fmt_num(price.get("buy", 0)), price.get("currency_name", ""))))
    if fm.get("fame_required"):
        info.append(("Fame required", fmt_num(fm["fame_required"])))
    if fm.get("rune_level"):
        info.append(("Rune level", fm["rune_level"]))
    if fm.get("rarity"):
        info.append(("Rarity (guessed column)", fm["rarity"]))
    if fm.get("period"):
        if fm.get("kind") == 32:
            info.append(("Period", "%s min of wearing time (costume duration, WM 0406; "
                         "[[gameplay/events-and-schedules|Events]] §9)" % fmt_num(fm["period"])))
        elif fm.get("kind") == 18:
            info.append(("Period", "%s = the crystal's durability (−5 per second transformed, WM 1107)" % fmt_num(fm["period"])))
        else:
            info.append(("Period", "%s (unit unknown)" % fm["period"]))
    if fm.get("no_sell"):
        info.append(("Sell", "cannot be sold (flags bit 1)"))
    if fm.get("set"):
        info.append(("Set", ctx.link("sets", fm["set"])))
    if fm.get("cooldown_s"):
        info.append(("Cooldown", "%s s (group %s)" % (fm["cooldown_s"], fm.get("cooldown_group", "-"))))
    if fm.get("use_buff"):
        info.append(("On use: buff", ctx.link("buffs", fm["use_buff"])))
    if fm.get("use_skill"):
        info.append(("On use: skill", ctx.link("skills", fm["use_skill"])))
    if fm.get("summon_unit"):
        info.append(("On use: summons", ctx.unit_link(fm["summon_unit"])))
    if fm.get("icon"):
        ic = fm["icon"]
        info.append(("Icon", "`ui/icons/%s` cell %s" % (ic.get("file"), ic.get("index"))))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))

    tip = ctx.s(row.get("comment_key")) if row else None
    if tip:
        L += ["### Tooltip", "", quote(tip)]

    stats = fm.get("stats") or []
    if stats:
        rows = []
        for s in stats:
            if isinstance(s, dict):
                nm, shown = stat_text(ix, s.get("code", 0), s.get("value", 0))
                applies = SCALE_TEXT.get(s.get("scale"), s.get("scale") or "")
                if s.get("from"):
                    applies += " (from %s)" % s["from"]
                rows.append((nm, shown, applies, s.get("code")))
        L += ["### Stats", ""]
        if any(isinstance(s, dict) and s.get("scale") in ("level", "tier") for s in stats):
            L += ["Weapon and armour stats grow with the item: the client multiplies the first "
                  "three option slots by *tier × 15 + reinforce level* and the next three by the "
                  "*tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two "
                  "multipliers is *inferred*).", ""]
        L += [table_md(["stat", "value", "applies", "code"], rows)]
    other = [o for o in (fm.get("options") or []) if isinstance(o, dict)]
    if other:
        L += ["### Other options", "", table_md(["code", "value", "meaning"], [
            (o.get("code"), o.get("value"), SPECIAL_TEXT.get(o.get("code"), "unknown")) for o in other])]

    if fm.get("skills"):
        w = ctx.table("WeaponBase").get(fm.get("weapon_base", 0))
        if w is not None:
            L += ["### Weapon base", "",
                  "WeaponBase row %d. The client adds these to the wielder's stats (`FUN_004410d6`; "
                  "which stat each one is, is not decoded yet): %s." % (
                      fm.get("weapon_base"), ", ".join("`%s` = %s" % (c, w.get(c)) for c in ("c2", "c3", "c4", "c5"))), ""]
        L += ["### Weapon skills", "",
              "Weapon base %s. Skills 1–4 are the normal Q/W/E/R skills, 5–8 the hero (transformed) ones." % fm.get("weapon_base"), ""]
        for n, sid in enumerate(repeat(w, "skill%d", skip_zero=False) if w else [], 1):
            if sid[0]:
                L.append("%d. %s" % (n, ctx.link("skills", sid[0])))
        L.append("")

    if fm.get("set"):
        s = ctx.table("SetBounsItem").get(fm["set"])
        if s is not None:
            pieces = [p for (p,) in repeat(s, "piece%d")]
            L += ["### Set bonus", "", "Pieces: " + ", ".join(ctx.link(TYPE, p) for p in pieces), ""]
            tiers = [(need, stat_text(ix, opt, val)[0], stat_text(ix, opt, val)[1])
                     for need, opt, val, _x in repeat(s, "bonus%d_need", "bonus%d_opt_type", "bonus%d_opt_value", "bonus%d_x")]
            L.append(table_md(["pieces", "bonus", "value"], tiers))

    if fm.get("reinforce"):
        s = ctx.table("ItemSancMet").get(fm["reinforce"])
        if s is not None:
            rows = []
            for step in range(1, 7):
                mats = repeat(s, "step%d_mat%%d_item" % step, "step%d_mat%%d_count" % step)
                rows.append((step, ", ".join("%s × %d" % (ctx.link(TYPE, it), n) for it, n in mats)))
            L += ["### Reinforcement", "",
                  "ItemSancMet row %d (inferred from Item_Base +0x92), %s gold per attempt. "
                  "Success rates are not in the client." % (fm["reinforce"], fmt_num(s.int("gold"))), "",
                  table_md(["step", "materials"], rows)]

    made = ix.made_by.get(id_, [])
    if made:
        L += ["### Crafting", "", table_md(["recipe", "materials", "gold", "success %"], [
            (r.int("id"), ", ".join("%s × %d" % (ctx.link(TYPE, it), n) for it, n, _ in
                                     repeat(r, "mat%d_item", "mat%d_count", "mat%d_x")),
             fmt_num(r.int("gold")), r.int("success%")) for r in made])]
    for r in ix.jewel_make.get(id_, []):
        L += ["Jewel upgrade (JewelSocketMake %d): %s from %s." % (
            r.int("id"), ", ".join("%s × %d" % (ctx.link(TYPE, it), n) for it, n in repeat(r, "mat%d_item", "mat%d_count")),
            ctx.link(TYPE, r.int("jewel_item"))), ""]

    # where to get it
    get = []
    for shop in sorted(ix.shops.get(id_, {})):
        npcs = ix.shop_npcs.get(shop, [])
        who = ", ".join(ctx.unit_link(u) for u in npcs[:6]) or "no NPC found"
        get.append("Sold in %s (%s)" % (ctx.link("shops", shop), who))
    for qid, n in ix.quest_rewards.get(id_, []):
        get.append("Reward of quest %s × %d" % (ctx.link("quests", qid), n))
    for qid, unit, need, rate in ix.quest_drops.get(id_, []):
        get.append("Quest drop: %s drops it at %s%% during %s (need %d)" % (
            ctx.unit_link(unit), rate, ctx.link("quests", qid), need))
    for unit, d in monster_drops(ctx).get(id_, []):
        extra = ", ".join("%s %s" % (k, d[k]) for k in ("rate", "count") if k in d)
        get.append("Dropped by %s%s (monster page)" % (ctx.link("monsters", unit), " — " + extra if extra else ""))
    for field in sorted(ix.dungeon_show.get(id_, ())):
        get.append("Shown as a reward of dungeon %s" % ctx.link("dungeons", field))
    for box in sorted(ix.boxes.get(id_, ())):
        get.append("In random box table row %d (RandomBox.cdb; odds are server side)" % box)
    for pool, grade in sorted(ix.gacha.get(id_, {}).items()):
        get.append("Hero gacha pool %02d, grade %d (Gacha_%02d.cdb; odds are server side)" % (pool, grade, pool))
    for r in ix.premium.get(id_, []):
        get.append("Premium shop entry %d: %s (currency code %d, discount %s%%)" % (
            r.int("id"), fmt_num(r.int("price")), r.int("currency"), r.int("discount%")))
    if id_ in ix.war:
        get.append("War winner reward (WinAffect row %d)" % ix.war[id_])
    extra_hand = [o for o in (fm.get("obtained_from") or []) if isinstance(o, dict)
                  and o not in obtained_from(ctx, ix, id_)]
    for o in extra_hand:
        get.append("%s (hand-entered)" % ", ".join("%s %s" % kv for kv in o.items()))
    L += ["### Where to get it", ""]
    L += ["- " + g for g in get] if get else ["Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`."]
    L.append("")

    use = []
    for r, n in ix.used_in.get(id_, []):
        use.append("Material (× %d) for %s (recipe %d)" % (n, ctx.link(TYPE, r.int("result_item")), r.int("id")))
    for sid in sorted(ix.sanc_mat.get(id_, ())):
        users = [i for i, f in ctx._pages.get(TYPE, {}).items() if f.get("reinforce") == sid]
        txt = ", ".join(ctx.link(TYPE, i) for i in users[:8]) + (" and %d more" % (len(users) - 8) if len(users) > 8 else "")
        use.append("Reinforcement material (ItemSancMet %d)%s" % (sid, ": " + txt if txt else ""))
    for r in ix.jewel_mat.get(id_, []):
        use.append("Jewel upgrade material for %s" % ctx.link(TYPE, r.int("next_item")))
    for field, n in sorted(ix.dungeon_cost.get(id_, {}).items()):
        use.append("Entry ticket (× %d) for dungeon %s" % (n, ctx.link("dungeons", field)))
    if use:
        L += ["### Used for", ""] + ["- " + u for u in use] + [""]

    srv = ix.server_drops.get(id_, [])
    if srv:
        L += ["### Current server", "",
              "`server/loot.py` drops it (our choice, not original data): " + "; ".join(
                  "%s %g%% × %d–%d" % (ctx.unit_link(u), c * 100, lo, hi) for u, c, lo, hi in srv), ""]
    ment = ctx.mentions(page.title if fm.get("name_key") else None)
    if ment:
        L += ["### Mentioned in", ""] + ["- [[%s|%s]]" % m for m in ment] + [""]
    return "\n".join(L)

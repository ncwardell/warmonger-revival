"""Classes: one page per Create_Char row (page id = the class's UnitDB unit id).

Create_Char has four rows: Saint (unit 1, class mask 1), Punisher (4, mask 2),
Guardian (5, mask 16) and Valkyrie (7, mask 4). The game only ever offered the
first three (docs/gameplay/video-character-creation-and-tutorial: three class
icons; no item, string or mastery is made for mask 4): the Valkyrie row has no
starting weapons, one portrait and the description string "Valkyrie".

Client sources:
  Create_Char   class mask, unit id, description key, up to 4 starting weapons
                (item + label key), face/hair/colour lists, portraits F/S/W
  Item_Base     Item_ReqClass_<mask> class names; req_class@33 class mask of
                every item -> what the class can equip; weapon option 200 ->
  WeaponBase    the weapon's 4 normal + 4 hero skills (the weapon decides the
                skills in this game), c14 = CostumeDB visual of the weapon
  CustmizeBase  face / hair / basic-costume parts per class
  Mastery       the class's character mastery tree (masteries pages)
  Level_Table   exp curve and the hp?/mp?/atk?/def? growth columns (shared by all
                classes; they do not match observed HP/MP, see the page)

Evidence (docs/gameplay):
  video-character-creation-and-tutorial §2: Guardian HP 450 / MP 700 at level 1,
  530/725 at 2, 610/750 at 3 -> +80 HP / +25 MP per level (no gear)
  video-early-quests: Punisher HUD HP/MP with starting and quest gear
  classes-and-legions §5 (WM 0420): Magic Resist per level Punisher +3, Saint
  +4, Guardian +6

Front matter:
  class_mask, unit_id, offered, starting_weapons [{item, label, weapon_base, skills}]
  equippable {weapons, costumes, armour, accessories}   item counts
  base_hp, base_mp, hp_per_level, mp_per_level   (required; only where observed)
  base_stats    radar / sheet stats at level 1     (required; not known yet)
  mr_per_level
"""
from . import _econ, items
from .common import Page, clean_name, fmt_num, quote, repeat, table_md

TYPE = "classes"
KIND = "class"
LABEL = "Class"
PLURAL = "Classes"
DESCRIPTION = ("The playable classes from the client's `Create_Char` table: Saint, Punisher and Guardian, "
               "plus the Valkyrie row the game never offered. Each class carries two weapons and the "
               "weapon decides the skills.")
REQUIRED = ["base_hp", "base_mp", "hp_per_level", "mp_per_level", "base_stats"]
OFFERED = {1, 4, 5}
SRC_GUARDIAN = ("docs: [[gameplay/video-character-creation-and-tutorial]] §2 (HP 450 / MP 700 at level 1, "
                "530/725 at 2, 610/750 at 3, no gear: +80 HP / +25 MP per level; video 2:45)")
SRC_MR = "docs: [[gameplay/classes-and-legions]] §5 (WM 0420: Magic Resist per level)"
SRC_PUNISHER = ("docs: [[gameplay/video-early-quests]] (Punisher HUD HP/MP with starting and quest gear: "
                "Lv 1 420/424, Lv 3 560/472, Lv 7 970/568, Lv 20 3240–3260/1000)")
MR_PER_LEVEL = {1: 4, 4: 3, 5: 6}
MR_AT_30 = {1: 120, 4: 90, 5: 150}          # as the patch note gives them
OBSERVED = {5: {"base_hp": 450, "base_mp": 700, "hp_per_level": 80, "mp_per_level": 25}}
PUNISHER_HUD = [(1, "420", "424"), (3, "560", "472"), (7, "970", "568"), (16, "2,795", "924"),
                (19, "3,005", "996"), (20, "3,240–3,260", "1,000")]


def name(ctx, id_):
    r = ctx.table("Create_Char").get(id_, "unit_id")
    if r is None:
        return None
    return ctx.s("Item_ReqClass_%d" % r.int("class_mask")) or clean_name(ctx.s(r.get("comment_key")) or "")


def equippable(ctx, cls):
    """{category slug: [item ids]} of items this class can equip (classes
    includes it, or 'all' for equipment kinds)."""
    out = {}
    for iid, fm in ctx.pages("items").items():
        kind = fm.get("kind")
        cl = fm.get("classes")
        if kind not in items.EQUIPMENT_KINDS and kind != 32:
            continue
        if cl == "all" or (isinstance(cl, list) and cls in cl):
            out.setdefault(items.category(fm), []).append(iid)
    return out


def build(ctx):
    wb = ctx.table("WeaponBase")
    for r in ctx.table("Create_Char"):
        uid = r.int("unit_id")
        cname = name(ctx, uid)
        f = {"class_mask": r.int("class_mask"), "unit_id": uid, "offered": uid in OFFERED}
        weapons = []
        for item, label in repeat(r, "weapon%d_item", "weapon%d_label_key"):
            e = {"item": item, "label": ctx.s(label) if isinstance(label, str) else None}
            ir = ctx.table("Item_Base").get(item)
            w = None
            if ir is not None:
                for n in range(1, 11):
                    if ir.int("opt%d_type" % n) == 200:
                        w = ir.int("opt%d_value" % n)
            if w:
                e["weapon_base"] = w
                wr = wb.get(w)
                if wr is not None:
                    e["skills"] = [s for (s,) in repeat(wr, "skill%d") if s]
            weapons.append({k: v for k, v in e.items() if v is not None})
        f["starting_weapons"] = weapons
        eq = equippable(ctx, cname) if uid in OFFERED else None
        f["equippable"] = None if eq is None else {
            "weapons": len(eq.get("weapons-" + (cname or "").lower(), [])),
            "costumes": len(eq.get("costume-items", [])),
            "armour": sum(len(eq.get(s, [])) for s in ("armor-helmet", "armor-body", "armor-gloves", "armor-shoes")),
            "accessories": len(eq.get("accessories", [])) + len(eq.get("runes", [])),
        }
        f = {k: v for k, v in f.items() if v is not None}
        f["portraits"] = sum(len([p for p in (r.get(c) or "").split(",") if p.strip()])
                             for c in ("portraits_F", "portraits_S", "portraits_W"))
        sources = ["client: Create_Char.cdb row %d" % r.int("class"),
                   "client strings: %s, Item_ReqClass_%d" % (r.get("comment_key"), r.int("class_mask"))]
        if uid in OBSERVED:
            f.update(OBSERVED[uid])
            sources.append(SRC_GUARDIAN)
        if uid in MR_PER_LEVEL:
            f["mr_per_level"] = MR_PER_LEVEL[uid]
            sources.append(SRC_MR)
        if uid == 4:
            sources.append(SRC_PUNISHER)
        yield Page(TYPE, uid, ctx.title(TYPE, uid), fields=f, sources=sources, body=body,
                   required=REQUIRED if uid in OFFERED else [])


def body(ctx, page):
    fm, uid = page.fm, page.id
    r = ctx.table("Create_Char").get(uid, "unit_id")
    cname = page.title
    L, info = [], []
    img = ctx.image(TYPE, uid)
    if img:
        info.append(("", "![%s](%s)" % (cname, img)))
    unit = ctx.table("UnitDB").get(uid)
    info.append(("Unit id", "`%d` (`UnitDB`: %s)" % (uid, (ctx.s(unit.get("name_key")) if unit is not None else None) or "?")))
    info.append(("Class mask", "`%s` (`Item_Base` req_class bit)" % fm.get("class_mask")))
    info.append(("Offered at creation", "yes" if fm.get("offered") else
                 "**no**: the client has this row but the game never offered the class"))
    for k, label in (("base_hp", "HP at level 1"), ("base_mp", "MP at level 1"),
                     ("hp_per_level", "HP per level"), ("mp_per_level", "MP per level"),
                     ("mr_per_level", "Magic Resist per level")):
        if fm.get(k) is not None:
            info.append((label, fmt_num(fm[k]) if isinstance(fm[k], int) else fm[k]))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))
    if not fm.get("offered"):
        L += ["> [!note] Never playable",
              "> `Create_Char` has a fourth row (unit 7, class mask 4, description string just "
              "\"Valkyrie\", chart `CreatChar.Chart_03` like the Saint) with no starting weapons, one "
              "portrait per set and no class-name string (`Item_ReqClass_4` does not exist). No item, "
              "mastery or skill is made for mask 4. The character-creation video shows only Saint, "
              "Punisher and Guardian ([[gameplay/video-character-creation-and-tutorial|video]]).", ""]
    desc = ctx.s(r.get("comment_key")) if r is not None else None
    if desc and fm.get("offered"):
        L += ["### Description", "", quote(desc)]

    weapons = [w for w in fm.get("starting_weapons") or [] if isinstance(w, dict)]
    if weapons:
        L += ["### Starting weapons", "",
              "Chosen at character creation (`Create_Char` weapon1–4). The weapon decides the skills: "
              "its `WeaponBase` row gives 4 normal skills (Q/W/E/R) and 4 hero-form skills.", ""]
        rows = []
        for w in weapons:
            sk = w.get("skills") or []
            rows.append((_econ.item_icon(ctx, w.get("item", 0)), ctx.link("items", w.get("item", 0)),
                         w.get("label") or "–", w.get("weapon_base", "–"),
                         ", ".join(ctx.link("skills", s) for s in sk[:4]) or "–",
                         ", ".join(ctx.link("skills", s) for s in sk[4:]) or "–"))
        L.append(table_md(["", "weapon", "label", "WeaponBase", "skills (Q/W/E/R)", "hero skills"], rows))

    eq = fm.get("equippable") if isinstance(fm.get("equippable"), dict) else {}
    if fm.get("offered"):
        slug = "weapons-" + cname.lower()
        L += ["### Equipment", "",
              "From each item's class mask (`Item_Base` req_class@33): weapons and costumes are made per "
              "class, armour and accessories fit every class.", "",
              table_md(["what", "items", "list"], [
                  ("Weapons", eq.get("weapons", 0), "[[wiki/items/%s|%s weapons]]" % (slug, cname)),
                  ("Armour", eq.get("armour", 0), "[[wiki/items/armor-helmet|helmets]], [[wiki/items/armor-body|body armour]], "
                   "[[wiki/items/armor-gloves|gloves]], [[wiki/items/armor-shoes|shoes]]"),
                  ("Accessories and runes", eq.get("accessories", 0),
                   "[[wiki/items/accessories|accessories]], [[wiki/items/runes|runes]]"),
                  ("Costumes", eq.get("costumes", 0), "[[wiki/costumes/index|costume sets]]"),
              ])]
        weap = sorted(i for i, f in ctx.pages("items").items()
                      if f.get("kind") == 31 and isinstance(f.get("classes"), list) and cname in f["classes"])
        if weap:
            L += ["All %s weapons: %s." % (cname, ", ".join(ctx.link("items", i) for i in weap)), ""]

    if not fm.get("offered"):
        return "\n".join(L)
    L += ["### HP, MP and stats", ""]
    if uid == 5:
        L += ["- At level 1 the Guardian has **450 HP / 700 MP**, at level 2 530/725 and at level 3 610/750, "
              "with no gear: **+80 HP and +25 MP per level** "
              "([[gameplay/video-character-creation-and-tutorial|character creation video]] §2, 2:45). *video*"]
    elif uid == 4:
        L += ["- Base HP/MP not seen without gear yet. The Punisher HUD with starting and quest gear "
              "([[gameplay/video-early-quests|early quests video]]) showed:", "",
              table_md(["level", "HP", "MP"], PUNISHER_HUD).rstrip("\n"), "",
              "  MP rose by 24 per level from level 1 to 7 (gear unchanged?); HP depends on gear. *video*"]
    elif uid == 1:
        L += ["- Base HP/MP not observed yet (no Saint video at low level)."]
    if fm.get("mr_per_level"):
        L += ["- Magic Resist per level: **+%s** (the patch note says %s at level 30) — WM 0420 "
              "([[gameplay/classes-and-legions|Classes]] §5). *notes*" % (
                  fm["mr_per_level"], MR_AT_30.get(uid, "?"))]
    if fm.get("offered"):
        L += ["- `base_stats` (the six radar stats on the creation screen: Attack, Ability Power, "
              "Magic Resist, Movement Speed, Attack Speed, Armor) are not in the client; the creation "
              "screen shows them only as a chart (`%s`)." % (r.get("chart_ui") if r is not None else "?")]
    L.append("")
    lt = ctx.table("Level_Table")
    rows = [(x.int("level"), fmt_num(x.int("exp")), x.get("hp"), x.get("mp"), x.get("atk"), x.get("def"))
            for x in lt if x.int("level") >= 1]
    L += ["### Level table", "",
          "`Level_Table` is shared by every class: `exp` is the total exp that ends the level; the "
          "`hp?`/`mp?`/`atk?`/`def?` columns grow linearly (+30 HP, +20 MP per level) but are not read "
          "by any client code found and do not match the observed Guardian values (+80 / +25), so "
          "they are not used as class growth.", "",
          table_md(["level", "exp", "hp?", "mp?", "atk?", "def?"], rows)]
    mast = sorted(i for i, f in ctx.pages("masteries").items() if f.get("class") == cname)
    if mast:
        L += ["### Masteries", "", "Character mastery tree (`Mastery`): " +
              ", ".join(ctx.link("masteries", m) for m in mast) + ".", ""]
    if fm.get("offered"):
        L += ["Hero forms: see [[wiki/heroes/index|Heroes]] (any class can transform at level 30).", ""]
    return "\n".join(L)

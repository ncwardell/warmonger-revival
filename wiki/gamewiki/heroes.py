"""Heroes: one page per HeroData row (Hero Form transformations; page id = hero id).

Client sources:
  HeroData    name/comment keys, 10 skill ids, weapon_or_base@30 (= the
              "<Hero> Transformation" Skill_Base id: 20001 Dark Knight Skull
              Transformation ...), stat1?/stat2?/hp?/mp? (guessed meanings; stat1 /
              stat2 look like Attack / Ability Power: the mage heroes Amaterasu
              and Tempest Fisher have stat2 > stat1 and more MP), portrait@54
  Item_Base   kind 18 Innocence items: option 201 = HeroData id, option 200 =
              the hero's WeaponBase row (its 8 skills, c14 = CostumeDB visual).
              Rows 8000-8007 -> heroes 1-8, the "Crystal :" rows 8500-8507 ->
              heroes 51-58 (period@3a = 1500 = the crystal's durability).
              Kind 36 "Piece :" items 9000-9007 are the crafting material.
  Item_Make   recipes 1501-1508 (100 pieces + 200 fragments -> Innocence) and
              1201-1208 (5 pieces + 50 fragments -> Crystal)
  CostumeDB   rows 1000-1007: the hero forms' visual sets
Heroes 9-14 (Slayer Komodo ... Chepa Sorcerer) have no Innocence item: no
trigger in the client (boss forms, or unfinished).

Evidence (docs/gameplay):
  events-and-schedules §9 / server-rules: hero durability 24 -> 240 (WM 0402),
  transformation cooldown 10 -> 120 s (WM 0621), Innocence Crystal: no level
  limit, durability 1,500, -5 per second transformed (WM 1107)
  classes-and-legions §1, §5: heroes only at level 30 (guides); share of gear
  stats 35 % (T1+0) .. 100 % (T3+15) (WM 0628)
  video-fort-war: Dark Knight Skull form observed for at least 8.5 min,
  max HP/MP x2.2, HP set to 50 % on transform

Front matter:
  stats          {stat1, stat2, hp, mp} HeroData columns          (required)
  duration       how long a transformation lasts                  (required)
  trigger        {item, kind} the Innocence item that grants it   (required)
  skills, transform_skill, weapon_base, visual, durability, level_required,
  base_hero (crystal rows: the normal hero with the same form)
"""
from .common import Page, fmt_num, quote, repeat, table_md

TYPE = "heroes"
KIND = "hero"
LABEL = "Hero"
PLURAL = "Heroes"
DESCRIPTION = ("Every hero form (\"Hero Form\" transformation, key X) in the client's `HeroData` table: "
               "portrait, stats, skills, duration and the Innocence item that unlocks it. Rows 51–58 are "
               "the same heroes granted by an Innocence *Crystal*. The *Scroll of Transform* consumables "
               "(Golem, Demon, Slime, Jack) are something else: they turn the player into a monster "
               "unit for 5 minutes ([[wiki/items/consumables|consumables]]).")
REQUIRED = ["stats", "duration", "trigger"]
HERO_OPT, WEAPON_OPT = 201, 200
SRC_DUR = ("docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 "
           "transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second "
           "transformed, no level limit)")
SRC_VIDEO = ("docs: [[gameplay/video-fort-war]] §Hero form (Dark Knight Skull form lasted at least "
             "8.5 min; max HP/MP ×2.2; HP set to 50 % on transform)")
SRC_LEVEL = ("docs: [[gameplay/classes-and-legions]] §1 (hero only at level 30, guides); client string "
             "Item_Hero_LevelLimit30")


def name(ctx, id_):
    r = ctx.table("HeroData").get(id_)
    n = ctx.s(r.get("name_key")) if r is not None else None
    return ("%s (Crystal)" % n) if n and id_ > 50 else n


def triggers(ctx):
    """{hero id: Item_Base row} via option 201 on kind-18 items."""
    if getattr(ctx, "_hero_items", None) is None:
        out = {}
        for r in ctx.table("Item_Base"):
            if r.int("kind") != 18:
                continue
            for n in range(1, 11):
                if r.int("opt%d_type" % n) == HERO_OPT:
                    out.setdefault(r.int("opt%d_value" % n), r)
        ctx._hero_items = out
    return ctx._hero_items


def _weapon_base(item_row):
    for n in range(1, 11):
        if item_row.int("opt%d_type" % n) == WEAPON_OPT:
            return item_row.int("opt%d_value" % n)
    return None


def build(ctx):
    trig = triggers(ctx)
    wb = ctx.table("WeaponBase")
    for r in ctx.table("HeroData"):
        id_ = r.int("id")
        f = {"name_key": r.str("name_key"),
             "stats": {"stat1": r.int("stat1"), "stat2": r.int("stat2"), "hp": r.int("hp"), "mp": r.int("mp")},
             "skills": [s for (s,) in repeat(r, "skill%d") if s],
             "transform_skill": r.int("weapon_or_base") or None}
        sources = ["client: HeroData.cdb id %d" % id_]
        if id_ > 50:
            f["base_hero"] = id_ - 50
        it = trig.get(id_)
        if it is not None:
            crystal = id_ > 50
            f["trigger"] = {"item": it.int("id"), "kind": "Innocence Crystal" if crystal else "Innocence"}
            sources.append("client: Item_Base.cdb id %d (kind 18, option 201 = %d)" % (it.int("id"), id_))
            w = _weapon_base(it)
            if w:
                f["weapon_base"] = w
                wr = wb.get(w)
                if wr is not None and wr.int("c14"):
                    f["visual"] = wr.int("c14")
            f["cooldown_s"] = 120
            if crystal:
                f["durability"] = 1500
                f["duration"] = {"durability": 1500, "drain_per_second": 5, "seconds": 300}
                f["level_required"] = None
                sources.append(SRC_DUR)
            else:
                f["durability"] = 240
                f["level_required"] = 30
                sources += [SRC_DUR, SRC_LEVEL]
                if id_ == 1:
                    f["observed_duration_min_s"] = 510
                    sources.append(SRC_VIDEO)
        f = {k: v for k, v in f.items() if v is not None}
        yield Page(TYPE, id_, ctx.title(TYPE, id_), fields=f, sources=sources, body=body)


def body(ctx, page):
    fm, id_ = page.fm, page.id
    r = ctx.table("HeroData").get(id_)
    L, info = [], []
    img = ctx.image(TYPE, id_)
    if img:
        info.append(("", "![%s](%s)" % (page.title, img)))
    info.append(("Hero id", "`%d`" % id_))
    trig = fm.get("trigger") if isinstance(fm.get("trigger"), dict) else None
    if trig:
        info.append(("Unlocked by", "%s (%s, worn in the Innocence slot)" % (
            ctx.link("items", trig.get("item", 0)), trig.get("kind"))))
    else:
        info.append(("Unlocked by", "no item in the client (no kind-18 item points at this hero)"))
    if fm.get("base_hero"):
        info.append(("Same form as", ctx.link(TYPE, fm["base_hero"])))
    elif id_ + 50 in ctx.pages(TYPE):
        info.append(("Crystal version", ctx.link(TYPE, id_ + 50)))
    if fm.get("transform_skill"):
        info.append(("Transform skill", ctx.link("skills", fm["transform_skill"])))
    if fm.get("level_required"):
        info.append(("Level required", fm["level_required"]))
    elif fm.get("base_hero"):
        info.append(("Level required", "none (WM 1107)"))
    if fm.get("cooldown_s"):
        info.append(("Cooldown", "%s s after transforming back (WM 0621)" % fm["cooldown_s"]))
    if fm.get("durability"):
        info.append(("Durability", fmt_num(fm["durability"])))
    if fm.get("visual"):
        info.append(("Visual", "CostumeDB row %s (WeaponBase %s c14)" % (fm["visual"], fm.get("weapon_base"))))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))
    tip = ctx.s(r.get("comment_key")) if r is not None else None
    if tip:
        L += ["### Description", "", quote(tip)]
    st = fm.get("stats") if isinstance(fm.get("stats"), dict) else {}
    L += ["### Stats", "",
          "`HeroData` columns. The decoder's names are guesses: `stat1` / `stat2` look like Attack / "
          "Ability Power (the mage heroes Amaterasu and Tempest Fisher have the higher `stat2` and "
          "more MP). In the [[gameplay/video-fort-war|fort-war video]] Dark Knight Skull raised max "
          "HP/MP from 7,282 / 1,660 to 16,214 / 3,645 (×2.2), which is not base + these values; the "
          "formula is unknown. A hero also gets a share of the gear's stats: 35 % at T1+0 up to "
          "100 % at T3+15 (WM 0628, [[gameplay/classes-and-legions|Classes]] §5).", "",
          table_md(["stat1 (Attack?)", "stat2 (Ability Power?)", "HP", "MP"],
                   [(fmt_num(st.get("stat1", 0)), fmt_num(st.get("stat2", 0)), fmt_num(st.get("hp", 0)),
                     fmt_num(st.get("mp", 0)))])]
    L += ["### Duration", ""]
    if fm.get("base_hero"):
        L += ["An Innocence Crystal has **1,500 durability** and loses **5 per second** while "
              "transformed, so a full crystal gives **300 s** of hero form; it has no level limit "
              "(WM 1107, [[gameplay/events-and-schedules|Events and schedules]] §9). The client row's "
              "period column holds the same 1,500.", ""]
    elif trig:
        L += ["Innocence durability was raised from 24 to **240** (WM 0402, "
              "[[gameplay/events-and-schedules|Events and schedules]] §9); how fast it drains while "
              "transformed is not known, so the duration is still open. In the fort-war video a "
              "Dark Knight Skull form lasted **at least 8.5 minutes** ([[gameplay/video-fort-war|video]]).", ""]
    else:
        L += ["Unknown: no item grants this form.", ""]
    skills = [s for s in fm.get("skills") or [] if isinstance(s, int)]
    if skills:
        L += ["### Skills", "", "`HeroData` skill1–10 (repeats dropped):", ""]
        seen = []
        for s in skills:
            if s not in seen:
                seen.append(s)
        L += ["%d. %s" % (n, ctx.link("skills", s)) for n, s in enumerate(seen, 1)] + [""]
    if fm.get("weapon_base"):
        w = ctx.table("WeaponBase").get(fm["weapon_base"])
        if w is not None:
            L += ["### Weapon base", "",
                  "The Innocence item's WeaponBase row %d: skills %s." % (fm["weapon_base"], ", ".join(
                      ctx.link("skills", s) for (s,) in repeat(w, "skill%d") if s)), ""]
    if trig:
        made = [m for m in ctx.table("Item_Make") if m.int("result_item") == trig.get("item")]
        if made:
            L += ["### How to get it", ""]
            for m in made:
                mats = ", ".join("%s × %d" % (ctx.link("items", it), n) for it, n in repeat(m, "mat%d_item", "mat%d_count"))
                L.append("- Craft %s from %s (%s)" % (ctx.link("items", trig["item"]), mats, ctx.link("recipes", m.int("id"))))
            L += ["- Innocence and pieces come from the Innocence gacha card (%s, "
                  "[[gameplay/progression-and-economy|Progression]] §6)." % ctx.link("gacha", 3), ""]
    boss = [u.int("id") for u in ctx.table("UnitDB")
            if ctx.unit_type(u.int("id")) == "monsters" and u.int("id") in ctx.pages("monsters")
            and (ctx.name("monsters", u.int("id")) or "").lower() == (ctx.name(TYPE, fm.get("base_hero") or id_) or "").lower()]
    if boss:
        L += ["### Monster with this name", "", ", ".join(ctx.link("monsters", b) for b in boss[:6]), ""]
    L += ["See also: [[wiki/items/hero-items|Innocence items]].", ""]
    return "\n".join(L)

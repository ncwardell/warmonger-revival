"""Masteries: character, fort and legion mastery nodes, one page each.

Three client tables, one wiki type (``kind`` tells them apart). Page ids:

  class unit id x 100 + Mastery id   character mastery (Saint 101-127,
                                     Punisher 401-427, Guardian 501-527)
  1000 + FortMastery id              fort mastery (1001-1028)
  2000 + GuildMastery id             legion mastery (2001-2014)

Client sources:
  Mastery       class@04 (= class unit id 1/4/5), tier@08, max_level@0c,
                c6@09 (0, 4, 8, 11, 14, 16 per tier: read as the points that
                must be spent before the tier opens, *guess*), slot@0b (position
                in the tree), name/comment keys, icon. Its name_key/comment_key
                strings (Mastery_N, MasteryComment_N) are in NO shipped string
                table (all 8 languages checked): the character mastery tree has
                no names or effects in the client. A Crush Online leftover?
  FortMastery   name/comment keys, kind@04 (FortMasteryKind_N category), c5@0c
                (tree position, *guess*), c6@10 (position it needs, *guess*),
                cost@14 (fort tax-treasury gold), c8@18 (effect value: Fort
                Shield +3, ...), icon
  GuildMastery  name/comment keys, tier, max level, legion level needed, value
                and cost per level (legion gold), effect_type, icon
Images: assets.py "masteries" (Mastery / FortMastery / GuildMastery icon_file +
icon_idx cells of ui/icons atlases), saved under the page ids above.

Evidence: docs/gameplay/classes-and-legions §4 (fort mastery: one point per
fort level, paid from the tax treasury: 10 M / 20 M / 50 M; usable by the whole
nation; crafting limits) and §3 (legion masteries); crush-mechanics (Elite
Warrior raises the EP cap +500; Acquisition drop rate).

Front matter:
  effect    what the node does                          (required)
  cost      what learning it costs                      (required for fort / legion)
  values    per-level values (legion)
  class, tier, max_level, slot, unlock_points (character); category, position,
  requires_position, value (fort); tier, max_level, legion_level, effect_type (legion)
"""
from .common import Page, clean_text, fmt_num, table_md

TYPE = "masteries"
KIND = "mastery"
LABEL = "Mastery"
PLURAL = "Masteries"
DESCRIPTION = ("Mastery trees from the client: the character mastery tree of each class (`Mastery`; "
               "its names and effects are missing from every shipped string table), the fort masteries "
               "(`FortMastery`, bought with a fort's tax treasury, used by the whole nation) and the "
               "legion masteries (`GuildMastery`, bought with legion gold).")
CHAR_REQUIRED = ["effect", "values"]
REQUIRED = ["effect", "cost"]
CLASS_NAMES = {1: "Saint", 4: "Punisher", 5: "Guardian"}
FORT, LEGION = 1000, 2000
SRC_FORT = ("docs: [[gameplay/classes-and-legions]] §4 (fort mastery points: one per fort level; unlock "
            "paid from the fort's tax treasury, 10 M / 20 M / 50 M, matching cost@14)")
SRC_LEGION = "docs: [[gameplay/classes-and-legions]] §3 (legion level-up and masteries, legion gold)"


def _rows(ctx):
    """{page id: (table, row)}."""
    if getattr(ctx, "_mastery_rows", None) is None:
        out = {}
        for r in ctx.table("Mastery"):
            out.setdefault(r.int("class") * 100 + r.int("id"), ("Mastery", r))
        for r in ctx.table("FortMastery"):
            out.setdefault(FORT + r.int("id"), ("FortMastery", r))
        for r in ctx.table("GuildMastery"):
            out.setdefault(LEGION + r.int("id"), ("GuildMastery", r))
        ctx._mastery_rows = out
    return ctx._mastery_rows


def icons(ctx):
    """[(page id, icon file, cell)] for assets.py."""
    out = []
    for pid, (_t, r) in sorted(_rows(ctx).items()):
        f = r.str("icon_file")
        if f:
            out.append((pid, f, r.int("icon_idx")))
    return out


def name(ctx, id_):
    t = _rows(ctx).get(id_)
    if t is None:
        return None
    table, r = t
    n = ctx.s(r.get("name_key"))
    if n:
        return n
    if table == "Mastery":
        return "%s mastery %d" % (CLASS_NAMES.get(r.int("class"), "Class %d" % r.int("class")), r.int("id"))
    return None


def build(ctx):
    for pid, (table, r) in sorted(_rows(ctx).items()):
        src = ["client: %s.cdb id %d" % (table, r.int("id"))]
        f = {"name_key": r.str("name_key"), "comment_key": r.str("comment_key")}
        req = REQUIRED
        comment = ctx.s(r.get("comment_key"))
        if comment:
            f["effect"] = clean_text(comment).replace("\n", "; ").strip()
        if table == "Mastery":
            kind, req = "character_mastery", CHAR_REQUIRED
            f.update({"class": CLASS_NAMES.get(r.int("class")), "class_unit": r.int("class"),
                      "mastery_id": r.int("id"), "tier": r.int("tier"), "max_level": r.int("max_level"),
                      "unlock_points": r.int("c6"), "slot": r.int("slot")})
        elif table == "FortMastery":
            kind = "fort_mastery"
            f.update({"mastery_id": r.int("id"), "category": r.int("kind"),
                      "category_name": ctx.s("FortMasteryKind_%d" % r.int("kind")),
                      "position": r.int("c5"), "requires_position": r.int("c6"),
                      "cost": {"amount": r.int("cost"), "currency": "fort tax-treasury gold"}})
            if r.int("c8"):
                f["value"] = r.int("c8")
            src.append(SRC_FORT)
        else:
            kind = "legion_mastery"
            lv = r.int("max_level")
            f.update({"mastery_id": r.int("id"), "tier": r.int("tier"), "max_level": lv,
                      "legion_level": r.int("need_guild_lv"), "effect_type": r.int("effect_type"),
                      "values": [r.int("value_lv%d" % n) for n in range(1, lv + 1)],
                      "cost": {"per_level": [r.int("cost_lv%d" % n) for n in range(1, lv + 1)],
                               "currency": "legion gold"}})
            src.append(SRC_LEGION)
        f = {k: v for k, v in f.items() if v is not None}
        yield Page(TYPE, pid, ctx.title(TYPE, pid), fields=f, sources=src, body=body, kind=kind,
                   required=req)


def body(ctx, page):
    fm, pid = page.fm, page.id
    table, r = _rows(ctx)[pid]
    L, info = [], []
    img = ctx.image(TYPE, pid)
    if img:
        info.append(("", "![%s](%s)" % (page.title, img)))
    info.append(("Table", "`%s` id %d" % (table, r.int("id"))))
    if table == "Mastery":
        cu = fm.get("class_unit")
        info.append(("Class", ctx.link("classes", cu, fm.get("class")) if cu else "?"))
        info += [("Tier", fm.get("tier")), ("Max level", fm.get("max_level")),
                 ("Tree slot", fm.get("slot")),
                 ("Opens after", "%s points spent (`c6`, *guess*)" % fm.get("unlock_points"))]
    elif table == "FortMastery":
        info += [("Category", "%s (%s)" % (fm.get("category_name") or "?", fm.get("category"))),
                 ("Tree position", "%s (needs position %s; *guess*)" % (fm.get("position"), fm.get("requires_position"))),
                 ("Cost", "%s gold from the fort's tax treasury" % fmt_num((fm.get("cost") or {}).get("amount", 0))
                  if isinstance(fm.get("cost"), dict) else fm.get("cost"))]
        if fm.get("value"):
            info.append(("Value", fm["value"]))
    else:
        info += [("Tier", fm.get("tier")), ("Max level", fm.get("max_level")),
                 ("Legion level needed", fm.get("legion_level")), ("Effect type", fm.get("effect_type"))]
    if fm.get("effect"):
        info.append(("Effect", fm["effect"]))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))
    if table == "Mastery":
        L += ["The client has no name or description for this node: `%s` / `%s` are missing from every "
              "shipped `StringAll_*.cdb`. What it did, its per-level values and its point cost are open "
              "(`effect`, `values`)." % (r.get("name_key"), r.get("comment_key")), ""]
        same = [p for p, f in ctx.pages(TYPE).items() if f.get("class_unit") == fm.get("class_unit") and p != pid]
        if same:
            L += ["Other %s masteries: %s." % (fm.get("class"), ", ".join(ctx.link(TYPE, p) for p in sorted(same))), ""]
    elif table == "GuildMastery":
        vals = fm.get("values") or []
        cost = (fm.get("cost") or {}).get("per_level", []) if isinstance(fm.get("cost"), dict) else []
        rows = [(n + 1, vals[n] if n < len(vals) else "", fmt_num(cost[n]) if n < len(cost) else "")
                for n in range(max(len(vals), len(cost)))]
        L += ["### Per level", "", "Value unit is not in the client (percent for most, *guess*); cost is "
              "legion gold.", "", table_md(["level", "value", "cost"], rows)]
    else:
        L += ["Fort masteries are bought with one mastery point per fort level plus tax-treasury gold and "
              "apply to everyone in the fort's nation ([[gameplay/classes-and-legions|Classes and legions]] §4).", ""]
        same = sorted(p for p, f in ctx.pages(TYPE).items() if f.get("category") == fm.get("category")
                      and FORT < p < LEGION and p != pid)
        if same:
            L += ["Same category: %s." % ", ".join(ctx.link(TYPE, p) for p in same), ""]
    return "\n".join(L)

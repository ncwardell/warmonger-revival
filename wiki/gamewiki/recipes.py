"""Recipes: one page per Item_Make row (page id = recipe id).

Client source: Item_Make.cdb (record 0x64). Column meanings beyond the
decoder's header come from docs/gameplay: the column after c21 (c22@4c) is the
output count and the next one (c23@50) the gold cost (items-and-crafting §3,
consumables: "Craft gold"; checked against the passion-conversion rows and
in-game screenshots). The decoder's ``gold@28`` is therefore NOT the gold cost;
it is kept as ``c28``. c19@40 (5 on gear rows) with fail_item?@44 is read here
as the superior-result chance and item (*guess*: crafted gear "has a small
chance to come out superior", reinforce-and-runes §4). c24@54 ranges 0..30 and
matches the scroll grades' levels (*guess*: required level,
GUI_ItemMake_NeedLevel_D).

Front matter:
  result        {item, count}                                      (required)
  materials     [{item, count[, x]}]                               (required)
  gold          gold per craft (before the fort's price rate)      (required)
  success_rate  % (Item_Make success%@38)                          (required)
  npc           UnitDB id(s) that offer the recipe -- not in the client (required)
  superior      {chance, item} when the row has one (guess, see above)
  category, filter_mask, level (c24 guess), c28 (raw @28)
"""
from . import _econ
from .common import Page, fmt_num, table_md

TYPE = "recipes"
KIND = "recipe"
LABEL = "Recipe"
DESCRIPTION = ("Every crafting recipe in the client's `Item_Make` table: materials, gold, success "
               "chance and result. Which NPC offers each recipe is not in the client data.")
REQUIRED = ["result", "materials", "gold", "success_rate", "npc"]

# Item_Make filter bits -> craft-window filter (GUI_ItemMakeFilter_*). Not
# decoded bit by bit yet; the category column is shown raw.
SRC_COLS = ("docs: [[gameplay/items-and-crafting]] §3 and [[gameplay/consumables]] (Item_Make c22 = "
            "output count, c23 = gold cost)")


def name(ctx, id_):
    r = ctx.table("Item_Make").get(id_)
    if r is None:
        return None
    n = ctx.name("items", r.int("result_item"))
    return "%s recipe" % n if n else None


def build(ctx):
    for r in ctx.table("Item_Make"):
        rid = r.int("id")
        mats = []
        for n in (1, 2, 3):
            it = r.int("mat%d_item" % n)
            if it:
                m = {"item": it, "count": r.int("mat%d_count" % n)}
                if r.int("mat%d_x" % n):
                    m["x"] = r.int("mat%d_x" % n)
                mats.append(m)
        f = {"result": {"item": r.int("result_item"), "count": r.int("c22") or 1},
             "materials": mats, "gold": r.int("c23"), "success_rate": r.int("success%"),
             "category": r.int("category"), "filter_mask": r.int("filter_mask")}
        if r.int("c19") or r.int("fail_item"):
            f["superior"] = {"chance": r.int("c19"), "item": r.int("fail_item")}
        if r.int("c24"):
            f["level"] = r.int("c24")
        extra = {k: r.int(k) for k in ("c2", "gold", "e1", "e2", "e3", "c21", "c26", "c27") if r.int(k)}
        if extra:
            f["raw"] = {("c28" if k == "gold" else k): v for k, v in extra.items()}
        sources = ["client: Item_Make.cdb id %d" % rid, SRC_COLS]
        yield Page(TYPE, rid, ctx.title(TYPE, rid), fields=f, sources=sources, body=body)


def body(ctx, page):
    fm, rid = page.fm, page.id
    res = fm.get("result") or {}
    it = res.get("item", 0) if isinstance(res, dict) else 0
    info = []
    img = ctx.image("items", it)
    if img:
        info.append(("", "![](%s)" % img))
    info.append(("Recipe id", "`%d` (`Item_Make`)" % rid))
    info.append(("Makes", "%s × %s" % (_econ.item_link(ctx, it), fmt_num(res.get("count", 1)))))
    info.append(("Gold", "%s (before the fort's price rate; one screenshot shows × 1.5)" % fmt_num(fm.get("gold") or 0)))
    info.append(("Success", "%s %%" % fm.get("success_rate")))
    sup = fm.get("superior")
    if isinstance(sup, dict):
        info.append(("Superior result", "%s %% → %s (*guess*: c19@40 / @44)" % (
            sup.get("chance"), _econ.item_link(ctx, sup.get("item", 0)))))
    if fm.get("level"):
        info.append(("Level (c24, *guess*)", fm["level"]))
    info.append(("Category / filter", "%s / `%s`" % (fm.get("category"), hex(fm.get("filter_mask") or 0))))
    npc = fm.get("npc")
    info.append(("Crafted at", ", ".join(ctx.unit_link(u) for u in npc if isinstance(u, int))
                 if isinstance(npc, list) and npc else "unknown (not in the client; add `npc:`)"))
    L = [table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info])]
    rows = [(_econ.item_icon(ctx, m.get("item", 0)), _econ.item_link(ctx, m.get("item", 0)),
             fmt_num(m.get("count", 0)), m.get("x", ""))
            for m in fm.get("materials") or [] if isinstance(m, dict)]
    L += ["### Materials", "", table_md(["", "item", "count", "x"], rows) if rows else "None listed.\n"]
    raw = fm.get("raw")
    if isinstance(raw, dict) and raw:
        L += ["Unknown columns: " + ", ".join("`%s` = %s" % kv for kv in raw.items()) +
              " (`c28` is the decoder's `gold@28`, which is not the gold cost).", ""]
    others = [r.int("id") for r in ctx.table("Item_Make") if r.int("result_item") == it and r.int("id") != rid]
    if others:
        L += ["Other recipes for the same item: " + ", ".join(ctx.link(TYPE, o, "recipe %d" % o) for o in others), ""]
    L += ["NPCs named as crafters in the guides: Farrell (weapons, passion conversion), Odin (gear), "
          "Alan (runes), Owen (alchemy), Paraman (superior weapons) — "
          "[[gameplay/items-and-crafting|Items and crafting]] §3.", ""]
    nm = ctx.name("items", it)
    ment = ctx.mentions(nm) if nm else []
    if ment:
        L += ["### Result mentioned in", ""] + ["- [[%s|%s]]" % m for m in ment] + [""]
    return "\n".join(L)

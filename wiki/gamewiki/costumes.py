"""Costumes: one page per costume set (page id = the set's lowest item id).

A costume set is every Item_Base row of kind 32 (Costume) with the same name:
one item per class (Saint / Punisher / Guardian, ``req_class``), sometimes
listed twice (Haple, Oracle and Christmas sets have a second, later block of
ids). The item pages hold the per-item data; this page puts the set together.

Client sources:
  Item_Base   kind 32 rows: name, class mask, period@3a, option slots. In the
              costume rows option 208 appears three times = the dye colour of
              costume parts 1-3 (values are ColorDB ids, *inferred*: the
              character-creation costume has three part colours,
              GUI_CharCreate_Color_C1..C3, and the dye packet names cpart1..3),
              option 209 = the costume's look (a model index, *inferred*: one
              value per set, sometimes +1 for one class, and the same in the
              duplicated blocks), followed by a second 209 = 0.
              Other options are the costume's stat bonus (ItemOption codes).
  ColorDB     dye palette: id -> r, g, b (0-255)
  CostumeDB   NOT these costumes: its rows are the 3-D visual sets of weapons
              (WeaponBase c14 = CostumeDB id: 100-273) and hero forms (1000-1007).
              They are shown on the class and hero pages.

Evidence (docs/gameplay):
  events-and-schedules §9 (WM 0406): costume duration 1,440 -> 2,610 min,
  counted only while worn. Item_Base period@3a holds 2,610 or 2,160 (minutes,
  *inferred* from the match) or 0 (permanent: Halloween, Developer and the
  second Christmas block).
  crush-patch-notes (CO 1222): carving a costume (making it permanent) at the
  Merits Costume Merchant; Costume Remover (item 1999) hides it but keeps the
  stats.

Front matter:
  items        [{item, class, period, look, colors}]   per class
  classes      classes that have a piece
  stats        [{code, stat, value}] the set's bonus (same on every piece)
  duration     {"minutes": n, "counts": "while worn"} or {"permanent": true}  (required)
  obtained_from  union of the items' obtained_from (item pages)            (required)
"""
from . import _econ, items
from .common import Page, fmt_num, quote, table_md

TYPE = "costumes"
KIND = "costume"
LABEL = "Costume"
DESCRIPTION = ("Every wearable costume set: the kind-32 items of the client's `Item_Base`, one piece "
               "per class, with their stat bonus, look and duration. (The client table `CostumeDB` "
               "is something else: the 3-D visual sets of weapons and hero forms, shown on the "
               "[[wiki/classes/index|class]] and [[wiki/heroes/index|hero]] pages.)")
REQUIRED = ["duration", "obtained_from"]
UNION_KEYS = ["obtained_from"]
COSTUME_KIND = 32
LOOK, COLOR = 209, 208
SRC_DURATION = ("docs: [[gameplay/events-and-schedules]] §9 (WM 0406: costume duration 1,440 → 2,610 min, "
                "counts only while worn); Item_Base period@3a read as minutes (inferred)")


def sets(ctx):
    """{set id: [Item_Base rows]} for every costume name; set id = lowest item id."""
    if getattr(ctx, "_costume_sets", None) is None:
        by_name = {}
        for r in ctx.table("Item_Base"):
            if r.int("kind") == COSTUME_KIND:
                by_name.setdefault(ctx.name("items", r.int("id")) or "Costume %d" % r.int("id"), []).append(r)
        ctx._costume_sets = {min(x.int("id") for x in rows): rows for rows in by_name.values()}
        ctx._costume_of = {r.int("id"): sid for sid, rows in ctx._costume_sets.items() for r in rows}
    return ctx._costume_sets


def set_of(ctx, item):
    """Costume set id of a costume item, or None."""
    sets(ctx)
    return ctx._costume_of.get(item)


def name(ctx, id_):
    rows = sets(ctx).get(id_)
    return ctx.name("items", id_) if rows else None


def _options(r):
    return [(r.int("opt%d_type" % n), r.int("opt%d_value" % n)) for n in range(1, 11)
            if r.int("opt%d_type" % n)]


class _Opt:
    def __init__(self, ctx):
        self.options = {r.int("code"): r for r in ctx.table("ItemOption")}


def build(ctx):
    ix = _Opt(ctx)
    item_pages = ctx.pages("items")
    for sid, rows in sorted(sets(ctx).items()):
        pieces, stats, periods = [], None, set()
        for r in sorted(rows, key=lambda x: x.int("id")):
            opts = _options(r)
            look = [v for c, v in opts if c == LOOK]
            mask = r.int("req_class")
            pieces.append({"item": r.int("id"),
                           "class": "all" if mask == 255 else ", ".join(n for b, n in items.CLASSES if mask & b),
                           "period": r.int("period"), "look": look[0] if look else None,
                           "colors": [v for c, v in opts if c == COLOR]})
            st = [{"code": c, "stat": items.stat_text(ix, c, v)[0], "value": v} for c, v in opts
                  if c not in (LOOK, COLOR) and c not in items.SPECIAL and (c < 200 or c in ix.options)]
            if stats is None or len(st) > len(stats):
                stats = st
            periods.add(r.int("period"))
        f = {"items": pieces,
             "classes": sorted({p["class"] for p in pieces}, key=lambda c: [n for _b, n in items.CLASSES].index(c)
                               if c in [n for _b, n in items.CLASSES] else 9),
             "stats": stats or []}
        sources = ["client: Item_Base.cdb kind 32 ids %s" % ", ".join(str(p["item"]) for p in pieces)]
        if periods == {0}:
            f["duration"] = {"permanent": True}
        elif 0 not in periods and len(periods) == 1:
            f["duration"] = {"minutes": periods.pop(), "counts": "while worn"}
            sources.append(SRC_DURATION)
        else:
            f["duration"] = {"minutes_by_item": {str(p["item"]): p["period"] for p in pieces},
                             "counts": "while worn", "note": "0 = permanent"}
            sources.append(SRC_DURATION)
        got = []
        for p in pieces:
            for o in (item_pages.get(p["item"]) or {}).get("obtained_from") or []:
                if isinstance(o, dict):
                    e = dict(o, item=p["item"])
                    if e not in got:
                        got.append(e)
        f["obtained_from"] = got
        yield Page(TYPE, sid, ctx.title(TYPE, sid), fields=f, sources=sources, body=body)


def _color(ctx, cid):
    r = ctx.table("ColorDB").get(cid)
    if r is None:
        return "colour %s" % cid
    return "`#%02x%02x%02x` (%d)" % (int(r.float("r")), int(r.float("g")), int(r.float("b")), cid)


def body(ctx, page):
    fm = page.fm
    pieces = [p for p in fm.get("items") or [] if isinstance(p, dict)]
    L = []
    imgs = " ".join("![](%s)" % ctx.image("items", p["item"]) for p in pieces if ctx.image("items", p.get("item", 0)))
    info = []
    if imgs:
        info.append(("", imgs))
    info.append(("Pieces", "%d, for %s" % (len(pieces), items.class_links(ctx, [
        c for c in fm.get("classes") or [] if c in items.CLASS_UNITS]))))
    dur = fm.get("duration") or {}
    if isinstance(dur, dict):
        if dur.get("permanent"):
            info.append(("Duration", "permanent (period 0)"))
        elif dur.get("minutes"):
            info.append(("Duration", "%s min (%.1f h) of wearing time" % (fmt_num(dur["minutes"]), dur["minutes"] / 60)))
        else:
            info.append(("Duration", "differs per piece (see below)"))
    stats = [s for s in fm.get("stats") or [] if isinstance(s, dict)]
    info.append(("Stat bonus", ", ".join("%s %s" % (s.get("stat"), _signed(s.get("value"))) for s in stats) or "none"))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))
    tip = None
    for p in pieces:
        row = ctx.table("Item_Base").get(p.get("item", 0))
        tip = tip or (ctx.s(row.get("comment_key")) if row else None)
    if tip:
        L += ["### Tooltip", "", quote(tip)]
    rows = []
    for p in pieces:
        rows.append((_econ.item_icon(ctx, p["item"]), ctx.link("items", p["item"]),
                     items.class_links(ctx, [p["class"]]) if p.get("class") in items.CLASS_UNITS else p.get("class"),
                     "permanent" if not p.get("period") else "%s min" % fmt_num(p["period"]),
                     p.get("look"), ", ".join(_color(ctx, c) for c in p.get("colors") or [])))
    L += ["### Pieces", "",
          "`look` is option 209 (the costume model, *inferred*); the colours are the "
          "three option-208 values, read as `ColorDB` ids for costume parts 1–3 (*inferred*).", "",
          table_md(["", "item", "class", "period", "look", "part colours"], rows)]
    L += ["### Duration", "",
          "Timed costumes run for their item period in minutes of **wearing** time: the timer only "
          "counts while the costume is worn (WM 0406 raised it from 1,440 to 2,610 minutes; "
          "[[gameplay/events-and-schedules|Events and schedules]] §9). The client rows hold 2,610 or "
          "2,160; period 0 is a permanent costume. In Crush Online a timed costume could be *carved* "
          "(made permanent, losing its bonus) at the Merits Costume Merchant, and a Costume Remover "
          "hides it while keeping the stats ([[gameplay/crush-patch-notes|Crush patch notes]]).", ""]
    got = [o for o in fm.get("obtained_from") or [] if isinstance(o, dict)]
    if got:
        L += ["### Where to get it", ""]
        for o in got:
            how = o.get("how")
            what = ctx.link("items", o["item"]) if isinstance(o.get("item"), int) else ""
            if how == "shop":
                L.append("- %s: sold in %s" % (what, ctx.link("shops", o.get("shop", 0))))
            elif how == "quest_reward":
                L.append("- %s: reward of quest %s" % (what, ctx.link("quests", o.get("quest", 0))))
            elif how == "random_box":
                L.append("- %s: random box %s" % (what, ctx.link("boxes", o.get("box", 0))))
            elif how == "gacha":
                L.append("- %s: %s" % (what, ctx.link("gacha", o.get("pool", 0))))
            else:
                L.append("- %s: %s" % (what, ", ".join("%s %s" % kv for kv in o.items() if kv[0] != "item")))
        L.append("")
    else:
        L += ["### Where to get it", "",
              "Nothing in the client data (no shop, box, quest or gacha row). Costumes were sold in the "
              "cash shop and by the Merits costume merchant for medals ([[gameplay/reinforce-and-runes|"
              "Reinforce and runes]]: costume medal prices); add the source to `obtained_from:`.", ""]
    L += ["See also: [[wiki/items/costume-items|all costume items]].", ""]
    return "\n".join(L)


def _signed(v):
    return "%+d" % v if isinstance(v, int) else str(v)

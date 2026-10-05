"""Upgrades: reinforcement tables (ItemSancMet rows, page id = row id) and rune
upgrade lines (JewelSocketMake groups, page id = 1000 + group).

Client sources:
  ItemSancMet      gold@04 + 6 steps x 5 {item, count}; Item_Base c41@92 points
                   equipment at a row (items.py, *inferred*)
  JewelSocketMake  one row per rune level: jewel_item, 3 {item, count},
                   next_item, level, group (21 groups of 10 = 21 rune lines;
                   reinforce-and-runes §1 says it matches the WM 0920 cost table)
Success rates are server side for both (contract craft_reinforce_rune_odds).

Front matter, reinforcement table (type "upgrade", kind "reinforcement"):
  gold            gold per attempt                                 (required)
  steps           [{step, materials: [{item, count}]}]             (required)
  success_rates   per step / level -- not in the client            (required)
  used_by         Item_Base ids whose c41@92 is this row
Front matter, rune line (type "upgrade", kind "rune_upgrade"):
  group, rune     JewelSocketMake group, the +0 rune item
  levels          [{row, level, item, next, materials}]            (required)
  success_rates                                                    (required)
"""
from . import _econ
from .common import Page, fmt_num, table_md

TYPE = "upgrades"
KIND = "reinforcement"
LABEL = "Upgrade"
DESCRIPTION = ("Reinforcement material tables (`ItemSancMet`, one page per row, shared by many items) "
               "and rune upgrade lines (`JewelSocketMake`, pages 1001–1021, one per rune). Success "
               "rates are not in the client.")
REQUIRED = ["gold", "steps", "success_rates"]
RUNE_BASE = 1000
REINFORCE_KINDS = (18, 31, 50, 51, 52, 53, 54, 55, 56, 57)     # as items.py
SRC_RUNES = ("docs: [[gameplay/reinforce-and-runes]] §1 (WM 0920 rune cost table matches "
             "JewelSocketMake +0→+9)")


def _users(ctx):
    if getattr(ctx, "_sanc_users", None) is None:
        out = {}
        for r in ctx.table("Item_Base"):
            if r.int("kind") in REINFORCE_KINDS and r.int("c41"):
                out.setdefault(r.int("c41"), []).append(r.int("id"))
        ctx._sanc_users = out
    return ctx._sanc_users


def _rune_groups(ctx):
    if getattr(ctx, "_rune_groups", None) is None:
        g = {}
        for r in ctx.table("JewelSocketMake"):
            g.setdefault(r.int("group"), []).append(r)
        for rows in g.values():
            rows.sort(key=lambda r: r.int("level"))
        ctx._rune_groups = g
    return ctx._rune_groups


def name(ctx, id_):
    if id_ > RUNE_BASE:
        rows = _rune_groups(ctx).get(id_ - RUNE_BASE)
        if not rows:
            return None
        n = ctx.name("items", rows[0].int("jewel_item"))
        return "%s upgrades" % n if n else None
    users = _users(ctx).get(id_, [])
    first = next((ctx.name("items", u) for u in users if ctx.name("items", u)), None)
    if first:
        return "Reinforcement %d: %s%s" % (id_, first, " and %d more" % (len(users) - 1) if len(users) > 1 else "")
    return "Reinforcement %d" % id_


def build(ctx):
    users = _users(ctx)
    for r in ctx.table("ItemSancMet"):
        sid = r.int("id")
        steps = []
        for step in range(1, 7):
            mats = [{"item": it, "count": n} for it, n in
                    ((r.int("step%d_mat%d_item" % (step, k)), r.int("step%d_mat%d_count" % (step, k)))
                     for k in range(1, 6)) if it]
            steps.append({"step": step, "materials": mats})
        f = {"gold": r.int("gold"), "steps": steps, "used_by": sorted(users.get(sid, []))}
        sources = ["client: ItemSancMet.cdb id %d" % sid,
                   "client: Item_Base.cdb c41@92 (inferred link to ItemSancMet)",
                   "contract: items.yaml reinforce 0x436, server_rules craft_reinforce_rune_odds"]
        yield Page(TYPE, sid, ctx.title(TYPE, sid), fields=f, sources=sources, body=sanc_body)
    for g, rows in sorted(_rune_groups(ctx).items()):
        pid = RUNE_BASE + g
        levels = []
        for r in rows:
            levels.append({"row": r.int("id"), "level": r.int("level"), "item": r.int("jewel_item"),
                           "next": r.int("next_item"),
                           "materials": [{"item": it, "count": n} for it, n in
                                         ((r.int("mat%d_item" % k), r.int("mat%d_count" % k)) for k in (1, 2, 3)) if it]})
        f = {"group": g, "rune": rows[0].int("jewel_item"), "levels": levels}
        sources = ["client: JewelSocketMake.cdb group %d (rows %d–%d)" % (g, rows[0].int("id"), rows[-1].int("id")),
                   SRC_RUNES, "contract: items.yaml rune_upgrade 0x4a8, server_rules craft_reinforce_rune_odds"]
        yield Page(TYPE, pid, ctx.title(TYPE, pid), fields=f, sources=sources, body=rune_body,
                   kind="rune_upgrade", required=["levels", "success_rates"])


def _mats(ctx, mats):
    return ", ".join("%s × %s" % (_econ.item_link(ctx, m.get("item", 0)), fmt_num(m.get("count", 0)))
                     for m in mats or [] if isinstance(m, dict)) or "–"


def sanc_body(ctx, page):
    fm, sid = page.fm, page.id
    users = [u for u in fm.get("used_by") or [] if isinstance(u, int)]
    info = []
    shown = next((u for u in users if ctx.name("items", u) and ctx.image("items", u)), None)
    if shown:
        info.append(("", "![](%s)" % ctx.image("items", shown)))
    info.append(("Table", "`ItemSancMet` row %d" % sid))
    info.append(("Gold per attempt", fmt_num(fm.get("gold") or 0)))
    info.append(("Success rates", fm.get("success_rates") or "unknown (server side)"))
    info.append(("Used by", "%d items" % len(users)))
    L = [table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info])]
    rows = [(s.get("step"), _mats(ctx, s.get("materials"))) for s in fm.get("steps") or [] if isinstance(s, dict)]
    L += ["### Materials per step", "",
          "Six material steps per row. Whether a step is a reinforce level band or a tier is not "
          "settled: the patch notes' six planned tiers fit six steps "
          "([[gameplay/reinforce-and-runes|Reinforce and runes]] §4, *guess*). One 2018 screenshot shows "
          "a T1 weapon +0→+1 costing 1,000 gold + 3 Red Passion Fragments [D].", "",
          table_md(["step", "materials"], rows)]
    if users:
        L += ["### Items that use it", "", ", ".join(ctx.link("items", u) for u in users), ""]
    L += ["### Rules from the patch notes", "",
          "- A failed reinforce drops the item one level and uses up the materials; Reinforcing "
          "Adjuvants (item 1100) prevent the drop (WM 0412).",
          "- Success falls slowly with tier and rarity; Rainbow Reinforcing Stones only work on their "
          "own rarity (WM 0406 / 0420).",
          "- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §4.", ""]
    return "\n".join(L)


def rune_body(ctx, page):
    fm = page.fm
    rune = fm.get("rune")
    info = []
    if isinstance(rune, int) and ctx.image("items", rune):
        info.append(("", "![](%s)" % ctx.image("items", rune)))
    info.append(("Rune line", "`JewelSocketMake` group %s" % fm.get("group")))
    info.append(("Starts at", _econ.item_link(ctx, rune or 0)))
    info.append(("Success rates", fm.get("success_rates") or "unknown (server side; patch notes give only trends)"))
    L = [table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info])]
    rows = []
    for lv in fm.get("levels") or []:
        if isinstance(lv, dict):
            nxt = lv.get("next") or 0
            rows.append(("+%s" % lv.get("level"), _econ.item_icon(ctx, lv.get("item", 0)),
                         _econ.item_link(ctx, lv.get("item", 0)),
                         _econ.item_link(ctx, nxt) if nxt else "– (max)", _mats(ctx, lv.get("materials")),
                         lv.get("row")))
    L += ["### Levels", "",
          "Each row upgrades the rune to the next item (C->S `0x4a8`). The +9 row has no next item, "
          "so its cost is never used. The costs match the 20 Sep 2018 patch table "
          "([[gameplay/reinforce-and-runes|Reinforce and runes]] §1).", "",
          table_md(["level", "", "rune", "becomes", "materials", "row"], rows)]
    L += ["### Rules from the patch notes", "",
          "- Cap +5 at launch, +9 from WM 0726; success falls with level, earlier for rarer runes "
          "(WM 0406); raised overall in WM 0920. A failure usually loses one level.",
          "- Source: [[gameplay/reinforce-and-runes|Reinforce and runes]] §3.", ""]
    return "\n".join(L)

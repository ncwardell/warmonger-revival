"""Gacha pools: one page per client pool Gacha_00..06 (page id = pool number).

Client sources: Gacha_NN.cdb (item, grade; no rates), strings
GUI_Herobind_Type0..3 (card names) and GUI_Herobind_GachaText_0..6 (tiers per
pool). Contract: items.yaml hero_gacha 0x4aa (type 0 free daily, 1..6 paid;
free bag slots needed per type), server_rules gacha_odds.

Front matter:
  pool              pool number (= 0x4aa gacha_type)
  contents          [{item, grade[, c4]}] in table order          (required)
  price             {amount, currency, currency_name[, free_every_hours]} (required)
  odds              draw odds -- not in the client, must be hand-entered (required)
  bag_slots_needed  free bag slots the client checks before a draw
"""
import json

from . import _econ
from .common import Page, fmt_num, quote, table_md

TYPE = "gacha"
KIND = "gacha_pool"
LABEL = "Gacha pool"
PLURAL = "Gacha pools"
DESCRIPTION = ("The hero gacha (\"Herobind\") pools `Gacha_00`–`Gacha_06`: what each card can give. "
               "The client has no odds; they were server side and never published.")
REQUIRED = ["contents", "price", "odds"]
POOLS = range(7)
SLOTS = [3, 10, 10, 5, 10, 10, 10]          # contract hero_gacha c2s note
NAMES = {0: "Daily gacha", 1: "Gear gacha", 2: "Weapon gacha", 3: "Innocence gacha",
         4: "Gear gacha (tiers 2-3)", 5: "Weapon gacha (tiers 2-3)", 6: "Unused gacha pool"}
# events-and-schedules §10 (WM 1018 image 2): card price in jewels. Which
# client pool is which card is inferred from the pool's contents and its
# GUI_Herobind_GachaText_N tier line.
PRICES = {1: 1000, 2: 2000, 3: 2000, 4: 4000, 5: 5000}
WM1018 = {
    1: "Normal Gear (1–3), Superior Gear (1–2), Normal / Superior Rainbow Reinforcing Stone",
    2: "Normal Weapon (1–3), Superior Weapon (1), Rare Weapon (1), Normal / Superior Rainbow stone",
    3: "Normal / Superior / Rare Innocence (1), Crystal: Innocence (1), Piece: Innocence",
    4: "Normal Gear (2–3), Superior Gear (2–3), Superior Set Gear (boss set) (2–3), Superior Rainbow stone (2–3)",
    5: "Normal / Superior Weapon (2–3), Rare Weapon (1–2), Normal / Superior / Rare Rainbow stone",
}
SRC_PRICE = ("docs: [[gameplay/events-and-schedules]] §10 (WM 1018 image 2: card prices in jewels; "
             "pool-to-card match inferred from contents and GUI_Herobind_GachaText_N)")


def name(ctx, id_):
    return NAMES.get(id_)


def build(ctx):
    for n in POOLS:
        try:
            t = ctx.table("Gacha_%02d" % n)
        except OSError:
            continue
        contents = []
        for r in t:
            e = {"item": r.int("item"), "grade": r.int("grade")}
            if r.int("c3") or r.int("c4"):
                e.update({k: r.int(k) for k in ("c3", "c4") if r.int(k)})
            contents.append(e)
        f = {"pool": n, "contents": contents}
        sources = ["client: Gacha_%02d.cdb" % n, "client strings: GUI_Herobind_GachaText_%d" % n,
                   "contract: items.yaml hero_gacha 0x4aa, server_rules gacha_odds"]
        if n == 0:
            f["price"] = {"amount": 0, "currency": 13, "currency_name": "free", "free_every_hours": 12}
        elif n in PRICES:
            f["price"] = {"amount": PRICES[n], "currency": 13, "currency_name": _econ.currency_name(13)}
            sources.append(SRC_PRICE)
        f["bag_slots_needed"] = SLOTS[n]
        yield Page(TYPE, n, ctx.title(TYPE, n), fields=f, sources=sources, body=body)


def body(ctx, page):
    fm, n = page.fm, page.id
    info = [("Pool", "`%d` (`Gacha_%02d.cdb`, 0x4aa gacha_type %d)" % (n, n, n))]
    card = ctx.s("GUI_Herobind_Type%d" % n)
    if card:
        info.append(("Card name", "%s (`GUI_Herobind_Type%d`)" % (card, n)))
    price = fm.get("price") or {}
    if isinstance(price, dict) and price:
        if price.get("free_every_hours"):
            info.append(("Price", "free, once every %s hours" % price["free_every_hours"]))
        else:
            info.append(("Price", "%s %s" % (fmt_num(price.get("amount", 0)), price.get("currency_name", ""))))
    info.append(("Bag slots needed", fm.get("bag_slots_needed")))
    odds = fm.get("odds")
    info.append(("Odds", (odds if isinstance(odds, str) else json.dumps(odds, ensure_ascii=False))
                 if odds else "unknown (server side, never published)"))
    contents = [c for c in fm.get("contents") or [] if isinstance(c, dict)]
    info.append(("Entries", "%d (%d distinct items)" % (len(contents), len({c.get('item') for c in contents}))))
    L = [table_md(["", ""], [("**%s**" % k, v) for k, v in info])]
    tip = ctx.s("GUI_Herobind_GachaText_%d" % n)
    if tip:
        L += ["### Card text", "", quote(tip)]
    if n in WM1018:
        L += ["### What the 2018 card listed", "",
              "[[gameplay/events-and-schedules|Events and schedules]] §10 (WM 1018 image): %s. "
              "The match of this client pool to that card is *inferred* from the tiers and contents." % WM1018[n], ""]
    by_grade = {}
    for c in contents:
        by_grade.setdefault(c.get("grade"), []).append(c)
    L += ["### Contents", "",
          "`grade` and `c3` are the table's own columns. In the paid pools grade 3 rows have `c3` 0, "
          "grade 2 rows `c3` 1 and grade 1 rows `c3` 2, and the Rainbow stones 641/643 appear once "
          "per rarity; so `c3` looks like the rarity (0 normal, 1 superior, 2 rare) and `grade` like "
          "a draw class, 3 the commonest (*guess*). Pools 4 and 5 set an unknown column `c4` = 1 "
          "on every row.", ""]
    for g in sorted(by_grade, key=lambda x: (x is None, x)):
        rows = []
        for c in by_grade[g]:
            it = c.get("item", 0)
            rows.append((_econ.item_icon(ctx, it), _econ.item_link(ctx, it), _econ.kind_name(ctx, it),
                         c.get("c3", 0)))
        L += ["#### Grade %s (%d)" % (g, len(rows)), "", table_md(["", "item", "kind", "c3"], rows)]
    L += ["### Odds", "",
          "Not in the client (`Gacha_NN` has items and grades only). The contract's "
          "`gacha_odds` suggestion (uniform within a grade, grade weights 70/25/5) is invented, not "
          "original data. Put real odds in `odds:` with a source.", ""]
    refs = _econ.gameplay_refs(r"gacha|herobind")
    if refs:
        L += ["### Seen in", ""] + _econ.refs_md(refs) + [""]
    return "\n".join(L)

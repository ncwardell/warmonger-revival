"""Shops: one page per NPC shop (Npc_Carry row), plus the Cash Mall
(PrimiumShop, page id 1000) and bag/warehouse expansion (ExpandSlot, page id
1001).

Client sources (data/tables/*.tsv, docs/spec/data-tables.md):
  Npc_Carry    shop_id@00 (= UnitDB u16@a2 of the NPC), c2..c4, then item
               records {code, p1, count, p2}; the list index is the 0x430
               shop_index (contract/items.yaml shop_buy)
  UnitDB       u16@a2 -> shop; name_key = person (TitleName_*), str@40 = role
  Item_Base    buy_currency@1f / buy_price@20 (base price), cost pair @24/@26
  PrimiumShop  cash mall catalogue (contract cash_mall_buy 0x484)
  ExpandSlot   bag (cost1) / warehouse (cost2) row prices (contract 0x47f)
Prices shown in game are the base price run through the client formula
(contract server_rules.price_formula) with the rates the server sends in
0x452; _econ.OBSERVED_RATES are the rates that reproduce the 2018 prices.

Front matter (NPC shop):
  npc            [UnitDB ids] that open this shop            (required)
  stock          [{slot, item, count, p1, p2}] in list order  (required)
  prices         [{item, currency, currency_name, base, buy, sell[, cost_pair]}]
                 one per distinct stocked item, buy/sell at price_rates (required)
  price_rates    {buy_rate, sell_rate, basis} percent rates (0x452)
  observed_prices  prices seen in play, only where docs/gameplay sources them
"""
from . import _econ, common
from .common import Page, fmt_num, table_md

TYPE = "shops"
KIND = "shop"
LABEL = "Shop"
DESCRIPTION = ("Every NPC shop in the client's `Npc_Carry` table (stock, prices and the NPCs that "
               "open it), plus the Cash Mall (`PrimiumShop`, page 1000) and bag/warehouse "
               "expansion prices (`ExpandSlot`, page 1001). Gacha pools and random boxes have their "
               "own sections ([[wiki/gacha/index|Gacha pools]], [[wiki/boxes/index|Random boxes]]).")
REQUIRED = ["stock", "prices", "npc"]
UNION_KEYS = ["observed_prices"]
CASH_MALL, EXPANSION = 1000, 1001

# Prices seen in play. Only numbers that docs/gameplay cites.
SRC_ECON4 = "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)"
SRC_VID = "docs: [[gameplay/video-tutorial-walkthrough]] 14:20; [[gameplay/video-character-creation-and-tutorial]] 8:40"
OBSERVED = {
    281: [(883, 79, "Gold"), (884, 79, "Gold"), (908, 19800, "Gold"), (688, 5500, "Gold"),
          (945, 158400, "Gold"), (946, 285120, "Gold"), (947, 1346400, "Gold"),
          (949, 3960000, "Gold"), (1105, 3960, "Gold")],
    287: [(883, 79, "Gold"), (884, 79, "Gold"), (906, 79, "Gold")],
    283: [(854, 2, "Silver Medal"), (855, 5, "Bronze Medal"), (856, 5, "Silver Medal"),
          (857, 5, "Bronze Medal"), (1051, 4, "Bronze Medal"), (1052, 3, "Silver Medal"),
          (1053, 2, "Gold Medal"), (1054, 1, "Mithril medal"), (689, 1, "Bronze Medal"),
          (690, 1, "Silver Medal"), (691, 1, "Gold Medal")],
}
OBSERVED_SRC = {281: SRC_ECON4, 287: SRC_VID,
                283: "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"}
OBSERVED_NOTE = {
    (287, 906): "shown as 'Scroll : Return' at 79, but item 906 has base 80 (formula: 633); "
                "the shop may have listed 911 or another 10-gold scroll",
    (283, 854): "client prices it in currency 10 (bronze)",
    (283, 857): "client prices it in currency 12 (gold medal)",
}


def _carry(ctx):
    return ctx.table("Npc_Carry")


def name(ctx, id_):
    if id_ == CASH_MALL:
        return ctx.s("GUI_Herobind_Title") or "Cash Mall"
    if id_ == EXPANSION:
        return "Bag and warehouse expansion"
    npcs = _econ.shop_npcs(ctx).get(id_, [])
    names = []
    for u in npcs:
        n = ctx.name(ctx.unit_type(u), u)
        if n and n not in names:
            names.append(n)
    if not names:
        return "Shop %d (no NPC)" % id_
    role = next((r for r in (_econ.unit_role(ctx, u) for u in npcs) if r), None)
    base = "%s's shop" % names[0]
    if role:
        base += " (%s)" % role
    # several shops share a keeper's name (Wren runs 281, 287 and 291)
    same = [s for s, us in _econ.shop_npcs(ctx).items()
            if s != id_ and any(ctx.name(ctx.unit_type(u), u) == names[0] for u in us)]
    return base + (" %d" % id_ if same else "")


def stock_of(row):
    out = []
    for slot in range(70):
        code = row.get("item%d_code" % (slot + 1))
        if code is None:
            break
        if row.int("item%d_code" % (slot + 1)):
            out.append({"slot": slot, "item": row.int("item%d_code" % (slot + 1)),
                        "count": row.int("item%d_count" % (slot + 1)),
                        "p1": row.int("item%d_p1" % (slot + 1)), "p2": row.int("item%d_p2" % (slot + 1))})
    return out


def build(ctx):
    npcs_by_shop = _econ.shop_npcs(ctx)
    for r in _carry(ctx):
        sid = r.int("shop_id")
        stock = stock_of(r)
        f = {}
        f["npc"] = sorted(npcs_by_shop.get(sid, []))
        f["stock"] = stock
        prices, seen = [], set()
        for e in stock:
            if e["item"] in seen:
                continue
            seen.add(e["item"])
            p = _econ.item_price(ctx, e["item"])
            if p is not None:
                prices.append(p)
        f["prices"] = prices
        f["price_rates"] = dict(_econ.OBSERVED_RATES)
        f["header"] = {"c2": r.int("c2"), "c3": r.int("c3"), "c4": r.int("c4")}
        sources = ["client: Npc_Carry.cdb shop %d" % sid]
        if f["npc"]:
            sources.append("client: UnitDB.cdb u16@a2 = %d (units %s)" % (sid, ", ".join(map(str, f["npc"]))))
        sources += _econ.RATE_SOURCES
        if sid in OBSERVED:
            f["observed_prices"] = [
                dict({"item": it, "shown": shown, "currency": cur, "source": OBSERVED_SRC[sid]},
                     **({"note": OBSERVED_NOTE[(sid, it)]} if (sid, it) in OBSERVED_NOTE else {}))
                for it, shown, cur in OBSERVED[sid]]
            sources.append(OBSERVED_SRC[sid])
        yield Page(TYPE, sid, ctx.title(TYPE, sid), fields=f, sources=sources, body=body)
    yield cash_mall(ctx)
    yield expansion(ctx)


# ------------------------------------------------------------------ cash mall

TABS = {1: "Item", 2: "Costume", 3: "Convenience", 4: "Package"}


def cash_mall(ctx):
    stock, prices = [], []
    for r in ctx.table("PrimiumShop"):
        e = {"entry": r.int("id"), "item": r.int("item"), "price": r.int("price"),
             "discount": r.int("c5"), "tab": r.int("currency"), "c3": r.int("c3"), "c10": r.int("discount%")}
        if r.int("sale_start") or r.int("sale_end"):
            e["sale"] = [r.int("sale_start"), r.int("sale_end")]
        stock.append(e)
        prices.append({"entry": e["entry"], "item": e["item"], "currency": 7,
                       "currency_name": "Purple Jewel",
                       "buy": e["price"] * (100 - e["discount"]) // 100})
    f = {"stock": stock, "prices": prices}
    sources = ["client: PrimiumShop.cdb (57 rows)",
               "contract: items.yaml cash_mall_buy 0x484 (price@08 x (100 - @14) / 100, purple jewels)",
               "client strings: GUI_Herobind_Title, GUI_Herobind_ShopFilter_1..4"]
    return Page(TYPE, CASH_MALL, ctx.title(TYPE, CASH_MALL), fields=f, sources=sources,
                body=cash_mall_body, required=["stock", "prices"])


def cash_mall_body(ctx, page):
    fm = page.fm
    L = [table_md(["", ""], [
        ("**Store**", "Cash Mall (`GUI_Herobind_Title`), opened from the NPC menu function 0x26 "
                      "or the HeroBind window (contract `cash_mall_buy`)"),
        ("**Currency**", "Purple Jewels (real money; [[gameplay/progression-and-economy|economy]] §1)"),
        ("**Entries**", len(fm.get("stock") or [])),
    ])]
    rows = []
    for e in fm.get("stock") or []:
        if not isinstance(e, dict):
            continue
        sale = ""
        if e.get("sale"):
            import datetime
            sale = " – ".join(datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d") for t in e["sale"])
        rows.append((e.get("entry"), _econ.item_icon(ctx, e.get("item", 0)), _econ.item_link(ctx, e.get("item", 0)),
                     fmt_num(e.get("price", 0)), e.get("discount", 0),
                     "%s (%s)" % (TABS.get(e.get("tab"), "?"), e.get("tab")), e.get("c10"), sale))
    L += ["### Catalogue", "",
          "`tab` is the `PrimiumShop` column the decoder calls `currency?@18`; its values 1–3 line up "
          "with the mall's filter tabs Item / Costume / Convenience (`GUI_Herobind_ShopFilter_1..3`) "
          "and with what each row sells (*inferred*). `c10` (@10: 0, 10, 25 or 50) is unknown; the "
          "decoder guesses a discount, but the contract reads the discount from @14 (all 0).", "",
          table_md(["entry", "", "item", "price", "discount %", "tab", "c10", "on sale (UTC)"], rows)]
    L += ["### Seen in", ""] + _econ.refs_md(_econ.gameplay_refs(r"Shop Mall|Cash Mall|cash shop|PrimiumShop")) + [""]
    return "\n".join(L)


# ------------------------------------------------------------------ expansion

def expansion(ctx):
    steps = []
    for r in ctx.table("ExpandSlot"):
        steps.append({"step": r.int("step"),
                      "bag": {"currency": r.int("currency1"), "amount": r.int("cost1")},
                      "warehouse": {"currency": r.int("currency2"), "amount": r.int("cost2")},
                      "cost3": r.int("cost3")})
    f = {"steps": steps,
         "observed_prices": [{"what": "bag step 5", "shown": 5000, "currency": "Gold",
                              "source": "docs: [[gameplay/video-character-creation-and-tutorial]] 16:20 "
                                        "(lesson 706 'Expand your Inventory': 'Gold : 5000')"}]}
    sources = ["client: ExpandSlot.cdb", "contract: items.yaml expand_capacity 0x47f, server_rules capacity",
               "docs: [[gameplay/video-character-creation-and-tutorial]] 16:20"]
    return Page(TYPE, EXPANSION, ctx.title(TYPE, EXPANSION), fields=f, sources=sources,
                body=expansion_body, required=["steps"])


def expansion_body(ctx, page):
    fm = page.fm
    L = [table_md(["", ""], [
        ("**What**", "Prices of each extra row (5 slots) of the bag and the personal warehouse"),
        ("**Packet**", "C->S / S->C `0x47f` {container 1 bag / 6 warehouse, step} (contract `expand_capacity`)"),
        ("**Limits**", "bag up to 14 rows, warehouse up to 18 (contract `capacity`)"),
    ])]
    rows = []
    for s in fm.get("steps") or []:
        if not isinstance(s, dict):
            continue
        b, w = s.get("bag") or {}, s.get("warehouse") or {}
        rows.append((s.get("step"),
                     "%s %s" % (fmt_num(b.get("amount", 0)), _econ.currency_name(b.get("currency", 0))) if b.get("currency") else "–",
                     "%s %s" % (fmt_num(w.get("amount", 0)), _econ.currency_name(w.get("currency", 0))) if w.get("currency") else "–",
                     fmt_num(s.get("cost3", 0))))
    L += ["### Steps", "",
          "Currency 2 = gold, 13 = jewels (yellow then purple, contract `jewels`). `cost3` (@14) is "
          "unknown: it rises 1,000,000 → 50,000,000 and is 0 from step 9.", "",
          table_md(["step (row)", "bag", "warehouse", "cost3"], rows)]
    obs = [o for o in fm.get("observed_prices") or [] if isinstance(o, dict)]
    if obs:
        L += ["### Seen in play", ""] + ["- %s: %s %s (%s)" % (o.get("what"), fmt_num(o.get("shown", 0)),
                                                               o.get("currency"), o.get("source", "").replace("docs: ", ""))
                                         for o in obs] + [""]
    L += ["### Seen in", ""] + _econ.refs_md(_econ.gameplay_refs(
        r"ExpandSlot|Expand your Inventory|slot prices|warehouse expansion|Expanding asked")) + [""]
    return "\n".join(L)


# ------------------------------------------------------------------- NPC shops

def body(ctx, page):
    fm, sid = page.fm, page.id
    L, info = [], []
    npcs = [u for u in fm.get("npc") or [] if isinstance(u, int)]
    img = next((ctx.image(ctx.unit_type(u), u) for u in npcs if ctx.image(ctx.unit_type(u), u)), None)
    if img:
        info.append(("", "![%s](%s)" % (common.link_text(page.title), img)))
    info.append(("Shop id", "`%d` (`Npc_Carry` shop_id = `UnitDB` u16@a2)" % sid))
    if npcs:
        info.append(("Run by", ", ".join("%s%s" % (ctx.unit_link(u), " (%s)" % _econ.unit_role(ctx, u)
                                                     if _econ.unit_role(ctx, u) else "") for u in npcs)))
    else:
        info.append(("Run by", "no unit in `UnitDB` opens this shop"))
    stock = [e for e in fm.get("stock") or [] if isinstance(e, dict)]
    info.append(("Stock", "%d entries, %d distinct items" % (len(stock), len({e.get('item') for e in stock}))))
    rates = fm.get("price_rates") or {}
    if rates:
        info.append(("Price rates", "buy %s %%, sell %s %% (0x452)" % (rates.get("buy_rate"), rates.get("sell_rate"))))
    hdr = fm.get("header") or {}
    if hdr:
        info.append(("Header", ", ".join("`%s` = %s" % kv for kv in hdr.items()) + " (meaning unknown)"))
    L.append(table_md(["", ""], [(("**%s**" % k) if k else "", v) for k, v in info]))

    if not npcs:
        L += ["> [!note]", "> No NPC in the client opens this shop, so players could not reach it unless "
              "the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).", ""]

    prices = {p.get("item"): p for p in fm.get("prices") or [] if isinstance(p, dict)}
    rows = []
    for e in stock:
        it = e.get("item", 0)
        p = prices.get(it) or {}
        rows.append((e.get("slot"), _econ.item_icon(ctx, it), _econ.item_link(ctx, it),
                     e.get("count"), e.get("p1") or "", p.get("currency_name", "–"),
                     fmt_num(p["base"]) if "base" in p else "–",
                     fmt_num(p["buy"]) if p.get("buy") is not None else "–",
                     fmt_num(p["sell"]) if p.get("sell") is not None else "–"))
    L += ["### Stock", "",
          "`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). "
          "*Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at "
          "this page's `price_rates` (client formula, see below). `p1` is the enchant level for "
          "weapons/armour or the dye colour for costumes.", "",
          table_md(["slot", "", "item", "count", "p1", "currency", "base", "buy", "sell"], rows)]
    dup = len(stock) - len({e.get("item") for e in stock})
    if dup:
        L += ["%d entries repeat an item already listed (the client shows every entry)." % dup, ""]
    pairs = [p for p in prices.values() if p.get("cost_pair")]
    if pairs:
        L += ["Second price (`Item_Base` cost pair @24/@26, charged as listed). The patch notes price "
              "Amplifying Passion at \"5 silver **or** 3 gold medals\" "
              "([[gameplay/reinforce-and-runes|runes]] §5), so this is probably an alternative way to "
              "pay, not an extra charge (*guess*): " + "; ".join(
            "%s: %s %s" % (ctx.link("items", p["item"]), fmt_num(p["cost_pair"].get("amount", 0)),
                           p["cost_pair"].get("currency_name")) for p in pairs), ""]

    obs = [o for o in fm.get("observed_prices") or [] if isinstance(o, dict)]
    if obs:
        orows = []
        for o in obs:
            p = prices.get(o.get("item")) or {}
            calc = p.get("buy")
            if calc is None:
                match = "?"
            elif calc != o.get("shown"):
                match = "no"
            elif str(o.get("currency", "")).lower() != str(p.get("currency_name", "")).lower() \
                    and "mithril" not in str(o.get("currency", "")).lower():
                match = "amount only (currency differs)"
            else:
                match = "yes"
            orows.append((_econ.item_link(ctx, o.get("item", 0)), "%s %s" % (fmt_num(o.get("shown", 0)), o.get("currency", "")),
                          fmt_num(calc) if calc is not None else "–", match, o.get("note", "")))
        L += ["### Prices seen in play", "",
              "Source: " + "; ".join(sorted({o.get("source", "").replace("docs: ", "") for o in obs})), "",
              table_md(["item", "shown", "formula", "match", "note"], orows)]

    L += ["### How prices are worked out", "",
          "The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` "
          "buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell "
          "prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; "
          "medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come "
          "from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** "
          "base ([[gameplay/progression-and-economy|economy]] §4, "
          "[[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and "
          "sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).", ""]

    refs = _econ.gameplay_refs(r"(?:shops?|Npc_Carry`?)\s+(?:\d{1,3}\s*(?:/|,|and|or)\s*)*%d\b" % sid)
    if refs:
        L += ["### Seen in", ""] + _econ.refs_md(refs) + [""]
    return "\n".join(L)

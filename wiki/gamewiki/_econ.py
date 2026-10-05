"""Shared helpers for the economy modules (shops, gacha, boxes, recipes,
upgrades). Private: the leading underscore keeps it out of entity_modules().

* currency names and the client's shop price formula (contract/items.yaml
  server_rules.price_formula) with the price rates observed in play
  (docs/gameplay/progression-and-economy.md §4, video-tutorial-walkthrough),
* gameplay_refs(): lines of the hand-written docs/gameplay pages that match a
  pattern, with the first video timestamp on the line, so a generated block
  can say "Seen in [[gameplay/x|X]] at 14:20".
"""
import re

from . import common
from .common import parse_front_matter

# Item_Base buy_currency codes. items.CURRENCIES is the reference; 13 is the
# ExpandSlot / gacha code for "jewels" (yellow + purple, contract jewels rule)
# and 16 pays the [Mithril] Medal Reward Box (guide: "1 mithril", so probably
# the Mithril medal -- *guess*).
def currency_name(code):
    from .items import CURRENCIES
    if code == 13:
        return "Jewels (yellow + purple)"
    if code == 16:
        return "currency 16 (Mithril medal?)"
    return CURRENCIES.get(code, "currency %d" % code)


# ------------------------------------------------------------ price formula
# contract/items.yaml server_rules.price_formula (FUN_004e0603 buy,
# FUN_004e06b5 sell): rates are percent values sent in S->C 0x452.
RAW_CODES = {9, 10, 11, 12, 15, 16}            # medals etc.: price as listed
SCALE = [100, 150, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]

# Observed in the 2018 game: gold items sold at 7.92 x base, bought back at
# 6.3 x base (docs/gameplay/progression-and-economy.md §4; video-tutorial-
# walkthrough 14:20). Under the client formula that is buy_rate 720 (+10 %)
# and sell_rate 700 (-10 %): *inferred*.
OBSERVED_RATES = {"buy_rate": 720, "sell_rate": 700,
                  "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under "
                           "contract price_formula; multipliers observed in 2018 play"}
RATE_SOURCES = [
    "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)",
    "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)",
    "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)",
]


def _rate(base, rate, tier=0):
    return SCALE[min(max(tier, 0), 9)] * (base // 100) // 100 * rate + (base % 100) * rate // 100


def buy_price(base, code, rate=720, tier=0):
    """Price the shop window shows for one unit (client formula)."""
    if code in RAW_CODES:
        return base
    if code == 17:                     # Dimensional Energy: +10 % only
        return base * 11 // 10
    return _rate(base, rate, tier) * 11 // 10


def sell_price(base, code, rate=700, tier=0):
    if code in RAW_CODES:
        return base
    if code == 17:
        return base * 81 // 100
    return _rate(base, rate, tier) * 9 // 10


def item_price(ctx, item, rates=None, tier=0):
    """{'item', 'currency', 'currency_name', 'base', 'buy', 'sell'} or None
    when the item is not in Item_Base."""
    rates = rates or OBSERVED_RATES
    r = ctx.table("Item_Base").get(item)
    if r is None:
        return None
    cur, base = r.int("buy_currency"), r.int("buy_price")
    out = {"item": item, "currency": cur, "currency_name": currency_name(cur), "base": base,
           "buy": buy_price(base, cur, rates.get("buy_rate", 720), tier),
           "sell": sell_price(base, cur, rates.get("sell_rate", 700), tier)}
    if r.int("c15") & 2 or cur in RAW_CODES or cur == 18:
        out["sell"] = None             # no-sell flag / medal and fame items (CantSellFameItem)
    pc, pa = r.int("sell_currency"), r.int("sell_price")
    if (pc, pa) != (cur, base) and (pc or pa):
        out["cost_pair"] = {"currency": pc, "currency_name": currency_name(pc), "amount": pa}
    return out


# ------------------------------------------------------- gameplay references

_DOCS = None


def _docs():
    global _DOCS
    if _DOCS is None:
        _DOCS = []
        for f in sorted((common.DOCS / "gameplay").glob("*.md")):
            fm, body = parse_front_matter(f.read_text(encoding="utf-8"))
            _DOCS.append(("gameplay/" + f.stem, str(fm.get("title") or f.stem), body.split("\n")))
    return _DOCS


TS_LINK = re.compile(r"\[(\d{1,2}:\d{2}(?::\d{2})?)\]\(https?://[^)]*(?:youtube|youtu\.be)")
TS_PARAM = re.compile(r"youtu[^)\s]*[?&]t=(\d+)s?")


def _timestamp(line):
    m = TS_LINK.search(line)
    if m:
        return m.group(1)
    m = TS_PARAM.search(line)
    if m:
        s = int(m.group(1))
        return "%d:%02d" % (s // 60, s % 60) if s < 3600 else "%d:%02d:%02d" % (s // 3600, s // 60 % 60, s % 60)
    return None


def _section(lines, i):
    for j in range(i, -1, -1):
        m = re.match(r"#{2,4} (.*)", lines[j])
        if m:
            return m.group(1).strip()
    return None


def gameplay_refs(pattern, flags=re.I, limit=3):
    """[(page, title, section, [timestamps])] of gameplay lines matching
    ``pattern`` (one entry per page, up to ``limit`` timestamps)."""
    rx = re.compile(pattern, flags)
    out = []
    for page, title, lines in _docs():
        hits, ts, sec = 0, [], None
        for i, line in enumerate(lines):
            if rx.search(line):
                hits += 1
                if sec is None:
                    sec = _section(lines, i)
                t = _timestamp(line)
                if t and t not in ts and len(ts) < limit:
                    ts.append(t)
        if hits:
            out.append((page, title, sec, ts))
    return out


def refs_md(refs, lead="Seen in"):
    """Markdown bullet lines for gameplay_refs() results."""
    out = []
    for page, title, sec, ts in refs:
        s = "%s [[%s|%s]]" % (lead, page, common.link_text(title))
        if sec:
            s += ", section *%s*" % common.link_text(sec)
        if ts:
            s += " at " + ", ".join(ts)
        out.append("- " + s)
    return out


# ---------------------------------------------------------------- shop NPCs

def shop_npcs(ctx):
    """{Npc_Carry shop id: [UnitDB ids]} (UnitDB u16@a2)."""
    if getattr(ctx, "_shop_npcs", None) is None:
        out = {}
        for u in ctx.table("UnitDB"):
            if u.int("u16@a2"):
                out.setdefault(u.int("u16@a2"), []).append(u.int("id"))
        ctx._shop_npcs = out
    return ctx._shop_npcs


def unit_role(ctx, uid):
    """UnitDB str@40 is the role line ('UnitName_204' = 'Merchant'); name_key
    is the person ('TitleName_3' = 'Wren')."""
    r = ctx.table("UnitDB").get(uid)
    return ctx.s(r.get("str@40")) if r is not None else None


def item_link(ctx, item, count=None):
    """Item link with icon; plain text for codes not in Item_Base."""
    if ctx.table("Item_Base").get(item) is None:
        return "item %d (not in `Item_Base`)" % item
    s = ctx.link("items", item)
    if count not in (None, 0, 1):
        s += " × %s" % common.fmt_num(count)
    return s


def item_icon(ctx, item):
    img = ctx.image("items", item)
    return "![](%s)" % img if img else ""


def kind_name(ctx, item):
    """'Weapon (31)' for an item id, from ItemKind; '–' if unknown."""
    r = ctx.table("Item_Base").get(item)
    if r is None:
        return "–"
    if getattr(ctx, "_kind_names", None) is None:
        ctx._kind_names = {k.int("kind"): (k.get("name") or "").strip() for k in ctx.table("ItemKind")}
    k = r.int("kind")
    return "%s (%d)" % (ctx._kind_names.get(k) or "?", k)

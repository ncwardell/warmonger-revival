"""NPC shops: price rates, buy, sell and buyback, from the committed wiki.

Wire layouts: contract/items.yaml 0x452, 0x430, 0x431, 0x4b7..0x4b9 and the
server_rules price_formula / shop_stock / buyback. The client opens a shop
locally from its own Npc_Carry row (NPC menu function 1) and sends no packet;
the server validates each request against the same row on the shop's wiki
page and charges the client's own formula (wiki/gamewiki/_econ.py).

Only gold-priced stock without grade bytes is sold here. Medal, fame and
Dimensional Energy currencies, and stock rows with p1/p2 set, are refused.
The buyback list is per connection and not saved: a test-server policy.
"""
import copy
import math
import struct

import gamedata
import loot
import sessions
import skills
import world
from proto import build
from wiki.gamewiki import _econ

GOLD = 2  # Item_Base buy currency code
SHOP_FUNCTION = 1  # NPC menu function "Shop" (UnitDB +0x8c..+0x8e)
INTERACT_RADIUS = 15.0  # as quests.near_npc; a server choice
BUYBACK_SIZE = 16
MSG_NOT_ENOUGH_MONEY = 52
MSG_QUEST_ITEM = 144
MSG_NO_SELL = 146


def _rates():
    """The one buy/sell percent pair the shop pages carry (sent in 0x452)."""
    pairs = {(page["price_rates"]["buy_rate"], page["price_rates"]["sell_rate"])
             for page in gamedata.pages("shops").values() if page.get("price_rates")}
    if len(pairs) != 1:
        raise ValueError(f"expected one shop price_rates pair on the wiki, got {sorted(pairs)}")
    buy, sell = pairs.pop()
    return gamedata.integer(buy, 1, 100000), gamedata.integer(sell, 1, 100000)


BUY_RATE, SELL_RATE = _rates()


def rates():
    """S->C 0x452 {buy_rate, sell_rate, sysmsg 0}; the client starts at 1 %."""
    return build(0x452, struct.pack("<IIi", BUY_RATE, SELL_RATE, 0))


def shop_of(npc_uid):
    """The wiki shop page behind a nearby shop NPC, or None."""
    u = world.UNITS.get(npc_uid)
    p = sessions.current().player
    if (u is None or world.is_monster(u) or not world.visible(u)
            or math.hypot(p["x"] - u.x, p["z"] - u.z) > INTERACT_RADIUS):
        return None
    npc = gamedata.pages("npcs").get(u.unit_id) or {}
    if not any(f.get("code") == SHOP_FUNCTION for f in npc.get("functions") or []):
        return None
    return gamedata.pages("shops").get(npc.get("shop"))


def gold_price(code):
    """(base buy price, item page) for a plain gold-priced item, else None."""
    page = gamedata.pages("items").get(code)
    if page is None:
        return None
    price = page.get("price") or {}
    pair = page.get("cost_pair") or []
    if price.get("currency") != GOLD or type(price.get("buy")) is not int or price["buy"] < 0:
        return None
    if any((c.get("currency"), c.get("amount")) != (GOLD, price["buy"]) for c in pair):
        return None  # a second cost the client also checks; not supported
    return price["buy"], page


def _transaction(change):
    """Run change() on a copy of the bag; keep it only if it returns a reply."""
    s = sessions.current()
    original, gold = s.inventory, s.loot["gold"]
    s.inventory = copy.deepcopy(original)
    try:
        out = change()
    finally:
        if not out:
            s.inventory, s.loot["gold"] = original, gold
    return out


def buy(packet):
    """C->S 0x430 {npc uid, shop index, quantity, item code, client rate}."""
    s = sessions.current()
    npc, index, quantity, code = struct.unpack_from("<HHHH", packet, 0x10)
    shop = shop_of(npc) if s.player["alive"] else None
    entry = next((e for e in (shop or {}).get("stock") or [] if e["slot"] == index), None)
    priced = gold_price(code)
    if (entry is None or entry["item"] != code or entry.get("p1") or entry.get("p2")
            or not priced or not 1 <= quantity <= loot.STACK_MAX):
        return None
    total = _econ.buy_price(priced[0], GOLD, BUY_RATE) * quantity
    if total > s.loot["gold"]:
        return loot.system_message(MSG_NOT_ENOUGH_MONEY)

    def change():
        touched, left = loot.add_to_bag(code, quantity)
        if left:
            return None
        s.loot["gold"] -= total
        return loot.gold_update() + b"".join(loot.slot_update(i) for i in touched)
    return _transaction(change) or loot.system_message(loot.MSG_INVENTORY_FULL)


def sell(packet):
    """C->S 0x431 {container 1, slot, npc uid, item code, quantity, client rate}."""
    s = sessions.current()
    container, slot = packet[0x10], packet[0x11]
    npc, code, quantity = struct.unpack_from("<HHH", packet, 0x12)
    bag, counts = s.inventory["bag"], s.inventory["count"]
    if (container != skills.BAG or slot >= skills.BAG_SLOTS or not s.player["alive"]
            or not code or bag[slot] != code or not 1 <= quantity <= (counts[slot] or 1)
            or shop_of(npc) is None):
        return None
    page = gamedata.pages("items").get(code) or {}
    if page.get("kind_name") in ("Quest", "Quest precept"):
        return loot.system_message(MSG_QUEST_ITEM)
    priced = gold_price(code)
    if priced is None or page.get("no_sell"):
        return loot.system_message(MSG_NO_SELL)
    left = (counts[slot] or 1) - quantity
    bag[slot], counts[slot] = (code, left) if left else (0, 0)
    s.loot["gold"] = min(0xFFFFFFFF, s.loot["gold"] + _econ.sell_price(priced[0], GOLD, SELL_RATE) * quantity)
    sold = getattr(s, "buyback", [])
    s.buyback = ([(code, quantity)] + sold)[:BUYBACK_SIZE]
    return loot.slot_update(slot, reason=0) + loot.gold_update()


def buyback_list(_packet=None):
    """C->S 0x4b7 -> S->C 0x4b8 {rate 0 = keep, 16 item records}."""
    s = sessions.current()
    records = b"".join(skills.item(c, n) for c, n in getattr(s, "buyback", []))
    return build(0x4B8, struct.pack("<I", 0) + records.ljust(BUYBACK_SIZE * skills.ITEM_SIZE, b"\0"),
                 extra=s.uid)


def buy_back(packet):
    """C->S 0x4b9 {index, client rate, item record}: charge the buy price."""
    s = sessions.current()
    index = struct.unpack_from("<H", packet, 0x10)[0]
    sold = getattr(s, "buyback", [])
    if not s.player["alive"] or index >= len(sold):
        return None
    code, count = sold[index]
    if packet[0x18:0x28] != skills.item(code, count):
        return None
    priced = gold_price(code)
    if priced is None:
        return None
    total = _econ.buy_price(priced[0], GOLD, BUY_RATE) * count
    if total > s.loot["gold"]:
        return loot.system_message(MSG_NOT_ENOUGH_MONEY)

    def change():
        touched, left = loot.add_to_bag(code, count)
        if left:
            return None
        s.loot["gold"] -= total
        s.buyback = sold[:index] + sold[index + 1:]
        return loot.gold_update() + b"".join(loot.slot_update(i, reason=0) for i in touched)
    out = _transaction(change)
    return out + buyback_list() if out else loot.system_message(loot.MSG_INVENTORY_FULL)


REPLIES = {0x430: buy, 0x431: sell, 0x4B7: buyback_list, 0x4B9: buy_back}

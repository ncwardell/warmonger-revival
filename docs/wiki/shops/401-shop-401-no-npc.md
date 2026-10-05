---
title: "Shop 401 (no NPC)"
type: "shop"
id: 401
status: "partial"
missing: ["npc"]
sources: ["client: Npc_Carry.cdb shop 401", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)", "client: [[gameplay/consumables]] §3 (Drop Chance Potion 764 in Npc_Carry list 401)"]
npc: []
stock:
  - {"slot": 0, "item": 700, "count": 25, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 701, "count": 25, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 854, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 854, "count": 4, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 855, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 857, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 856, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 856, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 1012, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 702, "count": 25, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 855, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 905, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 764, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 1100, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 703, "count": 25, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 1930, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 16, "item": 1931, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 17, "item": 1932, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 18, "item": 1933, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 19, "item": 1934, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 20, "item": 1935, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 21, "item": 1935, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 22, "item": 857, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 23, "item": 1012, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 24, "item": 703, "count": 25, "p1": 0, "p2": 0}
prices:
  - {"item": 700, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63, "cost_pair": {"currency": 18, "currency_name": "Fame", "amount": 10}}
  - {"item": 701, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126, "cost_pair": {"currency": 18, "currency_name": "Fame", "amount": 50}}
  - {"item": 854, "currency": 10, "currency_name": "Bronze Medal", "base": 2, "buy": 2, "sell": null}
  - {"item": 855, "currency": 10, "currency_name": "Bronze Medal", "base": 5, "buy": 5, "sell": null}
  - {"item": 857, "currency": 12, "currency_name": "Gold Medal", "base": 5, "buy": 5, "sell": null, "cost_pair": {"currency": 11, "currency_name": "Silver Medal", "amount": 5}}
  - {"item": 856, "currency": 11, "currency_name": "Silver Medal", "base": 5, "buy": 5, "sell": null}
  - {"item": 1012, "currency": 2, "currency_name": "Gold", "base": 0, "buy": 0, "sell": 0}
  - {"item": 702, "currency": 2, "currency_name": "Gold", "base": 40, "buy": 316, "sell": 252}
  - {"item": 905, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63}
  - {"item": 764, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63}
  - {"item": 1100, "currency": 16, "currency_name": "currency 16 (Mithril medal?)", "base": 1, "buy": 1, "sell": null}
  - {"item": 703, "currency": 2, "currency_name": "Gold", "base": 80, "buy": 633, "sell": 504}
  - {"item": 1930, "currency": 2, "currency_name": "Gold", "base": 500, "buy": 3960, "sell": 3150}
  - {"item": 1931, "currency": 2, "currency_name": "Gold", "base": 500, "buy": 3960, "sell": 3150}
  - {"item": 1932, "currency": 2, "currency_name": "Gold", "base": 500, "buy": 3960, "sell": 3150}
  - {"item": 1933, "currency": 2, "currency_name": "Gold", "base": 500, "buy": 3960, "sell": 3150}
  - {"item": 1934, "currency": 2, "currency_name": "Gold", "base": 500, "buy": 3960, "sell": 3150}
  - {"item": 1935, "currency": 2, "currency_name": "Gold", "base": 500, "buy": 3960, "sell": 3150}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=18810e type=ffcf9c id=63b4f9 sources=46b969 npc=97d170 stock=04dcf3 prices=5fe4ab price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
| **Shop id** | `401` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | no unit in `UnitDB` opens this shop |
| **Stock** | 25 entries, 18 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 1, `c3` = 1, `c4` = 4 (meaning unknown) |

> [!note]
> No NPC in the client opens this shop, so players could not reach it unless the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](../assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 25 |  | Gold | 10 | 79 | 63 |
| 1 | ![](../assets/items/701.png) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] | 25 |  | Gold | 20 | 158 | 126 |
| 2 | ![](../assets/items/854.png) | [[wiki/items/854-shining-passion\|Shining Passion]] | 2 |  | Bronze Medal | 2 | 2 | – |
| 3 | ![](../assets/items/854.png) | [[wiki/items/854-shining-passion\|Shining Passion]] | 4 |  | Bronze Medal | 2 | 2 | – |
| 4 | ![](../assets/items/855.png) | [[wiki/items/855-mysterious-passion\|Mysterious Passion]] | 1 |  | Bronze Medal | 5 | 5 | – |
| 5 | ![](../assets/items/857.png) | [[wiki/items/857-amplifying-passion\|Amplifying Passion]] | 1 |  | Gold Medal | 5 | 5 | – |
| 6 | ![](../assets/items/856.png) | [[wiki/items/856-brilliant-passion\|Brilliant Passion]] | 1 |  | Silver Medal | 5 | 5 | – |
| 7 | ![](../assets/items/856.png) | [[wiki/items/856-brilliant-passion\|Brilliant Passion]] | 2 |  | Silver Medal | 5 | 5 | – |
| 8 | ![](../assets/items/1012.png) | [[wiki/items/1012-shaia-stone\|Shaia Stone]] | 1 |  | Gold | 0 | 0 | 0 |
| 9 | ![](../assets/items/702.png) | [[wiki/items/702-crystal-red\|Crystal : Red]] | 25 |  | Gold | 40 | 316 | 252 |
| 10 | ![](../assets/items/855.png) | [[wiki/items/855-mysterious-passion\|Mysterious Passion]] | 3 |  | Bronze Medal | 5 | 5 | – |
| 11 | ![](../assets/items/905.png) | [[wiki/items/905-blessing-of-shaia\|Blessing of Shaia]] | 1 |  | Gold | 10 | 79 | 63 |
| 12 | ![](../assets/items/764.png) | [[wiki/items/764-drop-chance-potion\|Drop Chance Potion]] | 1 |  | Gold | 10 | 79 | 63 |
| 13 | ![](../assets/items/1100.png) | [[wiki/items/1100-reinforcing-adjuvants\|Reinforcing adjuvants]] | 1 |  | currency 16 (Mithril medal?) | 1 | 1 | – |
| 14 | ![](../assets/items/703.png) | [[wiki/items/703-crystal-black\|Crystal : Black]] | 25 |  | Gold | 80 | 633 | 504 |
| 15 | ![](../assets/items/1930.png) | [[wiki/items/1930-essence-of-darkness\|essence of Darkness]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 16 | ![](../assets/items/1931.png) | [[wiki/items/1931-essence-of-wind\|Essence of Wind]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 17 | ![](../assets/items/1932.png) | [[wiki/items/1932-essence-of-fire\|Essence of Fire]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 18 | ![](../assets/items/1933.png) | [[wiki/items/1933-essence-of-water\|Essence of Water]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 19 | ![](../assets/items/1934.png) | [[wiki/items/1934-essence-of-earth\|Essence of Earth]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 20 | ![](../assets/items/1935.png) | [[wiki/items/1935-essence-of-light\|Essence of Light]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 21 | ![](../assets/items/1935.png) | [[wiki/items/1935-essence-of-light\|Essence of Light]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 22 | ![](../assets/items/857.png) | [[wiki/items/857-amplifying-passion\|Amplifying Passion]] | 2 |  | Gold Medal | 5 | 5 | – |
| 23 | ![](../assets/items/1012.png) | [[wiki/items/1012-shaia-stone\|Shaia Stone]] | 1 |  | Gold | 0 | 0 | 0 |
| 24 | ![](../assets/items/703.png) | [[wiki/items/703-crystal-black\|Crystal : Black]] | 25 |  | Gold | 80 | 633 | 504 |

7 entries repeat an item already listed (the client shows every entry).

Second price (`Item_Base` cost pair @24/@26, charged as listed). The patch notes price Amplifying Passion at "5 silver **or** 3 gold medals" ([[gameplay/reinforce-and-runes|runes]] §5), so this is probably an alternative way to pay, not an extra charge (*guess*): [[wiki/items/700-crystal-blue|Crystal : Blue]]: 10 Fame; [[wiki/items/701-crystal-yellow|Crystal : Yellow]]: 50 Fame; [[wiki/items/857-amplifying-passion|Amplifying Passion]]: 5 Silver Medal

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).
<!-- generated:end -->

## Notes

This list holds the Drop Chance Potion (764, +40 % item drop chance for 1 h, base 10 gold) (*client*, [[gameplay/consumables|consumables]] §3). No NPC opens it. In the client, the potion is sold in the [[wiki/shops/1000-cash-mall|Cash Mall]] (entry 30).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/consumables]] §3 (Drop Chance Potion 764 in Npc_Carry list 401) (*client*)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

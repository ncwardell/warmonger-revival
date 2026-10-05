---
title: "Shop 225 (no NPC)"
type: "shop"
id: 225
status: "stub"
missing: ["npc"]
sources: ["client: Npc_Carry.cdb shop 225", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: []
stock:
  - {"slot": 1, "item": 816, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 814, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 812, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 810, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 808, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 806, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 804, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 802, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 808, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 806, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 804, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 802, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 16, "item": 808, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 17, "item": 806, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 18, "item": 804, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 19, "item": 802, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 21, "item": 808, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 22, "item": 806, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 23, "item": 804, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 24, "item": 802, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 816, "currency": 2, "currency_name": "Gold", "base": 30, "buy": 237, "sell": 189}
  - {"item": 814, "currency": 2, "currency_name": "Gold", "base": 30, "buy": 237, "sell": 189}
  - {"item": 812, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 810, "currency": 2, "currency_name": "Gold", "base": 40, "buy": 316, "sell": 252}
  - {"item": 808, "currency": 2, "currency_name": "Gold", "base": 30, "buy": 237, "sell": 189}
  - {"item": 806, "currency": 2, "currency_name": "Gold", "base": 40, "buy": 316, "sell": 252}
  - {"item": 804, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 802, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=46c9c9 type=ffcf9c id=cfe21c sources=6571a2 npc=97d170 stock=1ab8fc prices=60c0b1 price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
| **Shop id** | `225` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | no unit in `UnitDB` opens this shop |
| **Stock** | 20 entries, 8 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 1, `c3` = 1, `c4` = 4 (meaning unknown) |

> [!note]
> No NPC in the client opens this shop, so players could not reach it unless the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 1 | ![](wiki/assets/items/816.png) | [[wiki/items/816-onyx\|Onyx]] | 1 |  | Gold | 30 | 237 | 189 |
| 2 | ![](wiki/assets/items/814.png) | [[wiki/items/814-topaz\|Topaz]] | 1 |  | Gold | 30 | 237 | 189 |
| 3 | ![](wiki/assets/items/812.png) | [[wiki/items/812-red-bloodstone\|Red bloodstone]] | 1 |  | Gold | 20 | 158 | 126 |
| 4 | ![](wiki/assets/items/810.png) | [[wiki/items/810-diamond\|Diamond]] | 1 |  | Gold | 40 | 316 | 252 |
| 6 | ![](wiki/assets/items/808.png) | [[wiki/items/808-moonstone\|Moonstone]] | 1 |  | Gold | 30 | 237 | 189 |
| 7 | ![](wiki/assets/items/806.png) | [[wiki/items/806-emerald\|Emerald]] | 1 |  | Gold | 40 | 316 | 252 |
| 8 | ![](wiki/assets/items/804.png) | [[wiki/items/804-blue-bloodstone\|Blue bloodstone]] | 1 |  | Gold | 20 | 158 | 126 |
| 9 | ![](wiki/assets/items/802.png) | [[wiki/items/802-garnet\|Garnet]] | 1 |  | Gold | 20 | 158 | 126 |
| 11 | ![](wiki/assets/items/808.png) | [[wiki/items/808-moonstone\|Moonstone]] | 1 |  | Gold | 30 | 237 | 189 |
| 12 | ![](wiki/assets/items/806.png) | [[wiki/items/806-emerald\|Emerald]] | 1 |  | Gold | 40 | 316 | 252 |
| 13 | ![](wiki/assets/items/804.png) | [[wiki/items/804-blue-bloodstone\|Blue bloodstone]] | 1 |  | Gold | 20 | 158 | 126 |
| 14 | ![](wiki/assets/items/802.png) | [[wiki/items/802-garnet\|Garnet]] | 1 |  | Gold | 20 | 158 | 126 |
| 16 | ![](wiki/assets/items/808.png) | [[wiki/items/808-moonstone\|Moonstone]] | 1 |  | Gold | 30 | 237 | 189 |
| 17 | ![](wiki/assets/items/806.png) | [[wiki/items/806-emerald\|Emerald]] | 1 |  | Gold | 40 | 316 | 252 |
| 18 | ![](wiki/assets/items/804.png) | [[wiki/items/804-blue-bloodstone\|Blue bloodstone]] | 1 |  | Gold | 20 | 158 | 126 |
| 19 | ![](wiki/assets/items/802.png) | [[wiki/items/802-garnet\|Garnet]] | 1 |  | Gold | 20 | 158 | 126 |
| 21 | ![](wiki/assets/items/808.png) | [[wiki/items/808-moonstone\|Moonstone]] | 1 |  | Gold | 30 | 237 | 189 |
| 22 | ![](wiki/assets/items/806.png) | [[wiki/items/806-emerald\|Emerald]] | 1 |  | Gold | 40 | 316 | 252 |
| 23 | ![](wiki/assets/items/804.png) | [[wiki/items/804-blue-bloodstone\|Blue bloodstone]] | 1 |  | Gold | 20 | 158 | 126 |
| 24 | ![](wiki/assets/items/802.png) | [[wiki/items/802-garnet\|Garnet]] | 1 |  | Gold | 20 | 158 | 126 |

12 entries repeat an item already listed (the client shows every entry).

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

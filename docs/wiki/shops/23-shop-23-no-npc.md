---
title: "Shop 23 (no NPC)"
type: "shop"
id: 23
status: "stub"
missing: ["npc"]
sources: ["client: Npc_Carry.cdb shop 23", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: []
stock:
  - {"slot": 2, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 16, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 17, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 18, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 19, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 20, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 21, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 22, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 23, "item": 1010, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 24, "item": 1010, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 1010, "currency": 2, "currency_name": "Gold", "base": 0, "buy": 0, "sell": 0}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=9239c8 type=ffcf9c id=d435a6 sources=e42cbf npc=97d170 stock=5749fd prices=aafff8 price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
| **Shop id** | `23` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | no unit in `UnitDB` opens this shop |
| **Stock** | 21 entries, 1 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 1, `c3` = 1, `c4` = 4 (meaning unknown) |

> [!note]
> No NPC in the client opens this shop, so players could not reach it unless the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 2 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 3 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 4 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 5 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 6 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 7 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 8 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 9 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 10 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 11 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 12 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 14 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 16 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 17 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 18 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 19 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 20 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 21 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 22 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 23 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |
| 24 | ![](wiki/assets/items/1010.png) | [[wiki/items/1010-yellow-jewel-5000\|Yellow Jewel (5000)]] | 1 |  | Gold | 0 | 0 | 0 |

20 entries repeat an item already listed (the client shows every entry).

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

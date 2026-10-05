---
title: "Shop 285 (no NPC)"
type: "shop"
id: 285
status: "stub"
missing: ["prices", "npc"]
sources: ["client: Npc_Carry.cdb shop 285", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: []
stock:
  - {"slot": 0, "item": 8651, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 8657, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 8659, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 8655, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 8650, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 8654, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 8658, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 8663, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 8653, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 8660, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 8665, "count": 1, "p1": 0, "p2": 0}
prices: []
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
---
<!-- generated:start -->
<!-- generated-keys: title=502516 type=ffcf9c id=367ac6 sources=2e6d47 npc=97d170 stock=dd6613 prices=97d170 price_rates=c44eae header=702516 -->
|  |  |
|---|---|
| **Shop id** | `285` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | no unit in `UnitDB` opens this shop |
| **Stock** | 11 entries, 11 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 0, `c3` = 1, `c4` = 0 (meaning unknown) |

> [!note]
> No NPC in the client opens this shop, so players could not reach it unless the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 |  | item 8651 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 1 |  | item 8657 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 2 |  | item 8659 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 3 |  | item 8655 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 4 |  | item 8650 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 5 |  | item 8654 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 6 |  | item 8658 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 7 |  | item 8663 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 8 |  | item 8653 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 9 |  | item 8660 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 10 |  | item 8665 (not in `Item_Base`) | 1 |  | – | – | – | – |

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

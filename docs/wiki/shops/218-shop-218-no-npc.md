---
title: "Shop 218 (no NPC)"
type: "shop"
id: 218
status: "stub"
missing: ["npc"]
sources: ["client: Npc_Carry.cdb shop 218", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: []
stock:
  - {"slot": 0, "item": 1900, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 1900, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 1900, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 1900, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 1900, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 695, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 696, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 1900, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 695, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 696, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 1900, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 695, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 696, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 16, "item": 1900, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 17, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 18, "item": 695, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 19, "item": 696, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 20, "item": 1900, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 21, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 22, "item": 695, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 23, "item": 696, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 24, "item": 1900, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 25, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 26, "item": 695, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 27, "item": 696, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 28, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 29, "item": 695, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 1900, "currency": 2, "currency_name": "Gold", "base": 50, "buy": 396, "sell": 315}
  - {"item": 694, "currency": 2, "currency_name": "Gold", "base": 200, "buy": 1584, "sell": 1260}
  - {"item": 695, "currency": 2, "currency_name": "Gold", "base": 400, "buy": 3168, "sell": 2520}
  - {"item": 696, "currency": 2, "currency_name": "Gold", "base": 800, "buy": 6336, "sell": 5040}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=4ecda0 type=ffcf9c id=3d5bdf sources=4a67d5 npc=97d170 stock=37ea83 prices=272400 price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
| **Shop id** | `218` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | no unit in `UnitDB` opens this shop |
| **Stock** | 30 entries, 4 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 1, `c3` = 1, `c4` = 4 (meaning unknown) |

> [!note]
> No NPC in the client opens this shop, so players could not reach it unless the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 3 |  | Gold | 50 | 396 | 315 |
| 1 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 3 |  | Gold | 50 | 396 | 315 |
| 2 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 3 |  | Gold | 50 | 396 | 315 |
| 3 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 3 |  | Gold | 50 | 396 | 315 |
| 4 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 3 |  | Gold | 50 | 396 | 315 |
| 5 | ![](../assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 6 | ![](../assets/items/695.png) | [[wiki/items/695-gem-stone-red\|Gem Stone : Red]] | 1 |  | Gold | 400 | 3,168 | 2,520 |
| 7 | ![](../assets/items/696.png) | [[wiki/items/696-gem-stone-black\|Gem stone : Black]] | 1 |  | Gold | 800 | 6,336 | 5,040 |
| 8 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 3 |  | Gold | 50 | 396 | 315 |
| 9 | ![](../assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 10 | ![](../assets/items/695.png) | [[wiki/items/695-gem-stone-red\|Gem Stone : Red]] | 1 |  | Gold | 400 | 3,168 | 2,520 |
| 11 | ![](../assets/items/696.png) | [[wiki/items/696-gem-stone-black\|Gem stone : Black]] | 1 |  | Gold | 800 | 6,336 | 5,040 |
| 12 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 3 |  | Gold | 50 | 396 | 315 |
| 13 | ![](../assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 14 | ![](../assets/items/695.png) | [[wiki/items/695-gem-stone-red\|Gem Stone : Red]] | 1 |  | Gold | 400 | 3,168 | 2,520 |
| 15 | ![](../assets/items/696.png) | [[wiki/items/696-gem-stone-black\|Gem stone : Black]] | 1 |  | Gold | 800 | 6,336 | 5,040 |
| 16 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 3 |  | Gold | 50 | 396 | 315 |
| 17 | ![](../assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 18 | ![](../assets/items/695.png) | [[wiki/items/695-gem-stone-red\|Gem Stone : Red]] | 1 |  | Gold | 400 | 3,168 | 2,520 |
| 19 | ![](../assets/items/696.png) | [[wiki/items/696-gem-stone-black\|Gem stone : Black]] | 1 |  | Gold | 800 | 6,336 | 5,040 |
| 20 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 3 |  | Gold | 50 | 396 | 315 |
| 21 | ![](../assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 22 | ![](../assets/items/695.png) | [[wiki/items/695-gem-stone-red\|Gem Stone : Red]] | 1 |  | Gold | 400 | 3,168 | 2,520 |
| 23 | ![](../assets/items/696.png) | [[wiki/items/696-gem-stone-black\|Gem stone : Black]] | 1 |  | Gold | 800 | 6,336 | 5,040 |
| 24 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 3 |  | Gold | 50 | 396 | 315 |
| 25 | ![](../assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 26 | ![](../assets/items/695.png) | [[wiki/items/695-gem-stone-red\|Gem Stone : Red]] | 1 |  | Gold | 400 | 3,168 | 2,520 |
| 27 | ![](../assets/items/696.png) | [[wiki/items/696-gem-stone-black\|Gem stone : Black]] | 1 |  | Gold | 800 | 6,336 | 5,040 |
| 28 | ![](../assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 29 | ![](../assets/items/695.png) | [[wiki/items/695-gem-stone-red\|Gem Stone : Red]] | 1 |  | Gold | 400 | 3,168 | 2,520 |

26 entries repeat an item already listed (the client shows every entry).

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

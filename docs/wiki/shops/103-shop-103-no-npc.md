---
title: "Shop 103 (no NPC)"
type: "shop"
id: 103
status: "stub"
missing: ["npc"]
sources: ["client: Npc_Carry.cdb shop 103", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: []
stock:
  - {"slot": 0, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 2758, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 16, "item": 2758, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 17, "item": 2758, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 18, "item": 1932, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 19, "item": 1932, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 20, "item": 1932, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 21, "item": 1932, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 22, "item": 602, "count": 80, "p1": 0, "p2": 0}
  - {"slot": 23, "item": 2708, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 24, "item": 2708, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 25, "item": 2708, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 26, "item": 2708, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 27, "item": 2708, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 28, "item": 2708, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 29, "item": 2708, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 602, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 2758, "currency": 2, "currency_name": "Gold", "base": 500, "buy": 3960, "sell": 3150}
  - {"item": 1932, "currency": 2, "currency_name": "Gold", "base": 500, "buy": 3960, "sell": 3150}
  - {"item": 2708, "currency": 2, "currency_name": "Gold", "base": 500, "buy": 3960, "sell": 3150}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=a064b0 type=ffcf9c id=934385 sources=66e92c npc=97d170 stock=354e2d prices=6a75be price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
| **Shop id** | `103` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
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
| 0 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 1 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 2 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 3 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 4 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 5 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 6 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 7 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 8 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 9 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 10 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 11 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 12 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 13 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 14 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 15 | ![](wiki/assets/items/2758.png) | [[wiki/items/2758-the-arch-devil-akasha-s-sealed-weapon\|The Arch devil Akasha's Sealed Weapon]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 16 | ![](wiki/assets/items/2758.png) | [[wiki/items/2758-the-arch-devil-akasha-s-sealed-weapon\|The Arch devil Akasha's Sealed Weapon]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 17 | ![](wiki/assets/items/2758.png) | [[wiki/items/2758-the-arch-devil-akasha-s-sealed-weapon\|The Arch devil Akasha's Sealed Weapon]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 18 | ![](wiki/assets/items/1932.png) | [[wiki/items/1932-essence-of-fire\|Essence of Fire]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 19 | ![](wiki/assets/items/1932.png) | [[wiki/items/1932-essence-of-fire\|Essence of Fire]] | 2 |  | Gold | 500 | 3,960 | 3,150 |
| 20 | ![](wiki/assets/items/1932.png) | [[wiki/items/1932-essence-of-fire\|Essence of Fire]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 21 | ![](wiki/assets/items/1932.png) | [[wiki/items/1932-essence-of-fire\|Essence of Fire]] | 2 |  | Gold | 500 | 3,960 | 3,150 |
| 22 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 80 |  | Gold | 20 | 158 | 126 |
| 23 | ![](wiki/assets/items/2708.png) | [[wiki/items/2708-horn-of-akasha\|Horn of Akasha]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 24 | ![](wiki/assets/items/2708.png) | [[wiki/items/2708-horn-of-akasha\|Horn of Akasha]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 25 | ![](wiki/assets/items/2708.png) | [[wiki/items/2708-horn-of-akasha\|Horn of Akasha]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 26 | ![](wiki/assets/items/2708.png) | [[wiki/items/2708-horn-of-akasha\|Horn of Akasha]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 27 | ![](wiki/assets/items/2708.png) | [[wiki/items/2708-horn-of-akasha\|Horn of Akasha]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 28 | ![](wiki/assets/items/2708.png) | [[wiki/items/2708-horn-of-akasha\|Horn of Akasha]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 29 | ![](wiki/assets/items/2708.png) | [[wiki/items/2708-horn-of-akasha\|Horn of Akasha]] | 1 |  | Gold | 500 | 3,960 | 3,150 |

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

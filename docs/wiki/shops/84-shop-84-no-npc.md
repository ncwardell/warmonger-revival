---
title: "Shop 84 (no NPC)"
type: "shop"
id: 84
status: "stub"
missing: ["npc"]
sources: ["client: Npc_Carry.cdb shop 84", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: []
stock:
  - {"slot": 0, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 611, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 602, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 602, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 612, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 612, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 693, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 693, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 693, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 693, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 602, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 602, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 612, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 16, "item": 612, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 17, "item": 612, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 18, "item": 612, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 19, "item": 397, "count": 1, "p1": 0, "p2": 6}
  - {"slot": 20, "item": 398, "count": 1, "p1": 0, "p2": 7}
  - {"slot": 21, "item": 413, "count": 1, "p1": 0, "p2": 8}
  - {"slot": 22, "item": 414, "count": 1, "p1": 0, "p2": 7}
  - {"slot": 23, "item": 433, "count": 1, "p1": 0, "p2": 8}
  - {"slot": 24, "item": 434, "count": 1, "p1": 0, "p2": 7}
prices:
  - {"item": 1900, "currency": 2, "currency_name": "Gold", "base": 50, "buy": 396, "sell": 315}
  - {"item": 601, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 611, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 602, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 612, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 693, "currency": 2, "currency_name": "Gold", "base": 0, "buy": 0, "sell": 0}
  - {"item": 397, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
  - {"item": 398, "currency": 2, "currency_name": "Gold", "base": 200, "buy": 1584, "sell": 1260}
  - {"item": 413, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 414, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
  - {"item": 433, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 434, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=c17453 type=ffcf9c id=be461a sources=0acf2b npc=97d170 stock=c0c9df prices=77fe71 price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
| **Shop id** | `84` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | no unit in `UnitDB` opens this shop |
| **Stock** | 25 entries, 12 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 1, `c3` = 1, `c4` = 4 (meaning unknown) |

> [!note]
> No NPC in the client opens this shop, so players could not reach it unless the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 1 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 2 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 3 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 4 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 5 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 6 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 7 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 8 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 9 | ![](../assets/items/693.png) | [[wiki/items/693-gem-stone-blue\|Gem Stone : Blue]] | 1 |  | Gold | 0 | 0 | 0 |
| 10 | ![](../assets/items/693.png) | [[wiki/items/693-gem-stone-blue\|Gem Stone : Blue]] | 1 |  | Gold | 0 | 0 | 0 |
| 11 | ![](../assets/items/693.png) | [[wiki/items/693-gem-stone-blue\|Gem Stone : Blue]] | 1 |  | Gold | 0 | 0 | 0 |
| 12 | ![](../assets/items/693.png) | [[wiki/items/693-gem-stone-blue\|Gem Stone : Blue]] | 1 |  | Gold | 0 | 0 | 0 |
| 13 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 14 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 15 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 16 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 17 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 18 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 19 | ![](../assets/items/397.png) | [[wiki/items/397-spell-necklace\|Spell Necklace]] | 1 |  | Gold | 150 | 1,188 | 945 |
| 20 | ![](../assets/items/398.png) | [[wiki/items/398-spell-belt\|Spell Belt]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 21 | ![](../assets/items/413.png) | [[wiki/items/413-spirit-earring\|Spirit Earring]] | 1 |  | Gold | 100 | 792 | 630 |
| 22 | ![](../assets/items/414.png) | [[wiki/items/414-spirit-robe\|Spirit Robe]] | 1 |  | Gold | 150 | 1,188 | 945 |
| 23 | ![](../assets/items/433.png) | [[wiki/items/433-barrier-necklace\|Barrier Necklace]] | 1 |  | Gold | 100 | 792 | 630 |
| 24 | ![](../assets/items/434.png) | [[wiki/items/434-barrier-belt\|Barrier Belt]] | 1 |  | Gold | 150 | 1,188 | 945 |

13 entries repeat an item already listed (the client shows every entry).

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

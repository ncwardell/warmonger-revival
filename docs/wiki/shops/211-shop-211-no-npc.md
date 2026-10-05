---
title: "Shop 211 (no NPC)"
type: "shop"
id: 211
status: "stub"
missing: ["npc"]
sources: ["client: Npc_Carry.cdb shop 211", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: []
stock:
  - {"slot": 2, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 1901, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 613, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 612, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 1901, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 1901, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 1901, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 1901, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 695, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 1901, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 613, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 397, "count": 1, "p1": 0, "p2": 4}
  - {"slot": 16, "item": 398, "count": 1, "p1": 0, "p2": 4}
  - {"slot": 17, "item": 409, "count": 1, "p1": 0, "p2": 4}
  - {"slot": 18, "item": 410, "count": 1, "p1": 0, "p2": 4}
  - {"slot": 19, "item": 397, "count": 1, "p1": 0, "p2": 4}
  - {"slot": 20, "item": 398, "count": 1, "p1": 0, "p2": 8}
  - {"slot": 21, "item": 409, "count": 1, "p1": 0, "p2": 8}
  - {"slot": 22, "item": 410, "count": 1, "p1": 0, "p2": 8}
  - {"slot": 23, "item": 421, "count": 1, "p1": 0, "p2": 8}
  - {"slot": 24, "item": 422, "count": 1, "p1": 0, "p2": 8}
  - {"slot": 25, "item": 612, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 26, "item": 1901, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 27, "item": 602, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 28, "item": 603, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 29, "item": 613, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 1900, "currency": 2, "currency_name": "Gold", "base": 50, "buy": 396, "sell": 315}
  - {"item": 1901, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 613, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 612, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 694, "currency": 2, "currency_name": "Gold", "base": 200, "buy": 1584, "sell": 1260}
  - {"item": 695, "currency": 2, "currency_name": "Gold", "base": 400, "buy": 3168, "sell": 2520}
  - {"item": 397, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
  - {"item": 398, "currency": 2, "currency_name": "Gold", "base": 200, "buy": 1584, "sell": 1260}
  - {"item": 409, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 410, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
  - {"item": 421, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 422, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
  - {"item": 602, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 603, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=df5383 type=ffcf9c id=1b4a36 sources=17baa5 npc=97d170 stock=4f3293 prices=66e36f price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
| **Shop id** | `211` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | no unit in `UnitDB` opens this shop |
| **Stock** | 28 entries, 14 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 1, `c3` = 1, `c4` = 4 (meaning unknown) |

> [!note]
> No NPC in the client opens this shop, so players could not reach it unless the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 2 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 3 | ![](../assets/items/1901.png) | [[wiki/items/1901-faded-passion-piece\|Faded Passion Piece]] | 1 |  | Gold | 100 | 792 | 630 |
| 4 | ![](../assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 1 |  | Gold | 20 | 158 | 126 |
| 5 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 6 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 7 | ![](../assets/items/1901.png) | [[wiki/items/1901-faded-passion-piece\|Faded Passion Piece]] | 1 |  | Gold | 100 | 792 | 630 |
| 8 | ![](../assets/items/1901.png) | [[wiki/items/1901-faded-passion-piece\|Faded Passion Piece]] | 1 |  | Gold | 100 | 792 | 630 |
| 9 | ![](../assets/items/1901.png) | [[wiki/items/1901-faded-passion-piece\|Faded Passion Piece]] | 1 |  | Gold | 100 | 792 | 630 |
| 10 | ![](../assets/items/1901.png) | [[wiki/items/1901-faded-passion-piece\|Faded Passion Piece]] | 1 |  | Gold | 100 | 792 | 630 |
| 11 | ![](../assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 12 | ![](../assets/items/695.png) | [[wiki/items/695-gem-stone-red\|Gem Stone : Red]] | 1 |  | Gold | 400 | 3,168 | 2,520 |
| 13 | ![](../assets/items/1901.png) | [[wiki/items/1901-faded-passion-piece\|Faded Passion Piece]] | 1 |  | Gold | 100 | 792 | 630 |
| 14 | ![](../assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 1 |  | Gold | 20 | 158 | 126 |
| 15 | ![](../assets/items/397.png) | [[wiki/items/397-spell-necklace\|Spell Necklace]] | 1 |  | Gold | 150 | 1,188 | 945 |
| 16 | ![](../assets/items/398.png) | [[wiki/items/398-spell-belt\|Spell Belt]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 17 | ![](../assets/items/409.png) | [[wiki/items/409-guardian-helmet\|Guardian Helmet]] | 1 |  | Gold | 100 | 792 | 630 |
| 18 | ![](../assets/items/410.png) | [[wiki/items/410-guardian-armor\|Guardian Armor]] | 1 |  | Gold | 150 | 1,188 | 945 |
| 19 | ![](../assets/items/397.png) | [[wiki/items/397-spell-necklace\|Spell Necklace]] | 1 |  | Gold | 150 | 1,188 | 945 |
| 20 | ![](../assets/items/398.png) | [[wiki/items/398-spell-belt\|Spell Belt]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 21 | ![](../assets/items/409.png) | [[wiki/items/409-guardian-helmet\|Guardian Helmet]] | 1 |  | Gold | 100 | 792 | 630 |
| 22 | ![](../assets/items/410.png) | [[wiki/items/410-guardian-armor\|Guardian Armor]] | 1 |  | Gold | 150 | 1,188 | 945 |
| 23 | ![](../assets/items/421.png) | [[wiki/items/421-necklace-of-mediation\|Necklace of Mediation]] | 1 |  | Gold | 100 | 792 | 630 |
| 24 | ![](../assets/items/422.png) | [[wiki/items/422-belt-of-mediation\|Belt of Mediation]] | 1 |  | Gold | 150 | 1,188 | 945 |
| 25 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 26 | ![](../assets/items/1901.png) | [[wiki/items/1901-faded-passion-piece\|Faded Passion Piece]] | 1 |  | Gold | 100 | 792 | 630 |
| 27 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 28 | ![](../assets/items/603.png) | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] | 1 |  | Gold | 20 | 158 | 126 |
| 29 | ![](../assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 1 |  | Gold | 20 | 158 | 126 |

14 entries repeat an item already listed (the client shows every entry).

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

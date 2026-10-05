---
title: "Shop 104 (no NPC)"
type: "shop"
id: 104
status: "stub"
missing: ["npc"]
sources: ["client: Npc_Carry.cdb shop 104", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: []
stock:
  - {"slot": 0, "item": 1901, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 1902, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 1902, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 612, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 602, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 613, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 613, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 603, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 693, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 603, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 612, "count": 3, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 602, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 613, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 16, "item": 613, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 17, "item": 603, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 18, "item": 603, "count": 2, "p1": 0, "p2": 0}
  - {"slot": 19, "item": 399, "count": 1, "p1": 2, "p2": 2}
  - {"slot": 20, "item": 400, "count": 1, "p1": 1, "p2": 6}
  - {"slot": 21, "item": 411, "count": 1, "p1": 1, "p2": 10}
  - {"slot": 22, "item": 412, "count": 1, "p1": 1, "p2": 12}
  - {"slot": 23, "item": 429, "count": 1, "p1": 2, "p2": 3}
  - {"slot": 24, "item": 430, "count": 1, "p1": 2, "p2": 2}
prices:
  - {"item": 1901, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 1902, "currency": 2, "currency_name": "Gold", "base": 200, "buy": 1584, "sell": 1260}
  - {"item": 612, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 602, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 613, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 603, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 693, "currency": 2, "currency_name": "Gold", "base": 0, "buy": 0, "sell": 0}
  - {"item": 694, "currency": 2, "currency_name": "Gold", "base": 200, "buy": 1584, "sell": 1260}
  - {"item": 399, "currency": 2, "currency_name": "Gold", "base": 130, "buy": 1029, "sell": 819}
  - {"item": 400, "currency": 2, "currency_name": "Gold", "base": 110, "buy": 871, "sell": 693}
  - {"item": 411, "currency": 2, "currency_name": "Gold", "base": 130, "buy": 1029, "sell": 819}
  - {"item": 412, "currency": 2, "currency_name": "Gold", "base": 120, "buy": 950, "sell": 756}
  - {"item": 429, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 430, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=f99117 type=ffcf9c id=78a8ef sources=57ed5d npc=97d170 stock=c65e57 prices=5e642e price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
| **Shop id** | `104` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | no unit in `UnitDB` opens this shop |
| **Stock** | 25 entries, 14 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 1, `c3` = 1, `c4` = 4 (meaning unknown) |

> [!note]
> No NPC in the client opens this shop, so players could not reach it unless the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](wiki/assets/items/1901.png) | [[wiki/items/1901-faded-passion-piece\|Faded Passion Piece]] | 1 |  | Gold | 100 | 792 | 630 |
| 1 | ![](wiki/assets/items/1902.png) | [[wiki/items/1902-faded-passion-pattern\|Faded Passion Pattern]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 2 | ![](wiki/assets/items/1902.png) | [[wiki/items/1902-faded-passion-pattern\|Faded Passion Pattern]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 3 | ![](wiki/assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 3 |  | Gold | 20 | 158 | 126 |
| 4 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 5 | ![](wiki/assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 2 |  | Gold | 20 | 158 | 126 |
| 6 | ![](wiki/assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 2 |  | Gold | 20 | 158 | 126 |
| 7 | ![](wiki/assets/items/603.png) | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] | 1 |  | Gold | 20 | 158 | 126 |
| 8 | ![](wiki/assets/items/693.png) | [[wiki/items/693-gem-stone-blue\|Gem Stone : Blue]] | 1 |  | Gold | 0 | 0 | 0 |
| 9 | ![](wiki/assets/items/603.png) | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] | 2 |  | Gold | 20 | 158 | 126 |
| 10 | ![](wiki/assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 3 |  | Gold | 20 | 158 | 126 |
| 11 | ![](wiki/assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 2 |  | Gold | 20 | 158 | 126 |
| 12 | ![](wiki/assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 13 | ![](wiki/assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 14 | ![](wiki/assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 15 | ![](wiki/assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 2 |  | Gold | 20 | 158 | 126 |
| 16 | ![](wiki/assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 2 |  | Gold | 20 | 158 | 126 |
| 17 | ![](wiki/assets/items/603.png) | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] | 2 |  | Gold | 20 | 158 | 126 |
| 18 | ![](wiki/assets/items/603.png) | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] | 2 |  | Gold | 20 | 158 | 126 |
| 19 | ![](wiki/assets/items/399.png) | [[wiki/items/399-spell-bracelet\|Spell Bracelet]] | 1 | 2 | Gold | 130 | 1,029 | 819 |
| 20 | ![](wiki/assets/items/400.png) | [[wiki/items/400-spell-ring\|Spell Ring]] | 1 | 1 | Gold | 110 | 871 | 693 |
| 21 | ![](wiki/assets/items/411.png) | [[wiki/items/411-guardian-shoes\|Guardian Shoes]] | 1 | 1 | Gold | 130 | 1,029 | 819 |
| 22 | ![](wiki/assets/items/412.png) | [[wiki/items/412-guardian-gloves\|Guardian Gloves]] | 1 | 1 | Gold | 120 | 950 | 756 |
| 23 | ![](wiki/assets/items/429.png) | [[wiki/items/429-bandolier-necklace\|Bandolier Necklace]] | 1 | 2 | Gold | 100 | 792 | 630 |
| 24 | ![](wiki/assets/items/430.png) | [[wiki/items/430-bandolier-belt\|Bandolier Belt]] | 1 | 2 | Gold | 150 | 1,188 | 945 |

11 entries repeat an item already listed (the client shows every entry).

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

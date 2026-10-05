---
title: "Shop 222 (no NPC)"
type: "shop"
id: 222
status: "stub"
missing: ["npc"]
sources: ["client: Npc_Carry.cdb shop 222", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: []
stock:
  - {"slot": 1, "item": 611, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 612, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 602, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 613, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 613, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 613, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 603, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 603, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 612, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 602, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 611, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 16, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 17, "item": 422, "count": 1, "p1": 0, "p2": 2}
  - {"slot": 18, "item": 444, "count": 1, "p1": 0, "p2": 5}
  - {"slot": 19, "item": 423, "count": 1, "p1": 0, "p2": 4}
  - {"slot": 20, "item": 413, "count": 1, "p1": 1, "p2": 4}
  - {"slot": 21, "item": 414, "count": 1, "p1": 1, "p2": 5}
  - {"slot": 22, "item": 415, "count": 1, "p1": 2, "p2": 2}
  - {"slot": 23, "item": 700, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 24, "item": 700, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 611, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 601, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 612, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 602, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 613, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 603, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 422, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
  - {"item": 444, "currency": 2, "currency_name": "Gold", "base": 120, "buy": 950, "sell": 756}
  - {"item": 423, "currency": 2, "currency_name": "Gold", "base": 130, "buy": 1029, "sell": 819}
  - {"item": 413, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 414, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
  - {"item": 415, "currency": 2, "currency_name": "Gold", "base": 130, "buy": 1029, "sell": 819}
  - {"item": 700, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63, "cost_pair": {"currency": 18, "currency_name": "Fame", "amount": 10}}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=cd3374 type=ffcf9c id=1c6637 sources=66a29f npc=97d170 stock=687ff6 prices=303b92 price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
| **Shop id** | `222` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | no unit in `UnitDB` opens this shop |
| **Stock** | 21 entries, 13 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 1, `c3` = 1, `c4` = 4 (meaning unknown) |

> [!note]
> No NPC in the client opens this shop, so players could not reach it unless the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 1 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 2 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 3 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 4 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 5 | ![](../assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 1 |  | Gold | 20 | 158 | 126 |
| 6 | ![](../assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 1 |  | Gold | 20 | 158 | 126 |
| 7 | ![](../assets/items/613.png) | [[wiki/items/613-red-passion-fragments-c\|Red Passion Fragments (C)]] | 1 |  | Gold | 20 | 158 | 126 |
| 11 | ![](../assets/items/603.png) | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] | 1 |  | Gold | 20 | 158 | 126 |
| 12 | ![](../assets/items/603.png) | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] | 1 |  | Gold | 20 | 158 | 126 |
| 13 | ![](../assets/items/612.png) | [[wiki/items/612-red-passion-piece-d\|Red Passion Piece (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 14 | ![](../assets/items/602.png) | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 15 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 16 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 17 | ![](../assets/items/422.png) | [[wiki/items/422-belt-of-mediation\|Belt of Mediation]] | 1 |  | Gold | 150 | 1,188 | 945 |
| 18 | ![](../assets/items/444.png) | [[wiki/items/444-ring-of-rise\|Ring of Rise]] | 1 |  | Gold | 120 | 950 | 756 |
| 19 | ![](../assets/items/423.png) | [[wiki/items/423-bracelet-of-mediation\|Bracelet of Mediation]] | 1 |  | Gold | 130 | 1,029 | 819 |
| 20 | ![](../assets/items/413.png) | [[wiki/items/413-spirit-earring\|Spirit Earring]] | 1 | 1 | Gold | 100 | 792 | 630 |
| 21 | ![](../assets/items/414.png) | [[wiki/items/414-spirit-robe\|Spirit Robe]] | 1 | 1 | Gold | 150 | 1,188 | 945 |
| 22 | ![](../assets/items/415.png) | [[wiki/items/415-spirit-shoes\|Spirit Shoes]] | 1 | 2 | Gold | 130 | 1,029 | 819 |
| 23 | ![](../assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 1 |  | Gold | 10 | 79 | 63 |
| 24 | ![](../assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 1 |  | Gold | 10 | 79 | 63 |

8 entries repeat an item already listed (the client shows every entry).

Second price (`Item_Base` cost pair @24/@26, charged as listed). The patch notes price Amplifying Passion at "5 silver **or** 3 gold medals" ([[gameplay/reinforce-and-runes|runes]] §5), so this is probably an alternative way to pay, not an extra charge (*guess*): [[wiki/items/700-crystal-blue|Crystal : Blue]]: 10 Fame

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

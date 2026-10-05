---
title: "Owen's shop (Member of Red Union)"
type: "shop"
id: 8
status: "complete"
missing: []
sources: ["client: Npc_Carry.cdb shop 8", "client: UnitDB.cdb u16@a2 = 8 (units 337)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)", "client: [[gameplay/consumables]] §4 (Training Camp Owen 337 craft list 8, Odin list 6 = Item_Make category 0 copy, passion converter category 7)", "video: [[gameplay/npc-locations]] §4 Training Camp, video-measured (±3 units) (Owen 337)", "video: [[gameplay/video-character-creation-and-tutorial]] step 14 (camp Owen has only a greeting line)"]
npc: [337]
stock:
  - {"slot": 0, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 611, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 611, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 611, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 611, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 611, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 16, "item": 611, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 17, "item": 1900, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 18, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 19, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 20, "item": 611, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 21, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 22, "item": 611, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 23, "item": 601, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 24, "item": 611, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 601, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 611, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126}
  - {"item": 1900, "currency": 2, "currency_name": "Gold", "base": 50, "buy": 396, "sell": 315}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=2490da type=ffcf9c id=fe5dbb sources=bcd6d1 npc=e7736e stock=78a156 prices=32fa64 price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
|  | ![Owen's shop (Member of Red Union)](../assets/npcs/337.png) |
| **Shop id** | `8` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/337-owen\|Owen]] (Member of Red Union) |
| **Stock** | 25 entries, 3 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 1, `c3` = 1, `c4` = 4 (meaning unknown) |

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 1 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 2 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 3 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 4 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 5 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 6 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 7 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 8 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 9 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 10 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 11 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 12 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 13 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 14 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 15 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 16 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 17 | ![](../assets/items/1900.png) | [[wiki/items/1900-faded-passion-fragments\|Faded Passion fragments]] | 1 |  | Gold | 50 | 396 | 315 |
| 18 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 19 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 20 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 21 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 22 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 23 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |
| 24 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 1 |  | Gold | 20 | 158 | 126 |

22 entries repeat an item already listed (the client shows every entry).

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).

### Seen in

- Seen in [[gameplay/npc-locations|NPC and point-of-interest locations]], section *4. Training Camp (fields 88 / 92 / 96)* at 9:13
<!-- generated:end -->

## Notes

Opened by the Training Camp Owen (unit 337, Member of Red Union) (*video*, [[gameplay/npc-locations|NPC locations]] §4). His `UnitDB` list 8 is his **craft** list: `Item_Make` category 8, with only B-grade scrolls, tomes, elixirs and flasks and C/B potions (*client*, [[gameplay/consumables|consumables]] §4). In the 2018 relaunch video the camp Owen offers only a greeting line ([[gameplay/video-character-creation-and-tutorial|character creation video]] step 14).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/consumables]] §4 (Training Camp Owen 337 craft list 8, Odin list 6 = Item_Make category 0 copy, passion converter category 7) (*client*)
- [[gameplay/npc-locations]] §4 Training Camp, video-measured (±3 units) (Owen 337) (*video*)
- [[gameplay/video-character-creation-and-tutorial]] step 14 (camp Owen has only a greeting line) (*video*)

## Open questions

- The value 8 is read as a shop id here and as a craft list in [[gameplay/consumables|consumables]] §4. This `Npc_Carry` row (fragments 601, 611, 1900) may never open as a shop (*guess*).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

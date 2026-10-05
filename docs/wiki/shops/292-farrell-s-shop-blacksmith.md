---
title: "Farrell's shop (Blacksmith)"
type: "shop"
id: 292
status: "partial"
missing: ["prices"]
sources: ["client: Npc_Carry.cdb shop 292", "client: UnitDB.cdb u16@a2 = 292 (units 317)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)", "guide + image: [[gameplay/items-and-crafting]] §3 and [[gameplay/maps-and-dungeons]] §5 (Farrell: weapons and passion conversion)", "staff: [[gameplay/crush-patch-notes]] 2016-12-22 (Blacksmith Farrel now buys and sells items)", "guide + guess: [[gameplay/npc-locations]] §3 (Farrell 237/317 next to Odin, about (1995, 1700))"]
npc: [317]
stock:
  - {"slot": 0, "item": 8651, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 8657, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 8659, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 8650, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 8654, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 8658, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 8663, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 8653, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 8660, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 8665, "count": 1, "p1": 0, "p2": 0}
prices: []
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
---
<!-- generated:start -->
<!-- generated-keys: title=b64223 type=ffcf9c id=85f100 sources=f82d48 npc=49cc8c stock=660f95 prices=97d170 price_rates=c44eae header=702516 -->
|  |  |
|---|---|
|  | ![Farrell's shop (Blacksmith)](../assets/npcs/317.png) |
| **Shop id** | `292` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/317-farrell\|Farrell]] (Blacksmith) |
| **Stock** | 10 entries, 10 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 0, `c3` = 1, `c4` = 0 (meaning unknown) |

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 |  | item 8651 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 1 |  | item 8657 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 2 |  | item 8659 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 3 |  | item 8650 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 4 |  | item 8654 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 5 |  | item 8658 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 6 |  | item 8663 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 7 |  | item 8653 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 8 |  | item 8660 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 9 |  | item 8665 (not in `Item_Base`) | 1 |  | – | – | – | – |

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).
<!-- generated:end -->

## Notes

Farrell (unit 317; 237 is another Farrell) is the Blacksmith. He crafts weapons and converts Passion (*guides + image*, [[gameplay/items-and-crafting|crafting]] §3, [[gameplay/maps-and-dungeons|maps]] §5). One guide puts him next to Odin on the Fortress east arm; a server can place him at about (1995, 1700) (*guide + guess*, [[gameplay/npc-locations|NPC locations]] §3).

Crush Online added a shop to him on 22 Dec 2016 ("Blacksmith Farrel now buys and sells items", *staff*, [[gameplay/crush-patch-notes|CO patch notes]] 2016-12-22).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/items-and-crafting]] §3 and [[gameplay/maps-and-dungeons]] §5 (Farrell: weapons and passion conversion) (*guide + image*)
- [[gameplay/crush-patch-notes]] 2016-12-22 (Blacksmith Farrel now buys and sells items) (*staff*)
- [[gameplay/npc-locations]] §3 (Farrell 237/317 next to Odin, about (1995, 1700)) (*guide + guess*)

## Open questions

- `prices` stays missing: the ten stocked ids (8650-8665) have no `Item_Base` row, and no source shows what Farrell sold.
- Rank 1-2 Striker skill stones were sold for gold from the same patch ([[gameplay/crush-patch-notes|CO patch notes]] 2016-12-22). The notes do not name the NPC.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

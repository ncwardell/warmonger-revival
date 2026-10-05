---
title: "Arion's shop (Innocence Smith)"
type: "shop"
id: 290
status: "partial"
missing: ["prices"]
sources: ["client: Npc_Carry.cdb shop 290", "client: UnitDB.cdb u16@a2 = 290 (units 241)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)", "forum: [[gameplay/warmonger-forum]] §5 (5 [Low] cores sold by NPC Arion for 192,000 personal gold, Crush Online)", "staff: [[gameplay/crush-patch-notes]] 2016-10-14 (Arion, core smith, crafts the premium core Sacred Area)", "client: [[gameplay/npc-locations]] §8 (Arion/Arkin 241/243 still unplaced)"]
npc: [241]
stock:
  - {"slot": 0, "item": 1624, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 1625, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 1626, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 1627, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 1628, "count": 1, "p1": 0, "p2": 0}
prices: []
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
---
<!-- generated:start -->
<!-- generated-keys: title=1eea9f type=ffcf9c id=9d3237 sources=424f94 npc=bb3d98 stock=d24fe2 prices=97d170 price_rates=c44eae header=702516 -->
|  |  |
|---|---|
|  | ![Arion's shop (Innocence Smith)](../assets/npcs/241.png) |
| **Shop id** | `290` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/241-arion\|Arion]] (Innocence Smith) |
| **Stock** | 5 entries, 5 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 0, `c3` = 1, `c4` = 0 (meaning unknown) |

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 |  | item 1624 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 1 |  | item 1625 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 2 |  | item 1626 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 3 |  | item 1627 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 4 |  | item 1628 (not in `Item_Base`) | 1 |  | – | – | – | – |

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).
<!-- generated:end -->

## Notes

Arion (unit 241) is the core smith. In Crush Online he crafted fort cores; the premium core Sacred Area could be made there with the right labs (*staff*, [[gameplay/crush-patch-notes|CO patch notes]] 2016-10-14). Players wrote that **5 [Low] cores** were sold by Arion for 192,000 personal gold; crafted cores (28 kinds) were installed at Hadrian (*forum*, [[gameplay/warmonger-forum|Warmonger forum]] §5).

The client list has exactly five entries (1624-1628), none of them in `Item_Base`. They may be those five [Low] cores (*guess*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/warmonger-forum]] §5 (5 [Low] cores sold by NPC Arion for 192,000 personal gold, Crush Online) (*forum*)
- [[gameplay/crush-patch-notes]] 2016-10-14 (Arion, core smith, crafts the premium core Sacred Area) (*staff*)
- [[gameplay/npc-locations]] §8 (Arion/Arkin 241/243 still unplaced) (*client*)

## Open questions

- `prices` stays missing: the stocked ids have no `Item_Base` row, so no currency or base is known. The 192,000 gold is a Crush Online forum figure. It does not say whether that is per core or for all five.
- Where Arion stands is unknown ([[gameplay/npc-locations|NPC locations]] §8). [[gameplay/video-early-quests|early quests]] §3 gives unit 241 as the Scout Leader in the Land of Greed, which conflicts with UnitDB naming 241 Arion.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

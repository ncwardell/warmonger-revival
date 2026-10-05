---
title: "Wren's shop (Merchant) 291"
type: "shop"
id: 291
status: "complete"
missing: []
sources: ["client: Npc_Carry.cdb shop 291", "client: UnitDB.cdb u16@a2 = 291 (units 319)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: [319]
stock:
  - {"slot": 0, "item": 883, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 884, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 906, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 909, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 908, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 945, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 946, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 947, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 949, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 883, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63}
  - {"item": 884, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63}
  - {"item": 906, "currency": 2, "currency_name": "Gold", "base": 80, "buy": 633, "sell": 504}
  - {"item": 909, "currency": 2, "currency_name": "Gold", "base": 80, "buy": 633, "sell": 504}
  - {"item": 908, "currency": 2, "currency_name": "Gold", "base": 2500, "buy": 19800, "sell": 15750}
  - {"item": 945, "currency": 2, "currency_name": "Gold", "base": 20000, "buy": 158400, "sell": 126000}
  - {"item": 946, "currency": 2, "currency_name": "Gold", "base": 36000, "buy": 285120, "sell": 226800}
  - {"item": 947, "currency": 2, "currency_name": "Gold", "base": 170000, "buy": 1346400, "sell": 1071000}
  - {"item": 949, "currency": 2, "currency_name": "Gold", "base": 500000, "buy": 3960000, "sell": 3150000}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
---
<!-- generated:start -->
<!-- generated-keys: title=e07b39 type=ffcf9c id=371786 sources=7badf6 npc=01f605 stock=e29029 prices=94d9ef price_rates=c44eae header=702516 -->
|  |  |
|---|---|
|  | ![Wren's shop (Merchant) 291](wiki/assets/npcs/319.png) |
| **Shop id** | `291` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/319-wren\|Wren]] (Merchant) |
| **Stock** | 9 entries, 9 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 0, `c3` = 1, `c4` = 0 (meaning unknown) |

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](wiki/assets/items/883.png) | [[wiki/items/883-potion-of-health-d\|Potion of Health (D)]] | 1 |  | Gold | 10 | 79 | 63 |
| 1 | ![](wiki/assets/items/884.png) | [[wiki/items/884-potion-of-mana-d\|Potion of Mana (D)]] | 1 |  | Gold | 10 | 79 | 63 |
| 2 | ![](wiki/assets/items/906.png) | [[wiki/items/906-scroll-return\|Scroll : Return]] | 1 |  | Gold | 80 | 633 | 504 |
| 3 | ![](wiki/assets/items/909.png) | [[wiki/items/909-scroll-gaia\|Scroll : Gaia]] | 1 |  | Gold | 80 | 633 | 504 |
| 4 | ![](wiki/assets/items/908.png) | [[wiki/items/908-scroll-castle\|Scroll : Castle]] | 1 |  | Gold | 2,500 | 19,800 | 15,750 |
| 5 | ![](wiki/assets/items/945.png) | [[wiki/items/945-auto-decomposition-hammer-d\|Auto decomposition hammer (D)]] | 1 |  | Gold | 20,000 | 158,400 | 126,000 |
| 6 | ![](wiki/assets/items/946.png) | [[wiki/items/946-auto-decomposition-hammer-c\|Auto decomposition hammer (C)]] | 1 |  | Gold | 36,000 | 285,120 | 226,800 |
| 7 | ![](wiki/assets/items/947.png) | [[wiki/items/947-auto-decomposition-hammer-b\|Auto decomposition hammer (B)]] | 1 |  | Gold | 170,000 | 1,346,400 | 1,071,000 |
| 8 | ![](wiki/assets/items/949.png) | [[wiki/items/949-auto-decomposition-hammer-a\|Auto decomposition hammer (A)]] | 1 |  | Gold | 500,000 | 3,960,000 | 3,150,000 |

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).

### Seen in

- Seen in [[gameplay/consumables|Consumables and clickables]], section *4.2 Potions*
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

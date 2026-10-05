---
title: "Ashley's shop (Merits Costume Merchant)"
type: "shop"
id: 284
status: "complete"
missing: []
sources: ["client: Npc_Carry.cdb shop 284", "client: UnitDB.cdb u16@a2 = 284 (units 206)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: [206]
stock:
  - {"slot": 0, "item": 2027, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 2028, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 2029, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 2015, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 2016, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 2017, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 2018, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 2019, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 2020, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 2079, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 2080, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 2081, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 2082, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 2083, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 2084, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 1999, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 2027, "currency": 10, "currency_name": "Bronze Medal", "base": 50, "buy": 50, "sell": null}
  - {"item": 2028, "currency": 10, "currency_name": "Bronze Medal", "base": 50, "buy": 50, "sell": null}
  - {"item": 2029, "currency": 10, "currency_name": "Bronze Medal", "base": 50, "buy": 50, "sell": null}
  - {"item": 2015, "currency": 11, "currency_name": "Silver Medal", "base": 25, "buy": 25, "sell": null}
  - {"item": 2016, "currency": 11, "currency_name": "Silver Medal", "base": 25, "buy": 25, "sell": null}
  - {"item": 2017, "currency": 11, "currency_name": "Silver Medal", "base": 25, "buy": 25, "sell": null}
  - {"item": 2018, "currency": 12, "currency_name": "Gold Medal", "base": 10, "buy": 10, "sell": null}
  - {"item": 2019, "currency": 12, "currency_name": "Gold Medal", "base": 10, "buy": 10, "sell": null}
  - {"item": 2020, "currency": 12, "currency_name": "Gold Medal", "base": 10, "buy": 10, "sell": null}
  - {"item": 2079, "currency": 10, "currency_name": "Bronze Medal", "base": 40, "buy": 40, "sell": null}
  - {"item": 2080, "currency": 10, "currency_name": "Bronze Medal", "base": 40, "buy": 40, "sell": null}
  - {"item": 2081, "currency": 10, "currency_name": "Bronze Medal", "base": 40, "buy": 40, "sell": null}
  - {"item": 2082, "currency": 10, "currency_name": "Bronze Medal", "base": 30, "buy": 30, "sell": null}
  - {"item": 2083, "currency": 10, "currency_name": "Bronze Medal", "base": 30, "buy": 30, "sell": null}
  - {"item": 2084, "currency": 10, "currency_name": "Bronze Medal", "base": 30, "buy": 30, "sell": null}
  - {"item": 1999, "currency": 2, "currency_name": "Gold", "base": 50000, "buy": 396000, "sell": 315000}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
---
<!-- generated:start -->
<!-- generated-keys: title=a81e66 type=ffcf9c id=7f3541 sources=137d9b npc=6d18d7 stock=ef0876 prices=e7a76f price_rates=c44eae header=702516 -->
|  |  |
|---|---|
|  | ![Ashley's shop (Merits Costume Merchant)](wiki/assets/npcs/206.png) |
| **Shop id** | `284` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/206-ashley\|Ashley]] (Merits Costume Merchant) |
| **Stock** | 16 entries, 16 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 0, `c3` = 1, `c4` = 0 (meaning unknown) |

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](wiki/assets/items/2027.png) | [[wiki/items/2027-twisted-wind-set\|Twisted Wind Set]] | 1 |  | Bronze Medal | 50 | 50 | – |
| 1 | ![](wiki/assets/items/2028.png) | [[wiki/items/2028-twisted-wind-set\|Twisted Wind Set]] | 1 |  | Bronze Medal | 50 | 50 | – |
| 2 | ![](wiki/assets/items/2029.png) | [[wiki/items/2029-twisted-wind-set\|Twisted Wind Set]] | 1 |  | Bronze Medal | 50 | 50 | – |
| 3 | ![](wiki/assets/items/2015.png) | [[wiki/items/2015-crown-set\|Crown Set]] | 1 |  | Silver Medal | 25 | 25 | – |
| 4 | ![](wiki/assets/items/2016.png) | [[wiki/items/2016-crown-set\|Crown Set]] | 1 |  | Silver Medal | 25 | 25 | – |
| 5 | ![](wiki/assets/items/2017.png) | [[wiki/items/2017-crown-set\|Crown Set]] | 1 |  | Silver Medal | 25 | 25 | – |
| 6 | ![](wiki/assets/items/2018.png) | [[wiki/items/2018-helios-set\|Helios Set]] | 1 |  | Gold Medal | 10 | 10 | – |
| 7 | ![](wiki/assets/items/2019.png) | [[wiki/items/2019-helios-set\|Helios Set]] | 1 |  | Gold Medal | 10 | 10 | – |
| 8 | ![](wiki/assets/items/2020.png) | [[wiki/items/2020-helios-set\|Helios Set]] | 1 |  | Gold Medal | 10 | 10 | – |
| 9 | ![](wiki/assets/items/2079.png) | [[wiki/items/2079-haple-set\|Haple Set]] | 1 |  | Bronze Medal | 40 | 40 | – |
| 10 | ![](wiki/assets/items/2080.png) | [[wiki/items/2080-haple-set\|Haple Set]] | 1 |  | Bronze Medal | 40 | 40 | – |
| 11 | ![](wiki/assets/items/2081.png) | [[wiki/items/2081-haple-set\|Haple Set]] | 1 |  | Bronze Medal | 40 | 40 | – |
| 12 | ![](wiki/assets/items/2082.png) | [[wiki/items/2082-oracle-set\|Oracle Set]] | 1 |  | Bronze Medal | 30 | 30 | – |
| 13 | ![](wiki/assets/items/2083.png) | [[wiki/items/2083-oracle-set\|Oracle Set]] | 1 |  | Bronze Medal | 30 | 30 | – |
| 14 | ![](wiki/assets/items/2084.png) | [[wiki/items/2084-oracle-set\|Oracle Set]] | 1 |  | Bronze Medal | 30 | 30 | – |
| 15 | ![](wiki/assets/items/1999.png) | [[wiki/items/1999-costume-remover\|Costume Remover]] | 1 |  | Gold | 50,000 | 396,000 | 315,000 |

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).

### Seen in

- Seen in [[gameplay/npc-locations|NPC and point-of-interest locations]], section *3. Fortress (field 120)* at 37:09
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

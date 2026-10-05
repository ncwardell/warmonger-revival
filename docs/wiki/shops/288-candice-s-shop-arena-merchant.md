---
title: "Candice's shop (Arena Merchant)"
type: "shop"
id: 288
status: "complete"
missing: []
sources: ["client: Npc_Carry.cdb shop 288", "client: UnitDB.cdb u16@a2 = 288 (units 240)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)"]
npc: [240]
stock:
  - {"slot": 0, "item": 1035, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 1045, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 1035, "currency": 15, "currency_name": "Arena Medal", "base": 5, "buy": 5, "sell": null}
  - {"item": 1045, "currency": 15, "currency_name": "Arena Medal", "base": 7, "buy": 7, "sell": null}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
---
<!-- generated:start -->
<!-- generated-keys: title=a91e29 type=ffcf9c id=b70706 sources=99471c npc=d2fb2d stock=aef2bf prices=88861d price_rates=c44eae header=702516 -->
|  |  |
|---|---|
|  | ![Candice's shop (Arena Merchant)](../assets/npcs/240.png) |
| **Shop id** | `288` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/240-candice\|Candice]] (Arena Merchant) |
| **Stock** | 2 entries, 2 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 0, `c3` = 1, `c4` = 0 (meaning unknown) |

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](../assets/items/1035.png) | [[wiki/items/1035-box-of-the-victorious-i\|Box of the Victorious I]] | 1 |  | Arena Medal | 5 | 5 | – |
| 1 | ![](../assets/items/1045.png) | [[wiki/items/1045-box-of-the-participant-i\|Box of the Participant I]] | 1 |  | Arena Medal | 7 | 7 | – |

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

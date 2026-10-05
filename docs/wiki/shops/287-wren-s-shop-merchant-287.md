---
title: "Wren's shop (Merchant) 287"
type: "shop"
id: 287
status: "complete"
missing: []
sources: ["client: Npc_Carry.cdb shop 287", "client: UnitDB.cdb u16@a2 = 287 (units 238)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20; [[gameplay/video-character-creation-and-tutorial]] 8:40"]
npc: [238]
stock:
  - {"slot": 0, "item": 883, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 884, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 906, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 945, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 883, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63}
  - {"item": 884, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63}
  - {"item": 906, "currency": 2, "currency_name": "Gold", "base": 80, "buy": 633, "sell": 504}
  - {"item": 945, "currency": 2, "currency_name": "Gold", "base": 20000, "buy": 158400, "sell": 126000}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
observed_prices:
  - {"item": 883, "shown": 79, "currency": "Gold", "source": "docs: [[gameplay/video-tutorial-walkthrough]] 14:20; [[gameplay/video-character-creation-and-tutorial]] 8:40"}
  - {"item": 884, "shown": 79, "currency": "Gold", "source": "docs: [[gameplay/video-tutorial-walkthrough]] 14:20; [[gameplay/video-character-creation-and-tutorial]] 8:40"}
  - {"item": 906, "shown": 79, "currency": "Gold", "source": "docs: [[gameplay/video-tutorial-walkthrough]] 14:20; [[gameplay/video-character-creation-and-tutorial]] 8:40", "note": "shown as 'Scroll : Return' at 79, but item 906 has base 80 (formula: 633); the shop may have listed 911 or another 10-gold scroll"}
---
<!-- generated:start -->
<!-- generated-keys: title=76b355 type=ffcf9c id=f0a4ac sources=91990c npc=3e4a5c stock=f963fb prices=8d1d70 price_rates=c44eae header=702516 observed_prices=d0398d -->
|  |  |
|---|---|
|  | ![Wren's shop (Merchant) 287](wiki/assets/npcs/238.png) |
| **Shop id** | `287` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/238-wren\|Wren]] (Merchant) |
| **Stock** | 4 entries, 4 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 0, `c3` = 1, `c4` = 0 (meaning unknown) |

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](wiki/assets/items/883.png) | [[wiki/items/883-potion-of-health-d\|Potion of Health (D)]] | 1 |  | Gold | 10 | 79 | 63 |
| 1 | ![](wiki/assets/items/884.png) | [[wiki/items/884-potion-of-mana-d\|Potion of Mana (D)]] | 1 |  | Gold | 10 | 79 | 63 |
| 2 | ![](wiki/assets/items/906.png) | [[wiki/items/906-scroll-return\|Scroll : Return]] | 1 |  | Gold | 80 | 633 | 504 |
| 3 | ![](wiki/assets/items/945.png) | [[wiki/items/945-auto-decomposition-hammer-d\|Auto decomposition hammer (D)]] | 1 |  | Gold | 20,000 | 158,400 | 126,000 |

### Prices seen in play

Source: [[gameplay/video-tutorial-walkthrough]] 14:20; [[gameplay/video-character-creation-and-tutorial]] 8:40

| item | shown | formula | match | note |
|---|---|---|---|---|
| [[wiki/items/883-potion-of-health-d\|Potion of Health (D)]] | 79 Gold | 79 | yes |  |
| [[wiki/items/884-potion-of-mana-d\|Potion of Mana (D)]] | 79 Gold | 79 | yes |  |
| [[wiki/items/906-scroll-return\|Scroll : Return]] | 79 Gold | 633 | no | shown as 'Scroll : Return' at 79, but item 906 has base 80 (formula: 633); the shop may have listed 911 or another 10-gold scroll |

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).

### Seen in

- Seen in [[gameplay/consumables|Consumables and clickables]], section *4.2 Potions*
- Seen in [[gameplay/npc-locations|NPC and point-of-interest locations]], section *4. Training Camp (fields 88 / 92 / 96)* at 9:13
- Seen in [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]], section *6. Drops, shop, other numbers* at 16:54
- Seen in [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]], section *Shop and economy* at 14:20
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

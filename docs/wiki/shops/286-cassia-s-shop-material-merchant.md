---
title: "Cassia's shop (Material Merchant)"
type: "shop"
id: 286
status: "complete"
missing: []
sources: ["client: Npc_Carry.cdb shop 286", "client: UnitDB.cdb u16@a2 = 286 (units 212)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)", "video: [[gameplay/npc-locations]] §3 Fortress, video-measured (±3 units) (Cassia 212; 'NE in Fortress' guide)", "client: [[gameplay/consumables]] §5 (empty scrolls/flasks and Worked oil sold by Cassia, base prices)", "guide: [[gameplay/items-and-crafting]] §3-4 (materials sold by Cassia; containers for alchemy)", "video: [[gameplay/video-early-quests]] §2 step 15 and §3 (quest 13 at Cassia; 'go to Odin or Owen to craft')"]
npc: [212]
stock:
  - {"slot": 0, "item": 830, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 831, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 832, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 833, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 834, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 835, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 836, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 837, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 846, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 830, "currency": 2, "currency_name": "Gold", "base": 50, "buy": 396, "sell": 315}
  - {"item": 831, "currency": 2, "currency_name": "Gold", "base": 60, "buy": 475, "sell": 378}
  - {"item": 832, "currency": 2, "currency_name": "Gold", "base": 80, "buy": 633, "sell": 504}
  - {"item": 833, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 834, "currency": 2, "currency_name": "Gold", "base": 80, "buy": 633, "sell": 504}
  - {"item": 835, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 836, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
  - {"item": 837, "currency": 2, "currency_name": "Gold", "base": 200, "buy": 1584, "sell": 1260}
  - {"item": 846, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
---
<!-- generated:start -->
<!-- generated-keys: title=771f9c type=ffcf9c id=7edab1 sources=31058d npc=d093fd stock=c58af5 prices=3ccdac price_rates=c44eae header=702516 -->
|  |  |
|---|---|
|  | ![Cassia's shop (Material Merchant)](../assets/npcs/212.png) |
| **Shop id** | `286` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/212-cassia\|Cassia]] (Material Merchant) |
| **Stock** | 9 entries, 9 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 0, `c3` = 1, `c4` = 0 (meaning unknown) |

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](../assets/items/830.png) | [[wiki/items/830-empty-scroll-c\|Empty Scroll (C)]] | 1 |  | Gold | 50 | 396 | 315 |
| 1 | ![](../assets/items/831.png) | [[wiki/items/831-empty-scroll-b\|Empty Scroll (B)]] | 1 |  | Gold | 60 | 475 | 378 |
| 2 | ![](../assets/items/832.png) | [[wiki/items/832-empty-scroll-a\|Empty Scroll (A)]] | 1 |  | Gold | 80 | 633 | 504 |
| 3 | ![](../assets/items/833.png) | [[wiki/items/833-empty-scroll-s\|Empty Scroll (S)]] | 1 |  | Gold | 100 | 792 | 630 |
| 4 | ![](../assets/items/834.png) | [[wiki/items/834-empty-flask-c\|Empty Flask (C)]] | 1 |  | Gold | 80 | 633 | 504 |
| 5 | ![](../assets/items/835.png) | [[wiki/items/835-empty-flask-b\|Empty Flask (B)]] | 1 |  | Gold | 100 | 792 | 630 |
| 6 | ![](../assets/items/836.png) | [[wiki/items/836-empty-flask-a\|Empty Flask (A)]] | 1 |  | Gold | 150 | 1,188 | 945 |
| 7 | ![](../assets/items/837.png) | [[wiki/items/837-empty-flask-s\|Empty Flask (S)]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 8 | ![](../assets/items/846.png) | [[wiki/items/846-worked-oil\|Worked oil]] | 1 |  | Gold | 100 | 792 | 630 |

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).

### Seen in

- Seen in [[gameplay/consumables|Consumables and clickables]], section *5. Where the inputs come from*
- Seen in [[gameplay/npc-locations|NPC and point-of-interest locations]], section *3. Fortress (field 120)* at 32:51
<!-- generated:end -->

## Notes

Cassia (unit 212), the Material Merchant, stands in the north-east of the Fortress (*video*, [[gameplay/npc-locations|NPC locations]] §3; *guide*, [[gameplay/maps-and-dungeons|maps]] §5). She sells the alchemy **containers**: Empty Scroll [C]/[B]/[A]/[S] (830-833, base 50/60/80/100) and Empty Flask [C]-[S] (834-837, 80/100/150/200), plus Worked oil (846, 100) for dyes (*client*, [[gameplay/consumables|consumables]] §5). Each buff recipe at Owen takes one container, a gem powder and a dungeon secondary (*guide*, [[gameplay/items-and-crafting|crafting]] §4). The secondaries are drops and are not sold anywhere ([[gameplay/consumables|consumables]] §5).

In the 2018 launch video she sends the player to Odin or Owen to craft. Quest 13 "Battle preparations" sends the player to her and pays 100 Empty Flask [C] (*video*, [[gameplay/video-early-quests|early quests]] §2 step 15).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/npc-locations]] §3 Fortress, video-measured (±3 units) (Cassia 212; 'NE in Fortress' guide) (*video*)
- [[gameplay/consumables]] §5 (empty scrolls/flasks and Worked oil sold by Cassia, base prices) (*client*)
- [[gameplay/items-and-crafting]] §3-4 (materials sold by Cassia; containers for alchemy) (*guide*)
- [[gameplay/video-early-quests]] §2 step 15 and §3 (quest 13 at Cassia; 'go to Odin or Owen to craft') (*video*)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

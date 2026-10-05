---
title: "Shop 109 (no NPC)"
type: "shop"
id: 109
status: "partial"
missing: ["npc"]
sources: ["client: Npc_Carry.cdb shop 109", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)", "client + guess: [[gameplay/consumables]] §5 (lists 73-113 are non-shop lists, probably drop pools)"]
npc: []
stock:
  - {"slot": 0, "item": 1902, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 848, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 838, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 842, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 850, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 848, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 838, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 694, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 695, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 695, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 696, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 1902, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 84, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 85, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 780, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 401, "count": 1, "p1": 0, "p2": 3}
  - {"slot": 16, "item": 402, "count": 1, "p1": 0, "p2": 2}
  - {"slot": 17, "item": 411, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 18, "item": 412, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 19, "item": 435, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 20, "item": 436, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 21, "item": 411, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 22, "item": 412, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 23, "item": 435, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 24, "item": 436, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 1902, "currency": 2, "currency_name": "Gold", "base": 200, "buy": 1584, "sell": 1260}
  - {"item": 848, "currency": 2, "currency_name": "Gold", "base": 50, "buy": 396, "sell": 315}
  - {"item": 838, "currency": 2, "currency_name": "Gold", "base": 50, "buy": 396, "sell": 315}
  - {"item": 842, "currency": 2, "currency_name": "Gold", "base": 50, "buy": 396, "sell": 315}
  - {"item": 850, "currency": 2, "currency_name": "Gold", "base": 50, "buy": 396, "sell": 315}
  - {"item": 694, "currency": 2, "currency_name": "Gold", "base": 200, "buy": 1584, "sell": 1260}
  - {"item": 695, "currency": 2, "currency_name": "Gold", "base": 400, "buy": 3168, "sell": 2520}
  - {"item": 696, "currency": 2, "currency_name": "Gold", "base": 800, "buy": 6336, "sell": 5040}
  - {"item": 780, "currency": 2, "currency_name": "Gold", "base": 40, "buy": 316, "sell": 252}
  - {"item": 401, "currency": 2, "currency_name": "Gold", "base": 100, "buy": 792, "sell": 630}
  - {"item": 402, "currency": 2, "currency_name": "Gold", "base": 150, "buy": 1188, "sell": 945}
  - {"item": 411, "currency": 2, "currency_name": "Gold", "base": 130, "buy": 1029, "sell": 819}
  - {"item": 412, "currency": 2, "currency_name": "Gold", "base": 120, "buy": 950, "sell": 756}
  - {"item": 435, "currency": 2, "currency_name": "Gold", "base": 130, "buy": 1029, "sell": 819}
  - {"item": 436, "currency": 2, "currency_name": "Gold", "base": 120, "buy": 950, "sell": 756}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 1, "c3": 1, "c4": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=332499 type=ffcf9c id=a1422e sources=b66d57 npc=97d170 stock=ed0729 prices=dd5803 price_rates=c44eae header=5929ec -->
|  |  |
|---|---|
| **Shop id** | `109` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | no unit in `UnitDB` opens this shop |
| **Stock** | 25 entries, 17 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 1, `c3` = 1, `c4` = 4 (meaning unknown) |

> [!note]
> No NPC in the client opens this shop, so players could not reach it unless the server pushed it with `0x42f`. Rows like this look like test or leftover data (*guess*).

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](wiki/assets/items/1902.png) | [[wiki/items/1902-faded-passion-pattern\|Faded Passion Pattern]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 1 | ![](wiki/assets/items/848.png) | [[wiki/items/848-medical-herb-water\|Medical herb water]] | 1 |  | Gold | 50 | 396 | 315 |
| 2 | ![](wiki/assets/items/838.png) | [[wiki/items/838-ointment-of-spirit\|Ointment of Spirit]] | 1 |  | Gold | 50 | 396 | 315 |
| 3 | ![](wiki/assets/items/842.png) | [[wiki/items/842-burned-sulphur\|Burned sulphur]] | 1 |  | Gold | 50 | 396 | 315 |
| 4 | ![](wiki/assets/items/850.png) | [[wiki/items/850-refined-oil\|Refined oil]] | 1 |  | Gold | 50 | 396 | 315 |
| 5 | ![](wiki/assets/items/848.png) | [[wiki/items/848-medical-herb-water\|Medical herb water]] | 1 |  | Gold | 50 | 396 | 315 |
| 6 | ![](wiki/assets/items/838.png) | [[wiki/items/838-ointment-of-spirit\|Ointment of Spirit]] | 1 |  | Gold | 50 | 396 | 315 |
| 7 | ![](wiki/assets/items/694.png) | [[wiki/items/694-gem-stone-yellow\|Gem Stone : Yellow]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 8 | ![](wiki/assets/items/695.png) | [[wiki/items/695-gem-stone-red\|Gem Stone : Red]] | 1 |  | Gold | 400 | 3,168 | 2,520 |
| 9 | ![](wiki/assets/items/695.png) | [[wiki/items/695-gem-stone-red\|Gem Stone : Red]] | 1 |  | Gold | 400 | 3,168 | 2,520 |
| 10 | ![](wiki/assets/items/696.png) | [[wiki/items/696-gem-stone-black\|Gem stone : Black]] | 1 |  | Gold | 800 | 6,336 | 5,040 |
| 11 | ![](wiki/assets/items/1902.png) | [[wiki/items/1902-faded-passion-pattern\|Faded Passion Pattern]] | 1 |  | Gold | 200 | 1,584 | 1,260 |
| 12 |  | item 84 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 13 |  | item 85 (not in `Item_Base`) | 1 |  | – | – | – | – |
| 14 | ![](wiki/assets/items/780.png) | [[wiki/items/780-moon-crystal\|Moon Crystal]] | 1 |  | Gold | 40 | 316 | 252 |
| 15 | ![](wiki/assets/items/401.png) | [[wiki/items/401-helmet-of-life\|Helmet of Life]] | 1 |  | Gold | 100 | 792 | 630 |
| 16 | ![](wiki/assets/items/402.png) | [[wiki/items/402-armor-of-life\|Armor of Life]] | 1 |  | Gold | 150 | 1,188 | 945 |
| 17 | ![](wiki/assets/items/411.png) | [[wiki/items/411-guardian-shoes\|Guardian Shoes]] | 1 |  | Gold | 130 | 1,029 | 819 |
| 18 | ![](wiki/assets/items/412.png) | [[wiki/items/412-guardian-gloves\|Guardian Gloves]] | 1 |  | Gold | 120 | 950 | 756 |
| 19 | ![](wiki/assets/items/435.png) | [[wiki/items/435-barrier-bracelet\|Barrier Bracelet]] | 1 |  | Gold | 130 | 1,029 | 819 |
| 20 | ![](wiki/assets/items/436.png) | [[wiki/items/436-barrier-ring\|Barrier Ring]] | 1 |  | Gold | 120 | 950 | 756 |
| 21 | ![](wiki/assets/items/411.png) | [[wiki/items/411-guardian-shoes\|Guardian Shoes]] | 1 |  | Gold | 130 | 1,029 | 819 |
| 22 | ![](wiki/assets/items/412.png) | [[wiki/items/412-guardian-gloves\|Guardian Gloves]] | 1 |  | Gold | 120 | 950 | 756 |
| 23 | ![](wiki/assets/items/435.png) | [[wiki/items/435-barrier-bracelet\|Barrier Bracelet]] | 1 |  | Gold | 130 | 1,029 | 819 |
| 24 | ![](wiki/assets/items/436.png) | [[wiki/items/436-barrier-ring\|Barrier Ring]] | 1 |  | Gold | 120 | 950 | 756 |

8 entries repeat an item already listed (the client shows every entry).

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).
<!-- generated:end -->

## Notes

`Npc_Carry` lists 73-113 are where the dungeon secondaries (838-850) turn up in the client. They are flagged as non-shop lists and are probably drop pools, not shops (*guess*, [[gameplay/consumables|consumables]] §5). In play the secondaries were dungeon mob drops and were sold nowhere (*guide*, [[gameplay/consumables|consumables]] §5).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/consumables]] §5 (lists 73-113 are non-shop lists, probably drop pools) (*client + guess*)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

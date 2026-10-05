---
title: "Wren's shop (Merchant) 281"
type: "shop"
id: 281
status: "complete"
missing: []
sources: ["client: Npc_Carry.cdb shop 281", "client: UnitDB.cdb u16@a2 = 281 (units 203, 204, 330)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)", "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)", "video: [[gameplay/npc-locations]] §3 Fortress, video-measured (±3 units) (Wren 204)", "image: [[gameplay/maps-and-dungeons]] §5 (fortress layout, Wren's stock) and §2 Entry cost (Dimensional Energy 5,500 in every fortress)", "guide: [[gameplay/progression-and-economy]] §4, Crush Online shop prices (Crush stats guide, 2016)", "notes: [[gameplay/patch-history]] (WM 0328 Dimensional Energy 2,000 gold; WM 0404 Pyrotechnics sold for gold at Wren)", "player/staff: [[gameplay/crush-mechanics]] §3 (Magic Crafting Stone and Return scroll prices; dynamic NPC prices)", "staff: [[gameplay/crush-patch-notes]] 2016-12-15 (Magic Crafting Stone removed from the merchant)", "client: [[gameplay/consumables]] §4.2 (Wren sells the D potions)"]
npc: [203, 204, 330]
stock:
  - {"slot": 0, "item": 883, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 884, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 906, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 909, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 908, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 688, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 945, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 946, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 947, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 949, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 1105, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 2909, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 2910, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 2911, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 883, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63}
  - {"item": 884, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63}
  - {"item": 906, "currency": 2, "currency_name": "Gold", "base": 80, "buy": 633, "sell": 504}
  - {"item": 909, "currency": 2, "currency_name": "Gold", "base": 80, "buy": 633, "sell": 504}
  - {"item": 908, "currency": 2, "currency_name": "Gold", "base": 2500, "buy": 19800, "sell": 15750}
  - {"item": 688, "currency": 17, "currency_name": "Gold (+10%)", "base": 5000, "buy": 5500, "sell": 4050}
  - {"item": 945, "currency": 2, "currency_name": "Gold", "base": 20000, "buy": 158400, "sell": 126000}
  - {"item": 946, "currency": 2, "currency_name": "Gold", "base": 36000, "buy": 285120, "sell": 226800}
  - {"item": 947, "currency": 2, "currency_name": "Gold", "base": 170000, "buy": 1346400, "sell": 1071000}
  - {"item": 949, "currency": 2, "currency_name": "Gold", "base": 500000, "buy": 3960000, "sell": 3150000}
  - {"item": 1105, "currency": 2, "currency_name": "Gold", "base": 500, "buy": 3960, "sell": 3150}
  - {"item": 2909, "currency": 17, "currency_name": "Gold (+10%)", "base": 10000, "buy": 11000, "sell": 8100}
  - {"item": 2910, "currency": 17, "currency_name": "Gold (+10%)", "base": 10000, "buy": 11000, "sell": 8100}
  - {"item": 2911, "currency": 17, "currency_name": "Gold (+10%)", "base": 10000, "buy": 11000, "sell": 8100}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
observed_prices:
  - {"item": 883, "shown": 79, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)"}
  - {"item": 884, "shown": 79, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)"}
  - {"item": 908, "shown": 19800, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)"}
  - {"item": 688, "shown": 5500, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)"}
  - {"item": 945, "shown": 158400, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)"}
  - {"item": 946, "shown": 285120, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)"}
  - {"item": 947, "shown": 1346400, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)"}
  - {"item": 949, "shown": 3960000, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)"}
  - {"item": 1105, "shown": 3960, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)"}
  - {"item": 883, "shown": 96, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (Crush stats guide, 2016)", "note": "Crush Online price (x9.6 base)"}
  - {"item": 884, "shown": 96, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (Crush stats guide, 2016)", "note": "Crush Online price (x9.6 base)"}
  - {"item": 908, "shown": 24000, "currency": "Gold", "source": "docs: [[gameplay/progression-and-economy]] §4 (Crush stats guide, 2016)", "note": "Crush Online price (x9.6 base)"}
  - {"item": 688, "shown": 2000, "currency": "Gold", "source": "docs: [[gameplay/patch-history]] WM 0328 (patch notes)", "note": "price cut announced 28 Mar 2018; guides later show 5,500"}
---
<!-- generated:start -->
<!-- generated-keys: title=c2e85d type=ffcf9c id=d8502b sources=1bc495 npc=337b87 stock=d2e0c7 prices=b56340 price_rates=c44eae header=702516 observed_prices=bea614 -->
|  |  |
|---|---|
|  | ![Wren's shop (Merchant) 281](wiki/assets/npcs/204.png) |
| **Shop id** | `281` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/203\|NPC 203]], [[wiki/npcs/204-wren\|Wren]] (Merchant), [[wiki/npcs/330-tora\|Tora]] (Merchant) |
| **Stock** | 14 entries, 14 distinct items |
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
| 5 | ![](wiki/assets/items/688.png) | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 1 |  | Gold (+10%) | 5,000 | 5,500 | 4,050 |
| 6 | ![](wiki/assets/items/945.png) | [[wiki/items/945-auto-decomposition-hammer-d\|Auto decomposition hammer (D)]] | 1 |  | Gold | 20,000 | 158,400 | 126,000 |
| 7 | ![](wiki/assets/items/946.png) | [[wiki/items/946-auto-decomposition-hammer-c\|Auto decomposition hammer (C)]] | 1 |  | Gold | 36,000 | 285,120 | 226,800 |
| 8 | ![](wiki/assets/items/947.png) | [[wiki/items/947-auto-decomposition-hammer-b\|Auto decomposition hammer (B)]] | 1 |  | Gold | 170,000 | 1,346,400 | 1,071,000 |
| 9 | ![](wiki/assets/items/949.png) | [[wiki/items/949-auto-decomposition-hammer-a\|Auto decomposition hammer (A)]] | 1 |  | Gold | 500,000 | 3,960,000 | 3,150,000 |
| 10 | ![](wiki/assets/items/1105.png) | [[wiki/items/1105-pyrotechnics\|Pyrotechnics]] | 1 |  | Gold | 500 | 3,960 | 3,150 |
| 11 | ![](wiki/assets/items/2909.png) | [[wiki/items/2909-flare\|Flare]] | 1 |  | Gold (+10%) | 10,000 | 11,000 | 8,100 |
| 12 | ![](wiki/assets/items/2910.png) | [[wiki/items/2910-ward\|Ward]] | 1 |  | Gold (+10%) | 10,000 | 11,000 | 8,100 |
| 13 | ![](wiki/assets/items/2911.png) | [[wiki/items/2911-pinkward\|Pinkward]] | 1 |  | Gold (+10%) | 10,000 | 11,000 | 8,100 |

### Prices seen in play

Source: [[gameplay/patch-history]] WM 0328 (patch notes); [[gameplay/progression-and-economy]] §4 (Crush stats guide, 2016); [[gameplay/progression-and-economy]] §4 (guide screenshots, spring 2018)

| item | shown | formula | match | note |
|---|---|---|---|---|
| [[wiki/items/883-potion-of-health-d\|Potion of Health (D)]] | 79 Gold | 79 | yes |  |
| [[wiki/items/884-potion-of-mana-d\|Potion of Mana (D)]] | 79 Gold | 79 | yes |  |
| [[wiki/items/908-scroll-castle\|Scroll : Castle]] | 19,800 Gold | 19,800 | yes |  |
| [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 5,500 Gold | 5,500 | amount only (currency differs) |  |
| [[wiki/items/945-auto-decomposition-hammer-d\|Auto decomposition hammer (D)]] | 158,400 Gold | 158,400 | yes |  |
| [[wiki/items/946-auto-decomposition-hammer-c\|Auto decomposition hammer (C)]] | 285,120 Gold | 285,120 | yes |  |
| [[wiki/items/947-auto-decomposition-hammer-b\|Auto decomposition hammer (B)]] | 1,346,400 Gold | 1,346,400 | yes |  |
| [[wiki/items/949-auto-decomposition-hammer-a\|Auto decomposition hammer (A)]] | 3,960,000 Gold | 3,960,000 | yes |  |
| [[wiki/items/1105-pyrotechnics\|Pyrotechnics]] | 3,960 Gold | 3,960 | yes |  |
| [[wiki/items/883-potion-of-health-d\|Potion of Health (D)]] | 96 Gold | 79 | no | Crush Online price (x9.6 base) |
| [[wiki/items/884-potion-of-mana-d\|Potion of Mana (D)]] | 96 Gold | 79 | no | Crush Online price (x9.6 base) |
| [[wiki/items/908-scroll-castle\|Scroll : Castle]] | 24,000 Gold | 19,800 | no | Crush Online price (x9.6 base) |
| [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 2,000 Gold | 5,500 | no | price cut announced 28 Mar 2018; guides later show 5,500 |

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).

### Seen in

- Seen in [[gameplay/consumables|Consumables and clickables]], section *4.2 Potions*
- Seen in [[gameplay/npc-locations|NPC and point-of-interest locations]], section *3. Fortress (field 120)* at 31:37
<!-- generated:end -->

## Notes

Wren the Merchant (units 203, 204, 330) runs the fortress general store. Unit 204 stands on the Fortress east arm, at the top of the right-hand stairs (*video*, [[gameplay/npc-locations|NPC locations]] §3; *image*, [[gameplay/maps-and-dungeons|maps]] §5).

She sells HP/MP potions [D], Return / Gaia / Castle scrolls, Dimensional Energy, auto-decomposition hammers and Pyrotechnics (*image*, [[gameplay/maps-and-dungeons|maps]] §5; *client*, [[gameplay/consumables|consumables]] §4.2). Pyrotechnics became a gold item at Wren in the 4 Apr 2018 patch ([[gameplay/patch-history|patch history]] 0404). Dimensional Energy cost **5,500** gold in every fortress (*guides + image*, [[gameplay/maps-and-dungeons|maps]] §2 Entry cost).

Spring 2018 prices seen in guides are in the table above (*image*, [[gameplay/progression-and-economy|economy]] §4). In Crush Online (2016) the same shop showed potions and scrolls at 96, the Castle scroll at 24,000, Nexus Return at 480 and the Magic Crafting Stone at 48,000 gold, i.e. 9.6 x base ([[gameplay/progression-and-economy|economy]] §4).

## Behaviour

- Gold items cost 7.92 x base and sell for 6.3 x base; Dimensional Energy costs 1.1 x base (*image*, [[gameplay/progression-and-economy|economy]] §4).
- Crush Online staff described NPC prices as a "dynamic gold economy" tied to the land a nation holds. The Magic Crafting Stone moved 37,000 → 48,000 → 42,500 gold and the Return scroll 72 → 96 (*staff/player*, [[gameplay/crush-mechanics|Crush mechanics]] §3).
- The Magic Crafting Stone was taken out of the shop on 15 Dec 2016 and came only from the [Diamond] Medal Reward Box after that (*staff*, [[gameplay/crush-patch-notes|CO patch notes]] 2016-12-15).

## Sources

- [[gameplay/npc-locations]] §3 Fortress, video-measured (±3 units) (Wren 204) (*video*)
- [[gameplay/maps-and-dungeons]] §5 (fortress layout, Wren's stock) and §2 Entry cost (Dimensional Energy 5,500 in every fortress) (*image*)
- [[gameplay/progression-and-economy]] §4, Crush Online shop prices (Crush stats guide, 2016) (*guide*)
- [[gameplay/patch-history]] (WM 0328 Dimensional Energy 2,000 gold; WM 0404 Pyrotechnics sold for gold at Wren) (*notes*)
- [[gameplay/crush-mechanics]] §3 (Magic Crafting Stone and Return scroll prices; dynamic NPC prices) (*player/staff*)
- [[gameplay/crush-patch-notes]] 2016-12-15 (Magic Crafting Stone removed from the merchant) (*staff*)
- [[gameplay/consumables]] §4.2 (Wren sells the D potions) (*client*)

## Open questions

- The guides show Return and Gaia scrolls at 79 gold, which needs a base of 10 (items 911/912). This shop stocks 906/909 (base 80, 633 at these rates) ([[gameplay/progression-and-economy|economy]] §4).
- Dimensional Energy: 2,000 gold after the 28 Mar 2018 patch ([[gameplay/patch-history|patch history]] 0328), against 5,500 in the guides and base 5,000 in the client. The client value is kept.
- If prices really followed nation land (Crush Online), the server needs a rule for `price_rates`. The 7.92 / 6.3 rates are from one fortress in spring 2018.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

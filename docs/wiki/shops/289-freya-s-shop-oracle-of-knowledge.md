---
title: "Freya's shop (Oracle of Knowledge)"
type: "shop"
id: 289
status: "complete"
missing: []
sources: ["client: Npc_Carry.cdb shop 289", "client: UnitDB.cdb u16@a2 = 289 (units 200)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)", "image: [[gameplay/precept-shop]] §1, Crush Online forum screenshot (Oct 2016)", "client + guess: [[gameplay/precept-shop]] §1, §5 (unit 200 Freya is the only Oracle of Knowledge with shop 289)", "guide: [[gameplay/precept-shop]] §2 (one precept quest at a time; re-roll by dropping)", "video: [[gameplay/npc-locations]] §3 Fortress, video-measured (±3 units) (Freya 200)", "player: [[gameplay/crush-mechanics]] §7 (precepts removed in early 2017, Crush Online)"]
npc: [200]
stock:
  - {"slot": 0, "item": 1201, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 1202, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 1203, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 1204, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 1251, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 1252, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 1253, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 1201, "currency": 2, "currency_name": "Gold", "base": 10000, "buy": 79200, "sell": 63000}
  - {"item": 1202, "currency": 2, "currency_name": "Gold", "base": 10000, "buy": 79200, "sell": 63000}
  - {"item": 1203, "currency": 2, "currency_name": "Gold", "base": 10000, "buy": 79200, "sell": 63000}
  - {"item": 1204, "currency": 2, "currency_name": "Gold", "base": 10000, "buy": 79200, "sell": 63000}
  - {"item": 1251, "currency": 2, "currency_name": "Gold", "base": 25000, "buy": 198000, "sell": 157500}
  - {"item": 1252, "currency": 2, "currency_name": "Gold", "base": 25000, "buy": 198000, "sell": 157500}
  - {"item": 1253, "currency": 2, "currency_name": "Gold", "base": 25000, "buy": 198000, "sell": 157500}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
observed_prices:
  - {"item": 1201, "shown": 4650, "currency": "Gold", "source": "docs: [[gameplay/precept-shop]] §1 (Crush Online screenshot, Oct 2016)", "note": "Rank[D] precept slot; the screenshot does not say which of the D items 1201-1204 it was; Crush Online price"}
  - {"item": 1251, "shown": 9300, "currency": "Gold", "source": "docs: [[gameplay/precept-shop]] §1 (Crush Online screenshot, Oct 2016)", "note": "Rank[C] precept slot (one of 1251-1255); Crush Online price"}
  - {"item": 1301, "shown": 18600, "currency": "Gold", "source": "docs: [[gameplay/precept-shop]] §1 (Crush Online screenshot, Oct 2016)", "note": "Rank[B] precept (1301/1302); not in Npc_Carry 289; Crush Online price"}
---
<!-- generated:start -->
<!-- generated-keys: title=513feb type=ffcf9c id=6b0f4d sources=5b0863 npc=4bef22 stock=c1cbb9 prices=844572 price_rates=c44eae header=702516 -->
|  |  |
|---|---|
|  | ![Freya's shop (Oracle of Knowledge)](../assets/npcs/200.png) |
| **Shop id** | `289` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/200-freya\|Freya]] (Oracle of Knowledge) |
| **Stock** | 7 entries, 7 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 0, `c3` = 1, `c4` = 0 (meaning unknown) |

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](../assets/items/1201.png) | [[wiki/items/1201-d-rank-quest\|D Rank Quest]] | 1 |  | Gold | 10,000 | 79,200 | 63,000 |
| 1 | ![](../assets/items/1202.png) | [[wiki/items/1202-d-rank-quest\|D Rank Quest]] | 1 |  | Gold | 10,000 | 79,200 | 63,000 |
| 2 | ![](../assets/items/1203.png) | [[wiki/items/1203-d-rank-quest\|D Rank Quest]] | 1 |  | Gold | 10,000 | 79,200 | 63,000 |
| 3 | ![](../assets/items/1204.png) | [[wiki/items/1204-d-rank-quest\|D Rank Quest]] | 1 |  | Gold | 10,000 | 79,200 | 63,000 |
| 4 | ![](../assets/items/1251.png) | [[wiki/items/1251-c-rank-quest\|C Rank Quest]] | 1 |  | Gold | 25,000 | 198,000 | 157,500 |
| 5 | ![](../assets/items/1252.png) | [[wiki/items/1252-c-rank-quest\|C Rank Quest]] | 1 |  | Gold | 25,000 | 198,000 | 157,500 |
| 6 | ![](../assets/items/1253.png) | [[wiki/items/1253-c-rank-quest\|C Rank Quest]] | 1 |  | Gold | 25,000 | 198,000 | 157,500 |

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).

### Seen in

- Seen in [[gameplay/npc-locations|NPC and point-of-interest locations]], section *3. Fortress (field 120)* at 32:07
- Seen in [[gameplay/precept-shop|Precept shop and precept quests]], section *1. Shop prices*
- Seen in [[gameplay/server-rules|Server rules checklist]], section *Added from the source hunt (see ((gameplay/sources/Sources and gaps)))*
<!-- generated:end -->

## Notes

Freya (unit 200, Oracle of Knowledge) sells the **precept** scrolls. Of the three units that share her name and portrait (198, 199, 200) only 200 opens this shop, so in the final client the precept seller is Freya herself (*client + guess*, [[gameplay/precept-shop|precept shop]] §1, §5). She stands on the Fortress plaza just south of the central pillar, marked by a book icon on the minimap (*image*, [[gameplay/precept-shop|precept shop]] §5; *video*, [[gameplay/npc-locations|NPC locations]] §3).

Using a precept starts a repeatable "Rank[D/C] Crafting" quest: D items 1201-1204 start quests 800-803 and C items 1251-1253 start 811-813, all in the Fortress and ending with "return to Freya" (*client*, [[gameplay/precept-shop|precept shop]] §1, §4).

In Crush Online (Oct 2016) the shop window showed Rank[D] at **4,650**, Rank[C] at **9,300** and Rank[B] at **18,600** gold, one scroll per slot (*image*, [[gameplay/precept-shop|precept shop]] §1, [screenshot](http://i.imgur.com/ST4OtVY.jpg)).

## Behaviour

- A player can hold only **one** precept quest. It must be finished or dropped before another scroll can be used, or the game says "You can not receive this quest anymore" (*guide*, [[gameplay/precept-shop|precept shop]] §2).
- Dropping a bad roll and buying a new scroll is the way to re-roll (*guide*, [[gameplay/precept-shop|precept shop]] §2).
- Precept quests appear in their own "Precept" group in the quest log (*image*, [[gameplay/precept-shop|precept shop]] §2).
- The client quests have a level 30 prerequisite (pre1 type 4, a = 30; *guess* that it is a minimum level, [[gameplay/precept-shop|precept shop]] §4).

## Sources

- [[gameplay/precept-shop]] §1, Crush Online forum screenshot (Oct 2016) (*image*)
- [[gameplay/precept-shop]] §1, §5 (unit 200 Freya is the only Oracle of Knowledge with shop 289) (*client + guess*)
- [[gameplay/precept-shop]] §2 (one precept quest at a time; re-roll by dropping) (*guide*)
- [[gameplay/npc-locations]] §3 Fortress, video-measured (±3 units) (Freya 200) (*video*)
- [[gameplay/crush-mechanics]] §7 (precepts removed in early 2017, Crush Online) (*player*)

## Open questions

- **Price.** The 2016 shop charged 4,650 / 9,300 / 18,600 gold. The client bases are 10,000 / 25,000 (79,200 / 198,000 at this page's rates). The 2016 ratios do not fit one multiplier, so either the bases changed or the 2016 server set its own prices (*guess*, [[gameplay/precept-shop|precept shop]] §1). The front matter keeps the client prices; the server has to choose ([[gameplay/server-rules|server rules]]).
- **Stock.** No B precept (1301/1302) is stocked, and C items 1254/1255 are not stocked either; their quests 814/815 do not exist in `Quest.tsv` (*client*, [[gameplay/precept-shop|precept shop]] §1).
- **Rewards.** In 2016 the quests paid 1-5 medals and 20-150 Spellstone D at random; the client rows pay fixed Passion fragments (*guide* vs *client*, [[gameplay/precept-shop|precept shop]] §2, §4).
- Players reported that precepts were removed in early 2017 (*player*, [[gameplay/crush-mechanics|Crush mechanics]] §7). Whether Warmonger (2018) sold them is not known.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

---
title: "Athan's shop (Merits Merchant)"
type: "shop"
id: 283
status: "complete"
missing: []
sources: ["client: Npc_Carry.cdb shop 283", "client: UnitDB.cdb u16@a2 = 283 (units 207)", "docs: [[gameplay/progression-and-economy]] §4 (shop prices 7.92 x base, sell 6.3 x base; guide images)", "docs: [[gameplay/video-tutorial-walkthrough]] 14:20 (Wren 287: 79 gold; sell 315 / 630)", "contract: items.yaml server_rules.price_formula (client FUN_004e0603 / FUN_004e06b5)", "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"]
npc: [207]
stock:
  - {"slot": 0, "item": 854, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 1, "item": 855, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 2, "item": 856, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 3, "item": 857, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 4, "item": 1051, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 5, "item": 1052, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 6, "item": 1053, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 7, "item": 1054, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 8, "item": 1057, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 9, "item": 1058, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 10, "item": 1059, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 11, "item": 689, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 12, "item": 690, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 13, "item": 691, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 14, "item": 700, "count": 1, "p1": 0, "p2": 0}
  - {"slot": 15, "item": 701, "count": 1, "p1": 0, "p2": 0}
prices:
  - {"item": 854, "currency": 10, "currency_name": "Bronze Medal", "base": 2, "buy": 2, "sell": null}
  - {"item": 855, "currency": 10, "currency_name": "Bronze Medal", "base": 5, "buy": 5, "sell": null}
  - {"item": 856, "currency": 11, "currency_name": "Silver Medal", "base": 5, "buy": 5, "sell": null}
  - {"item": 857, "currency": 12, "currency_name": "Gold Medal", "base": 5, "buy": 5, "sell": null, "cost_pair": {"currency": 11, "currency_name": "Silver Medal", "amount": 5}}
  - {"item": 1051, "currency": 10, "currency_name": "Bronze Medal", "base": 4, "buy": 4, "sell": null}
  - {"item": 1052, "currency": 11, "currency_name": "Silver Medal", "base": 3, "buy": 3, "sell": null}
  - {"item": 1053, "currency": 12, "currency_name": "Gold Medal", "base": 2, "buy": 2, "sell": null}
  - {"item": 1054, "currency": 16, "currency_name": "currency 16 (Mithril medal?)", "base": 1, "buy": 1, "sell": null}
  - {"item": 1057, "currency": 10, "currency_name": "Bronze Medal", "base": 3, "buy": 3, "sell": null}
  - {"item": 1058, "currency": 10, "currency_name": "Bronze Medal", "base": 3, "buy": 3, "sell": null}
  - {"item": 1059, "currency": 10, "currency_name": "Bronze Medal", "base": 3, "buy": 3, "sell": null}
  - {"item": 689, "currency": 10, "currency_name": "Bronze Medal", "base": 1, "buy": 1, "sell": null}
  - {"item": 690, "currency": 11, "currency_name": "Silver Medal", "base": 1, "buy": 1, "sell": null}
  - {"item": 691, "currency": 12, "currency_name": "Gold Medal", "base": 1, "buy": 1, "sell": null}
  - {"item": 700, "currency": 2, "currency_name": "Gold", "base": 10, "buy": 79, "sell": 63, "cost_pair": {"currency": 18, "currency_name": "Fame", "amount": 10}}
  - {"item": 701, "currency": 2, "currency_name": "Gold", "base": 20, "buy": 158, "sell": 126, "cost_pair": {"currency": 18, "currency_name": "Fame", "amount": 50}}
price_rates: {"buy_rate": 720, "sell_rate": 700, "basis": "inferred: 7.92 = 7.20 x 1.1 (buy), 6.3 = 7.00 x 0.9 (sell) under contract price_formula; multipliers observed in 2018 play"}
header: {"c2": 0, "c3": 1, "c4": 0}
observed_prices:
  - {"item": 854, "shown": 2, "currency": "Silver Medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)", "note": "client prices it in currency 10 (bronze)"}
  - {"item": 855, "shown": 5, "currency": "Bronze Medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"}
  - {"item": 856, "shown": 5, "currency": "Silver Medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"}
  - {"item": 857, "shown": 5, "currency": "Bronze Medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)", "note": "client prices it in currency 12 (gold medal)"}
  - {"item": 1051, "shown": 4, "currency": "Bronze Medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"}
  - {"item": 1052, "shown": 3, "currency": "Silver Medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"}
  - {"item": 1053, "shown": 2, "currency": "Gold Medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"}
  - {"item": 1054, "shown": 1, "currency": "Mithril medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"}
  - {"item": 689, "shown": 1, "currency": "Bronze Medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"}
  - {"item": 690, "shown": 1, "currency": "Silver Medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"}
  - {"item": 691, "shown": 1, "currency": "Gold Medal", "source": "docs: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)"}
---
<!-- generated:start -->
<!-- generated-keys: title=c5e2ec type=ffcf9c id=3032a4 sources=401c1b npc=46007a stock=4c10be prices=29d3c2 price_rates=c44eae header=702516 observed_prices=183282 -->
|  |  |
|---|---|
|  | ![Athan's shop (Merits Merchant)](../assets/npcs/207.png) |
| **Shop id** | `283` (`Npc_Carry` shop_id = `UnitDB` u16@a2) |
| **Run by** | [[wiki/npcs/207-athan\|Athan]] (Merits Merchant) |
| **Stock** | 16 entries, 16 distinct items |
| **Price rates** | buy 720 %, sell 700 % (0x452) |
| **Header** | `c2` = 0, `c3` = 1, `c4` = 0 (meaning unknown) |

### Stock

`slot` is the index the client sends as `shop_index` when buying (C->S `0x430`). *Base* is `Item_Base` buy_price@20; *buy* and *sell* are what the shop window shows at this page's `price_rates` (client formula, see below). `p1` is the enchant level for weapons/armour or the dye colour for costumes.

| slot |  | item | count | p1 | currency | base | buy | sell |
|---|---|---|---|---|---|---|---|---|
| 0 | ![](../assets/items/854.png) | [[wiki/items/854-shining-passion\|Shining Passion]] | 1 |  | Bronze Medal | 2 | 2 | – |
| 1 | ![](../assets/items/855.png) | [[wiki/items/855-mysterious-passion\|Mysterious Passion]] | 1 |  | Bronze Medal | 5 | 5 | – |
| 2 | ![](../assets/items/856.png) | [[wiki/items/856-brilliant-passion\|Brilliant Passion]] | 1 |  | Silver Medal | 5 | 5 | – |
| 3 | ![](../assets/items/857.png) | [[wiki/items/857-amplifying-passion\|Amplifying Passion]] | 1 |  | Gold Medal | 5 | 5 | – |
| 4 | ![](../assets/items/1051.png) | [[wiki/items/1051-bronze-medal-reward-box\|(Bronze) Medal Reward Box]] | 1 |  | Bronze Medal | 4 | 4 | – |
| 5 | ![](../assets/items/1052.png) | [[wiki/items/1052-silver-medal-reward-box\|(Silver) Medal Reward Box]] | 1 |  | Silver Medal | 3 | 3 | – |
| 6 | ![](../assets/items/1053.png) | [[wiki/items/1053-gold-medal-reward-box\|(Gold) Medal Reward Box]] | 1 |  | Gold Medal | 2 | 2 | – |
| 7 | ![](../assets/items/1054.png) | [[wiki/items/1054-mithril-medal-reward-box\|(Mithril) Medal Reward Box]] | 1 |  | currency 16 (Mithril medal?) | 1 | 1 | – |
| 8 | ![](../assets/items/1057.png) | [[wiki/items/1057-random-box-of-dye\|Random box of dye]] | 1 |  | Bronze Medal | 3 | 3 | – |
| 9 | ![](../assets/items/1058.png) | [[wiki/items/1058-random-box-of-dye\|Random box of dye]] | 1 |  | Bronze Medal | 3 | 3 | – |
| 10 | ![](../assets/items/1059.png) | [[wiki/items/1059-random-box-of-dye\|Random box of dye]] | 1 |  | Bronze Medal | 3 | 3 | – |
| 11 | ![](../assets/items/689.png) | [[wiki/items/689-tier-1-time-energy\|Tier 1 : Time energy]] | 1 |  | Bronze Medal | 1 | 1 | – |
| 12 | ![](../assets/items/690.png) | [[wiki/items/690-tier-2-time-energy\|Tier 2 : Time energy]] | 1 |  | Silver Medal | 1 | 1 | – |
| 13 | ![](../assets/items/691.png) | [[wiki/items/691-tier-3-time-energy\|Tier 3 : Time energy]] | 1 |  | Gold Medal | 1 | 1 | – |
| 14 | ![](../assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 1 |  | Gold | 10 | 79 | 63 |
| 15 | ![](../assets/items/701.png) | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] | 1 |  | Gold | 20 | 158 | 126 |

Second price (`Item_Base` cost pair @24/@26, charged as listed). The patch notes price Amplifying Passion at "5 silver **or** 3 gold medals" ([[gameplay/reinforce-and-runes|runes]] §5), so this is probably an alternative way to pay, not an extra charge (*guess*): [[wiki/items/857-amplifying-passion|Amplifying Passion]]: 5 Silver Medal; [[wiki/items/700-crystal-blue|Crystal : Blue]]: 10 Fame; [[wiki/items/701-crystal-yellow|Crystal : Yellow]]: 50 Fame

### Prices seen in play

Source: [[gameplay/progression-and-economy]] §4 Athan (noob guide image)

| item | shown | formula | match | note |
|---|---|---|---|---|
| [[wiki/items/854-shining-passion\|Shining Passion]] | 2 Silver Medal | 2 | amount only (currency differs) | client prices it in currency 10 (bronze) |
| [[wiki/items/855-mysterious-passion\|Mysterious Passion]] | 5 Bronze Medal | 5 | yes |  |
| [[wiki/items/856-brilliant-passion\|Brilliant Passion]] | 5 Silver Medal | 5 | yes |  |
| [[wiki/items/857-amplifying-passion\|Amplifying Passion]] | 5 Bronze Medal | 5 | amount only (currency differs) | client prices it in currency 12 (gold medal) |
| [[wiki/items/1051-bronze-medal-reward-box\|(Bronze) Medal Reward Box]] | 4 Bronze Medal | 4 | yes |  |
| [[wiki/items/1052-silver-medal-reward-box\|(Silver) Medal Reward Box]] | 3 Silver Medal | 3 | yes |  |
| [[wiki/items/1053-gold-medal-reward-box\|(Gold) Medal Reward Box]] | 2 Gold Medal | 2 | yes |  |
| [[wiki/items/1054-mithril-medal-reward-box\|(Mithril) Medal Reward Box]] | 1 Mithril medal | 1 | yes |  |
| [[wiki/items/689-tier-1-time-energy\|Tier 1 : Time energy]] | 1 Bronze Medal | 1 | yes |  |
| [[wiki/items/690-tier-2-time-energy\|Tier 2 : Time energy]] | 1 Silver Medal | 1 | yes |  |
| [[wiki/items/691-tier-3-time-energy\|Tier 3 : Time energy]] | 1 Gold Medal | 1 | yes |  |

### How prices are worked out

The client computes every price from `Item_Base` (contract `price_formula`, `FUN_004e0603` buy, `FUN_004e06b5` sell): gold-type prices are *base × buy_rate / 100 + 10 %*, sell prices *base × sell_rate / 100 − 10 %*; Dimensional Energy (currency 17) costs base + 10 %; medal currencies (9–12, 15, 16) are charged as listed and cannot be sold back. The rates come from the server (`0x452`). In 2018 gold items cost **7.92 ×** base and sold for **6.3 ×** base ([[gameplay/progression-and-economy|economy]] §4, [[gameplay/video-tutorial-walkthrough|tutorial video]] 14:20), which is buy_rate 720 and sell_rate 700 (*inferred*). The guide's 10 % fort tax may be the +10 % (*guess*).

### Seen in

- Seen in [[gameplay/consumables|Consumables and clickables]], section *5. Where the inputs come from*
- Seen in [[gameplay/npc-locations|NPC and point-of-interest locations]], section *3. Fortress (field 120)* at 38:01
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

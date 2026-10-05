---
title: "Bag and warehouse expansion"
type: "shop"
id: 1001
status: "complete"
missing: []
sources: ["client: ExpandSlot.cdb", "contract: items.yaml expand_capacity 0x47f, server_rules capacity", "docs: [[gameplay/video-character-creation-and-tutorial]] 16:20"]
steps:
  - {"step": 1, "bag": {"currency": 2, "amount": 0}, "warehouse": {"currency": 2, "amount": 0}, "cost3": 0}
  - {"step": 2, "bag": {"currency": 2, "amount": 0}, "warehouse": {"currency": 2, "amount": 0}, "cost3": 0}
  - {"step": 3, "bag": {"currency": 2, "amount": 0}, "warehouse": {"currency": 13, "amount": 40}, "cost3": 1000000}
  - {"step": 4, "bag": {"currency": 2, "amount": 0}, "warehouse": {"currency": 13, "amount": 80}, "cost3": 2000000}
  - {"step": 5, "bag": {"currency": 2, "amount": 5000}, "warehouse": {"currency": 13, "amount": 250}, "cost3": 5000000}
  - {"step": 6, "bag": {"currency": 2, "amount": 10000}, "warehouse": {"currency": 13, "amount": 500}, "cost3": 10000000}
  - {"step": 7, "bag": {"currency": 13, "amount": 100}, "warehouse": {"currency": 13, "amount": 750}, "cost3": 20000000}
  - {"step": 8, "bag": {"currency": 13, "amount": 250}, "warehouse": {"currency": 13, "amount": 1000}, "cost3": 50000000}
  - {"step": 9, "bag": {"currency": 13, "amount": 250}, "warehouse": {"currency": 13, "amount": 1250}, "cost3": 0}
  - {"step": 10, "bag": {"currency": 13, "amount": 500}, "warehouse": {"currency": 13, "amount": 1500}, "cost3": 0}
  - {"step": 11, "bag": {"currency": 13, "amount": 500}, "warehouse": {"currency": 13, "amount": 1500}, "cost3": 0}
  - {"step": 12, "bag": {"currency": 13, "amount": 500}, "warehouse": {"currency": 13, "amount": 2000}, "cost3": 0}
  - {"step": 13, "bag": {"currency": 13, "amount": 1000}, "warehouse": {"currency": 13, "amount": 2000}, "cost3": 0}
  - {"step": 14, "bag": {"currency": 13, "amount": 1000}, "warehouse": {"currency": 13, "amount": 3000}, "cost3": 0}
  - {"step": 15, "bag": {"currency": 0, "amount": 0}, "warehouse": {"currency": 13, "amount": 3000}, "cost3": 0}
  - {"step": 16, "bag": {"currency": 0, "amount": 0}, "warehouse": {"currency": 13, "amount": 4000}, "cost3": 0}
  - {"step": 17, "bag": {"currency": 0, "amount": 0}, "warehouse": {"currency": 13, "amount": 4000}, "cost3": 0}
  - {"step": 18, "bag": {"currency": 0, "amount": 0}, "warehouse": {"currency": 13, "amount": 5000}, "cost3": 0}
observed_prices:
  - {"what": "bag step 5", "shown": 5000, "currency": "Gold", "source": "docs: [[gameplay/video-character-creation-and-tutorial]] 16:20 (lesson 706 'Expand your Inventory': 'Gold : 5000')"}
---
<!-- generated:start -->
<!-- generated-keys: title=ee1fc4 type=ffcf9c id=dd0190 sources=e994a5 steps=089a2b observed_prices=93be22 -->
|  |  |
|---|---|
| **What** | Prices of each extra row (5 slots) of the bag and the personal warehouse |
| **Packet** | C->S / S->C `0x47f` {container 1 bag / 6 warehouse, step} (contract `expand_capacity`) |
| **Limits** | bag up to 14 rows, warehouse up to 18 (contract `capacity`) |

### Steps

Currency 2 = gold, 13 = jewels (yellow then purple, contract `jewels`). `cost3` (@14) is unknown: it rises 1,000,000 → 50,000,000 and is 0 from step 9.

| step (row) | bag | warehouse | cost3 |
|---|---|---|---|
| 1 | 0 Gold | 0 Gold | 0 |
| 2 | 0 Gold | 0 Gold | 0 |
| 3 | 0 Gold | 40 Jewels (yellow + purple) | 1,000,000 |
| 4 | 0 Gold | 80 Jewels (yellow + purple) | 2,000,000 |
| 5 | 5,000 Gold | 250 Jewels (yellow + purple) | 5,000,000 |
| 6 | 10,000 Gold | 500 Jewels (yellow + purple) | 10,000,000 |
| 7 | 100 Jewels (yellow + purple) | 750 Jewels (yellow + purple) | 20,000,000 |
| 8 | 250 Jewels (yellow + purple) | 1,000 Jewels (yellow + purple) | 50,000,000 |
| 9 | 250 Jewels (yellow + purple) | 1,250 Jewels (yellow + purple) | 0 |
| 10 | 500 Jewels (yellow + purple) | 1,500 Jewels (yellow + purple) | 0 |
| 11 | 500 Jewels (yellow + purple) | 1,500 Jewels (yellow + purple) | 0 |
| 12 | 500 Jewels (yellow + purple) | 2,000 Jewels (yellow + purple) | 0 |
| 13 | 1,000 Jewels (yellow + purple) | 2,000 Jewels (yellow + purple) | 0 |
| 14 | 1,000 Jewels (yellow + purple) | 3,000 Jewels (yellow + purple) | 0 |
| 15 | – | 3,000 Jewels (yellow + purple) | 0 |
| 16 | – | 4,000 Jewels (yellow + purple) | 0 |
| 17 | – | 4,000 Jewels (yellow + purple) | 0 |
| 18 | – | 5,000 Jewels (yellow + purple) | 0 |

### Seen in play

- bag step 5: 5,000 Gold ([[gameplay/video-character-creation-and-tutorial]] 16:20 (lesson 706 'Expand your Inventory': 'Gold : 5000'))

### Seen in

- Seen in [[gameplay/classes-and-legions|Classes, nations and legions]], section *3. Legions (guilds)*
- Seen in [[gameplay/crush-mechanics|Crush Online mechanics from the forum]], section *10. Economy, VIP, cash shop*
- Seen in [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]], section *Timeline*
- Seen in [[gameplay/items-and-crafting|Items, upgrades and crafting]], section *6. Inventory and storage*
- Seen in [[gameplay/progression-and-economy|Progression and economy]], section *3. Currencies*
- Seen in [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]], section *Training Camp (field 92) and back* at 15:50
- Seen in [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]], section *Steps* at 19:30
- Seen in [[gameplay/warmonger-forum|Warmonger forum (2018)]], section *8. VIP and account*
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

---
title: "Bracelet of Life"
type: "item"
id: 407
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 407"]
name_key: "ItemName_407"
kind: 56
kind_name: "Bracelet"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 130}
cost_pair:
  - {"currency": 2, "amount": 130}
stats:
  - {"code": 1, "stat": "Attack", "value": 4, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "level"}
  - {"code": 32, "stat": "Health Regeneration", "value": 1, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 32, "stat": "Health Regeneration", "value": 2, "scale": "tier"}
  - {"code": 1, "stat": "Attack", "value": 40, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 200, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 8, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_10.png", "index": 34}
obtained_from:
  - {"how": "shop", "shop": 36}
  - {"how": "shop", "shop": 44}
  - {"how": "shop", "shop": 60}
  - {"how": "shop", "shop": 81}
  - {"how": "shop", "shop": 93}
  - {"how": "shop", "shop": 105}
  - {"how": "shop", "shop": 113}
  - {"how": "shop", "shop": 117}
  - {"how": "shop", "shop": 214}
  - {"how": "craft", "recipe": 11}
  - {"how": "craft", "recipe": 2011}
  - {"how": "quest_reward", "quest": 10, "count": 1}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=27f5f4 type=d36ca9 id=e6de89 sources=50ace3 name_key=631cb1 kind=54ceb9 kind_name=c2576a classes=92d079 bind=2be88c price=05bfea cost_pair=c1b652 stats=9671d1 reinforce=356a19 icon=9fd4c9 obtained_from=cc1eed -->
|  |  |
|---|---|
|  | ![Bracelet of Life](../assets/items/407.png) |
| **Item id** | `407` |
| **Kind** | Bracelet (56) |
| **Classes** | all |
| **Buy price** | 130 Gold |
| **Icon** | `ui/icons/Items_10.png` cell 34 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Attack | +4 | × (tier × 15 + reinforce level) | 1 |
| Health | +20 | × (tier × 15 + reinforce level) | 31 |
| Health Regeneration | +1 | × (tier × 15 + reinforce level) | 32 |
| Health | +20 | × tier | 31 |
| Health Regeneration | +2 | × tier | 32 |
| Attack | +40 | flat | 1 |
| Health | +200 | flat | 31 |
| Health Regeneration | +8 | flat | 32 |

### Reinforcement

ItemSancMet row 1 (inferred from Item_Base +0x92), 1,000 gold per attempt. Success rates are not in the client.

| step | materials |
|---|---|
| 1 | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] × 1 |
| 2 | [[wiki/items/602-blue-passion-piece-d\|Blue Passion Piece (D)]] × 1 |
| 3 | [[wiki/items/603-blue-passion-fragments-c\|Blue Passion Fragments (C)]] × 1 |
| 4 | [[wiki/items/604-blue-passion-piece-c\|Blue Passion Piece (C)]] × 2 |
| 5 | [[wiki/items/605-blue-passion-fragments-b\|Blue Passion Fragments (B)]] × 5 |
| 6 | [[wiki/items/606-blue-passion-piece-b\|Blue Passion Piece (B)]] × 7 |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 11 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |
| 2011 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |

### Where to get it

- Sold in [[wiki/shops/36-shop-36-no-npc|Shop 36 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/44-shop-44-no-npc|Shop 44 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/60-shop-60-no-npc|Shop 60 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/81-shop-81-no-npc|Shop 81 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/93-shop-93-no-npc|Shop 93 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/105-shop-105-no-npc|Shop 105 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/113-shop-113-no-npc|Shop 113 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/117-shop-117-no-npc|Shop 117 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/214-shop-214-no-npc|Shop 214 (no NPC)]] (no NPC found)
- Reward of quest [[wiki/quests/10-find-the-secret-document|Find the Secret Document]] × 1
- Hero gacha pool 00, grade 3 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)

### Mentioned in

- [[gameplay/gear-stats|Gear stats (Crush Online artifacts)]]
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]
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

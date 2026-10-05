---
title: "Necklace of Life"
type: "item"
id: 405
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 405"]
name_key: "ItemName_405"
kind: 54
kind_name: "Necklace"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 150}
cost_pair:
  - {"currency": 2, "amount": 150}
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
icon: {"file": "Items_10.png", "index": 32}
obtained_from:
  - {"how": "shop", "shop": 31}
  - {"how": "shop", "shop": 47}
  - {"how": "shop", "shop": 55}
  - {"how": "shop", "shop": 76}
  - {"how": "shop", "shop": 88}
  - {"how": "shop", "shop": 100}
  - {"how": "shop", "shop": 212}
  - {"how": "craft", "recipe": 9}
  - {"how": "craft", "recipe": 2009}
  - {"how": "quest_reward", "quest": 100, "count": 1}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=3f8b96 type=d36ca9 id=7ee51d sources=3cb7f8 name_key=65b8c0 kind=80e28a kind_name=7b4b74 classes=92d079 bind=2be88c price=6d19d1 cost_pair=ca8a4e stats=9671d1 reinforce=356a19 icon=01e276 obtained_from=7b73c4 -->
|  |  |
|---|---|
|  | ![Necklace of Life](wiki/assets/items/405.png) |
| **Item id** | `405` |
| **Kind** | Necklace (54) |
| **Classes** | all |
| **Buy price** | 150 Gold |
| **Icon** | `ui/icons/Items_10.png` cell 32 |

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
| 9 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |
| 2009 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |

### Where to get it

- Sold in [[wiki/shops/31-shop-31-no-npc|Shop 31 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/47-shop-47-no-npc|Shop 47 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/55-shop-55-no-npc|Shop 55 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/76-shop-76-no-npc|Shop 76 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/88-shop-88-no-npc|Shop 88 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/100-shop-100-no-npc|Shop 100 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/212-shop-212-no-npc|Shop 212 (no NPC)]] (no NPC found)
- Reward of quest [[wiki/quests/100-hunting-for-furs|Hunting for Furs]] × 1
- Hero gacha pool 00, grade 3 (Gacha_00.cdb; odds are server side)
- Hero gacha pool 01, grade 3 (Gacha_01.cdb; odds are server side)
- Hero gacha pool 04, grade 3 (Gacha_04.cdb; odds are server side)

### Mentioned in

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

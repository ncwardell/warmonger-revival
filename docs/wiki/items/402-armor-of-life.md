---
title: "Armor of Life"
type: "item"
id: 402
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 402"]
name_key: "ItemName_402"
kind: 51
kind_name: "Armor"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 150}
cost_pair:
  - {"currency": 2, "amount": 150}
stats:
  - {"code": 6, "stat": "Armor", "value": 2, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 1, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 25, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 12, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 6, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 250, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 10, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_10.png", "index": 13}
obtained_from:
  - {"how": "shop", "shop": 28}
  - {"how": "shop", "shop": 40}
  - {"how": "shop", "shop": 52}
  - {"how": "shop", "shop": 73}
  - {"how": "shop", "shop": 85}
  - {"how": "shop", "shop": 97}
  - {"how": "shop", "shop": 109}
  - {"how": "shop", "shop": 215}
  - {"how": "craft", "recipe": 6}
  - {"how": "craft", "recipe": 2006}
  - {"how": "quest_reward", "quest": 5, "count": 1}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=b634ee type=d36ca9 id=5e6367 sources=7103b3 name_key=305e0f kind=b7eb6c kind_name=e687cb classes=92d079 bind=2be88c price=6d19d1 cost_pair=ca8a4e stats=ec86ed reinforce=356a19 icon=a5b1b1 obtained_from=6e93d2 -->
|  |  |
|---|---|
|  | ![Armor of Life](wiki/assets/items/402.png) |
| **Item id** | `402` |
| **Kind** | Armor (51) |
| **Classes** | all |
| **Buy price** | 150 Gold |
| **Icon** | `ui/icons/Items_10.png` cell 13 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +2 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +1 | × (tier × 15 + reinforce level) | 7 |
| Health | +25 | × (tier × 15 + reinforce level) | 31 |
| Health | +20 | × tier | 31 |
| Mana | +10 | × tier | 33 |
| Armor | +12 | flat | 6 |
| Magic Resist | +6 | flat | 7 |
| Health | +250 | flat | 31 |
| Movement(%) | Movement +10% | flat | 105 |

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
| 6 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |
| 2006 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |

### Where to get it

- Sold in [[wiki/shops/28-shop-28-no-npc|Shop 28 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/40-shop-40-no-npc|Shop 40 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/52-shop-52-no-npc|Shop 52 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/73-shop-73-no-npc|Shop 73 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/85-shop-85-no-npc|Shop 85 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/97-shop-97-no-npc|Shop 97 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/109-shop-109-no-npc|Shop 109 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/215-shop-215-no-npc|Shop 215 (no NPC)]] (no NPC found)
- Reward of quest [[wiki/quests/5-united-problem-solvers|United Problem Solvers]] × 1
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

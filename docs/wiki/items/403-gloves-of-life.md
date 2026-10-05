---
title: "Gloves of Life"
type: "item"
id: 403
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 403"]
name_key: "ItemName_403"
kind: 52
kind_name: "Gloves"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 130}
cost_pair:
  - {"currency": 2, "amount": 130}
stats:
  - {"code": 6, "stat": "Armor", "value": 2, "scale": "level"}
  - {"code": 7, "stat": "Magic Resist", "value": 1, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 25, "scale": "level"}
  - {"code": 31, "stat": "Health", "value": 20, "scale": "tier"}
  - {"code": 33, "stat": "Mana", "value": 10, "scale": "tier"}
  - {"code": 6, "stat": "Armor", "value": 10, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 5, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 130, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 20, "scale": "flat"}
reinforce: 1
icon: {"file": "Items_10.png", "index": 14}
obtained_from:
  - {"how": "shop", "shop": 32}
  - {"how": "shop", "shop": 48}
  - {"how": "shop", "shop": 56}
  - {"how": "shop", "shop": 77}
  - {"how": "shop", "shop": 89}
  - {"how": "shop", "shop": 101}
  - {"how": "shop", "shop": 216}
  - {"how": "craft", "recipe": 7}
  - {"how": "craft", "recipe": 2007}
  - {"how": "quest_reward", "quest": 2, "count": 1}
  - {"how": "gacha", "pool": 0}
  - {"how": "gacha", "pool": 1}
  - {"how": "gacha", "pool": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=a66ac6 type=d36ca9 id=8980dc sources=5422f1 name_key=bf3f9e kind=a93349 kind_name=f6564c classes=92d079 bind=2be88c price=05bfea cost_pair=c1b652 stats=f4f99a reinforce=356a19 icon=c03e6f obtained_from=da954b -->
|  |  |
|---|---|
|  | ![Gloves of Life](../assets/items/403.png) |
| **Item id** | `403` |
| **Kind** | Gloves (52) |
| **Classes** | all |
| **Buy price** | 130 Gold |
| **Icon** | `ui/icons/Items_10.png` cell 14 |

### Stats

Weapon and armour stats grow with the item: the client multiplies the first three option slots by *tier × 15 + reinforce level* and the next three by the *tier*; the rest are flat (`FUN_004410d6`, *client*; reading of the two multipliers is *inferred*).

| stat | value | applies | code |
|---|---|---|---|
| Armor | +2 | × (tier × 15 + reinforce level) | 6 |
| Magic Resist | +1 | × (tier × 15 + reinforce level) | 7 |
| Health | +25 | × (tier × 15 + reinforce level) | 31 |
| Health | +20 | × tier | 31 |
| Mana | +10 | × tier | 33 |
| Armor | +10 | flat | 6 |
| Magic Resist | +5 | flat | 7 |
| Health | +130 | flat | 31 |
| Movement(%) | Movement +20% | flat | 105 |

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
| 7 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |
| 2007 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10 | 150 | 100 |

### Where to get it

- Sold in [[wiki/shops/32-shop-32-no-npc|Shop 32 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/48-shop-48-no-npc|Shop 48 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/56-shop-56-no-npc|Shop 56 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/77-shop-77-no-npc|Shop 77 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/89-shop-89-no-npc|Shop 89 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/101-shop-101-no-npc|Shop 101 (no NPC)]] (no NPC found)
- Sold in [[wiki/shops/216-shop-216-no-npc|Shop 216 (no NPC)]] (no NPC found)
- Reward of quest [[wiki/quests/2-the-slime-is-mine|The Slime is mine]] × 1
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

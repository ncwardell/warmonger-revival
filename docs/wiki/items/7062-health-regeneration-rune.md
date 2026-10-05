---
title: "Health Regeneration Rune"
type: "item"
id: 7062
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7062", "client (server-only table): Item_Jewel.cdb id 62"]
name_key: "ItemName_7062"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 32, "stat": "Health Regeneration", "value": 2, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 20, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 7}
icon: {"file": "Items_28.png", "index": 46}
obtained_from:
  - {"how": "craft", "recipe": 1807}
  - {"how": "quest_reward", "quest": 49, "count": 1}
  - {"how": "quest_reward", "quest": 784, "count": 1}
  - {"how": "random_box", "box": 46}
---
<!-- generated:start -->
<!-- generated-keys: title=6644fe type=d36ca9 id=48379a sources=5cd1c9 name_key=b6d27e kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=289a96 options=f9ea2e icon=12c590 obtained_from=d3f32f -->
|  |  |
|---|---|
|  | ![Health Regeneration Rune](wiki/assets/items/7062.png) |
| **Item id** | `7062` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_28.png` cell 46 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Health Regeneration | +2 | flat | 32 |
| Health Regeneration | +20 | flat (from Item_Jewel) | 32 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 7 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1807 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/802-garnet\|Garnet]] × 1 | 175 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/49-war-objects|War - Objects]] × 1
- Reward of quest [[wiki/quests/784-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]] × 1
- In random box table row 46 (RandomBox.cdb; odds are server side)
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

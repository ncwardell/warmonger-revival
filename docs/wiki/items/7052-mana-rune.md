---
title: "Mana Rune"
type: "item"
id: 7052
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7052", "client (server-only table): Item_Jewel.cdb id 52"]
name_key: "ItemName_7052"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 33, "stat": "Mana", "value": 20, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 40, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 6}
icon: {"file": "Items_27.png", "index": 60}
obtained_from:
  - {"how": "craft", "recipe": 1806}
  - {"how": "quest_reward", "quest": 53, "count": 1}
  - {"how": "quest_reward", "quest": 123, "count": 1}
  - {"how": "random_box", "box": 46}
---
<!-- generated:start -->
<!-- generated-keys: title=1e6304 type=d36ca9 id=6ed3c5 sources=6c9c71 name_key=7a0ff5 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=0b3548 options=533fa4 icon=6397a6 obtained_from=1fe5d9 -->
|  |  |
|---|---|
|  | ![Mana Rune](wiki/assets/items/7052.png) |
| **Item id** | `7052` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_27.png` cell 60 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Mana | +20 | flat | 33 |
| Mana | +40 | flat (from Item_Jewel) | 33 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 6 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1806 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/806-emerald\|Emerald]] × 2 | 200 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/53-safety-factor-management|Safety factor Management]] × 1
- Reward of quest [[wiki/quests/123-rune-reinforcement|Rune Reinforcement]] × 1
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

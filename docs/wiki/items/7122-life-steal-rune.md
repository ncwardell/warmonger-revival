---
title: "Life Steal Rune"
type: "item"
id: 7122
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7122", "client (server-only table): Item_Jewel.cdb id 122"]
name_key: "ItemName_7122"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 41, "stat": "Life Steal(%)", "value": 1, "scale": "flat"}
  - {"code": 41, "stat": "Life Steal(%)", "value": 3, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 13}
icon: {"file": "Items_28.png", "index": 36}
obtained_from:
  - {"how": "craft", "recipe": 1813}
  - {"how": "quest_reward", "quest": 23, "count": 1}
  - {"how": "quest_reward", "quest": 24, "count": 1}
  - {"how": "quest_reward", "quest": 25, "count": 1}
  - {"how": "quest_reward", "quest": 46, "count": 1}
  - {"how": "random_box", "box": 48}
---
<!-- generated:start -->
<!-- generated-keys: title=431cea type=d36ca9 id=4f4913 sources=bb207b name_key=a24d40 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=b86970 options=1b1fe1 icon=820784 obtained_from=6c87ea -->
|  |  |
|---|---|
|  | ![Life Steal Rune](wiki/assets/items/7122.png) |
| **Item id** | `7122` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_28.png` cell 36 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Life Steal(%) | Life Steal +1% | flat | 41 |
| Life Steal(%) | Life Steal +3% | flat (from Item_Jewel) | 41 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 13 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1813 | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/802-garnet\|Garnet]] × 5 | 0 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/23-stepping-up-your-game|Stepping up your game]] × 1
- Reward of quest [[wiki/quests/24-stepping-up-your-game|Stepping up your game]] × 1
- Reward of quest [[wiki/quests/25-stepping-up-your-game|Stepping up your game]] × 1
- Reward of quest [[wiki/quests/46-to-oracle-of-knowledge|To Oracle of knowledge]] × 1
- In random box table row 48 (RandomBox.cdb; odds are server side)

### Mentioned in

- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
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

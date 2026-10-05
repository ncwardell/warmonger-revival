---
title: "Movement(%) Rune"
type: "item"
id: 7162
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7162", "client (server-only table): Item_Jewel.cdb id 162"]
name_key: "ItemName_7162"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 2, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 3, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 17}
icon: {"file": "Items_29.png", "index": 52}
obtained_from:
  - {"how": "craft", "recipe": 1817}
  - {"how": "quest_reward", "quest": 34, "count": 1}
  - {"how": "quest_reward", "quest": 44, "count": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=e6c26c type=d36ca9 id=dff52c sources=9ffb88 name_key=5362ad kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=55ac0f options=30ea72 icon=c26d74 obtained_from=4c0696 -->
|  |  |
|---|---|
|  | ![Movement(%) Rune](wiki/assets/items/7162.png) |
| **Item id** | `7162` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_29.png` cell 52 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Movement(%) | Movement +2% | flat | 105 |
| Movement(%) | Movement +3% | flat (from Item_Jewel) | 105 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 17 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1817 | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/814-topaz\|Topaz]] × 5 | 0 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/34-tow-canyon|Tow Canyon]] × 1
- Reward of quest [[wiki/quests/44-innocence-report|Innocence report]] × 1
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

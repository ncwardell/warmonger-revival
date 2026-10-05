---
title: "Magic Resist Rune"
type: "item"
id: 7032
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7032", "client (server-only table): Item_Jewel.cdb id 32"]
name_key: "ItemName_7032"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 7, "stat": "Magic Resist", "value": 6, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 3, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 4}
icon: {"file": "Items_28.png", "index": 56}
obtained_from:
  - {"how": "craft", "recipe": 1804}
  - {"how": "quest_reward", "quest": 41, "count": 1}
  - {"how": "quest_reward", "quest": 122, "count": 1}
  - {"how": "random_box", "box": 47}
---
<!-- generated:start -->
<!-- generated-keys: title=9c916e type=d36ca9 id=b3a1ea sources=152531 name_key=849a90 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=1f8000 options=2ddee2 icon=8606c0 obtained_from=e838dd -->
|  |  |
|---|---|
|  | ![Magic Resist Rune](wiki/assets/items/7032.png) |
| **Item id** | `7032` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_28.png` cell 56 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic Resist | +6 | flat | 7 |
| Magic Resist | +3 | flat (from Item_Jewel) | 7 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 4 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1804 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/808-moonstone\|Moonstone]] × 2 | 200 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/41-innocence-s-recovery-operation|Innocence's recovery operation]] × 1
- Reward of quest [[wiki/quests/122-rune-equipment|Rune Equipment.]] × 1
- In random box table row 47 (RandomBox.cdb; odds are server side)
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

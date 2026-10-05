---
title: "Magic Resist Rune"
type: "item"
id: 7039
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7039", "client (server-only table): Item_Jewel.cdb id 39"]
name_key: "ItemName_7039"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 7
stats:
  - {"code": 7, "stat": "Magic Resist", "value": 46, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 23, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 4}
icon: {"file": "Items_28.png", "index": 63}
obtained_from:
  - {"how": "jewel_craft", "recipe": 37}
---
<!-- generated:start -->
<!-- generated-keys: title=9c916e type=d36ca9 id=5d6f91 sources=875e0b name_key=f471a7 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=902ba3 stats=3c366d options=2ddee2 icon=61bcd0 obtained_from=984d5a -->
|  |  |
|---|---|
|  | ![Magic Resist Rune](wiki/assets/items/7039.png) |
| **Item id** | `7039` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 7 |
| **Icon** | `ui/icons/Items_28.png` cell 63 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic Resist | +46 | flat | 7 |
| Magic Resist | +23 | flat (from Item_Jewel) | 7 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 4 | rune grade? |

Jewel upgrade (JewelSocketMake 37): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 100, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 60, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7038-magic-resist-rune|Magic Resist Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.
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

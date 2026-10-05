---
title: "Movement(%) Rune"
type: "item"
id: 7170
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7170", "client (server-only table): Item_Jewel.cdb id 170"]
name_key: "ItemName_7170"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 11, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 29, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 17}
icon: {"file": "Items_29.png", "index": 60}
obtained_from:
  - {"how": "jewel_craft", "recipe": 168}
---
<!-- generated:start -->
<!-- generated-keys: title=e6c26c type=d36ca9 id=a2456a sources=acef7e name_key=797d9d kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=53a42a options=30ea72 icon=20fcd0 obtained_from=8edc5b -->
|  |  |
|---|---|
|  | ![Movement(%) Rune](wiki/assets/items/7170.png) |
| **Item id** | `7170` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_29.png` cell 60 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Movement(%) | Movement +11% | flat | 105 |
| Movement(%) | Movement +29% | flat (from Item_Jewel) | 105 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 17 | rune grade? |

Jewel upgrade (JewelSocketMake 168): [[wiki/items/702-crystal-red|Crystal : Red]] × 40, [[wiki/items/614-red-passion-piece-c|Red Passion Piece (C)]] × 20, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7169-movement-rune|Movement(%) Rune]].

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

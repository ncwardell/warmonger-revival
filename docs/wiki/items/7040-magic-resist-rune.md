---
title: "Magic Resist Rune"
type: "item"
id: 7040
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7040", "client (server-only table): Item_Jewel.cdb id 40"]
name_key: "ItemName_7040"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 7, "stat": "Magic Resist", "value": 53, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 29, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 4}
icon: {"file": "Items_29.png", "index": 0}
obtained_from:
  - {"how": "jewel_craft", "recipe": 38}
---
<!-- generated:start -->
<!-- generated-keys: title=9c916e type=d36ca9 id=491fd8 sources=0ad7c6 name_key=bc1cff kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=ff8540 options=2ddee2 icon=4b82a4 obtained_from=478b23 -->
|  |  |
|---|---|
|  | ![Magic Resist Rune](wiki/assets/items/7040.png) |
| **Item id** | `7040` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_29.png` cell 0 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic Resist | +53 | flat | 7 |
| Magic Resist | +29 | flat (from Item_Jewel) | 7 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 4 | rune grade? |

Jewel upgrade (JewelSocketMake 38): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 10, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7039-magic-resist-rune|Magic Resist Rune]].

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

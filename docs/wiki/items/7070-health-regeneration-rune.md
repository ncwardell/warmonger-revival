---
title: "Health Regeneration Rune"
type: "item"
id: 7070
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7070", "client (server-only table): Item_Jewel.cdb id 70"]
name_key: "ItemName_7070"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 32, "stat": "Health Regeneration", "value": 17, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 192, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 7}
icon: {"file": "Items_28.png", "index": 54}
obtained_from:
  - {"how": "jewel_craft", "recipe": 68}
---
<!-- generated:start -->
<!-- generated-keys: title=6644fe type=d36ca9 id=ae3ea1 sources=0d95dd name_key=07e813 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=8f6472 options=f9ea2e icon=8caf70 obtained_from=277b9a -->
|  |  |
|---|---|
|  | ![Health Regeneration Rune](wiki/assets/items/7070.png) |
| **Item id** | `7070` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_28.png` cell 54 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Health Regeneration | +17 | flat | 32 |
| Health Regeneration | +192 | flat (from Item_Jewel) | 32 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 7 | rune grade? |

Jewel upgrade (JewelSocketMake 68): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 10, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7069-health-regeneration-rune|Health Regeneration Rune]].

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

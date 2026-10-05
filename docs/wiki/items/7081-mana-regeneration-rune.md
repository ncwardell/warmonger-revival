---
title: "Mana Regeneration Rune"
type: "item"
id: 7081
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7081", "client (server-only table): Item_Jewel.cdb id 81"]
name_key: "ItemName_7081"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 34, "stat": "Mana Regeneration", "value": 20, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 180, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 8}
icon: {"file": "Items_28.png", "index": 25}
obtained_from:
  - {"how": "jewel_craft", "recipe": 79}
---
<!-- generated:start -->
<!-- generated-keys: title=cbe828 type=d36ca9 id=cf41f3 sources=d4e6d0 name_key=95eda5 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=766282 options=b7f834 icon=8d8a6b obtained_from=995752 -->
|  |  |
|---|---|
|  | ![Mana Regeneration Rune](wiki/assets/items/7081.png) |
| **Item id** | `7081` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_28.png` cell 25 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Mana Regeneration | +20 | flat | 34 |
| Mana Regeneration | +180 | flat (from Item_Jewel) | 34 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 8 | rune grade? |

Jewel upgrade (JewelSocketMake 79): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7080-mana-regeneration-rune|Mana Regeneration Rune]].

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

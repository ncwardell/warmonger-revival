---
title: "Health Rune"
type: "item"
id: 7051
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7051", "client (server-only table): Item_Jewel.cdb id 51"]
name_key: "ItemName_7051"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 31, "stat": "Health", "value": 320, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 600, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 5}
icon: {"file": "Items_28.png", "index": 35}
obtained_from:
  - {"how": "jewel_craft", "recipe": 49}
---
<!-- generated:start -->
<!-- generated-keys: title=2c9f18 type=d36ca9 id=3869cc sources=3f3db3 name_key=8322d1 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=36ea1b options=37a1ac icon=80d4f6 obtained_from=eb2a38 -->
|  |  |
|---|---|
|  | ![Health Rune](wiki/assets/items/7051.png) |
| **Item id** | `7051` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_28.png` cell 35 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Health | +320 | flat | 31 |
| Health | +600 | flat (from Item_Jewel) | 31 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 5 | rune grade? |

Jewel upgrade (JewelSocketMake 49): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7050-health-rune|Health Rune]].

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

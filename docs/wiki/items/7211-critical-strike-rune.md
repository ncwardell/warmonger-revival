---
title: "Critical Strike (%) Rune"
type: "item"
id: 7211
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7211", "client (server-only table): Item_Jewel.cdb id 211"]
name_key: "ItemName_7211"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 109, "stat": "Critical Strike +(%)", "value": 14, "scale": "flat"}
  - {"code": 110, "stat": "Critical Strike Deal(%)", "value": 60, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 21}
icon: {"file": "Items_27.png", "index": 19}
obtained_from:
  - {"how": "jewel_craft", "recipe": 209}
---
<!-- generated:start -->
<!-- generated-keys: title=93afc2 type=d36ca9 id=1b76ad sources=543948 name_key=91b34d kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=83a37b options=0ca6e9 icon=692e46 obtained_from=09472a -->
|  |  |
|---|---|
|  | ![Critical Strike (%) Rune](wiki/assets/items/7211.png) |
| **Item id** | `7211` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_27.png` cell 19 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Critical Strike +(%) | Critical Strike +14% | flat | 109 |
| Critical Strike Deal(%) | Critical Strike Deal +60% | flat (from Item_Jewel) | 110 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 21 | rune grade? |

Jewel upgrade (JewelSocketMake 209): [[wiki/items/702-crystal-red|Crystal : Red]] × 60, [[wiki/items/614-red-passion-piece-c|Red Passion Piece (C)]] × 30, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7210-critical-strike-rune|Critical Strike (%) Rune]].

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

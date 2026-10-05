---
title: "Critical Strike (%) Rune"
type: "item"
id: 7210
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7210", "client (server-only table): Item_Jewel.cdb id 210"]
name_key: "ItemName_7210"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 109, "stat": "Critical Strike +(%)", "value": 12, "scale": "flat"}
  - {"code": 110, "stat": "Critical Strike Deal(%)", "value": 48, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 21}
icon: {"file": "Items_27.png", "index": 18}
obtained_from:
  - {"how": "jewel_craft", "recipe": 208}
---
<!-- generated:start -->
<!-- generated-keys: title=93afc2 type=d36ca9 id=36ad2c sources=ec89c1 name_key=d96e9e kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=2e156a options=0ca6e9 icon=858f76 obtained_from=7583a7 -->
|  |  |
|---|---|
|  | ![Critical Strike (%) Rune](wiki/assets/items/7210.png) |
| **Item id** | `7210` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_27.png` cell 18 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Critical Strike +(%) | Critical Strike +12% | flat | 109 |
| Critical Strike Deal(%) | Critical Strike Deal +48% | flat (from Item_Jewel) | 110 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 21 | rune grade? |

Jewel upgrade (JewelSocketMake 208): [[wiki/items/702-crystal-red|Crystal : Red]] × 40, [[wiki/items/614-red-passion-piece-c|Red Passion Piece (C)]] × 20, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7209-critical-strike-rune|Critical Strike (%) Rune]].

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

---
title: "Critical Strike (%) Rune"
type: "item"
id: 7205
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7205", "client (server-only table): Item_Jewel.cdb id 205"]
name_key: "ItemName_7205"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 3
stats:
  - {"code": 109, "stat": "Critical Strike +(%)", "value": 4, "scale": "flat"}
  - {"code": 110, "stat": "Critical Strike Deal(%)", "value": 11, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 21}
icon: {"file": "Items_27.png", "index": 13}
obtained_from:
  - {"how": "jewel_craft", "recipe": 203}
---
<!-- generated:start -->
<!-- generated-keys: title=93afc2 type=d36ca9 id=691bd1 sources=4d0497 name_key=8431e4 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=77de68 stats=a1747f options=0ca6e9 icon=ea9ead obtained_from=855333 -->
|  |  |
|---|---|
|  | ![Critical Strike (%) Rune](wiki/assets/items/7205.png) |
| **Item id** | `7205` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 3 |
| **Icon** | `ui/icons/Items_27.png` cell 13 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Critical Strike +(%) | Critical Strike +4% | flat | 109 |
| Critical Strike Deal(%) | Critical Strike Deal +11% | flat (from Item_Jewel) | 110 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 21 | rune grade? |

Jewel upgrade (JewelSocketMake 203): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 40, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 20, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7204-critical-strike-rune|Critical Strike (%) Rune]].

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

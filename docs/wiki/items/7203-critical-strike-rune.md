---
title: "Critical Strike (%) Rune"
type: "item"
id: 7203
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7203", "client (server-only table): Item_Jewel.cdb id 203"]
name_key: "ItemName_7203"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 109, "stat": "Critical Strike +(%)", "value": 2, "scale": "flat"}
  - {"code": 110, "stat": "Critical Strike Deal(%)", "value": 6, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 21}
icon: {"file": "Items_27.png", "index": 11}
obtained_from:
  - {"how": "jewel_craft", "recipe": 201}
---
<!-- generated:start -->
<!-- generated-keys: title=93afc2 type=d36ca9 id=9fb761 sources=4c2b40 name_key=4c1e0f kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=ee9d3a options=0ca6e9 icon=5ac93d obtained_from=f80ffa -->
|  |  |
|---|---|
|  | ![Critical Strike (%) Rune](wiki/assets/items/7203.png) |
| **Item id** | `7203` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_27.png` cell 11 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Critical Strike +(%) | Critical Strike +2% | flat | 109 |
| Critical Strike Deal(%) | Critical Strike Deal +6% | flat (from Item_Jewel) | 110 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 21 | rune grade? |

Jewel upgrade (JewelSocketMake 201): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 10, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7202-critical-strike-rune|Critical Strike (%) Rune]].

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

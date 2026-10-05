---
title: "Movement(%) Rune"
type: "item"
id: 7163
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7163", "client (server-only table): Item_Jewel.cdb id 163"]
name_key: "ItemName_7163"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 3, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 4, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 17}
icon: {"file": "Items_29.png", "index": 53}
obtained_from:
  - {"how": "jewel_craft", "recipe": 161}
---
<!-- generated:start -->
<!-- generated-keys: title=e6c26c type=d36ca9 id=77e643 sources=7ceb7e name_key=b1eb11 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=22ef52 options=30ea72 icon=750bb6 obtained_from=7c07d1 -->
|  |  |
|---|---|
|  | ![Movement(%) Rune](../assets/items/7163.png) |
| **Item id** | `7163` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_29.png` cell 53 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Movement(%) | Movement +3% | flat | 105 |
| Movement(%) | Movement +4% | flat (from Item_Jewel) | 105 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 17 | rune grade? |

Jewel upgrade (JewelSocketMake 161): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 10, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7162-movement-rune|Movement(%) Rune]].

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

---
title: "Movement(%) Rune"
type: "item"
id: 7167
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7167", "client (server-only table): Item_Jewel.cdb id 167"]
name_key: "ItemName_7167"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 7, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 13, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 17}
icon: {"file": "Items_29.png", "index": 57}
obtained_from:
  - {"how": "jewel_craft", "recipe": 165}
---
<!-- generated:start -->
<!-- generated-keys: title=e6c26c type=d36ca9 id=d7d0c5 sources=a493b0 name_key=b24e10 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=c1978b options=30ea72 icon=007fc6 obtained_from=af47a2 -->
|  |  |
|---|---|
|  | ![Movement(%) Rune](wiki/assets/items/7167.png) |
| **Item id** | `7167` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_29.png` cell 57 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Movement(%) | Movement +7% | flat | 105 |
| Movement(%) | Movement +13% | flat (from Item_Jewel) | 105 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 17 | rune grade? |

Jewel upgrade (JewelSocketMake 165): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 80, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 40, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7166-movement-rune|Movement(%) Rune]].

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

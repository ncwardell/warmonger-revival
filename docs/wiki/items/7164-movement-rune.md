---
title: "Movement(%) Rune"
type: "item"
id: 7164
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7164", "client (server-only table): Item_Jewel.cdb id 164"]
name_key: "ItemName_7164"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 2
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 4, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 5, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 17}
icon: {"file": "Items_29.png", "index": 54}
obtained_from:
  - {"how": "random_box", "box": 50}
  - {"how": "jewel_craft", "recipe": 162}
---
<!-- generated:start -->
<!-- generated-keys: title=e6c26c type=d36ca9 id=9632b9 sources=a91bac name_key=ad4c33 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=da4b92 stats=21521e options=30ea72 icon=adc160 obtained_from=51e041 -->
|  |  |
|---|---|
|  | ![Movement(%) Rune](wiki/assets/items/7164.png) |
| **Item id** | `7164` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 2 |
| **Icon** | `ui/icons/Items_29.png` cell 54 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Movement(%) | Movement +4% | flat | 105 |
| Movement(%) | Movement +5% | flat (from Item_Jewel) | 105 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 17 | rune grade? |

Jewel upgrade (JewelSocketMake 162): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 20, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 15, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7163-movement-rune|Movement(%) Rune]].

### Where to get it

- In random box table row 50 (RandomBox.cdb; odds are server side)
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

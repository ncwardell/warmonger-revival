---
title: "Movement(%) Rune"
type: "item"
id: 7166
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7166", "client (server-only table): Item_Jewel.cdb id 166"]
name_key: "ItemName_7166"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 4
stats:
  - {"code": 105, "stat": "Movement(%)", "value": 6, "scale": "flat"}
  - {"code": 105, "stat": "Movement(%)", "value": 9, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 17}
icon: {"file": "Items_29.png", "index": 56}
obtained_from:
  - {"how": "jewel_craft", "recipe": 164}
---
<!-- generated:start -->
<!-- generated-keys: title=e6c26c type=d36ca9 id=ff022b sources=7166fd name_key=90176c kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=1b6453 stats=0822f2 options=30ea72 icon=39293d obtained_from=1ac83e -->
|  |  |
|---|---|
|  | ![Movement(%) Rune](wiki/assets/items/7166.png) |
| **Item id** | `7166` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 4 |
| **Icon** | `ui/icons/Items_29.png` cell 56 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Movement(%) | Movement +6% | flat | 105 |
| Movement(%) | Movement +9% | flat (from Item_Jewel) | 105 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 17 | rune grade? |

Jewel upgrade (JewelSocketMake 164): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 60, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 30, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7165-movement-rune|Movement(%) Rune]].

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

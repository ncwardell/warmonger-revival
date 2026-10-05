---
title: "Mana Regeneration Rune"
type: "item"
id: 7075
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7075", "client (server-only table): Item_Jewel.cdb id 75"]
name_key: "ItemName_7075"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 3
stats:
  - {"code": 34, "stat": "Mana Regeneration", "value": 5, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 33, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 8}
icon: {"file": "Items_28.png", "index": 19}
obtained_from:
  - {"how": "jewel_craft", "recipe": 73}
---
<!-- generated:start -->
<!-- generated-keys: title=cbe828 type=d36ca9 id=4eb2d0 sources=f2d80c name_key=7f3eb7 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=77de68 stats=f04099 options=b7f834 icon=65e6c9 obtained_from=637206 -->
|  |  |
|---|---|
|  | ![Mana Regeneration Rune](wiki/assets/items/7075.png) |
| **Item id** | `7075` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 3 |
| **Icon** | `ui/icons/Items_28.png` cell 19 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Mana Regeneration | +5 | flat | 34 |
| Mana Regeneration | +33 | flat (from Item_Jewel) | 34 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 8 | rune grade? |

Jewel upgrade (JewelSocketMake 73): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 20, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 20 from [[wiki/items/7074-mana-regeneration-rune|Mana Regeneration Rune]].

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

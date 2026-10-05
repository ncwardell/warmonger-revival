---
title: "Spell Vamp Rune"
type: "item"
id: 7138
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7138", "client (server-only table): Item_Jewel.cdb id 138"]
name_key: "ItemName_7138"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 6
stats:
  - {"code": 43, "stat": "Spell Vamp(%)", "value": 7, "scale": "flat"}
  - {"code": 43, "stat": "Spell Vamp(%)", "value": 17, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 14}
icon: {"file": "Items_28.png", "index": 12}
obtained_from:
  - {"how": "jewel_craft", "recipe": 136}
---
<!-- generated:start -->
<!-- generated-keys: title=a02465 type=d36ca9 id=dd9d78 sources=0c8075 name_key=84d616 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=c1dfd9 stats=40b785 options=f4abe0 icon=5124fd obtained_from=c9be72 -->
|  |  |
|---|---|
|  | ![Spell Vamp Rune](../assets/items/7138.png) |
| **Item id** | `7138` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 6 |
| **Icon** | `ui/icons/Items_28.png` cell 12 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Spell Vamp(%) | Spell Vamp +7% | flat | 43 |
| Spell Vamp(%) | Spell Vamp +17% | flat (from Item_Jewel) | 43 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 14 | rune grade? |

Jewel upgrade (JewelSocketMake 136): [[wiki/items/702-crystal-red|Crystal : Red]] × 10, [[wiki/items/614-red-passion-piece-c|Red Passion Piece (C)]] × 10, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7137-spell-vamp-rune|Spell Vamp Rune]].

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

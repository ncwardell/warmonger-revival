---
title: "Mana Rune"
type: "item"
id: 7058
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7058", "client (server-only table): Item_Jewel.cdb id 58"]
name_key: "ItemName_7058"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 6
stats:
  - {"code": 33, "stat": "Mana", "value": 95, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 232, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 6}
icon: {"file": "Items_28.png", "index": 2}
obtained_from:
  - {"how": "jewel_craft", "recipe": 56}
---
<!-- generated:start -->
<!-- generated-keys: title=1e6304 type=d36ca9 id=2c36a0 sources=cf9dc6 name_key=b51899 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=c1dfd9 stats=d34ab4 options=533fa4 icon=ee56b2 obtained_from=a658a5 -->
|  |  |
|---|---|
|  | ![Mana Rune](../assets/items/7058.png) |
| **Item id** | `7058` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 6 |
| **Icon** | `ui/icons/Items_28.png` cell 2 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Mana | +95 | flat | 33 |
| Mana | +232 | flat (from Item_Jewel) | 33 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 6 | rune grade? |

Jewel upgrade (JewelSocketMake 56): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 80, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7057-mana-rune|Mana Rune]].

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

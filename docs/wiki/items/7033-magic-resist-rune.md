---
title: "Magic Resist Rune"
type: "item"
id: 7033
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7033", "client (server-only table): Item_Jewel.cdb id 33"]
name_key: "ItemName_7033"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 7, "stat": "Magic Resist", "value": 11, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 4, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 4}
icon: {"file": "Items_28.png", "index": 57}
obtained_from:
  - {"how": "jewel_craft", "recipe": 31}
---
<!-- generated:start -->
<!-- generated-keys: title=9c916e type=d36ca9 id=75a58d sources=531eeb name_key=2594da kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=7cc44d options=2ddee2 icon=1f0381 obtained_from=bfbb9a -->
|  |  |
|---|---|
|  | ![Magic Resist Rune](wiki/assets/items/7033.png) |
| **Item id** | `7033` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_28.png` cell 57 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic Resist | +11 | flat | 7 |
| Magic Resist | +4 | flat (from Item_Jewel) | 7 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 4 | rune grade? |

Jewel upgrade (JewelSocketMake 31): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 10, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 10 from [[wiki/items/7032-magic-resist-rune|Magic Resist Rune]].

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

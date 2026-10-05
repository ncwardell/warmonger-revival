---
title: "Attack Speed(%) Rune"
type: "item"
id: 7180
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7180", "client (server-only table): Item_Jewel.cdb id 180"]
name_key: "ItemName_7180"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 103, "stat": "Attack Speed(%)", "value": 11, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 48, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 18}
icon: {"file": "Items_27.png", "index": 38}
obtained_from:
  - {"how": "jewel_craft", "recipe": 178}
---
<!-- generated:start -->
<!-- generated-keys: title=55340f type=d36ca9 id=7d87a4 sources=921ad3 name_key=45929c kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=b00c13 options=109d7f icon=81521d obtained_from=f532d5 -->
|  |  |
|---|---|
|  | ![Attack Speed(%) Rune](wiki/assets/items/7180.png) |
| **Item id** | `7180` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_27.png` cell 38 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack Speed(%) | Attack Speed +11% | flat | 103 |
| Attack Speed(%) | Attack Speed +48% | flat (from Item_Jewel) | 103 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 18 | rune grade? |

Jewel upgrade (JewelSocketMake 178): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 10, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7179-attack-speed-rune|Attack Speed(%) Rune]].

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

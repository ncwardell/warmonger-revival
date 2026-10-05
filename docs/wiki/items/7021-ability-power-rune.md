---
title: "Ability Power Rune"
type: "item"
id: 7021
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7021", "client (server-only table): Item_Jewel.cdb id 21"]
name_key: "ItemName_7021"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 2, "stat": "Ability Power", "value": 60, "scale": "flat"}
  - {"code": 2, "stat": "Ability Power", "value": 96, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 2}
icon: {"file": "Items_27.png", "index": 49}
obtained_from:
  - {"how": "jewel_craft", "recipe": 19}
---
<!-- generated:start -->
<!-- generated-keys: title=df6caa type=d36ca9 id=151537 sources=85a257 name_key=7f8fb8 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=4126a4 options=27669a icon=522d52 obtained_from=a0f8b7 -->
|  |  |
|---|---|
|  | ![Ability Power Rune](../assets/items/7021.png) |
| **Item id** | `7021` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_27.png` cell 49 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +60 | flat | 2 |
| Ability Power | +96 | flat (from Item_Jewel) | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 2 | rune grade? |

Jewel upgrade (JewelSocketMake 19): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7020-ability-power-rune|Ability Power Rune]].

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

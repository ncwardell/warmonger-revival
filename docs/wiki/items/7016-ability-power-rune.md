---
title: "Ability Power Rune"
type: "item"
id: 7016
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7016", "client (server-only table): Item_Jewel.cdb id 16"]
name_key: "ItemName_7016"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 4
stats:
  - {"code": 2, "stat": "Ability Power", "value": 27, "scale": "flat"}
  - {"code": 2, "stat": "Ability Power", "value": 24, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 2}
icon: {"file": "Items_27.png", "index": 44}
obtained_from:
  - {"how": "jewel_craft", "recipe": 14}
---
<!-- generated:start -->
<!-- generated-keys: title=df6caa type=d36ca9 id=66cda3 sources=2040a0 name_key=ebda28 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=1b6453 stats=78ad42 options=27669a icon=4b0a8b obtained_from=0e008f -->
|  |  |
|---|---|
|  | ![Ability Power Rune](wiki/assets/items/7016.png) |
| **Item id** | `7016` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 4 |
| **Icon** | `ui/icons/Items_27.png` cell 44 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +27 | flat | 2 |
| Ability Power | +24 | flat (from Item_Jewel) | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 2 | rune grade? |

Jewel upgrade (JewelSocketMake 14): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 30, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30 from [[wiki/items/7015-ability-power-rune|Ability Power Rune]].

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

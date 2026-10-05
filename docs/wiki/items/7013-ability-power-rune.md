---
title: "Ability Power Rune"
type: "item"
id: 7013
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7013", "client (server-only table): Item_Jewel.cdb id 13"]
name_key: "ItemName_7013"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 2, "stat": "Ability Power", "value": 11, "scale": "flat"}
  - {"code": 2, "stat": "Ability Power", "value": 10, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 2}
icon: {"file": "Items_27.png", "index": 41}
obtained_from:
  - {"how": "jewel_craft", "recipe": 11}
---
<!-- generated:start -->
<!-- generated-keys: title=df6caa type=d36ca9 id=a73a88 sources=2ab9c0 name_key=a21847 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=ca6642 options=27669a icon=5759a1 obtained_from=782308 -->
|  |  |
|---|---|
|  | ![Ability Power Rune](../assets/items/7013.png) |
| **Item id** | `7013` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_27.png` cell 41 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +11 | flat | 2 |
| Ability Power | +10 | flat (from Item_Jewel) | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 2 | rune grade? |

Jewel upgrade (JewelSocketMake 11): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 10, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 10 from [[wiki/items/7012-ability-power-rune|Ability Power Rune]].

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

---
title: "Ability Power Rune"
type: "item"
id: 7019
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7019", "client (server-only table): Item_Jewel.cdb id 19"]
name_key: "ItemName_7019"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 7
stats:
  - {"code": 2, "stat": "Ability Power", "value": 46, "scale": "flat"}
  - {"code": 2, "stat": "Ability Power", "value": 61, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 2}
icon: {"file": "Items_27.png", "index": 47}
obtained_from:
  - {"how": "jewel_craft", "recipe": 17}
---
<!-- generated:start -->
<!-- generated-keys: title=df6caa type=d36ca9 id=eb2776 sources=14a86d name_key=2a3752 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=902ba3 stats=8ae16c options=27669a icon=7a60b2 obtained_from=b317c0 -->
|  |  |
|---|---|
|  | ![Ability Power Rune](../assets/items/7019.png) |
| **Item id** | `7019` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 7 |
| **Icon** | `ui/icons/Items_27.png` cell 47 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +46 | flat | 2 |
| Ability Power | +61 | flat (from Item_Jewel) | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 2 | rune grade? |

Jewel upgrade (JewelSocketMake 17): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 100, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 60, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7018-ability-power-rune|Ability Power Rune]].

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

---
title: "Ability Power Rune"
type: "item"
id: 7014
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7014", "client (server-only table): Item_Jewel.cdb id 14"]
name_key: "ItemName_7014"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 2
stats:
  - {"code": 2, "stat": "Ability Power", "value": 16, "scale": "flat"}
  - {"code": 2, "stat": "Ability Power", "value": 13, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 2}
icon: {"file": "Items_27.png", "index": 42}
obtained_from:
  - {"how": "jewel_craft", "recipe": 12}
---
<!-- generated:start -->
<!-- generated-keys: title=df6caa type=d36ca9 id=390531 sources=49804b name_key=de8431 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=da4b92 stats=0efa14 options=27669a icon=711e54 obtained_from=ce5246 -->
|  |  |
|---|---|
|  | ![Ability Power Rune](wiki/assets/items/7014.png) |
| **Item id** | `7014` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 2 |
| **Icon** | `ui/icons/Items_27.png` cell 42 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +16 | flat | 2 |
| Ability Power | +13 | flat (from Item_Jewel) | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 2 | rune grade? |

Jewel upgrade (JewelSocketMake 12): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 15, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 15 from [[wiki/items/7013-ability-power-rune|Ability Power Rune]].

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

---
title: "Health Rune"
type: "item"
id: 7045
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7045", "client (server-only table): Item_Jewel.cdb id 45"]
name_key: "ItemName_7045"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 3
stats:
  - {"code": 31, "stat": "Health", "value": 110, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 110, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 5}
icon: {"file": "Items_28.png", "index": 29}
obtained_from:
  - {"how": "jewel_craft", "recipe": 43}
---
<!-- generated:start -->
<!-- generated-keys: title=2c9f18 type=d36ca9 id=7dd7f8 sources=41aba5 name_key=fe9b3c kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=77de68 stats=f1354d options=37a1ac icon=8a98f8 obtained_from=bb85e9 -->
|  |  |
|---|---|
|  | ![Health Rune](../assets/items/7045.png) |
| **Item id** | `7045` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 3 |
| **Icon** | `ui/icons/Items_28.png` cell 29 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Health | +110 | flat | 31 |
| Health | +110 | flat (from Item_Jewel) | 31 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 5 | rune grade? |

Jewel upgrade (JewelSocketMake 43): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 20, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 20 from [[wiki/items/7044-health-rune|Health Rune]].

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

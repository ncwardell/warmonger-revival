---
title: "Health Rune"
type: "item"
id: 7043
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7043", "client (server-only table): Item_Jewel.cdb id 43"]
name_key: "ItemName_7043"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 31, "stat": "Health", "value": 70, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 60, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 5}
icon: {"file": "Items_28.png", "index": 27}
obtained_from:
  - {"how": "jewel_craft", "recipe": 41}
---
<!-- generated:start -->
<!-- generated-keys: title=2c9f18 type=d36ca9 id=9cd6a6 sources=6d44ae name_key=451dc5 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=f5de96 options=37a1ac icon=4ff275 obtained_from=fd8bd2 -->
|  |  |
|---|---|
|  | ![Health Rune](../assets/items/7043.png) |
| **Item id** | `7043` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_28.png` cell 27 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Health | +70 | flat | 31 |
| Health | +60 | flat (from Item_Jewel) | 31 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 5 | rune grade? |

Jewel upgrade (JewelSocketMake 41): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 10, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 10 from [[wiki/items/7042-health-rune|Health Rune]].

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

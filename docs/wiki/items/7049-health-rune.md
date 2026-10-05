---
title: "Health Rune"
type: "item"
id: 7049
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7049", "client (server-only table): Item_Jewel.cdb id 49"]
name_key: "ItemName_7049"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 7
stats:
  - {"code": 31, "stat": "Health", "value": 240, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 380, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 5}
icon: {"file": "Items_28.png", "index": 33}
obtained_from:
  - {"how": "jewel_craft", "recipe": 47}
---
<!-- generated:start -->
<!-- generated-keys: title=2c9f18 type=d36ca9 id=c9a6a8 sources=536a8e name_key=971298 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=902ba3 stats=81682a options=37a1ac icon=a9c5f5 obtained_from=24f6ba -->
|  |  |
|---|---|
|  | ![Health Rune](../assets/items/7049.png) |
| **Item id** | `7049` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 7 |
| **Icon** | `ui/icons/Items_28.png` cell 33 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Health | +240 | flat | 31 |
| Health | +380 | flat (from Item_Jewel) | 31 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 5 | rune grade? |

Jewel upgrade (JewelSocketMake 47): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 100, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 60, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7048-health-rune|Health Rune]].

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

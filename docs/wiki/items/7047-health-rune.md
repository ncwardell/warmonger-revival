---
title: "Health Rune"
type: "item"
id: 7047
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7047", "client (server-only table): Item_Jewel.cdb id 47"]
name_key: "ItemName_7047"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 31, "stat": "Health", "value": 170, "scale": "flat"}
  - {"code": 31, "stat": "Health", "value": 210, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 5}
icon: {"file": "Items_28.png", "index": 31}
obtained_from:
  - {"how": "jewel_craft", "recipe": 45}
---
<!-- generated:start -->
<!-- generated-keys: title=2c9f18 type=d36ca9 id=261f4c sources=21d760 name_key=8f0688 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=704398 options=37a1ac icon=55c7a6 obtained_from=944141 -->
|  |  |
|---|---|
|  | ![Health Rune](wiki/assets/items/7047.png) |
| **Item id** | `7047` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_28.png` cell 31 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Health | +170 | flat | 31 |
| Health | +210 | flat (from Item_Jewel) | 31 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 5 | rune grade? |

Jewel upgrade (JewelSocketMake 45): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 60, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7046-health-rune|Health Rune]].

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

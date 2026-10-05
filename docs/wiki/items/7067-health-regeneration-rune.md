---
title: "Health Regeneration Rune"
type: "item"
id: 7067
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7067", "client (server-only table): Item_Jewel.cdb id 67"]
name_key: "ItemName_7067"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 32, "stat": "Health Regeneration", "value": 9, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 84, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 7}
icon: {"file": "Items_28.png", "index": 51}
obtained_from:
  - {"how": "jewel_craft", "recipe": 65}
---
<!-- generated:start -->
<!-- generated-keys: title=6644fe type=d36ca9 id=9218a5 sources=bd6755 name_key=91567f kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=606cac options=f9ea2e icon=5411c1 obtained_from=82d8fb -->
|  |  |
|---|---|
|  | ![Health Regeneration Rune](wiki/assets/items/7067.png) |
| **Item id** | `7067` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_28.png` cell 51 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Health Regeneration | +9 | flat | 32 |
| Health Regeneration | +84 | flat (from Item_Jewel) | 32 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 7 | rune grade? |

Jewel upgrade (JewelSocketMake 65): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 60, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7066-health-regeneration-rune|Health Regeneration Rune]].

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

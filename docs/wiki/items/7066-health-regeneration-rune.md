---
title: "Health Regeneration Rune"
type: "item"
id: 7066
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7066", "client (server-only table): Item_Jewel.cdb id 66"]
name_key: "ItemName_7066"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 4
stats:
  - {"code": 32, "stat": "Health Regeneration", "value": 7, "scale": "flat"}
  - {"code": 32, "stat": "Health Regeneration", "value": 60, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 7}
icon: {"file": "Items_28.png", "index": 50}
obtained_from:
  - {"how": "jewel_craft", "recipe": 64}
---
<!-- generated:start -->
<!-- generated-keys: title=6644fe type=d36ca9 id=4c07fa sources=45372d name_key=d94c06 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=1b6453 stats=62f578 options=f9ea2e icon=359719 obtained_from=919858 -->
|  |  |
|---|---|
|  | ![Health Regeneration Rune](wiki/assets/items/7066.png) |
| **Item id** | `7066` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 4 |
| **Icon** | `ui/icons/Items_28.png` cell 50 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Health Regeneration | +7 | flat | 32 |
| Health Regeneration | +60 | flat (from Item_Jewel) | 32 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 7 | rune grade? |

Jewel upgrade (JewelSocketMake 64): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 30, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30 from [[wiki/items/7065-health-regeneration-rune|Health Regeneration Rune]].

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

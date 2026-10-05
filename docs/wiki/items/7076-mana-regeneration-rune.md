---
title: "Mana Regeneration Rune"
type: "item"
id: 7076
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7076", "client (server-only table): Item_Jewel.cdb id 76"]
name_key: "ItemName_7076"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 4
stats:
  - {"code": 34, "stat": "Mana Regeneration", "value": 7, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 45, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 8}
icon: {"file": "Items_28.png", "index": 20}
obtained_from:
  - {"how": "jewel_craft", "recipe": 74}
---
<!-- generated:start -->
<!-- generated-keys: title=cbe828 type=d36ca9 id=c9032f sources=6dd08e name_key=75747b kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=1b6453 stats=d883b9 options=b7f834 icon=595c8b obtained_from=d39c71 -->
|  |  |
|---|---|
|  | ![Mana Regeneration Rune](wiki/assets/items/7076.png) |
| **Item id** | `7076` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 4 |
| **Icon** | `ui/icons/Items_28.png` cell 20 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Mana Regeneration | +7 | flat | 34 |
| Mana Regeneration | +45 | flat (from Item_Jewel) | 34 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 8 | rune grade? |

Jewel upgrade (JewelSocketMake 74): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 30, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30 from [[wiki/items/7075-mana-regeneration-rune|Mana Regeneration Rune]].

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

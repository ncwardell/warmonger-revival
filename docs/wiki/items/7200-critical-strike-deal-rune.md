---
title: "Critical Strike Deal Rune"
type: "item"
id: 7200
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7200", "client (server-only table): Item_Jewel.cdb id 200"]
name_key: "ItemName_7200"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 10, "stat": "Critical Strike Deal", "value": 26, "scale": "flat"}
  - {"code": 10, "stat": "Critical Strike Deal", "value": 96, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 20}
icon: {"file": "Items_27.png", "index": 28}
obtained_from:
  - {"how": "jewel_craft", "recipe": 198}
---
<!-- generated:start -->
<!-- generated-keys: title=3e9edc type=d36ca9 id=85146e sources=96a95b name_key=ce0a89 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=cdaee4 options=1a760e icon=6a7922 obtained_from=c02be4 -->
|  |  |
|---|---|
|  | ![Critical Strike Deal Rune](wiki/assets/items/7200.png) |
| **Item id** | `7200` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_27.png` cell 28 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Critical Strike Deal | +26 | flat | 10 |
| Critical Strike Deal | +96 | flat (from Item_Jewel) | 10 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 20 | rune grade? |

Jewel upgrade (JewelSocketMake 198): [[wiki/items/703-crystal-black|Crystal : Black]] × 60, [[wiki/items/616-red-passion-piece-b|Red Passion Piece (B)]] × 30, [[wiki/items/857-amplifying-passion|Amplifying Passion]] × 1 from [[wiki/items/7199-critical-strike-deal-rune|Critical Strike Deal Rune]].

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

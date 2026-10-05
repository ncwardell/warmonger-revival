---
title: "Magic resist Penetration Rune"
type: "item"
id: 7099
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7099", "client (server-only table): Item_Jewel.cdb id 99"]
name_key: "ItemName_7099"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 7
stats:
  - {"code": 14, "stat": "Magic resist Penetration", "value": 11, "scale": "flat"}
  - {"code": 14, "stat": "Magic resist Penetration", "value": 76, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 10}
icon: {"file": "Items_29.png", "index": 9}
obtained_from:
  - {"how": "jewel_craft", "recipe": 97}
---
<!-- generated:start -->
<!-- generated-keys: title=641d2f type=d36ca9 id=164532 sources=cfb38f name_key=7de1bf kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=902ba3 stats=7de379 options=054ccf icon=55c49b obtained_from=3297fe -->
|  |  |
|---|---|
|  | ![Magic resist Penetration Rune](../assets/items/7099.png) |
| **Item id** | `7099` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 7 |
| **Icon** | `ui/icons/Items_29.png` cell 9 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration | +11 | flat | 14 |
| Magic resist Penetration | +76 | flat (from Item_Jewel) | 14 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 10 | rune grade? |

Jewel upgrade (JewelSocketMake 97): [[wiki/items/702-crystal-red|Crystal : Red]] × 20, [[wiki/items/614-red-passion-piece-c|Red Passion Piece (C)]] × 15, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7098-magic-resist-penetration-rune|Magic resist Penetration Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
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

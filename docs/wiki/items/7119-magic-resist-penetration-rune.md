---
title: "Magic resist Penetration(%) Rune"
type: "item"
id: 7119
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7119", "client (server-only table): Item_Jewel.cdb id 119"]
name_key: "ItemName_7119"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 7
stats:
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 8, "scale": "flat"}
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 23, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 12}
icon: {"file": "Items_29.png", "index": 19}
obtained_from:
  - {"how": "jewel_craft", "recipe": 117}
---
<!-- generated:start -->
<!-- generated-keys: title=bd6293 type=d36ca9 id=1653c8 sources=1ec935 name_key=a77f13 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=902ba3 stats=f90d58 options=b78b55 icon=d020aa obtained_from=a4db2a -->
|  |  |
|---|---|
|  | ![Magic resist Penetration(%) Rune](../assets/items/7119.png) |
| **Item id** | `7119` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 7 |
| **Icon** | `ui/icons/Items_29.png` cell 19 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration(%) | Magic resist Penetration +8% | flat | 114 |
| Magic resist Penetration(%) | Magic resist Penetration +23% | flat (from Item_Jewel) | 114 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 12 | rune grade? |

Jewel upgrade (JewelSocketMake 117): [[wiki/items/703-crystal-black|Crystal : Black]] × 40, [[wiki/items/616-red-passion-piece-b|Red Passion Piece (B)]] × 20, [[wiki/items/857-amplifying-passion|Amplifying Passion]] × 1 from [[wiki/items/7118-magic-resist-penetration-rune|Magic resist Penetration(%) Rune]].

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

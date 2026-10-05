---
title: "Magic resist Penetration(%) Rune"
type: "item"
id: 7113
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7113", "client (server-only table): Item_Jewel.cdb id 113"]
name_key: "ItemName_7113"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 2, "scale": "flat"}
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 4, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 12}
icon: {"file": "Items_29.png", "index": 13}
obtained_from:
  - {"how": "jewel_craft", "recipe": 111}
---
<!-- generated:start -->
<!-- generated-keys: title=bd6293 type=d36ca9 id=4f4880 sources=769608 name_key=830eb4 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=6ba637 options=b78b55 icon=a5d274 obtained_from=3a37cb -->
|  |  |
|---|---|
|  | ![Magic resist Penetration(%) Rune](wiki/assets/items/7113.png) |
| **Item id** | `7113` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_29.png` cell 13 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration(%) | Magic resist Penetration +2% | flat | 114 |
| Magic resist Penetration(%) | Magic resist Penetration +4% | flat (from Item_Jewel) | 114 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 12 | rune grade? |

Jewel upgrade (JewelSocketMake 111): [[wiki/items/702-crystal-red|Crystal : Red]] × 10, [[wiki/items/615-red-passion-fragments-b|Red Passion Fragments (B)]] × 15, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7112-magic-resist-penetration-rune|Magic resist Penetration(%) Rune]].

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

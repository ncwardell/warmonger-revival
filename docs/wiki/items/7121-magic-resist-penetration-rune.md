---
title: "Magic resist Penetration(%) Rune"
type: "item"
id: 7121
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7121", "client (server-only table): Item_Jewel.cdb id 121"]
name_key: "ItemName_7121"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 10, "scale": "flat"}
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 36, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 12}
icon: {"file": "Items_29.png", "index": 21}
obtained_from:
  - {"how": "jewel_craft", "recipe": 119}
---
<!-- generated:start -->
<!-- generated-keys: title=bd6293 type=d36ca9 id=1c6c78 sources=682ce3 name_key=894283 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=8596c9 options=b78b55 icon=663894 obtained_from=75564c -->
|  |  |
|---|---|
|  | ![Magic resist Penetration(%) Rune](../assets/items/7121.png) |
| **Item id** | `7121` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_29.png` cell 21 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration(%) | Magic resist Penetration +10% | flat | 114 |
| Magic resist Penetration(%) | Magic resist Penetration +36% | flat (from Item_Jewel) | 114 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 12 | rune grade? |

Jewel upgrade (JewelSocketMake 119): [[wiki/items/703-crystal-black|Crystal : Black]] × 80, [[wiki/items/616-red-passion-piece-b|Red Passion Piece (B)]] × 40, [[wiki/items/857-amplifying-passion|Amplifying Passion]] × 1 from [[wiki/items/7120-magic-resist-penetration-rune|Magic resist Penetration(%) Rune]].

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

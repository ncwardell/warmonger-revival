---
title: "Magic resist Penetration(%) Rune"
type: "item"
id: 7117
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7117", "client (server-only table): Item_Jewel.cdb id 117"]
name_key: "ItemName_7117"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 6, "scale": "flat"}
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 13, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 12}
icon: {"file": "Items_29.png", "index": 17}
obtained_from:
  - {"how": "jewel_craft", "recipe": 115}
---
<!-- generated:start -->
<!-- generated-keys: title=bd6293 type=d36ca9 id=37fe4c sources=f60978 name_key=82b7ac kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=95355e options=b78b55 icon=b60d82 obtained_from=de1c13 -->
|  |  |
|---|---|
|  | ![Magic resist Penetration(%) Rune](wiki/assets/items/7117.png) |
| **Item id** | `7117` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_29.png` cell 17 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration(%) | Magic resist Penetration +6% | flat | 114 |
| Magic resist Penetration(%) | Magic resist Penetration +13% | flat (from Item_Jewel) | 114 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 12 | rune grade? |

Jewel upgrade (JewelSocketMake 115): [[wiki/items/703-crystal-black|Crystal : Black]] × 10, [[wiki/items/616-red-passion-piece-b|Red Passion Piece (B)]] × 10, [[wiki/items/857-amplifying-passion|Amplifying Passion]] × 1 from [[wiki/items/7116-magic-resist-penetration-rune|Magic resist Penetration(%) Rune]].

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

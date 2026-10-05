---
title: "Magic resist Penetration Rune"
type: "item"
id: 7100
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7100", "client (server-only table): Item_Jewel.cdb id 100"]
name_key: "ItemName_7100"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 14, "stat": "Magic resist Penetration", "value": 12, "scale": "flat"}
  - {"code": 14, "stat": "Magic resist Penetration", "value": 96, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 10}
icon: {"file": "Items_29.png", "index": 10}
obtained_from:
  - {"how": "jewel_craft", "recipe": 98}
---
<!-- generated:start -->
<!-- generated-keys: title=641d2f type=d36ca9 id=d4ed6c sources=4b239d name_key=fcaa45 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=428eb9 options=054ccf icon=a87067 obtained_from=7fc746 -->
|  |  |
|---|---|
|  | ![Magic resist Penetration Rune](wiki/assets/items/7100.png) |
| **Item id** | `7100` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_29.png` cell 10 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration | +12 | flat | 14 |
| Magic resist Penetration | +96 | flat (from Item_Jewel) | 14 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 10 | rune grade? |

Jewel upgrade (JewelSocketMake 98): [[wiki/items/702-crystal-red|Crystal : Red]] × 40, [[wiki/items/614-red-passion-piece-c|Red Passion Piece (C)]] × 20, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7099-magic-resist-penetration-rune|Magic resist Penetration Rune]].

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

---
title: "Magic resist Penetration(%) Rune"
type: "item"
id: 7112
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7112", "client (server-only table): Item_Jewel.cdb id 112"]
name_key: "ItemName_7112"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 1, "scale": "flat"}
  - {"code": 114, "stat": "Magic resist Penetration(%)", "value": 3, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 12}
icon: {"file": "Items_29.png", "index": 12}
obtained_from:
  - {"how": "craft", "recipe": 1812}
---
<!-- generated:start -->
<!-- generated-keys: title=bd6293 type=d36ca9 id=c7b6db sources=2402bd name_key=82cb39 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=7dc50d options=b78b55 icon=cc6f64 obtained_from=2d37d4 -->
|  |  |
|---|---|
|  | ![Magic resist Penetration(%) Rune](../assets/items/7112.png) |
| **Item id** | `7112` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_29.png` cell 12 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration(%) | Magic resist Penetration +1% | flat | 114 |
| Magic resist Penetration(%) | Magic resist Penetration +3% | flat (from Item_Jewel) | 114 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 12 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1812 | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/808-moonstone\|Moonstone]] × 10 | 0 | 100 |

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

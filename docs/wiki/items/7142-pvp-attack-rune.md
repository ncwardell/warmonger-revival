---
title: "PvP Attack Rune"
type: "item"
id: 7142
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7142", "client (server-only table): Item_Jewel.cdb id 142"]
name_key: "ItemName_7142"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 141, "stat": "PvP Attack", "value": 1, "scale": "flat"}
  - {"code": 136, "stat": "Damage(%)+", "value": 2, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 15}
icon: {"file": "Items_25.png", "index": 12}
obtained_from:
  - {"how": "craft", "recipe": 1815}
---
<!-- generated:start -->
<!-- generated-keys: title=e67265 type=d36ca9 id=e3d595 sources=caca96 name_key=937a21 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=5e248a options=0522b7 icon=7f3334 obtained_from=8d1efa -->
|  |  |
|---|---|
|  | ![PvP Attack Rune](../assets/items/7142.png) |
| **Item id** | `7142` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_25.png` cell 12 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Attack | +1 | flat | 141 |
| Damage(%)+ | Damage +2%+ | flat (from Item_Jewel) | 136 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 15 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1815 | [[wiki/items/703-crystal-black\|Crystal : Black]] × 10, [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/854-shining-passion\|Shining Passion]] × 3 | 0 | 100 |

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

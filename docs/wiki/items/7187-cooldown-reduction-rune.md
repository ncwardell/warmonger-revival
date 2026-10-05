---
title: "Cooldown Reduction Rune"
type: "item"
id: 7187
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7187", "client (server-only table): Item_Jewel.cdb id 187"]
name_key: "ItemName_7187"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 6, "scale": "flat"}
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 8, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 19}
icon: {"file": "Items_27.png", "index": 55}
obtained_from:
  - {"how": "jewel_craft", "recipe": 185}
---
<!-- generated:start -->
<!-- generated-keys: title=a62c86 type=d36ca9 id=1a3a63 sources=6402e7 name_key=ecb4a5 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=824ed3 options=c1a4c7 icon=9413d3 obtained_from=17ef95 -->
|  |  |
|---|---|
|  | ![Cooldown Reduction Rune](wiki/assets/items/7187.png) |
| **Item id** | `7187` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_27.png` cell 55 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Cooldown Reduction(%) | Cooldown Reduction +6% | flat | 212 |
| Cooldown Reduction(%) | Cooldown Reduction +8% | flat (from Item_Jewel) | 212 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 19 | rune grade? |

Jewel upgrade (JewelSocketMake 185): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 80, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 40, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7186-cooldown-reduction-rune|Cooldown Reduction Rune]].

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

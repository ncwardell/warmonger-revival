---
title: "Cooldown Reduction Rune"
type: "item"
id: 7184
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7184", "client (server-only table): Item_Jewel.cdb id 184"]
name_key: "ItemName_7184"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 2
stats:
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 3, "scale": "flat"}
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 3, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 19}
icon: {"file": "Items_27.png", "index": 52}
obtained_from:
  - {"how": "jewel_craft", "recipe": 182}
---
<!-- generated:start -->
<!-- generated-keys: title=a62c86 type=d36ca9 id=91b39c sources=f1a591 name_key=65c15c kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=da4b92 stats=e1964a options=c1a4c7 icon=bf3eb0 obtained_from=afc4e3 -->
|  |  |
|---|---|
|  | ![Cooldown Reduction Rune](wiki/assets/items/7184.png) |
| **Item id** | `7184` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 2 |
| **Icon** | `ui/icons/Items_27.png` cell 52 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Cooldown Reduction(%) | Cooldown Reduction +3% | flat | 212 |
| Cooldown Reduction(%) | Cooldown Reduction +3% | flat (from Item_Jewel) | 212 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 19 | rune grade? |

Jewel upgrade (JewelSocketMake 182): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 20, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 15, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7183-cooldown-reduction-rune|Cooldown Reduction Rune]].

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

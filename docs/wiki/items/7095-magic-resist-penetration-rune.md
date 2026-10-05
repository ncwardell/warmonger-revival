---
title: "Magic resist Penetration Rune"
type: "item"
id: 7095
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7095", "client (server-only table): Item_Jewel.cdb id 95"]
name_key: "ItemName_7095"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 3
stats:
  - {"code": 14, "stat": "Magic resist Penetration", "value": 4, "scale": "flat"}
  - {"code": 14, "stat": "Magic resist Penetration", "value": 22, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 10}
icon: {"file": "Items_29.png", "index": 5}
obtained_from:
  - {"how": "jewel_craft", "recipe": 93}
---
<!-- generated:start -->
<!-- generated-keys: title=641d2f type=d36ca9 id=2bf041 sources=28965b name_key=629719 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=77de68 stats=d3d3eb options=054ccf icon=7ea553 obtained_from=cbf0b5 -->
|  |  |
|---|---|
|  | ![Magic resist Penetration Rune](wiki/assets/items/7095.png) |
| **Item id** | `7095` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 3 |
| **Icon** | `ui/icons/Items_29.png` cell 5 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration | +4 | flat | 14 |
| Magic resist Penetration | +22 | flat (from Item_Jewel) | 14 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 10 | rune grade? |

Jewel upgrade (JewelSocketMake 93): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 40, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 20, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7094-magic-resist-penetration-rune|Magic resist Penetration Rune]].

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

---
title: "PvP Attack Rune"
type: "item"
id: 7145
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7145", "client (server-only table): Item_Jewel.cdb id 145"]
name_key: "ItemName_7145"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 3
stats:
  - {"code": 141, "stat": "PvP Attack", "value": 4, "scale": "flat"}
  - {"code": 136, "stat": "Damage(%)+", "value": 4, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 15}
icon: {"file": "Items_25.png", "index": 15}
obtained_from:
  - {"how": "jewel_craft", "recipe": 143}
---
<!-- generated:start -->
<!-- generated-keys: title=e67265 type=d36ca9 id=4a1604 sources=56df14 name_key=d066a2 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=77de68 stats=773ce0 options=0522b7 icon=576133 obtained_from=59431f -->
|  |  |
|---|---|
|  | ![PvP Attack Rune](wiki/assets/items/7145.png) |
| **Item id** | `7145` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 3 |
| **Icon** | `ui/icons/Items_25.png` cell 15 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Attack | +4 | flat | 141 |
| Damage(%)+ | Damage +4%+ | flat (from Item_Jewel) | 136 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 15 | rune grade? |

Jewel upgrade (JewelSocketMake 143): [[wiki/items/702-crystal-red|Crystal : Red]] × 40, [[wiki/items/615-red-passion-fragments-b|Red Passion Fragments (B)]] × 30, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7144-pvp-attack-rune|PvP Attack Rune]].

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

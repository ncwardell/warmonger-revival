---
title: "PvP Attack Rune"
type: "item"
id: 7143
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7143", "client (server-only table): Item_Jewel.cdb id 143"]
name_key: "ItemName_7143"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 141, "stat": "PvP Attack", "value": 2, "scale": "flat"}
  - {"code": 136, "stat": "Damage(%)+", "value": 2, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 15}
icon: {"file": "Items_25.png", "index": 13}
obtained_from:
  - {"how": "jewel_craft", "recipe": 141}
---
<!-- generated:start -->
<!-- generated-keys: title=e67265 type=d36ca9 id=308550 sources=99d288 name_key=97c7cb kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=8facca options=0522b7 icon=5dc1de obtained_from=0964e1 -->
|  |  |
|---|---|
|  | ![PvP Attack Rune](wiki/assets/items/7143.png) |
| **Item id** | `7143` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_25.png` cell 13 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Attack | +2 | flat | 141 |
| Damage(%)+ | Damage +2%+ | flat (from Item_Jewel) | 136 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 15 | rune grade? |

Jewel upgrade (JewelSocketMake 141): [[wiki/items/702-crystal-red|Crystal : Red]] × 10, [[wiki/items/615-red-passion-fragments-b|Red Passion Fragments (B)]] × 15, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7142-pvp-attack-rune|PvP Attack Rune]].

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

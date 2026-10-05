---
title: "PvP Attack Rune"
type: "item"
id: 7150
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7150", "client (server-only table): Item_Jewel.cdb id 150"]
name_key: "ItemName_7150"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 141, "stat": "PvP Attack", "value": 9, "scale": "flat"}
  - {"code": 136, "stat": "Damage(%)+", "value": 19, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 15}
icon: {"file": "Items_30.png", "index": 0}
obtained_from:
  - {"how": "jewel_craft", "recipe": 148}
---
<!-- generated:start -->
<!-- generated-keys: title=e67265 type=d36ca9 id=6891fa sources=0e580d name_key=803256 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=cee6f6 options=0522b7 icon=a2149d obtained_from=ec1f40 -->
|  |  |
|---|---|
|  | ![PvP Attack Rune](wiki/assets/items/7150.png) |
| **Item id** | `7150` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_30.png` cell 0 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Attack | +9 | flat | 141 |
| Damage(%)+ | Damage +19%+ | flat (from Item_Jewel) | 136 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 15 | rune grade? |

Jewel upgrade (JewelSocketMake 148): [[wiki/items/703-crystal-black|Crystal : Black]] × 60, [[wiki/items/616-red-passion-piece-b|Red Passion Piece (B)]] × 30, [[wiki/items/857-amplifying-passion|Amplifying Passion]] × 1 from [[wiki/items/7149-pvp-attack-rune|PvP Attack Rune]].

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

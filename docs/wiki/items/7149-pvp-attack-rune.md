---
title: "PvP Attack Rune"
type: "item"
id: 7149
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7149", "client (server-only table): Item_Jewel.cdb id 149"]
name_key: "ItemName_7149"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 7
stats:
  - {"code": 141, "stat": "PvP Attack", "value": 8, "scale": "flat"}
  - {"code": 136, "stat": "Damage(%)+", "value": 15, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 15}
icon: {"file": "Items_29.png", "index": 63}
obtained_from:
  - {"how": "jewel_craft", "recipe": 147}
---
<!-- generated:start -->
<!-- generated-keys: title=e67265 type=d36ca9 id=b7e1ba sources=653d92 name_key=3fb8a6 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=902ba3 stats=222b70 options=0522b7 icon=0da54f obtained_from=cf0e4a -->
|  |  |
|---|---|
|  | ![PvP Attack Rune](../assets/items/7149.png) |
| **Item id** | `7149` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 7 |
| **Icon** | `ui/icons/Items_29.png` cell 63 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Attack | +8 | flat | 141 |
| Damage(%)+ | Damage +15%+ | flat (from Item_Jewel) | 136 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 15 | rune grade? |

Jewel upgrade (JewelSocketMake 147): [[wiki/items/703-crystal-black|Crystal : Black]] × 40, [[wiki/items/616-red-passion-piece-b|Red Passion Piece (B)]] × 20, [[wiki/items/857-amplifying-passion|Amplifying Passion]] × 1 from [[wiki/items/7148-pvp-attack-rune|PvP Attack Rune]].

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

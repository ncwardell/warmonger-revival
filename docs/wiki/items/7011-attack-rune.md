---
title: "Attack Rune"
type: "item"
id: 7011
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7011", "client (server-only table): Item_Jewel.cdb id 11"]
name_key: "ItemName_7011"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 1, "stat": "Attack", "value": 45, "scale": "flat"}
  - {"code": 1, "stat": "Attack", "value": 120, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 1}
icon: {"file": "Items_27.png", "index": 9}
obtained_from:
  - {"how": "jewel_craft", "recipe": 9}
---
<!-- generated:start -->
<!-- generated-keys: title=839df9 type=d36ca9 id=0c7d78 sources=0a2704 name_key=1052d3 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=741b1e options=88c977 icon=8e87fa obtained_from=4710c2 -->
|  |  |
|---|---|
|  | ![Attack Rune](../assets/items/7011.png) |
| **Item id** | `7011` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_27.png` cell 9 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack | +45 | flat | 1 |
| Attack | +120 | flat (from Item_Jewel) | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 1 | rune grade? |

Jewel upgrade (JewelSocketMake 9): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7010-attack-rune|Attack Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
- [[gameplay/video-rune-upgrades|Video notes: rune upgrade attempts (ZonderCoRe)]]
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

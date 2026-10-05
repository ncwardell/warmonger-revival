---
title: "Attack Rune"
type: "item"
id: 7003
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7003", "client (server-only table): Item_Jewel.cdb id 3"]
name_key: "ItemName_7003"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 1, "stat": "Attack", "value": 6, "scale": "flat"}
  - {"code": 1, "stat": "Attack", "value": 12, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 1}
icon: {"file": "Items_27.png", "index": 1}
obtained_from:
  - {"how": "jewel_craft", "recipe": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=839df9 type=d36ca9 id=a9b77c sources=1f3d41 name_key=0685bb kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=e0d651 options=88c977 icon=606829 obtained_from=5e754b -->
|  |  |
|---|---|
|  | ![Attack Rune](../assets/items/7003.png) |
| **Item id** | `7003` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_27.png` cell 1 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack | +6 | flat | 1 |
| Attack | +12 | flat (from Item_Jewel) | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 1 | rune grade? |

Jewel upgrade (JewelSocketMake 1): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 10, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 10 from [[wiki/items/7002-attack-rune|Attack Rune]].

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

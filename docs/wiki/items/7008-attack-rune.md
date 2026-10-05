---
title: "Attack Rune"
type: "item"
id: 7008
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7008", "client (server-only table): Item_Jewel.cdb id 8"]
name_key: "ItemName_7008"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 6
stats:
  - {"code": 1, "stat": "Attack", "value": 27, "scale": "flat"}
  - {"code": 1, "stat": "Attack", "value": 58, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 1}
icon: {"file": "Items_27.png", "index": 6}
obtained_from:
  - {"how": "jewel_craft", "recipe": 6}
---
<!-- generated:start -->
<!-- generated-keys: title=839df9 type=d36ca9 id=28cd4e sources=3620c0 name_key=9d6ff8 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=c1dfd9 stats=f0310a options=88c977 icon=24e6f6 obtained_from=3c5551 -->
|  |  |
|---|---|
|  | ![Attack Rune](../assets/items/7008.png) |
| **Item id** | `7008` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 6 |
| **Icon** | `ui/icons/Items_27.png` cell 6 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack | +27 | flat | 1 |
| Attack | +58 | flat (from Item_Jewel) | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 1 | rune grade? |

Jewel upgrade (JewelSocketMake 6): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 80, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7007-attack-rune|Attack Rune]].

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

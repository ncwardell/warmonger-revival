---
title: "Attack Rune"
type: "item"
id: 7004
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7004", "client (server-only table): Item_Jewel.cdb id 4"]
name_key: "ItemName_7004"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 2
stats:
  - {"code": 1, "stat": "Attack", "value": 9, "scale": "flat"}
  - {"code": 1, "stat": "Attack", "value": 16, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 1}
icon: {"file": "Items_27.png", "index": 2}
obtained_from:
  - {"how": "jewel_craft", "recipe": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=839df9 type=d36ca9 id=f78eed sources=a302b5 name_key=4e66b0 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=da4b92 stats=8bb4eb options=88c977 icon=8aaeff obtained_from=697e2f -->
|  |  |
|---|---|
|  | ![Attack Rune](../assets/items/7004.png) |
| **Item id** | `7004` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 2 |
| **Icon** | `ui/icons/Items_27.png` cell 2 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack | +9 | flat | 1 |
| Attack | +16 | flat (from Item_Jewel) | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 1 | rune grade? |

Jewel upgrade (JewelSocketMake 2): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 15, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 15 from [[wiki/items/7003-attack-rune|Attack Rune]].

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

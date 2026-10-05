---
title: "Attack Rune"
type: "item"
id: 7007
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7007", "client (server-only table): Item_Jewel.cdb id 7"]
name_key: "ItemName_7007"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 1, "stat": "Attack", "value": 22, "scale": "flat"}
  - {"code": 1, "stat": "Attack", "value": 42, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 1}
icon: {"file": "Items_27.png", "index": 5}
obtained_from:
  - {"how": "jewel_craft", "recipe": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=839df9 type=d36ca9 id=2a5418 sources=6637c3 name_key=e181d5 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=82788a options=88c977 icon=914087 obtained_from=ba6cf5 -->
|  |  |
|---|---|
|  | ![Attack Rune](wiki/assets/items/7007.png) |
| **Item id** | `7007` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_27.png` cell 5 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack | +22 | flat | 1 |
| Attack | +42 | flat (from Item_Jewel) | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 1 | rune grade? |

Jewel upgrade (JewelSocketMake 5): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 60, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7006-attack-rune|Attack Rune]].

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

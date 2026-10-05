---
title: "Magic Resist Rune"
type: "item"
id: 7036
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7036", "client (server-only table): Item_Jewel.cdb id 36"]
name_key: "ItemName_7036"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 4
stats:
  - {"code": 7, "stat": "Magic Resist", "value": 27, "scale": "flat"}
  - {"code": 7, "stat": "Magic Resist", "value": 9, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 4}
icon: {"file": "Items_28.png", "index": 60}
obtained_from:
  - {"how": "jewel_craft", "recipe": 34}
---
<!-- generated:start -->
<!-- generated-keys: title=9c916e type=d36ca9 id=fe9ffc sources=d8ce38 name_key=8830da kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=1b6453 stats=99c2bf options=2ddee2 icon=d18bbb obtained_from=146aac -->
|  |  |
|---|---|
|  | ![Magic Resist Rune](wiki/assets/items/7036.png) |
| **Item id** | `7036` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 4 |
| **Icon** | `ui/icons/Items_28.png` cell 60 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic Resist | +27 | flat | 7 |
| Magic Resist | +9 | flat (from Item_Jewel) | 7 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 4 | rune grade? |

Jewel upgrade (JewelSocketMake 34): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 30, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30 from [[wiki/items/7035-magic-resist-rune|Magic Resist Rune]].

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

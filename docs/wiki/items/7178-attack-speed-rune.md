---
title: "Attack Speed(%) Rune"
type: "item"
id: 7178
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7178", "client (server-only table): Item_Jewel.cdb id 178"]
name_key: "ItemName_7178"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 6
stats:
  - {"code": 103, "stat": "Attack Speed(%)", "value": 7, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 29, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 18}
icon: {"file": "Items_27.png", "index": 36}
obtained_from:
  - {"how": "jewel_craft", "recipe": 176}
---
<!-- generated:start -->
<!-- generated-keys: title=55340f type=d36ca9 id=93c96b sources=36be63 name_key=745a43 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=c1dfd9 stats=79f6ed options=109d7f icon=1ca53d obtained_from=f63255 -->
|  |  |
|---|---|
|  | ![Attack Speed(%) Rune](wiki/assets/items/7178.png) |
| **Item id** | `7178` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 6 |
| **Icon** | `ui/icons/Items_27.png` cell 36 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack Speed(%) | Attack Speed +7% | flat | 103 |
| Attack Speed(%) | Attack Speed +29% | flat (from Item_Jewel) | 103 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 18 | rune grade? |

Jewel upgrade (JewelSocketMake 176): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 80, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7177-attack-speed-rune|Attack Speed(%) Rune]].

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

---
title: "Attack Speed(%) Rune"
type: "item"
id: 7176
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7176", "client (server-only table): Item_Jewel.cdb id 176"]
name_key: "ItemName_7176"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 4
stats:
  - {"code": 103, "stat": "Attack Speed(%)", "value": 5, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 15, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 18}
icon: {"file": "Items_27.png", "index": 34}
obtained_from:
  - {"how": "jewel_craft", "recipe": 174}
---
<!-- generated:start -->
<!-- generated-keys: title=55340f type=d36ca9 id=a793f8 sources=b44531 name_key=f96369 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=1b6453 stats=d9a95b options=109d7f icon=e63447 obtained_from=dd852a -->
|  |  |
|---|---|
|  | ![Attack Speed(%) Rune](../assets/items/7176.png) |
| **Item id** | `7176` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 4 |
| **Icon** | `ui/icons/Items_27.png` cell 34 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack Speed(%) | Attack Speed +5% | flat | 103 |
| Attack Speed(%) | Attack Speed +15% | flat (from Item_Jewel) | 103 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 18 | rune grade? |

Jewel upgrade (JewelSocketMake 174): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 30, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 30 from [[wiki/items/7175-attack-speed-rune|Attack Speed(%) Rune]].

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

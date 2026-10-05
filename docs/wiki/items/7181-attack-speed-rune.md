---
title: "Attack Speed(%) Rune"
type: "item"
id: 7181
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7181", "client (server-only table): Item_Jewel.cdb id 181"]
name_key: "ItemName_7181"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 103, "stat": "Attack Speed(%)", "value": 13, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 60, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 18}
icon: {"file": "Items_27.png", "index": 39}
obtained_from:
  - {"how": "jewel_craft", "recipe": 179}
---
<!-- generated:start -->
<!-- generated-keys: title=55340f type=d36ca9 id=2085e7 sources=ecfc53 name_key=0e70b4 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=c9de67 options=109d7f icon=8e0bca obtained_from=dfd6a4 -->
|  |  |
|---|---|
|  | ![Attack Speed(%) Rune](../assets/items/7181.png) |
| **Item id** | `7181` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_27.png` cell 39 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack Speed(%) | Attack Speed +13% | flat | 103 |
| Attack Speed(%) | Attack Speed +60% | flat (from Item_Jewel) | 103 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 18 | rune grade? |

Jewel upgrade (JewelSocketMake 179): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7180-attack-speed-rune|Attack Speed(%) Rune]].

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

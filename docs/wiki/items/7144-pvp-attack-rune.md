---
title: "PvP Attack Rune"
type: "item"
id: 7144
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7144", "client (server-only table): Item_Jewel.cdb id 144"]
name_key: "ItemName_7144"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 2
stats:
  - {"code": 141, "stat": "PvP Attack", "value": 3, "scale": "flat"}
  - {"code": 136, "stat": "Damage(%)+", "value": 3, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 15}
icon: {"file": "Items_25.png", "index": 14}
obtained_from:
  - {"how": "random_box", "box": 50}
  - {"how": "jewel_craft", "recipe": 142}
---
<!-- generated:start -->
<!-- generated-keys: title=e67265 type=d36ca9 id=b23edb sources=8308a8 name_key=753937 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=da4b92 stats=2361b6 options=0522b7 icon=cdbc7a obtained_from=17ca7f -->
|  |  |
|---|---|
|  | ![PvP Attack Rune](wiki/assets/items/7144.png) |
| **Item id** | `7144` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 2 |
| **Icon** | `ui/icons/Items_25.png` cell 14 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Attack | +3 | flat | 141 |
| Damage(%)+ | Damage +3%+ | flat (from Item_Jewel) | 136 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 15 | rune grade? |

Jewel upgrade (JewelSocketMake 142): [[wiki/items/702-crystal-red|Crystal : Red]] × 20, [[wiki/items/615-red-passion-fragments-b|Red Passion Fragments (B)]] × 20, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7143-pvp-attack-rune|PvP Attack Rune]].

### Where to get it

- In random box table row 50 (RandomBox.cdb; odds are server side)
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

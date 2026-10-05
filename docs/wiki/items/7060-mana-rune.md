---
title: "Mana Rune"
type: "item"
id: 7060
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7060", "client (server-only table): Item_Jewel.cdb id 60"]
name_key: "ItemName_7060"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 33, "stat": "Mana", "value": 135, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 384, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 6}
icon: {"file": "Items_28.png", "index": 4}
obtained_from:
  - {"how": "jewel_craft", "recipe": 58}
---
<!-- generated:start -->
<!-- generated-keys: title=1e6304 type=d36ca9 id=e39150 sources=c31ad5 name_key=e3a2de kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=e260d5 options=533fa4 icon=9a77e2 obtained_from=bd29e2 -->
|  |  |
|---|---|
|  | ![Mana Rune](../assets/items/7060.png) |
| **Item id** | `7060` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_28.png` cell 4 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Mana | +135 | flat | 33 |
| Mana | +384 | flat (from Item_Jewel) | 33 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 6 | rune grade? |

Jewel upgrade (JewelSocketMake 58): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 10, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7059-mana-rune|Mana Rune]].

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

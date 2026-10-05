---
title: "Mana Rune"
type: "item"
id: 7054
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7054", "client (server-only table): Item_Jewel.cdb id 54"]
name_key: "ItemName_7054"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 2
stats:
  - {"code": 33, "stat": "Mana", "value": 40, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 64, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 6}
icon: {"file": "Items_27.png", "index": 62}
obtained_from:
  - {"how": "jewel_craft", "recipe": 52}
---
<!-- generated:start -->
<!-- generated-keys: title=1e6304 type=d36ca9 id=d05f29 sources=fee30e name_key=ecc296 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=da4b92 stats=e57d71 options=533fa4 icon=776cfb obtained_from=b980c3 -->
|  |  |
|---|---|
|  | ![Mana Rune](../assets/items/7054.png) |
| **Item id** | `7054` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 2 |
| **Icon** | `ui/icons/Items_27.png` cell 62 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Mana | +40 | flat | 33 |
| Mana | +64 | flat (from Item_Jewel) | 33 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 6 | rune grade? |

Jewel upgrade (JewelSocketMake 52): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 15, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 15 from [[wiki/items/7053-mana-rune|Mana Rune]].

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

---
title: "Mana Regeneration Rune"
type: "item"
id: 7080
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7080", "client (server-only table): Item_Jewel.cdb id 80"]
name_key: "ItemName_7080"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 34, "stat": "Mana Regeneration", "value": 17, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 144, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 8}
icon: {"file": "Items_28.png", "index": 24}
obtained_from:
  - {"how": "jewel_craft", "recipe": 78}
---
<!-- generated:start -->
<!-- generated-keys: title=cbe828 type=d36ca9 id=bc5b26 sources=69a920 name_key=f7107e kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=e754e2 options=b7f834 icon=007a51 obtained_from=ab4dfa -->
|  |  |
|---|---|
|  | ![Mana Regeneration Rune](wiki/assets/items/7080.png) |
| **Item id** | `7080` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_28.png` cell 24 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Mana Regeneration | +17 | flat | 34 |
| Mana Regeneration | +144 | flat (from Item_Jewel) | 34 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 8 | rune grade? |

Jewel upgrade (JewelSocketMake 78): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 10, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 10, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7079-mana-regeneration-rune|Mana Regeneration Rune]].

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

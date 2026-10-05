---
title: "Cooldown Reduction Rune"
type: "item"
id: 7189
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7189", "client (server-only table): Item_Jewel.cdb id 189"]
name_key: "ItemName_7189"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 7
stats:
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 8, "scale": "flat"}
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 15, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 19}
icon: {"file": "Items_27.png", "index": 57}
obtained_from:
  - {"how": "jewel_craft", "recipe": 187}
---
<!-- generated:start -->
<!-- generated-keys: title=a62c86 type=d36ca9 id=047e38 sources=9b9757 name_key=0f04c6 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=902ba3 stats=d4bd04 options=c1a4c7 icon=4dfabc obtained_from=3d0598 -->
|  |  |
|---|---|
|  | ![Cooldown Reduction Rune](wiki/assets/items/7189.png) |
| **Item id** | `7189` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 7 |
| **Icon** | `ui/icons/Items_27.png` cell 57 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Cooldown Reduction(%) | Cooldown Reduction +8% | flat | 212 |
| Cooldown Reduction(%) | Cooldown Reduction +15% | flat (from Item_Jewel) | 212 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 19 | rune grade? |

Jewel upgrade (JewelSocketMake 187): [[wiki/items/702-crystal-red|Crystal : Red]] × 20, [[wiki/items/614-red-passion-piece-c|Red Passion Piece (C)]] × 15, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7188-cooldown-reduction-rune|Cooldown Reduction Rune]].

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

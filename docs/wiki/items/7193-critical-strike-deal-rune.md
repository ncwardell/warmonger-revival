---
title: "Critical Strike Deal Rune"
type: "item"
id: 7193
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7193", "client (server-only table): Item_Jewel.cdb id 193"]
name_key: "ItemName_7193"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 1
stats:
  - {"code": 10, "stat": "Critical Strike Deal", "value": 5, "scale": "flat"}
  - {"code": 10, "stat": "Critical Strike Deal", "value": 12, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 20}
icon: {"file": "Items_27.png", "index": 21}
obtained_from:
  - {"how": "jewel_craft", "recipe": 191}
---
<!-- generated:start -->
<!-- generated-keys: title=3e9edc type=d36ca9 id=e89d99 sources=de0a89 name_key=a7ac18 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=356a19 stats=19b485 options=1a760e icon=5bbcb9 obtained_from=cafa7c -->
|  |  |
|---|---|
|  | ![Critical Strike Deal Rune](../assets/items/7193.png) |
| **Item id** | `7193` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 1 |
| **Icon** | `ui/icons/Items_27.png` cell 21 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Critical Strike Deal | +5 | flat | 10 |
| Critical Strike Deal | +12 | flat (from Item_Jewel) | 10 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 20 | rune grade? |

Jewel upgrade (JewelSocketMake 191): [[wiki/items/702-crystal-red|Crystal : Red]] × 10, [[wiki/items/615-red-passion-fragments-b|Red Passion Fragments (B)]] × 15, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7192-critical-strike-deal-rune|Critical Strike Deal Rune]].

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

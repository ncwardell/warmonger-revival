---
title: "Critical Strike Deal Rune"
type: "item"
id: 7192
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7192", "client (server-only table): Item_Jewel.cdb id 192"]
name_key: "ItemName_7192"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 10, "stat": "Critical Strike Deal", "value": 3, "scale": "flat"}
  - {"code": 10, "stat": "Critical Strike Deal", "value": 10, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 20}
icon: {"file": "Items_27.png", "index": 20}
obtained_from:
  - {"how": "craft", "recipe": 1820}
---
<!-- generated:start -->
<!-- generated-keys: title=3e9edc type=d36ca9 id=8e5b51 sources=0c969f name_key=1cfcd9 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=5e8e0d options=1a760e icon=a9fbcc obtained_from=dc3a31 -->
|  |  |
|---|---|
|  | ![Critical Strike Deal Rune](../assets/items/7192.png) |
| **Item id** | `7192` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_27.png` cell 20 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Critical Strike Deal | +3 | flat | 10 |
| Critical Strike Deal | +10 | flat (from Item_Jewel) | 10 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 20 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1820 | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/814-topaz\|Topaz]] × 10 | 0 | 100 |

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

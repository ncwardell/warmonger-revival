---
title: "Mana Rune"
type: "item"
id: 7057
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7057", "client (server-only table): Item_Jewel.cdb id 57"]
name_key: "ItemName_7057"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 33, "stat": "Mana", "value": 80, "scale": "flat"}
  - {"code": 33, "stat": "Mana", "value": 168, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 6}
icon: {"file": "Items_28.png", "index": 1}
obtained_from:
  - {"how": "jewel_craft", "recipe": 55}
---
<!-- generated:start -->
<!-- generated-keys: title=1e6304 type=d36ca9 id=42e931 sources=1d6d2c name_key=4b6b6f kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=5211b0 options=533fa4 icon=780739 obtained_from=f1e24b -->
|  |  |
|---|---|
|  | ![Mana Rune](wiki/assets/items/7057.png) |
| **Item id** | `7057` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_28.png` cell 1 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Mana | +80 | flat | 33 |
| Mana | +168 | flat (from Item_Jewel) | 33 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 6 | rune grade? |

Jewel upgrade (JewelSocketMake 55): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 60, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7056-mana-rune|Mana Rune]].

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

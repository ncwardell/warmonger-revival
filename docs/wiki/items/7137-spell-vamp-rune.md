---
title: "Spell Vamp Rune"
type: "item"
id: 7137
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7137", "client (server-only table): Item_Jewel.cdb id 137"]
name_key: "ItemName_7137"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 43, "stat": "Spell Vamp(%)", "value": 6, "scale": "flat"}
  - {"code": 43, "stat": "Spell Vamp(%)", "value": 13, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 14}
icon: {"file": "Items_28.png", "index": 11}
obtained_from:
  - {"how": "jewel_craft", "recipe": 135}
---
<!-- generated:start -->
<!-- generated-keys: title=a02465 type=d36ca9 id=c4a79f sources=497b43 name_key=8ef6b0 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=b0d345 options=f4abe0 icon=b19a6a obtained_from=ac72e0 -->
|  |  |
|---|---|
|  | ![Spell Vamp Rune](wiki/assets/items/7137.png) |
| **Item id** | `7137` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_28.png` cell 11 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Spell Vamp(%) | Spell Vamp +6% | flat | 43 |
| Spell Vamp(%) | Spell Vamp +13% | flat (from Item_Jewel) | 43 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 14 | rune grade? |

Jewel upgrade (JewelSocketMake 135): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 80, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 40, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7136-spell-vamp-rune|Spell Vamp Rune]].

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

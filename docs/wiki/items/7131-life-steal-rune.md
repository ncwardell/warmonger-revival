---
title: "Life Steal Rune"
type: "item"
id: 7131
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7131", "client (server-only table): Item_Jewel.cdb id 131"]
name_key: "ItemName_7131"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 41, "stat": "Life Steal(%)", "value": 10, "scale": "flat"}
  - {"code": 41, "stat": "Life Steal(%)", "value": 36, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 13}
icon: {"file": "Items_28.png", "index": 45}
obtained_from:
  - {"how": "jewel_craft", "recipe": 129}
---
<!-- generated:start -->
<!-- generated-keys: title=431cea type=d36ca9 id=473301 sources=e894d1 name_key=04b52b kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=b99cc7 options=1b1fe1 icon=139f4a obtained_from=b54b4b -->
|  |  |
|---|---|
|  | ![Life Steal Rune](../assets/items/7131.png) |
| **Item id** | `7131` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_28.png` cell 45 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Life Steal(%) | Life Steal +10% | flat | 41 |
| Life Steal(%) | Life Steal +36% | flat (from Item_Jewel) | 41 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 13 | rune grade? |

Jewel upgrade (JewelSocketMake 129): [[wiki/items/702-crystal-red|Crystal : Red]] × 60, [[wiki/items/614-red-passion-piece-c|Red Passion Piece (C)]] × 30, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7130-life-steal-rune|Life Steal Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
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

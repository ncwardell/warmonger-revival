---
title: "Life Steal Rune"
type: "item"
id: 7127
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7127", "client (server-only table): Item_Jewel.cdb id 127"]
name_key: "ItemName_7127"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 41, "stat": "Life Steal(%)", "value": 6, "scale": "flat"}
  - {"code": 41, "stat": "Life Steal(%)", "value": 13, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 13}
icon: {"file": "Items_28.png", "index": 41}
obtained_from:
  - {"how": "jewel_craft", "recipe": 125}
---
<!-- generated:start -->
<!-- generated-keys: title=431cea type=d36ca9 id=caebf4 sources=6da283 name_key=5fa432 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=a1749a options=1b1fe1 icon=ee9a62 obtained_from=7ea595 -->
|  |  |
|---|---|
|  | ![Life Steal Rune](../assets/items/7127.png) |
| **Item id** | `7127` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_28.png` cell 41 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Life Steal(%) | Life Steal +6% | flat | 41 |
| Life Steal(%) | Life Steal +13% | flat (from Item_Jewel) | 41 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 13 | rune grade? |

Jewel upgrade (JewelSocketMake 125): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 80, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 40, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7126-life-steal-rune|Life Steal Rune]].

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

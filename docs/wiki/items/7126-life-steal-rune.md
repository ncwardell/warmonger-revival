---
title: "Life Steal Rune"
type: "item"
id: 7126
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7126", "client (server-only table): Item_Jewel.cdb id 126"]
name_key: "ItemName_7126"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 4
stats:
  - {"code": 41, "stat": "Life Steal(%)", "value": 5, "scale": "flat"}
  - {"code": 41, "stat": "Life Steal(%)", "value": 9, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 13}
icon: {"file": "Items_28.png", "index": 40}
obtained_from:
  - {"how": "jewel_craft", "recipe": 124}
---
<!-- generated:start -->
<!-- generated-keys: title=431cea type=d36ca9 id=f8040f sources=a47a07 name_key=dac6f3 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=1b6453 stats=68800a options=1b1fe1 icon=376e5a obtained_from=57e3fe -->
|  |  |
|---|---|
|  | ![Life Steal Rune](wiki/assets/items/7126.png) |
| **Item id** | `7126` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 4 |
| **Icon** | `ui/icons/Items_28.png` cell 40 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Life Steal(%) | Life Steal +5% | flat | 41 |
| Life Steal(%) | Life Steal +9% | flat (from Item_Jewel) | 41 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 13 | rune grade? |

Jewel upgrade (JewelSocketMake 124): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 60, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 30, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7125-life-steal-rune|Life Steal Rune]].

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

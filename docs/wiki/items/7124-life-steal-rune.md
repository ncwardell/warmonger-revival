---
title: "Life Steal Rune"
type: "item"
id: 7124
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7124", "client (server-only table): Item_Jewel.cdb id 124"]
name_key: "ItemName_7124"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 2
stats:
  - {"code": 41, "stat": "Life Steal(%)", "value": 3, "scale": "flat"}
  - {"code": 41, "stat": "Life Steal(%)", "value": 5, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 13}
icon: {"file": "Items_28.png", "index": 38}
obtained_from:
  - {"how": "jewel_craft", "recipe": 122}
---
<!-- generated:start -->
<!-- generated-keys: title=431cea type=d36ca9 id=52d058 sources=27c99c name_key=185f52 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=da4b92 stats=808b61 options=1b1fe1 icon=e1f5a3 obtained_from=b880f0 -->
|  |  |
|---|---|
|  | ![Life Steal Rune](../assets/items/7124.png) |
| **Item id** | `7124` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 2 |
| **Icon** | `ui/icons/Items_28.png` cell 38 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Life Steal(%) | Life Steal +3% | flat | 41 |
| Life Steal(%) | Life Steal +5% | flat (from Item_Jewel) | 41 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 13 | rune grade? |

Jewel upgrade (JewelSocketMake 122): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 20, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 15, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7123-life-steal-rune|Life Steal Rune]].

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

---
title: "PvP Armor Rune"
type: "item"
id: 7157
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7157", "client (server-only table): Item_Jewel.cdb id 157"]
name_key: "ItemName_7157"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 142, "stat": "PvP Armor", "value": 6, "scale": "flat"}
  - {"code": 137, "stat": "option 137", "value": 8, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 16}
icon: {"file": "Items_25.png", "index": 23}
obtained_from:
  - {"how": "jewel_craft", "recipe": 155}
---
<!-- generated:start -->
<!-- generated-keys: title=1f4563 type=d36ca9 id=09c30c sources=b86f1b name_key=182e87 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=350c53 options=3a5286 icon=063f8a obtained_from=faee22 -->
|  |  |
|---|---|
|  | ![PvP Armor Rune](wiki/assets/items/7157.png) |
| **Item id** | `7157` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_25.png` cell 23 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Armor | +6 | flat | 142 |
| option 137 | +8 | flat (from Item_Jewel) | 137 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 16 | rune grade? |

Jewel upgrade (JewelSocketMake 155): [[wiki/items/703-crystal-black|Crystal : Black]] × 10, [[wiki/items/616-red-passion-piece-b|Red Passion Piece (B)]] × 10, [[wiki/items/857-amplifying-passion|Amplifying Passion]] × 1 from [[wiki/items/7156-pvp-armor-rune|PvP Armor Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
- [[gameplay/sources|Sources and gaps]]
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

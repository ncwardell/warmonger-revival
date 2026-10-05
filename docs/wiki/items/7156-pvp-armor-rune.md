---
title: "PvP Armor Rune"
type: "item"
id: 7156
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7156", "client (server-only table): Item_Jewel.cdb id 156"]
name_key: "ItemName_7156"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 4
stats:
  - {"code": 142, "stat": "PvP Armor", "value": 5, "scale": "flat"}
  - {"code": 137, "stat": "option 137", "value": 6, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 16}
icon: {"file": "Items_25.png", "index": 22}
obtained_from:
  - {"how": "jewel_craft", "recipe": 154}
---
<!-- generated:start -->
<!-- generated-keys: title=1f4563 type=d36ca9 id=998e0e sources=dac2d3 name_key=612198 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=1b6453 stats=6f04c1 options=3a5286 icon=cae818 obtained_from=e8e469 -->
|  |  |
|---|---|
|  | ![PvP Armor Rune](wiki/assets/items/7156.png) |
| **Item id** | `7156` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 4 |
| **Icon** | `ui/icons/Items_25.png` cell 22 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Armor | +5 | flat | 142 |
| option 137 | +6 | flat (from Item_Jewel) | 137 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 16 | rune grade? |

Jewel upgrade (JewelSocketMake 154): [[wiki/items/702-crystal-red|Crystal : Red]] × 60, [[wiki/items/615-red-passion-fragments-b|Red Passion Fragments (B)]] × 40, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7155-pvp-armor-rune|PvP Armor Rune]].

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

---
title: "PvP Armor Rune"
type: "item"
id: 7154
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7154", "client (server-only table): Item_Jewel.cdb id 154"]
name_key: "ItemName_7154"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 2
stats:
  - {"code": 142, "stat": "PvP Armor", "value": 3, "scale": "flat"}
  - {"code": 137, "stat": "option 137", "value": 3, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 16}
icon: {"file": "Items_25.png", "index": 20}
obtained_from:
  - {"how": "random_box", "box": 50}
  - {"how": "jewel_craft", "recipe": 152}
---
<!-- generated:start -->
<!-- generated-keys: title=1f4563 type=d36ca9 id=63990a sources=812512 name_key=59ac10 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=da4b92 stats=825bca options=3a5286 icon=759655 obtained_from=ad55f0 -->
|  |  |
|---|---|
|  | ![PvP Armor Rune](wiki/assets/items/7154.png) |
| **Item id** | `7154` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 2 |
| **Icon** | `ui/icons/Items_25.png` cell 20 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Armor | +3 | flat | 142 |
| option 137 | +3 | flat (from Item_Jewel) | 137 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 16 | rune grade? |

Jewel upgrade (JewelSocketMake 152): [[wiki/items/702-crystal-red|Crystal : Red]] × 20, [[wiki/items/615-red-passion-fragments-b|Red Passion Fragments (B)]] × 20, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7153-pvp-armor-rune|PvP Armor Rune]].

### Where to get it

- In random box table row 50 (RandomBox.cdb; odds are server side)

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

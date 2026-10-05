---
title: "PvP Armor Rune"
type: "item"
id: 7152
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7152", "client (server-only table): Item_Jewel.cdb id 152"]
name_key: "ItemName_7152"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 142, "stat": "PvP Armor", "value": 1, "scale": "flat"}
  - {"code": 137, "stat": "option 137", "value": 2, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 16}
icon: {"file": "Items_25.png", "index": 18}
obtained_from:
  - {"how": "craft", "recipe": 1816}
---
<!-- generated:start -->
<!-- generated-keys: title=1f4563 type=d36ca9 id=456734 sources=e26519 name_key=0201bf kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=3b8ce1 options=3a5286 icon=07c22a obtained_from=28f519 -->
|  |  |
|---|---|
|  | ![PvP Armor Rune](wiki/assets/items/7152.png) |
| **Item id** | `7152` |
| **Kind** | Rune (35) |
| **Category** | [[wiki/items/runes\|Runes and gem stones]] |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_25.png` cell 18 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| PvP Armor | +1 | flat | 142 |
| option 137 | +2 | flat (from Item_Jewel) | 137 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 16 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1816 | [[wiki/items/703-crystal-black\|Crystal : Black]] × 10, [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/854-shining-passion\|Shining Passion]] × 3 | 0 | 100 |

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

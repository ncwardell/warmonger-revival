---
title: "Armor Rune"
type: "item"
id: 7025
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7025", "client (server-only table): Item_Jewel.cdb id 25"]
name_key: "ItemName_7025"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 3
stats:
  - {"code": 6, "stat": "Armor", "value": 13, "scale": "flat"}
  - {"code": 6, "stat": "Armor", "value": 11, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 3}
icon: {"file": "Items_29.png", "index": 25}
obtained_from:
  - {"how": "jewel_craft", "recipe": 23}
---
<!-- generated:start -->
<!-- generated-keys: title=3a5337 type=d36ca9 id=179472 sources=63f0d3 name_key=9a8aed kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=77de68 stats=d5a307 options=1d3c27 icon=66eba2 obtained_from=e25ed5 -->
|  |  |
|---|---|
|  | ![Armor Rune](wiki/assets/items/7025.png) |
| **Item id** | `7025` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 3 |
| **Icon** | `ui/icons/Items_29.png` cell 25 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor | +13 | flat | 6 |
| Armor | +11 | flat (from Item_Jewel) | 6 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 3 | rune grade? |

Jewel upgrade (JewelSocketMake 23): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 20, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 20 from [[wiki/items/7024-armor-rune|Armor Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
- [[gameplay/sources|Sources and gaps]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
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

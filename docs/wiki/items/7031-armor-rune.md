---
title: "Armor Rune"
type: "item"
id: 7031
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7031", "client (server-only table): Item_Jewel.cdb id 31"]
name_key: "ItemName_7031"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 6, "stat": "Armor", "value": 45, "scale": "flat"}
  - {"code": 6, "stat": "Armor", "value": 60, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 3}
icon: {"file": "Items_29.png", "index": 31}
obtained_from:
  - {"how": "jewel_craft", "recipe": 29}
---
<!-- generated:start -->
<!-- generated-keys: title=3a5337 type=d36ca9 id=e78e39 sources=33b150 name_key=620b41 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=2392e5 options=1d3c27 icon=d28d57 obtained_from=01df10 -->
|  |  |
|---|---|
|  | ![Armor Rune](../assets/items/7031.png) |
| **Item id** | `7031` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_29.png` cell 31 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor | +45 | flat | 6 |
| Armor | +60 | flat (from Item_Jewel) | 6 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 3 | rune grade? |

Jewel upgrade (JewelSocketMake 29): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 20, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 15, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7030-armor-rune|Armor Rune]].

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

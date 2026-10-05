---
title: "Armor Rune"
type: "item"
id: 7027
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7027", "client (server-only table): Item_Jewel.cdb id 27"]
name_key: "ItemName_7027"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 5
stats:
  - {"code": 6, "stat": "Armor", "value": 22, "scale": "flat"}
  - {"code": 6, "stat": "Armor", "value": 21, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 3}
icon: {"file": "Items_29.png", "index": 27}
obtained_from:
  - {"how": "jewel_craft", "recipe": 25}
---
<!-- generated:start -->
<!-- generated-keys: title=3a5337 type=d36ca9 id=8bfcbc sources=b206bb name_key=12c2c3 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=ac3478 stats=234de7 options=1d3c27 icon=16f21b obtained_from=19504d -->
|  |  |
|---|---|
|  | ![Armor Rune](../assets/items/7027.png) |
| **Item id** | `7027` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 5 |
| **Icon** | `ui/icons/Items_29.png` cell 27 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor | +22 | flat | 6 |
| Armor | +21 | flat (from Item_Jewel) | 6 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 3 | rune grade? |

Jewel upgrade (JewelSocketMake 25): [[wiki/items/700-crystal-blue|Crystal : Blue]] × 60, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40, [[wiki/items/854-shining-passion|Shining Passion]] × 1 from [[wiki/items/7026-armor-rune|Armor Rune]].

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

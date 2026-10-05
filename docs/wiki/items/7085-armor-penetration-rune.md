---
title: "Armor Penetration Rune"
type: "item"
id: 7085
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7085", "client (server-only table): Item_Jewel.cdb id 85"]
name_key: "ItemName_7085"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 3
stats:
  - {"code": 13, "stat": "Armor Penetration", "value": 4, "scale": "flat"}
  - {"code": 13, "stat": "Armor Penetration", "value": 22, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 9}
icon: {"file": "Items_29.png", "index": 35}
obtained_from:
  - {"how": "jewel_craft", "recipe": 83}
---
<!-- generated:start -->
<!-- generated-keys: title=49e5d7 type=d36ca9 id=d0b4db sources=338f6e name_key=5995bf kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=77de68 stats=6de31d options=9b3b47 icon=744e1a obtained_from=bc711f -->
|  |  |
|---|---|
|  | ![Armor Penetration Rune](../assets/items/7085.png) |
| **Item id** | `7085` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 3 |
| **Icon** | `ui/icons/Items_29.png` cell 35 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor Penetration | +4 | flat | 13 |
| Armor Penetration | +22 | flat (from Item_Jewel) | 13 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 9 | rune grade? |

Jewel upgrade (JewelSocketMake 83): [[wiki/items/701-crystal-yellow|Crystal : Yellow]] × 40, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 20, [[wiki/items/855-mysterious-passion|Mysterious Passion]] × 1 from [[wiki/items/7084-armor-penetration-rune|Armor Penetration Rune]].

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Mentioned in

- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
- [[gameplay/video-rune-upgrades|Video notes: rune upgrade attempts (ZonderCoRe)]]
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

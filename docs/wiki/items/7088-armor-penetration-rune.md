---
title: "Armor Penetration Rune"
type: "item"
id: 7088
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7088", "client (server-only table): Item_Jewel.cdb id 88"]
name_key: "ItemName_7088"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 6
stats:
  - {"code": 13, "stat": "Armor Penetration", "value": 10, "scale": "flat"}
  - {"code": 13, "stat": "Armor Penetration", "value": 58, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 9}
icon: {"file": "Items_29.png", "index": 38}
obtained_from:
  - {"how": "jewel_craft", "recipe": 86}
---
<!-- generated:start -->
<!-- generated-keys: title=49e5d7 type=d36ca9 id=5a398b sources=952a1e name_key=96aa04 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=c1dfd9 stats=b2854a options=9b3b47 icon=abb60f obtained_from=d8262e -->
|  |  |
|---|---|
|  | ![Armor Penetration Rune](../assets/items/7088.png) |
| **Item id** | `7088` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 6 |
| **Icon** | `ui/icons/Items_29.png` cell 38 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor Penetration | +10 | flat | 13 |
| Armor Penetration | +58 | flat (from Item_Jewel) | 13 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 9 | rune grade? |

Jewel upgrade (JewelSocketMake 86): [[wiki/items/702-crystal-red|Crystal : Red]] × 10, [[wiki/items/614-red-passion-piece-c|Red Passion Piece (C)]] × 10, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7087-armor-penetration-rune|Armor Penetration Rune]].

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

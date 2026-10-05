---
title: "Armor Penetration Rune"
type: "item"
id: 7091
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7091", "client (server-only table): Item_Jewel.cdb id 91"]
name_key: "ItemName_7091"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 13, "stat": "Armor Penetration", "value": 16, "scale": "flat"}
  - {"code": 13, "stat": "Armor Penetration", "value": 120, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 9}
icon: {"file": "Items_29.png", "index": 41}
obtained_from:
  - {"how": "jewel_craft", "recipe": 89}
---
<!-- generated:start -->
<!-- generated-keys: title=49e5d7 type=d36ca9 id=97448d sources=3e9b4b name_key=2b16ee kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=c496f1 options=9b3b47 icon=35c3a7 obtained_from=944a17 -->
|  |  |
|---|---|
|  | ![Armor Penetration Rune](wiki/assets/items/7091.png) |
| **Item id** | `7091` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_29.png` cell 41 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor Penetration | +16 | flat | 13 |
| Armor Penetration | +120 | flat (from Item_Jewel) | 13 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 9 | rune grade? |

Jewel upgrade (JewelSocketMake 89): [[wiki/items/702-crystal-red|Crystal : Red]] × 60, [[wiki/items/614-red-passion-piece-c|Red Passion Piece (C)]] × 30, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7090-armor-penetration-rune|Armor Penetration Rune]].

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

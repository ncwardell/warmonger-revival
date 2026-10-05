---
title: "Armor Penetration(%) Rune"
type: "item"
id: 7110
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7110", "client (server-only table): Item_Jewel.cdb id 110"]
name_key: "ItemName_7110"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 8
stats:
  - {"code": 113, "stat": "Armor Penetration(%)", "value": 9, "scale": "flat"}
  - {"code": 113, "stat": "Armor Penetration(%)", "value": 29, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 11}
icon: {"file": "Items_29.png", "index": 50}
obtained_from:
  - {"how": "jewel_craft", "recipe": 108}
---
<!-- generated:start -->
<!-- generated-keys: title=bbf7a2 type=d36ca9 id=26a2c2 sources=dc53b9 name_key=47779e kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=fe5dbb stats=78e561 options=586751 icon=d071b7 obtained_from=f7ef81 -->
|  |  |
|---|---|
|  | ![Armor Penetration(%) Rune](../assets/items/7110.png) |
| **Item id** | `7110` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 8 |
| **Icon** | `ui/icons/Items_29.png` cell 50 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor Penetration(%) | Armor Penetration +9% | flat | 113 |
| Armor Penetration(%) | Armor Penetration +29% | flat (from Item_Jewel) | 113 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 11 | rune grade? |

Jewel upgrade (JewelSocketMake 108): [[wiki/items/703-crystal-black|Crystal : Black]] × 60, [[wiki/items/616-red-passion-piece-b|Red Passion Piece (B)]] × 30, [[wiki/items/857-amplifying-passion|Amplifying Passion]] × 1 from [[wiki/items/7109-armor-penetration-rune|Armor Penetration(%) Rune]].

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

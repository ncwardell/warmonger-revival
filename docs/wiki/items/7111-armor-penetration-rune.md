---
title: "Armor Penetration(%) Rune"
type: "item"
id: 7111
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7111", "client (server-only table): Item_Jewel.cdb id 111"]
name_key: "ItemName_7111"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 9
stats:
  - {"code": 113, "stat": "Armor Penetration(%)", "value": 10, "scale": "flat"}
  - {"code": 113, "stat": "Armor Penetration(%)", "value": 36, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 11}
icon: {"file": "Items_29.png", "index": 51}
obtained_from:
  - {"how": "jewel_craft", "recipe": 109}
---
<!-- generated:start -->
<!-- generated-keys: title=bbf7a2 type=d36ca9 id=fde4e0 sources=bb9811 name_key=8ac9a3 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=0ade7c stats=d40576 options=586751 icon=6e5db8 obtained_from=a0fe22 -->
|  |  |
|---|---|
|  | ![Armor Penetration(%) Rune](wiki/assets/items/7111.png) |
| **Item id** | `7111` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 9 |
| **Icon** | `ui/icons/Items_29.png` cell 51 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor Penetration(%) | Armor Penetration +10% | flat | 113 |
| Armor Penetration(%) | Armor Penetration +36% | flat (from Item_Jewel) | 113 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 11 | rune grade? |

Jewel upgrade (JewelSocketMake 109): [[wiki/items/703-crystal-black|Crystal : Black]] × 80, [[wiki/items/616-red-passion-piece-b|Red Passion Piece (B)]] × 40, [[wiki/items/857-amplifying-passion|Amplifying Passion]] × 1 from [[wiki/items/7110-armor-penetration-rune|Armor Penetration(%) Rune]].

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

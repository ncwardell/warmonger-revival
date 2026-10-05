---
title: "Armor Penetration(%) Rune"
type: "item"
id: 7106
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7106", "client (server-only table): Item_Jewel.cdb id 106"]
name_key: "ItemName_7106"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 4
stats:
  - {"code": 113, "stat": "Armor Penetration(%)", "value": 5, "scale": "flat"}
  - {"code": 113, "stat": "Armor Penetration(%)", "value": 9, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 11}
icon: {"file": "Items_29.png", "index": 46}
obtained_from:
  - {"how": "jewel_craft", "recipe": 104}
---
<!-- generated:start -->
<!-- generated-keys: title=bbf7a2 type=d36ca9 id=b368c4 sources=dab3ec name_key=0070fb kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=1b6453 stats=237a3d options=586751 icon=b9d5ce obtained_from=15d5e5 -->
|  |  |
|---|---|
|  | ![Armor Penetration(%) Rune](../assets/items/7106.png) |
| **Item id** | `7106` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Rune level** | 4 |
| **Icon** | `ui/icons/Items_29.png` cell 46 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor Penetration(%) | Armor Penetration +5% | flat | 113 |
| Armor Penetration(%) | Armor Penetration +9% | flat (from Item_Jewel) | 113 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 11 | rune grade? |

Jewel upgrade (JewelSocketMake 104): [[wiki/items/702-crystal-red|Crystal : Red]] × 60, [[wiki/items/615-red-passion-fragments-b|Red Passion Fragments (B)]] × 40, [[wiki/items/856-brilliant-passion|Brilliant Passion]] × 1 from [[wiki/items/7105-armor-penetration-rune|Armor Penetration(%) Rune]].

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

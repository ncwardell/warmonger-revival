---
title: "Armor Penetration(%) Rune"
type: "item"
id: 7102
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7102", "client (server-only table): Item_Jewel.cdb id 102"]
name_key: "ItemName_7102"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 113, "stat": "Armor Penetration(%)", "value": 1, "scale": "flat"}
  - {"code": 113, "stat": "Armor Penetration(%)", "value": 3, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 11}
icon: {"file": "Items_29.png", "index": 42}
obtained_from:
  - {"how": "craft", "recipe": 1811}
---
<!-- generated:start -->
<!-- generated-keys: title=bbf7a2 type=d36ca9 id=67c39b sources=ddb583 name_key=f21664 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=dd1651 options=586751 icon=236d5c obtained_from=82a0c5 -->
|  |  |
|---|---|
|  | ![Armor Penetration(%) Rune](wiki/assets/items/7102.png) |
| **Item id** | `7102` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_29.png` cell 42 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor Penetration(%) | Armor Penetration +1% | flat | 113 |
| Armor Penetration(%) | Armor Penetration +3% | flat (from Item_Jewel) | 113 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 11 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1811 | [[wiki/items/702-crystal-red\|Crystal : Red]] × 10, [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/810-diamond\|Diamond]] × 10 | 0 | 100 |

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

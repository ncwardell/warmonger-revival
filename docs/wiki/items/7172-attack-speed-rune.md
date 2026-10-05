---
title: "Attack Speed(%) Rune"
type: "item"
id: 7172
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7172", "client (server-only table): Item_Jewel.cdb id 172"]
name_key: "ItemName_7172"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 103, "stat": "Attack Speed(%)", "value": 1, "scale": "flat"}
  - {"code": 103, "stat": "Attack Speed(%)", "value": 5, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 18}
icon: {"file": "Items_27.png", "index": 30}
obtained_from:
  - {"how": "craft", "recipe": 1818}
  - {"how": "quest_reward", "quest": 34, "count": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=55340f type=d36ca9 id=2b5980 sources=81e12b name_key=2a3136 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=c1bf15 options=109d7f icon=ccbdad obtained_from=957c3a -->
|  |  |
|---|---|
|  | ![Attack Speed(%) Rune](../assets/items/7172.png) |
| **Item id** | `7172` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_27.png` cell 30 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack Speed(%) | Attack Speed +1% | flat | 103 |
| Attack Speed(%) | Attack Speed +5% | flat (from Item_Jewel) | 103 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 18 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1818 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/812-red-bloodstone\|Red bloodstone]] × 2 | 0 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/34-tow-canyon|Tow Canyon]] × 1
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

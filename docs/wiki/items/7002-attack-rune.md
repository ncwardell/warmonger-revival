---
title: "Attack Rune"
type: "item"
id: 7002
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7002", "client (server-only table): Item_Jewel.cdb id 2"]
name_key: "ItemName_7002"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 1, "stat": "Attack", "value": 3, "scale": "flat"}
  - {"code": 1, "stat": "Attack", "value": 10, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 1}
icon: {"file": "Items_27.png", "index": 0}
obtained_from:
  - {"how": "craft", "recipe": 1801}
  - {"how": "quest_reward", "quest": 47, "count": 1}
  - {"how": "quest_reward", "quest": 51, "count": 1}
  - {"how": "quest_reward", "quest": 110, "count": 1}
  - {"how": "quest_reward", "quest": 770, "count": 1}
  - {"how": "random_box", "box": 47}
---
<!-- generated:start -->
<!-- generated-keys: title=839df9 type=d36ca9 id=76096e sources=bc4b6d name_key=975799 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=77af56 options=88c977 icon=e86d2e obtained_from=5a4f15 -->
|  |  |
|---|---|
|  | ![Attack Rune](../assets/items/7002.png) |
| **Item id** | `7002` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_27.png` cell 0 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Attack | +3 | flat | 1 |
| Attack | +10 | flat (from Item_Jewel) | 1 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 1 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1801 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/812-red-bloodstone\|Red bloodstone]] × 2 | 200 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/47-create-potion|Create Potion]] × 1
- Reward of quest [[wiki/quests/51-war-winning-means|War - Winning means]] × 1
- Reward of quest [[wiki/quests/110-gear-manufacturing|Gear manufacturing]] × 1
- Reward of quest [[wiki/quests/770-group-border-area-hard-mode|Group - Border Area Hard Mode]] × 1
- In random box table row 47 (RandomBox.cdb; odds are server side)

### Mentioned in

- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
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

---
title: "Mana Regeneration Rune"
type: "item"
id: 7072
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7072", "client (server-only table): Item_Jewel.cdb id 72"]
name_key: "ItemName_7072"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 34, "stat": "Mana Regeneration", "value": 2, "scale": "flat"}
  - {"code": 34, "stat": "Mana Regeneration", "value": 15, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 8}
icon: {"file": "Items_28.png", "index": 16}
obtained_from:
  - {"how": "craft", "recipe": 1808}
  - {"how": "quest_reward", "quest": 50, "count": 1}
  - {"how": "quest_reward", "quest": 784, "count": 1}
  - {"how": "random_box", "box": 46}
---
<!-- generated:start -->
<!-- generated-keys: title=cbe828 type=d36ca9 id=4a1ad6 sources=9cb190 name_key=4ca3e7 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=0ff5d7 options=b7f834 icon=be226a obtained_from=80c731 -->
|  |  |
|---|---|
|  | ![Mana Regeneration Rune](wiki/assets/items/7072.png) |
| **Item id** | `7072` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_28.png` cell 16 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Mana Regeneration | +2 | flat | 34 |
| Mana Regeneration | +15 | flat (from Item_Jewel) | 34 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 8 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1808 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/806-emerald\|Emerald]] × 1 | 175 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/50-war-winning-means|War - Winning means]] × 1
- Reward of quest [[wiki/quests/784-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]] × 1
- In random box table row 46 (RandomBox.cdb; odds are server side)
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

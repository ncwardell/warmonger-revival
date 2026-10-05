---
title: "Spell Vamp Rune"
type: "item"
id: 7132
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7132", "client (server-only table): Item_Jewel.cdb id 132"]
name_key: "ItemName_7132"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 43, "stat": "Spell Vamp(%)", "value": 1, "scale": "flat"}
  - {"code": 43, "stat": "Spell Vamp(%)", "value": 3, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 14}
icon: {"file": "Items_28.png", "index": 6}
obtained_from:
  - {"how": "craft", "recipe": 1814}
  - {"how": "quest_reward", "quest": 23, "count": 1}
  - {"how": "quest_reward", "quest": 24, "count": 1}
  - {"how": "quest_reward", "quest": 25, "count": 1}
  - {"how": "quest_reward", "quest": 46, "count": 1}
  - {"how": "random_box", "box": 48}
---
<!-- generated:start -->
<!-- generated-keys: title=a02465 type=d36ca9 id=504f78 sources=3bd69a name_key=63efea kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=d0dd70 options=f4abe0 icon=f14a17 obtained_from=946202 -->
|  |  |
|---|---|
|  | ![Spell Vamp Rune](../assets/items/7132.png) |
| **Item id** | `7132` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_28.png` cell 6 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Spell Vamp(%) | Spell Vamp +1% | flat | 43 |
| Spell Vamp(%) | Spell Vamp +3% | flat (from Item_Jewel) | 43 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 14 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1814 | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/806-emerald\|Emerald]] × 5 | 0 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/23-stepping-up-your-game|Stepping up your game]] × 1
- Reward of quest [[wiki/quests/24-stepping-up-your-game|Stepping up your game]] × 1
- Reward of quest [[wiki/quests/25-stepping-up-your-game|Stepping up your game]] × 1
- Reward of quest [[wiki/quests/46-to-oracle-of-knowledge|To Oracle of knowledge]] × 1
- In random box table row 48 (RandomBox.cdb; odds are server side)
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

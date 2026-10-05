---
title: "Ability Power Rune"
type: "item"
id: 7012
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7012", "client (server-only table): Item_Jewel.cdb id 12"]
name_key: "ItemName_7012"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 2, "stat": "Ability Power", "value": 6, "scale": "flat"}
  - {"code": 2, "stat": "Ability Power", "value": 8, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 2}
icon: {"file": "Items_27.png", "index": 40}
obtained_from:
  - {"how": "craft", "recipe": 1802}
  - {"how": "quest_reward", "quest": 47, "count": 1}
  - {"how": "quest_reward", "quest": 51, "count": 1}
  - {"how": "quest_reward", "quest": 110, "count": 1}
  - {"how": "quest_reward", "quest": 770, "count": 1}
  - {"how": "random_box", "box": 47}
---
<!-- generated:start -->
<!-- generated-keys: title=df6caa type=d36ca9 id=95155b sources=6f9a70 name_key=3041ee kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=f737ae options=27669a icon=0d1226 obtained_from=40fe7e -->
|  |  |
|---|---|
|  | ![Ability Power Rune](../assets/items/7012.png) |
| **Item id** | `7012` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_27.png` cell 40 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Ability Power | +6 | flat | 2 |
| Ability Power | +8 | flat (from Item_Jewel) | 2 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 2 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1802 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/804-blue-bloodstone\|Blue bloodstone]] × 2 | 200 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/47-create-potion|Create Potion]] × 1
- Reward of quest [[wiki/quests/51-war-winning-means|War - Winning means]] × 1
- Reward of quest [[wiki/quests/110-gear-manufacturing|Gear manufacturing]] × 1
- Reward of quest [[wiki/quests/770-group-border-area-hard-mode|Group - Border Area Hard Mode]] × 1
- In random box table row 47 (RandomBox.cdb; odds are server side)
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

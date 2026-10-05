---
title: "Armor Rune"
type: "item"
id: 7022
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7022", "client (server-only table): Item_Jewel.cdb id 22"]
name_key: "ItemName_7022"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 6, "stat": "Armor", "value": 3, "scale": "flat"}
  - {"code": 6, "stat": "Armor", "value": 5, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 3}
icon: {"file": "Items_29.png", "index": 22}
obtained_from:
  - {"how": "craft", "recipe": 1803}
  - {"how": "quest_reward", "quest": 12, "count": 1}
  - {"how": "quest_reward", "quest": 41, "count": 1}
  - {"how": "quest_reward", "quest": 48, "count": 1}
  - {"how": "random_box", "box": 47}
---
<!-- generated:start -->
<!-- generated-keys: title=3a5337 type=d36ca9 id=fca763 sources=8e4167 name_key=3f6a40 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=8792d7 options=1d3c27 icon=850fb8 obtained_from=b03757 -->
|  |  |
|---|---|
|  | ![Armor Rune](../assets/items/7022.png) |
| **Item id** | `7022` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_29.png` cell 22 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Armor | +3 | flat | 6 |
| Armor | +5 | flat (from Item_Jewel) | 6 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 3 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1803 | [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/810-diamond\|Diamond]] × 2 | 200 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/12-an-urgent-message|An urgent message]] × 1
- Reward of quest [[wiki/quests/41-innocence-s-recovery-operation|Innocence's recovery operation]] × 1
- Reward of quest [[wiki/quests/48-doping-create|Doping Create]] × 1
- In random box table row 47 (RandomBox.cdb; odds are server side)

### Mentioned in

- [[gameplay/items-and-crafting|Items, upgrades and crafting]]
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
- [[gameplay/sources|Sources and gaps]]
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]
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

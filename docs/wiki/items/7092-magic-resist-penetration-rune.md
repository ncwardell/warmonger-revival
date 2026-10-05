---
title: "Magic resist Penetration Rune"
type: "item"
id: 7092
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 7092", "client (server-only table): Item_Jewel.cdb id 92"]
name_key: "ItemName_7092"
kind: 35
kind_name: "Rune"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 10}
cost_pair:
  - {"currency": 2, "amount": 10}
rune_level: 0
stats:
  - {"code": 14, "stat": "Magic resist Penetration", "value": 1, "scale": "flat"}
  - {"code": 14, "stat": "Magic resist Penetration", "value": 10, "scale": "flat", "from": "Item_Jewel"}
options:
  - {"code": 202, "value": 10}
icon: {"file": "Items_29.png", "index": 2}
obtained_from:
  - {"how": "craft", "recipe": 1810}
  - {"how": "quest_reward", "quest": 35, "count": 1}
  - {"how": "quest_reward", "quest": 36, "count": 1}
  - {"how": "quest_reward", "quest": 111, "count": 1}
  - {"how": "quest_reward", "quest": 112, "count": 1}
  - {"how": "quest_reward", "quest": 113, "count": 1}
  - {"how": "random_box", "box": 48}
---
<!-- generated:start -->
<!-- generated-keys: title=641d2f type=d36ca9 id=b3db2f sources=6766c0 name_key=c25014 kind=972a67 kind_name=a3317b classes=92d079 bind=883bf8 price=8c6ae2 cost_pair=982f5a rune_level=b6589f stats=684436 options=054ccf icon=df68fb obtained_from=12a3f7 -->
|  |  |
|---|---|
|  | ![Magic resist Penetration Rune](../assets/items/7092.png) |
| **Item id** | `7092` |
| **Kind** | Rune (35) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 10 Gold |
| **Icon** | `ui/icons/Items_29.png` cell 2 |

### Tooltip

> The Rune ability is applied, when equip weapon which set Runes..

### Stats

| stat | value | applies | code |
|---|---|---|---|
| Magic resist Penetration | +1 | flat | 14 |
| Magic resist Penetration | +10 | flat (from Item_Jewel) | 14 |

### Other options

| code | value | meaning |
|---|---|---|
| 202 | 10 | rune grade? |

### Crafting

| recipe | materials | gold | success % |
|---|---|---|---|
| 1810 | [[wiki/items/701-crystal-yellow\|Crystal : Yellow]] × 10, [[wiki/items/700-crystal-blue\|Crystal : Blue]] × 10, [[wiki/items/808-moonstone\|Moonstone]] × 5 | 0 | 100 |

### Where to get it

- Reward of quest [[wiki/quests/35-demon-hell|Demon Hell]] × 1
- Reward of quest [[wiki/quests/36-thorn-s-hell|Thorn's Hell]] × 1
- Reward of quest [[wiki/quests/111-weapon-manufacturing|Weapon manufacturing]] × 1
- Reward of quest [[wiki/quests/112-weapon-manufacturing|Weapon manufacturing]] × 1
- Reward of quest [[wiki/quests/113-weapon-manufacturing|Weapon manufacturing]] × 1
- In random box table row 48 (RandomBox.cdb; odds are server side)

### Mentioned in

- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
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

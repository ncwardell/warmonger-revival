---
title: "Flask of Devour [C] : 2 Mana Steal with each attack. Maximum Mana +50"
type: "buff"
id: 2121
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2121", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2121"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 42, "stat": "Devour(%)", "value": 2}
  - {"code": 33, "stat": "Mana", "value": 50}
icon: {"file": "Items_30.png", "index": 24}
applied_by:
  - {"item": 748}
---
<!-- generated:start -->
<!-- generated-keys: title=a1474b type=6143a1 id=965b38 sources=2360ab name_key=7ca4b9 duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=b9b744 icon=86ae5c applied_by=70f8c0 -->
|  |  |
|---|---|
|  | ![Flask of Devour (C) : 2 Mana Steal with each attack. Maximum Mana +50](../assets/buffs/2121.png) |
| **Buff id** | `2121` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 24 |

### Tooltip

> Flask of Devour [C] : 2 Mana Steal with each attack. 
> Maximum Mana +50

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 42 | Devour(%) | 2 |
| 33 | Mana | 50 |

### Applied by

- Using [[wiki/items/748-flask-of-devour-c|Flask of Devour (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 63): Flask · Flask of Devour · 748–751 · 2121–2124 · Mana steal per hit 2 / 4 / 6 / 8 and max MP +50 / 100 / 150 / 200
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

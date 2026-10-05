---
title: "Flask of Devour [A] : 6 Mana Steal with each attack. Maximum Mana +150"
type: "buff"
id: 2123
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2123", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2123"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 42, "stat": "Devour(%)", "value": 6}
  - {"code": 33, "stat": "Mana", "value": 150}
icon: {"file": "Items_30.png", "index": 30}
applied_by:
  - {"item": 750}
---
<!-- generated:start -->
<!-- generated-keys: title=56ab9d type=6143a1 id=676465 sources=2ce11f name_key=65ce41 duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=217d3f icon=f397b6 applied_by=efc6e8 -->
|  |  |
|---|---|
|  | ![Flask of Devour (A) : 6 Mana Steal with each attack. Maximum Mana +150](../assets/buffs/2123.png) |
| **Buff id** | `2123` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 30 |

### Tooltip

> Flask of Devour [A] : 6 Mana Steal with each attack. 
> Maximum Mana +150

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 42 | Devour(%) | 6 |
| 33 | Mana | 150 |

### Applied by

- Using [[wiki/items/750-flask-of-devour-a|Flask of Devour (A)]] (Item_Base option 301)
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

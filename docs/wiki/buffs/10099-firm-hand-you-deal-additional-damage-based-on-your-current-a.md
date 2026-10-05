---
title: "Firm Hand : You deal additional damage based on your current Armor"
type: "buff"
id: 10099
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10099", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10099"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 1, "stat": "Attack", "value": 0}
  - {"code": 106, "stat": "Armor(%)", "value": 30}
icon: {"file": "Skill_Dolorece_01.png", "index": 17}
applied_by:
  - {"skill": 5109, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=0a3cac type=6143a1 id=b43de4 sources=1923c7 name_key=a7d0e5 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=da95f8 icon=159906 applied_by=4f6809 -->
|  |  |
|---|---|
|  | ![Firm Hand : You deal additional damage based on your current Armor](../assets/buffs/10099.png) |
| **Buff id** | `10099` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 17 |

### Tooltip

> Firm Hand : You deal additional damage based on your current Armor

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 1 | Attack | 0 |
| 106 | Armor(%) | 30 |

### Applied by

- Skill [[wiki/skills/5109-firm-hand|Firm Hand]], effect slot 1 (type 314, rate 100%)
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

---
title: "Suppressive Fire : Reduced Attack and Movement Speed for 3 seconds"
type: "buff"
id: 30088
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30088", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10088"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1009
effects:
  - {"code": 18, "stat": "code 18 (unknown)", "value": -30}
  - {"code": 19, "stat": "code 19 (unknown)", "value": -30}
icon: {"file": "Skill_Einsel_01.png", "index": 19}
applied_by:
  - {"skill": 10106, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=1bc172 type=6143a1 id=146764 sources=ac1196 name_key=334b82 duration=0aac5a is_buff=b6589f stack_type=356a19 group=ab68fc effects=2f7462 icon=52a60d applied_by=3d6605 -->
|  |  |
|---|---|
|  | ![Suppressive Fire : Reduced Attack and Movement Speed for 3 seconds](../assets/buffs/30088.png) |
| **Buff id** | `30088` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1009 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 19 |

### Tooltip

> Suppressive Fire : Reduced Attack and Movement Speed for 3 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 18 | code 18 (unknown) | -30 |
| 19 | code 19 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/10106-bullet-shower|Bullet shower]], effect slot 3 (type 314, rate 100%)
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

---
title: "Lightning protection"
type: "buff"
id: 10433
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10433", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10433"
duration: {"ticks": 65, "seconds": 13.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 433, "stat": "code 433 (unknown)", "value": 10}
  - {"code": 206, "stat": "code 206 (unknown)", "value": 5484}
icon: {"file": "Policy.png", "index": 34}
applied_by:
  - {"skill": 5483, "slot": 2, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=393f9f type=6143a1 id=9acc93 sources=e06728 name_key=63b398 duration=cdb31a is_buff=b6589f stack_type=356a19 group=b6589f effects=1def9e icon=9835a6 applied_by=b79ae2 -->
|  |  |
|---|---|
|  | ![Lightning protection](wiki/assets/buffs/10433.png) |
| **Buff id** | `10433` |
| **Duration** | 13 s (65 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 34 |

### Tooltip

> Lightning protection

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 433 | code 433 (unknown) | 10 |
| 206 | code 206 (unknown) | 5,484 |

### Applied by

- Skill [[wiki/skills/5483|Skill 5483]], effect slot 2 (type 301, rate 100%)
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

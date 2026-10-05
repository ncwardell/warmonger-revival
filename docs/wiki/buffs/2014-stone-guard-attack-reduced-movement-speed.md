---
title: "Stone Guard Attack : Reduced Movement Speed."
type: "buff"
id: 2014
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2014", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2014"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 117, "stat": "code 117 (unknown)", "value": -20}
icon: {"file": "Policy.png", "index": 0}
applied_by:
  - {"skill": 9, "slot": 3, "type": 314, "rate": 100}
  - {"skill": 16, "slot": 3, "type": 314, "rate": 100}
  - {"skill": 20, "slot": 2, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=9f26e5 type=6143a1 id=39e214 sources=80e0ec name_key=9aef50 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=48c46c icon=f877b6 applied_by=81adec -->
|  |  |
|---|---|
|  | ![Stone Guard Attack : Reduced Movement Speed.](wiki/assets/buffs/2014.png) |
| **Buff id** | `2014` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Stone Guard Attack : Reduced Movement Speed.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 117 | code 117 (unknown) | -20 |

### Applied by

- Skill [[wiki/skills/9|Skill 9]], effect slot 3 (type 314, rate 100%)
- Skill [[wiki/skills/16|Skill 16]], effect slot 3 (type 314, rate 100%)
- Skill [[wiki/skills/20|Skill 20]], effect slot 2 (type 314, rate 100%)
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

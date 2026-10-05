---
title: "Amplified damage : Reduced Attack and Movement Speed."
type: "buff"
id: 2015
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2015", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2015"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 110, "stat": "Critical Strike Deal(%)", "value": -50}
  - {"code": 117, "stat": "code 117 (unknown)", "value": -25}
icon: {"file": "Policy.png", "index": 0}
applied_by:
  - {"skill": 13, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=72aeb0 type=6143a1 id=9cdda6 sources=8620a3 name_key=38a22b duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=e582ae icon=f877b6 applied_by=267159 -->
|  |  |
|---|---|
|  | ![Amplified damage : Reduced Attack and Movement Speed.](../assets/buffs/2015.png) |
| **Buff id** | `2015` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Amplified damage : Reduced Attack and Movement Speed.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 110 | Critical Strike Deal(%) | -50 |
| 117 | code 117 (unknown) | -25 |

### Applied by

- Skill [[wiki/skills/13|Skill 13]], effect slot 3 (type 314, rate 100%)
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

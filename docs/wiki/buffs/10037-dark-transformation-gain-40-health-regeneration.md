---
title: "Dark Transformation : Gain 40% Health Regeneration"
type: "buff"
id: 10037
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10037", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10037"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 433, "stat": "code 433 (unknown)", "value": 5}
  - {"code": 206, "stat": "code 206 (unknown)", "value": 5042}
icon: {"file": "Skill_Dolorece_01.png", "index": 7}
applied_by:
  - {"skill": 5041, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=95b904 type=6143a1 id=79c499 sources=5bb5dc name_key=ea1179 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=9b3b92 icon=3af2a9 applied_by=36918e -->
|  |  |
|---|---|
|  | ![Dark Transformation : Gain 40% Health Regeneration](wiki/assets/buffs/10037.png) |
| **Buff id** | `10037` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 7 |

### Tooltip

> Dark Transformation : Gain 40% Health Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 433 | code 433 (unknown) | 5 |
| 206 | code 206 (unknown) | 5,042 |

### Applied by

- Skill [[wiki/skills/5041-dark-transformation|Dark Transformation]], effect slot 1 (type 301, rate 100%)
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

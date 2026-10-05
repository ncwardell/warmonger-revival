---
title: "Rapid Dash : Increased damage"
type: "buff"
id: 10173
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10173", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10173"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 1, "stat": "Attack", "value": 20}
  - {"code": 116, "stat": "code 116 (unknown)", "value": 20}
icon: {"file": "Skill_Einsel_01.png", "index": 30}
applied_by:
  - {"skill": 5148, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=c34ea9 type=6143a1 id=3480ce sources=683a04 name_key=eb407a duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=97631f icon=4bb647 applied_by=bf0de3 -->
|  |  |
|---|---|
|  | ![Rapid Dash : Increased damage](wiki/assets/buffs/10173.png) |
| **Buff id** | `10173` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 30 |

### Tooltip

> Rapid Dash : Increased damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 1 | Attack | 20 |
| 116 | code 116 (unknown) | 20 |

### Applied by

- Skill [[wiki/skills/5148-rapid-dash|Rapid Dash]], effect slot 1 (type 301, rate 100%)
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

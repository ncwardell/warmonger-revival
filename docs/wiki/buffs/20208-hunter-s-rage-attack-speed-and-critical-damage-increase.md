---
title: "Hunter's Rage: Attack Speed and Critical Damage Increase"
type: "buff"
id: 20208
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20208", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20208"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 10, "stat": "Critical Strike Deal", "value": 100}
  - {"code": 116, "stat": "code 116 (unknown)", "value": 20}
icon: {"file": "Skill_Boss_01.dds", "index": 34}
applied_by:
  - {"skill": 20207, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=9c7699 type=6143a1 id=b4863e sources=d788cc name_key=b0768d duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=f9abee icon=056ae7 applied_by=6fac98 -->
|  |  |
|---|---|
|  | ![Hunter's Rage: Attack Speed and Critical Damage Increase](wiki/assets/buffs/20208.png) |
| **Buff id** | `20208` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 34 |

### Tooltip

> Hunter's Rage: Attack Speed and Critical Damage Increase

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 10 | Critical Strike Deal | 100 |
| 116 | code 116 (unknown) | 20 |

### Applied by

- Skill [[wiki/skills/20207-hunter-s-rage|Hunter's Rage]], effect slot 1 (type 301, rate 100%)
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

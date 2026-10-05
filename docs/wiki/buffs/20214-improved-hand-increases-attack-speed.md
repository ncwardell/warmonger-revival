---
title: "Improved Hand: Increases attack speed"
type: "buff"
id: 20214
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20214", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20214"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 405, "stat": "code 405 (unknown)", "value": 5}
  - {"code": 116, "stat": "code 116 (unknown)", "value": 3}
icon: {"file": "Skill_Boss_01.dds", "index": 37}
applied_by:
  - {"skill": 20212, "slot": 3, "type": 301, "rate": 100}
  - {"skill": 20216, "slot": 4, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=6e3a79 type=6143a1 id=99aee4 sources=1ef7e6 name_key=2b6909 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=2ea2bc icon=e79476 applied_by=8cc737 -->
|  |  |
|---|---|
|  | ![Improved Hand: Increases attack speed](../assets/buffs/20214.png) |
| **Buff id** | `20214` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 37 |

### Tooltip

> Improved Hand: Increases attack speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 405 | code 405 (unknown) | 5 |
| 116 | code 116 (unknown) | 3 |

### Applied by

- Skill [[wiki/skills/20212-improved-hand|Improved Hand]], effect slot 3 (type 301, rate 100%)
- Skill [[wiki/skills/20216-hunting-eye|Hunting Eye]], effect slot 4 (type 301, rate 100%)
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

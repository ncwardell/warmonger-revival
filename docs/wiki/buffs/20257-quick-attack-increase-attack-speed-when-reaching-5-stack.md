---
title: "Quick attack : Increase attack speed when reaching 5 stack"
type: "buff"
id: 20257
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20257"]
name_key: "SkillBuff_20257"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 401, "stat": "code 401 (unknown)", "value": 4}
  - {"code": 402, "stat": "basic attack override", "value": 20262}
icon: {"file": "Skill_Boss_01.dds", "index": 53}
applied_by:
  - {"skill": 20258, "slot": 2, "type": 303, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=8e569f type=6143a1 id=b90325 sources=100573 name_key=8ea3cb duration=6c141f is_buff=b6589f stack_type=356a19 group=b6589f effects=3fa0ca icon=e8b5ca applied_by=3e3819 -->
|  |  |
|---|---|
|  | ![Quick attack : Increase attack speed when reaching 5 stack](wiki/assets/buffs/20257.png) |
| **Buff id** | `20257` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 53 |

### Tooltip

> Quick attack : Increase attack speed when reaching 5 stack

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 401 | code 401 (unknown) | 4 |
| 402 | basic attack override | 20,262 ([[wiki/skills/20262\|Skill 20262]]) |

### Applied by

- Skill [[wiki/skills/20258-quick-attack|Quick attack]], effect slot 2 (type 303, rate 100%)
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

---
title: "Breeze : Increased Ability Power and Movement Speed"
type: "buff"
id: 10012
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10012", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10012"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 102, "stat": "Ability Power(%)", "value": 20}
  - {"code": 17, "stat": "code 17 (unknown)", "value": 50}
icon: {"file": "Skill_Einsel_01.png", "index": 1}
applied_by:
  - {"skill": 5009, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=4c34e7 type=6143a1 id=fcf3e8 sources=40311b name_key=8f8fa1 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=712e4c icon=86c28e applied_by=1f1947 -->
|  |  |
|---|---|
|  | ![Breeze : Increased Ability Power and Movement Speed](../assets/buffs/10012.png) |
| **Buff id** | `10012` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 1 |

### Tooltip

> Breeze : Increased Ability Power and Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 102 | Ability Power(%) | 20 |
| 17 | code 17 (unknown) | 50 |

### Applied by

- Skill [[wiki/skills/5009-breeze|Breeze]], effect slot 1 (type 314, rate 100%)
- Nation policy 13 `PolicyName_13` (Policy.cdb, server-only; buff_or_skill)
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

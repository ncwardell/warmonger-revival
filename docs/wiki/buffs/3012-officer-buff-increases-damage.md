---
title: "Officer Buff: Increases Damage"
type: "buff"
id: 3012
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 3012", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_3012"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 101, "stat": "Attack(%)", "value": 50}
icon: {"file": "Mastery_01.png", "index": 0}
applied_by:
  - {"skill": 3011, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=c23a7e type=6143a1 id=a385d9 sources=58216d name_key=f04588 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=8ef1f2 icon=f1f3b7 applied_by=679058 -->
|  |  |
|---|---|
|  | ![Officer Buff: Increases Damage](../assets/buffs/3012.png) |
| **Buff id** | `3012` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Mastery_01.png` cell 0 |

### Tooltip

> Officer Buff: Increases Damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 101 | Attack(%) | 50 |

### Applied by

- Skill [[wiki/skills/3011|Skill 3011]], effect slot 1 (type 314, rate 100%)
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

---
title: "Unyielding Will : Reduce 50% all type of damage during 5 secs and get 40 Attack."
type: "buff"
id: 10352
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10352", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10352"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 1, "stat": "Attack", "value": 40}
  - {"code": 11, "stat": "Armor(%)", "value": 50}
  - {"code": 12, "stat": "Magic Resist(%)", "value": 50}
icon: {"file": "Skill_Dolorece_01.png", "index": 15}
applied_by:
  - {"skill": 5297, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=f4124d type=6143a1 id=fb8af9 sources=69668a name_key=d99160 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=165ed3 icon=a431e0 applied_by=08ce60 -->
|  |  |
|---|---|
|  | ![Unyielding Will : Reduce 50% all type of damage during 5 secs and get 40 Attack.](wiki/assets/buffs/10352.png) |
| **Buff id** | `10352` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 15 |

### Tooltip

> Unyielding Will : Reduce 50% all type of damage during 5 secs and 
>  get 40 Attack.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 1 | Attack | 40 |
| 11 | Armor(%) | 50 |
| 12 | Magic Resist(%) | 50 |

### Applied by

- Skill [[wiki/skills/5297-unyielding-will|Unyielding Will]], effect slot 1 (type 314, rate 100%)
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

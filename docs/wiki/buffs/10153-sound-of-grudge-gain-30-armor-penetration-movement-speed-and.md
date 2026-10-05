---
title: "Sound of Grudge : Gain 30 Armor Penetration, Movement Speed and 4 Health Regeneration."
type: "buff"
id: 10153
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10153", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10153"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 13, "stat": "Armor Penetration", "value": 30}
  - {"code": 17, "stat": "code 17 (unknown)", "value": 70}
  - {"code": 32, "stat": "Health Regeneration", "value": 4}
icon: {"file": "Skill_Dolorece_01.png", "index": 25}
applied_by:
  - {"skill": 5130, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=600a6e type=6143a1 id=b795e2 sources=4ff9f6 name_key=534ed2 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=626419 icon=f0762b applied_by=cd39b4 -->
|  |  |
|---|---|
|  | ![Sound of Grudge : Gain 30 Armor Penetration, Movement Speed and 4 Health Regeneration.](wiki/assets/buffs/10153.png) |
| **Buff id** | `10153` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 25 |

### Tooltip

> Sound of Grudge : Gain 30 Armor Penetration, Movement Speed 
>  and 4 Health Regeneration.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 13 | Armor Penetration | 30 |
| 17 | code 17 (unknown) | 70 |
| 32 | Health Regeneration | 4 |

### Applied by

- Skill [[wiki/skills/5130-sound-of-grudge|Sound of Grudge]], effect slot 1 (type 301, rate 100%)
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

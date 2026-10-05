---
title: "Rapid Fire: Creates a shield that absorbs Damage for 10 seconds"
type: "buff"
id: 10118
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10118", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10118"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 300}
  - {"code": 101, "stat": "Attack(%)", "value": 10}
icon: {"file": "Skill_Dolorece_01.png", "index": 23}
applied_by:
  - {"skill": 5119, "slot": 1, "type": 308, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=42e97f type=6143a1 id=39cb4b sources=9deaa7 name_key=084fb4 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=816ad5 icon=60dd2b applied_by=3092fc -->
|  |  |
|---|---|
|  | ![Rapid Fire: Creates a shield that absorbs Damage for 10 seconds](wiki/assets/buffs/10118.png) |
| **Buff id** | `10118` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 23 |

### Tooltip

> Rapid Fire: Creates a shield that absorbs Damage for 10 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 300 |
| 101 | Attack(%) | 10 |

### Applied by

- Skill [[wiki/skills/5119-man-in-the-war|Man in the war]], effect slot 1 (type 308, rate 100%)
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

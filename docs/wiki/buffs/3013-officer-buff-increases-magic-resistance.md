---
title: "Officer Buff: Increases Magic Resistance"
type: "buff"
id: 3013
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 3013", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_3013"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 107, "stat": "Magic Resist(%)", "value": 30}
icon: {"file": "Mastery_01.png", "index": 19}
applied_by:
  - {"skill": 3012, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=b2cde2 type=6143a1 id=9bf5ce sources=0a4b51 name_key=83fcb3 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=4d7471 icon=13f17b applied_by=8ff31e -->
|  |  |
|---|---|
|  | ![Officer Buff: Increases Magic Resistance](wiki/assets/buffs/3013.png) |
| **Buff id** | `3013` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Mastery_01.png` cell 19 |

### Tooltip

> Officer Buff: Increases Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 107 | Magic Resist(%) | 30 |

### Applied by

- Skill [[wiki/skills/3012|Skill 3012]], effect slot 1 (type 314, rate 100%)
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

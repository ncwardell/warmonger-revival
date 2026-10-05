---
title: "Quick attack : Increase attack speed for 5 seconds"
type: "buff"
id: 20258
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20258", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20258"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 116, "stat": "code 116 (unknown)", "value": 10}
icon: {"file": "Skill_Boss_01.dds", "index": 54}
applied_by:
  - {"skill": 20262, "slot": 3, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=3be5b1 type=6143a1 id=0717f7 sources=7e2ec0 name_key=c4a727 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=939e09 icon=071b0c applied_by=ea436d -->
|  |  |
|---|---|
|  | ![Quick attack : Increase attack speed for 5 seconds](wiki/assets/buffs/20258.png) |
| **Buff id** | `20258` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 54 |

### Tooltip

> Quick attack : Increase attack speed for 5 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 116 | code 116 (unknown) | 10 |

### Applied by

- Skill [[wiki/skills/20262|Skill 20262]], effect slot 3 (type 301, rate 100%)
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

---
title: "Test Buff 1"
type: "buff"
id: 900
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 900", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_900"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 1, "stat": "Attack", "value": 2000}
  - {"code": 16, "stat": "code 16 (unknown)", "value": 300}
  - {"code": 2, "stat": "Ability Power", "value": 2000}
icon: {"file": "Policy.png", "index": 0}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=b06753 type=6143a1 id=28cc22 sources=1c6817 name_key=ca0081 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=85bed6 icon=f877b6 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Test Buff 1](wiki/assets/buffs/900.png) |
| **Buff id** | `900` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Test Buff 1

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 1 | Attack | 2,000 |
| 16 | code 16 (unknown) | 300 |
| 2 | Ability Power | 2,000 |
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

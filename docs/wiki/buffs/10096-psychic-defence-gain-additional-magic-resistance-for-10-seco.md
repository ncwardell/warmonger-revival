---
title: "Psychic Defence : Gain additional Magic Resistance for 10 seconds"
type: "buff"
id: 10096
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10096", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10096"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 7, "stat": "Magic Resist", "value": 30}
  - {"code": 107, "stat": "Magic Resist(%)", "value": 10}
icon: {"file": "Policy.png", "index": 0}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=66ea5f type=6143a1 id=f686dc sources=55365f name_key=99d6e9 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=52ee92 icon=f877b6 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Psychic Defence : Gain additional Magic Resistance for 10 seconds](wiki/assets/buffs/10096.png) |
| **Buff id** | `10096` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Psychic Defence : Gain additional Magic Resistance for 10 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 7 | Magic Resist | 30 |
| 107 | Magic Resist(%) | 10 |
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

---
title: "Slayer : When player kill enemy, gain attack +3 (Maximum +10). When you die, lose all stacks."
type: "buff"
id: 10325
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10325"]
name_key: "SkillBuff_10325"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 18
effects:
  - {"code": 401, "stat": "code 401 (unknown)", "value": 10}
  - {"code": 1, "stat": "Attack", "value": 3}
icon: {"file": "Mastery_01.png", "index": 40}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=380559 type=6143a1 id=bd56a0 sources=9030f7 name_key=851059 duration=6c141f is_buff=b6589f stack_type=356a19 group=9e6a55 effects=c83574 icon=593d40 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Slayer : When player kill enemy, gain attack +3 (Maximum +10). When you die, lose all stacks.](wiki/assets/buffs/10325.png) |
| **Buff id** | `10325` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 18 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Mastery_01.png` cell 40 |

### Tooltip

> Slayer : When player kill enemy, gain attack +3 (Maximum +10). 
> When you die, lose all stacks.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 401 | code 401 (unknown) | 10 |
| 1 | Attack | 3 |
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

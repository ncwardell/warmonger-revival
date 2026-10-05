---
title: "Invisible prison"
type: "buff"
id: 20210
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20210", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20210"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 232, "stat": "level? (char+0x658)", "value": 4}
icon: {"file": "Skill_Boss_01.dds", "index": 36}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=db02bb type=6143a1 id=666687 sources=5ec298 name_key=22f663 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=ec8689 icon=da8658 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Invisible prison](../assets/buffs/20210.png) |
| **Buff id** | `20210` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 36 |

### Tooltip

> Invisible prison

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 232 | level? (char+0x658) | 4 |
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

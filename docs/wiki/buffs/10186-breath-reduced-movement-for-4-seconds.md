---
title: "Breath : Reduced Movement for 4 seconds"
type: "buff"
id: 10186
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10186", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10186"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Policy.png", "index": 34}
applied_by:
  - {"skill": 5154, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=0e6d5b type=6143a1 id=898d94 sources=537cf0 name_key=e1d0d5 duration=3d2da5 is_buff=b6589f stack_type=356a19 group=e3cbba effects=732c70 icon=9835a6 applied_by=4597eb -->
|  |  |
|---|---|
|  | ![Breath : Reduced Movement for 4 seconds](wiki/assets/buffs/10186.png) |
| **Buff id** | `10186` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy.png` cell 34 |

### Tooltip

> Breath : Reduced Movement for 4 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/5154|Skill 5154]], effect slot 3 (type 314, rate 100%)
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

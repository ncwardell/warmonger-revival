---
title: "Reduced Movement and Attack Speed"
type: "buff"
id: 2057
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2057", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2057"
duration: {"ticks": 150, "seconds": 30.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 118, "stat": "code 118 (unknown)", "value": -30}
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Policy.png", "index": 0}
applied_by:
  - {"skill": 25, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=318981 type=6143a1 id=77047a sources=41196d name_key=58f945 duration=faac5c is_buff=b6589f stack_type=356a19 group=e3cbba effects=0b8164 icon=f877b6 applied_by=269b9b -->
|  |  |
|---|---|
|  | ![Reduced Movement and Attack Speed](../assets/buffs/2057.png) |
| **Buff id** | `2057` |
| **Duration** | 30 s (150 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Reduced Movement and Attack Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 118 | code 118 (unknown) | -30 |
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/25|Skill 25]], effect slot 1 (type 314, rate 100%)
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

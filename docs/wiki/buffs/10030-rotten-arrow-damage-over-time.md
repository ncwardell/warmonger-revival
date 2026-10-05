---
title: "Rotten Arrow: Damage over time"
type: "buff"
id: 10030
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10030", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10030"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10030
effects:
  - {"code": 433, "stat": "code 433 (unknown)", "value": 5}
  - {"code": 431, "stat": "code 431 (unknown)", "value": 100}
icon: {"file": "Skill_Miriam_01.png", "index": 1}
applied_by:
  - {"skill": 5033, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=1ed262 type=6143a1 id=c52651 sources=4ba825 name_key=8f8cdc duration=3d2da5 is_buff=b6589f stack_type=356a19 group=c52651 effects=d146d8 icon=a498d1 applied_by=6be667 -->
|  |  |
|---|---|
|  | ![Rotten Arrow: Damage over time](../assets/buffs/10030.png) |
| **Buff id** | `10030` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10030 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 1 |

### Tooltip

> Rotten Arrow: Damage over time

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 433 | code 433 (unknown) | 5 |
| 431 | code 431 (unknown) | 100 |

### Applied by

- Skill [[wiki/skills/5033-rotten-arrow|Rotten Arrow]], effect slot 3 (type 314, rate 100%)
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

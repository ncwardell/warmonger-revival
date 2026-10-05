---
title: "Two Flame : Damage over time for 6 seconds"
type: "buff"
id: 19959
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 19959", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_19959"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 19959
effects:
  - {"code": 433, "stat": "code 433 (unknown)", "value": 5}
  - {"code": 431, "stat": "code 431 (unknown)", "value": 200}
icon: {"file": "Skill_Boss_01.dds", "index": 10}
applied_by:
  - {"skill": 19960, "slot": 4, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=17c920 type=6143a1 id=be82e6 sources=682cd0 name_key=fe8613 duration=0aac5a is_buff=b6589f stack_type=356a19 group=be82e6 effects=ef944b icon=593306 applied_by=0503e7 -->
|  |  |
|---|---|
|  | ![Two Flame : Damage over time for 6 seconds](../assets/buffs/19959.png) |
| **Buff id** | `19959` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 19959 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 10 |

### Tooltip

> Two Flame : Damage over time for 6 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 433 | code 433 (unknown) | 5 |
| 431 | code 431 (unknown) | 200 |

### Applied by

- Skill [[wiki/skills/19960-two-flames|Two Flames]], effect slot 4 (type 314, rate 100%)
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

---
title: "Wild Threat : Damage over time"
type: "buff"
id: 10052
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10052", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10052"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10520
effects:
  - {"code": 433, "stat": "code 433 (unknown)", "value": 5}
  - {"code": 431, "stat": "code 431 (unknown)", "value": 100}
icon: {"file": "Skill_Miriam_01.png", "index": 21}
applied_by:
  - {"skill": 5056, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=a04526 type=6143a1 id=e783f4 sources=960c6b name_key=214a46 duration=870e64 is_buff=b6589f stack_type=356a19 group=c1bcfc effects=d146d8 icon=a6e82f applied_by=2ff11c -->
|  |  |
|---|---|
|  | ![Wild Threat : Damage over time](../assets/buffs/10052.png) |
| **Buff id** | `10052` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10520 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 21 |

### Tooltip

> Wild Threat : Damage over time

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 433 | code 433 (unknown) | 5 |
| 431 | code 431 (unknown) | 100 |

### Applied by

- Skill [[wiki/skills/5056-wild-threat|Wild Threat]], effect slot 3 (type 314, rate 100%)
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

---
title: "Spraying Poison : Damage over time for 6 seconds"
type: "buff"
id: 10178
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10178", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10178"
duration: {"ticks": 30, "seconds": 6.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10178
effects:
  - {"code": 433, "stat": "code 433 (unknown)", "value": 5}
  - {"code": 431, "stat": "code 431 (unknown)", "value": 100}
icon: {"file": "Policy.png", "index": 34}
applied_by:
  - {"skill": 5152, "slot": 4, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=5d1221 type=6143a1 id=9d2ce5 sources=e4b82e name_key=176e7d duration=5d0a7b is_buff=b6589f stack_type=356a19 group=9d2ce5 effects=d146d8 icon=9835a6 applied_by=d72cb0 -->
|  |  |
|---|---|
|  | ![Spraying Poison : Damage over time for 6 seconds](../assets/buffs/10178.png) |
| **Buff id** | `10178` |
| **Duration** | 6 s (30 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10178 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy.png` cell 34 |

### Tooltip

> Spraying Poison : Damage over time for 6 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 433 | code 433 (unknown) | 5 |
| 431 | code 431 (unknown) | 100 |

### Applied by

- Skill [[wiki/skills/5152|Skill 5152]], effect slot 4 (type 314, rate 100%)
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

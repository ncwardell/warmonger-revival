---
title: "Fate's Call"
type: "buff"
id: 10133
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10133", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10133"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 433, "stat": "code 433 (unknown)", "value": 5}
  - {"code": 437, "stat": "code 437 (unknown)", "value": 70}
icon: {"file": "Items_02.png", "index": 34}
applied_by:
  - {"skill": 506, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=081501 type=6143a1 id=0fc7cb sources=5c36ed name_key=4bec00 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=b242bb icon=d790ef applied_by=b250b6 -->
|  |  |
|---|---|
|  | ![Fate's Call](../assets/buffs/10133.png) |
| **Buff id** | `10133` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_02.png` cell 34 |

### Tooltip

> Fate's Call

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 433 | code 433 (unknown) | 5 |
| 437 | code 437 (unknown) | 70 |

### Applied by

- Skill [[wiki/skills/506-fate-s-call|Fate's Call]], effect slot 1 (type 314, rate 100%)
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

---
title: "Flash Bang : Reduced Movement Speed"
type: "buff"
id: 10171
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10171", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10171"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -10}
icon: {"file": "Skill_Einsel_01.png", "index": 29}
applied_by:
  - {"skill": 5147, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=815bb5 type=6143a1 id=6594cf sources=820736 name_key=ddd78b duration=3d2da5 is_buff=b6589f stack_type=356a19 group=e3cbba effects=f20633 icon=bd7250 applied_by=db4515 -->
|  |  |
|---|---|
|  | ![Flash Bang : Reduced Movement Speed](../assets/buffs/10171.png) |
| **Buff id** | `10171` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 29 |

### Tooltip

> Flash Bang : Reduced Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -10 |

### Applied by

- Skill [[wiki/skills/5147-flash-bang|Flash Bang]], effect slot 3 (type 314, rate 100%)
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

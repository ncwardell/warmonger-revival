---
title: "Eye of the Storm : Reduced Movement and Attack Speed"
type: "buff"
id: 30014
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30014", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10014"
duration: {"ticks": 10, "seconds": 2.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -20}
  - {"code": 18, "stat": "code 18 (unknown)", "value": -150}
icon: {"file": "Skill_Einsel_01.png", "index": 3}
applied_by:
  - {"skill": 10013, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=758be6 type=6143a1 id=ca60b1 sources=dd145e name_key=cd0f2f duration=2a0b1e is_buff=b6589f stack_type=356a19 group=e3cbba effects=5aec95 icon=fae5ad applied_by=dd8cfc -->
|  |  |
|---|---|
|  | ![Eye of the Storm : Reduced Movement and Attack Speed](../assets/buffs/30014.png) |
| **Buff id** | `30014` |
| **Duration** | 2 s (10 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 3 |

### Tooltip

> Eye of the Storm : Reduced Movement and Attack Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -20 |
| 18 | code 18 (unknown) | -150 |

### Applied by

- Skill [[wiki/skills/10013|Skill 10013]], effect slot 1 (type 314, rate 100%)
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

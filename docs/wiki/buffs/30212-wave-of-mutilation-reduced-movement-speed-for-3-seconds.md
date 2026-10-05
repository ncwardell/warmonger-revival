---
title: "Wave of Mutilation : Reduced Movement Speed for 3 seconds"
type: "buff"
id: 30212
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30212", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10212"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Skill_Einsel_01.png", "index": 32}
applied_by:
  - {"skill": 10177, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=50a7a4 type=6143a1 id=7c49a9 sources=a1a236 name_key=17fbf4 duration=0aac5a is_buff=b6589f stack_type=356a19 group=e3cbba effects=732c70 icon=8a093a applied_by=defabc -->
|  |  |
|---|---|
|  | ![Wave of Mutilation : Reduced Movement Speed for 3 seconds](wiki/assets/buffs/30212.png) |
| **Buff id** | `30212` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 32 |

### Tooltip

> Wave of Mutilation : Reduced Movement Speed for 3 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/10177-hand-of-curse|Hand of Curse]], effect slot 3 (type 314, rate 100%)
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

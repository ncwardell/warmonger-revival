---
title: "Sharp Edges : Bleeds for 3 seconds"
type: "buff"
id: 10111
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10111", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10111"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10111
effects:
  - {"code": 433, "stat": "code 433 (unknown)", "value": 5}
  - {"code": 431, "stat": "code 431 (unknown)", "value": 100}
icon: {"file": "Skill_Miriam_01.png", "index": 12}
applied_by:
  - {"skill": 5112, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=ffbf4b type=6143a1 id=31146f sources=27d080 name_key=e3b258 duration=0aac5a is_buff=b6589f stack_type=356a19 group=31146f effects=d146d8 icon=5a5175 applied_by=aeae39 -->
|  |  |
|---|---|
|  | ![Sharp Edges : Bleeds for 3 seconds](../assets/buffs/10111.png) |
| **Buff id** | `10111` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10111 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 12 |

### Tooltip

> Sharp Edges : Bleeds for 3 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 433 | code 433 (unknown) | 5 |
| 431 | code 431 (unknown) | 100 |

### Applied by

- Skill [[wiki/skills/5112-sharp-edges|Sharp Edges]], effect slot 3 (type 314, rate 100%)
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

---
title: "Quick step back : Decreased Move Speed"
type: "buff"
id: 10355
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10355", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10355"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Skill_Dolorece_01.png", "index": 30}
applied_by:
  - {"skill": 5301, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=2b393b type=6143a1 id=8c75b8 sources=b2a5d1 name_key=7b5909 duration=0aac5a is_buff=b6589f stack_type=356a19 group=e3cbba effects=732c70 icon=b534c0 applied_by=a08ef9 -->
|  |  |
|---|---|
|  | ![Quick step back : Decreased Move Speed](wiki/assets/buffs/10355.png) |
| **Buff id** | `10355` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 30 |

### Tooltip

> Quick step back : Decreased Move Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/5301-step-back|Step Back]], effect slot 3 (type 314, rate 100%)
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

---
title: "Puddle : Reduced Movement Speed"
type: "buff"
id: 20155
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20155", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20155"
duration: {"ticks": 5, "seconds": 1.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -50}
icon: {"file": "Skill_Boss_01.dds", "index": 25}
applied_by:
  - {"skill": 20155, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=e40fba type=6143a1 id=232bb1 sources=55f563 name_key=b1ab56 duration=76674f is_buff=b6589f stack_type=356a19 group=e3cbba effects=115285 icon=f7179c applied_by=37688f -->
|  |  |
|---|---|
|  | ![Puddle : Reduced Movement Speed](wiki/assets/buffs/20155.png) |
| **Buff id** | `20155` |
| **Duration** | 1 s (5 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 25 |

### Tooltip

> Puddle : Reduced Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -50 |

### Applied by

- Skill [[wiki/skills/20155-puddle|Puddle]], effect slot 1 (type 314, rate 100%)
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

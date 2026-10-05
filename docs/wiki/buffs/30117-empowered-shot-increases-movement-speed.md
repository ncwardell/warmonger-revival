---
title: "Empowered Shot: Increases Movement Speed"
type: "buff"
id: 30117
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30117", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10117"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Skill_Dolorece_01.png", "index": 21}
applied_by:
  - {"skill": 10117, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=74e9d2 type=6143a1 id=f09421 sources=c8d14f name_key=1a9630 duration=0aac5a is_buff=b6589f stack_type=356a19 group=e3cbba effects=732c70 icon=ac6851 applied_by=42a1ee -->
|  |  |
|---|---|
|  | ![Empowered Shot: Increases Movement Speed](../assets/buffs/30117.png) |
| **Buff id** | `30117` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 21 |

### Tooltip

> Empowered Shot: Increases Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/10117-empowered-shot|Empowered Shot]], effect slot 3 (type 314, rate 100%)
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

---
title: "Aura of Demise : Damages enemies around you"
type: "buff"
id: 30035
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30035", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10035"
duration: {"ticks": 40, "seconds": 8.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 433, "stat": "code 433 (unknown)", "value": 10}
  - {"code": 206, "stat": "code 206 (unknown)", "value": 10039}
icon: {"file": "Skill_Dolorece_01.png", "index": 5}
applied_by:
  - {"skill": 10038, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=68b909 type=6143a1 id=a5b7e6 sources=894b15 name_key=b5af52 duration=8c4b49 is_buff=b6589f stack_type=356a19 group=b6589f effects=644f14 icon=f51da1 applied_by=74c783 -->
|  |  |
|---|---|
|  | ![Aura of Demise : Damages enemies around you](../assets/buffs/30035.png) |
| **Buff id** | `30035` |
| **Duration** | 8 s (40 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 5 |

### Tooltip

> Aura of Demise : Damages enemies around you

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 433 | code 433 (unknown) | 10 |
| 206 | code 206 (unknown) | 10,039 |

### Applied by

- Skill [[wiki/skills/10038-aura-of-demise|Aura of Demise]], effect slot 1 (type 301, rate 100%)
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

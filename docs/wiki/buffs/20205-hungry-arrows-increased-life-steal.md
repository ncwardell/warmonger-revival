---
title: "Hungry arrows: increased Life Steal"
type: "buff"
id: 20205
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20205", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20205"
duration: {"ticks": 5, "seconds": 1.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 41, "stat": "Life Steal(%)", "value": 5}
icon: {"file": "Skill_Boss_01.dds", "index": 32}
applied_by:
  - {"skill": 20205, "slot": 1, "type": 304, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=2fd365 type=6143a1 id=570f73 sources=540da1 name_key=028d2a duration=76674f is_buff=b6589f stack_type=356a19 group=b6589f effects=5b7686 icon=6834b3 applied_by=6644ac -->
|  |  |
|---|---|
|  | ![Hungry arrows: increased Life Steal](../assets/buffs/20205.png) |
| **Buff id** | `20205` |
| **Duration** | 1 s (5 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 32 |

### Tooltip

> Hungry arrows: increased Life Steal

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 41 | Life Steal(%) | 5 |

### Applied by

- Skill [[wiki/skills/20205-hungry-arrows|Hungry arrows]], effect slot 1 (type 304, rate 100%)
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

---
title: "Covert Steps: Your basic Attacks deal additional damage"
type: "buff"
id: 20203
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20203", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20203"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 2
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 20203}
icon: {"file": "Skill_Boss_01.dds", "index": 31}
applied_by:
  - {"skill": 20202, "slot": 2, "type": 301, "rate": 100}
  - {"skill": 20203, "slot": 4, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=9cd0f7 type=6143a1 id=87f06e sources=4f09fb name_key=74941e duration=870e64 is_buff=b6589f stack_type=da4b92 group=b6589f effects=1461e1 icon=10f839 applied_by=7ff4e5 -->
|  |  |
|---|---|
|  | ![Covert Steps: Your basic Attacks deal additional damage](wiki/assets/buffs/20203.png) |
| **Buff id** | `20203` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 2 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 31 |

### Tooltip

> Covert Steps: Your basic Attacks deal additional damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 20,203 ([[wiki/skills/20203-covert-step\|Covert Step]]) |

### Applied by

- Skill [[wiki/skills/20202-covert-step|Covert Step]], effect slot 2 (type 301, rate 100%)
- Skill [[wiki/skills/20203-covert-step|Covert Step]], effect slot 4 (type 302, rate 100%)
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

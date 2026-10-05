---
title: "Restriction : Your next basic attack deals additional damage"
type: "buff"
id: 10043
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10043", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10043"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 5049}
icon: {"file": "Skill_Einsel_01.png", "index": 20}
applied_by:
  - {"skill": 5048, "slot": 1, "type": 301, "rate": 100}
  - {"skill": 5049, "slot": 3, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=9b0757 type=6143a1 id=8ad6f5 sources=1f195a name_key=001768 duration=3d2da5 is_buff=b6589f stack_type=356a19 group=b6589f effects=86fae5 icon=b7a24b applied_by=4933e9 -->
|  |  |
|---|---|
|  | ![Restriction : Your next basic attack deals additional damage](../assets/buffs/10043.png) |
| **Buff id** | `10043` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 20 |

### Tooltip

> Restriction : Your next basic attack deals additional damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 5,049 ([[wiki/skills/5049-restriction\|Restriction]]) |

### Applied by

- Skill [[wiki/skills/5048-restriction|Restriction]], effect slot 1 (type 301, rate 100%)
- Skill [[wiki/skills/5049-restriction|Restriction]], effect slot 3 (type 302, rate 100%)
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

---
title: "Secret Movement : Your next basic attack will deal additional damage"
type: "buff"
id: 10040
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10040", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10040"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 5044}
icon: {"file": "Skill_Miriam_01.png", "index": 4}
applied_by:
  - {"skill": 5043, "slot": 2, "type": 301, "rate": 100}
  - {"skill": 5044, "slot": 4, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=1c6871 type=6143a1 id=c92291 sources=2f1f2c name_key=19010e duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=a649a3 icon=a12d2b applied_by=487624 -->
|  |  |
|---|---|
|  | ![Secret Movement : Your next basic attack will deal additional damage](wiki/assets/buffs/10040.png) |
| **Buff id** | `10040` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 4 |

### Tooltip

> Secret Movement : Your next basic attack will deal additional damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 5,044 ([[wiki/skills/5044-secret-movement\|Secret Movement]]) |

### Applied by

- Skill [[wiki/skills/5043-secret-movement|Secret Movement]], effect slot 2 (type 301, rate 100%)
- Skill [[wiki/skills/5044-secret-movement|Secret Movement]], effect slot 4 (type 302, rate 100%)
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

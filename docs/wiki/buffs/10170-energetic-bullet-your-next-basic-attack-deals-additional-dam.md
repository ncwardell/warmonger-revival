---
title: "Energetic Bullet : Your next basic attack deals additional damage"
type: "buff"
id: 10170
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10170", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10170"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 5146}
icon: {"file": "Skill_Einsel_01.png", "index": 28}
applied_by:
  - {"skill": 5145, "slot": 3, "type": 301, "rate": 100}
  - {"skill": 5146, "slot": 4, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=77a885 type=6143a1 id=c2c44c sources=293788 name_key=f3a179 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=e1ae3e icon=721c7c applied_by=1c7945 -->
|  |  |
|---|---|
|  | ![Energetic Bullet : Your next basic attack deals additional damage](wiki/assets/buffs/10170.png) |
| **Buff id** | `10170` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 28 |

### Tooltip

> Energetic Bullet : Your next basic attack deals additional damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 5,146 ([[wiki/skills/5146-triggers-energetic-bullet\|Triggers Energetic Bullet]]) |

### Applied by

- Skill [[wiki/skills/5145-energetic-bullet|Energetic Bullet]], effect slot 3 (type 301, rate 100%)
- Skill [[wiki/skills/5146-triggers-energetic-bullet|Triggers Energetic Bullet]], effect slot 4 (type 302, rate 100%)
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

---
title: "Shadow Walk : Your next Attack deals bonus damage"
type: "buff"
id: 10142
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10142", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10142"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 5125}
icon: {"file": "Skill_Miriam_01.png", "index": 17}
applied_by:
  - {"skill": 5027, "slot": 4, "type": 301, "rate": 100}
  - {"skill": 5125, "slot": 4, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=a6f985 type=6143a1 id=2505a3 sources=2134bc name_key=de0711 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=f97ee6 icon=67ccf4 applied_by=62846d -->
|  |  |
|---|---|
|  | ![Shadow Walk : Your next Attack deals bonus damage](wiki/assets/buffs/10142.png) |
| **Buff id** | `10142` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 17 |

### Tooltip

> Shadow Walk : Your next Attack deals bonus damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 5,125 ([[wiki/skills/5125-shadow-walk\|Shadow Walk]]) |

### Applied by

- Skill [[wiki/skills/5027-shadow-walk|Shadow Walk]], effect slot 4 (type 301, rate 100%)
- Skill [[wiki/skills/5125-shadow-walk|Shadow Walk]], effect slot 4 (type 302, rate 100%)
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

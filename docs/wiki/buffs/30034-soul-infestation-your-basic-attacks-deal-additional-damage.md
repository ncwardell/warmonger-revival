---
title: "Soul Infestation : Your basic Attacks deal additional damage"
type: "buff"
id: 30034
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30034", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10034"
duration: {"ticks": 30, "seconds": 6.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 10037}
icon: {"file": "Skill_Dolorece_01.png", "index": 4}
applied_by:
  - {"skill": 10036, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=7807d5 type=6143a1 id=36ba38 sources=1cad76 name_key=68fff5 duration=5d0a7b is_buff=b6589f stack_type=356a19 group=b6589f effects=c3a13d icon=01c963 applied_by=f8d652 -->
|  |  |
|---|---|
|  | ![Soul Infestation : Your basic Attacks deal additional damage](../assets/buffs/30034.png) |
| **Buff id** | `30034` |
| **Duration** | 6 s (30 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 4 |

### Tooltip

> Soul Infestation : Your basic Attacks deal additional damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 10,037 ([[wiki/skills/10037-soul-infestation\|Soul Infestation]]) |

### Applied by

- Skill [[wiki/skills/10036-soul-infestation|Soul Infestation]], effect slot 1 (type 301, rate 100%)
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

---
title: "Lightning protection : You gain 30% Attack speed and Movement speed, Damage"
type: "buff"
id: 10434
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10434", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10434"
duration: {"ticks": 65, "seconds": 13.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 103, "stat": "Attack Speed(%)", "value": 30}
  - {"code": 105, "stat": "Movement(%)", "value": 30}
  - {"code": 101, "stat": "Attack(%)", "value": 30}
icon: {"file": "Policy.png", "index": 34}
applied_by:
  - {"skill": 5483, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=af45d4 type=6143a1 id=082fd2 sources=c6b7f2 name_key=bb97f9 duration=cdb31a is_buff=b6589f stack_type=356a19 group=b6589f effects=582a66 icon=9835a6 applied_by=c3d17b -->
|  |  |
|---|---|
|  | ![Lightning protection : You gain 30% Attack speed and Movement speed, Damage](../assets/buffs/10434.png) |
| **Buff id** | `10434` |
| **Duration** | 13 s (65 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 34 |

### Tooltip

> Lightning protection : You gain 30% Attack speed and Movement speed, Damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 103 | Attack Speed(%) | 30 |
| 105 | Movement(%) | 30 |
| 101 | Attack(%) | 30 |

### Applied by

- Skill [[wiki/skills/5483|Skill 5483]], effect slot 1 (type 301, rate 100%)
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

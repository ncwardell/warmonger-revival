---
title: "Nimble Pursuit : Your next basic attack deals additional damage based on your targets current HP."
type: "buff"
id: 10098
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10098", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10098"
duration: {"ticks": 30, "seconds": 6.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 5108}
icon: {"file": "Skill_Dolorece_01.png", "index": 16}
applied_by:
  - {"skill": 5107, "slot": 1, "type": 301, "rate": 100}
  - {"skill": 5108, "slot": 4, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=3c593c type=6143a1 id=4f7a3e sources=388568 name_key=15c839 duration=5d0a7b is_buff=b6589f stack_type=356a19 group=b6589f effects=8a4294 icon=197b6c applied_by=0b5482 -->
|  |  |
|---|---|
|  | ![Nimble Pursuit : Your next basic attack deals additional damage based on your targets current HP.](wiki/assets/buffs/10098.png) |
| **Buff id** | `10098` |
| **Duration** | 6 s (30 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 16 |

### Tooltip

> Nimble Pursuit : Your next basic attack deals additional damage based on your targets current HP.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 5,108 ([[wiki/skills/5108-triggers-nimble-pursuit\|Triggers Nimble Pursuit.]]) |

### Applied by

- Skill [[wiki/skills/5107-nimble-pursuit|Nimble Pursuit]], effect slot 1 (type 301, rate 100%)
- Skill [[wiki/skills/5108-triggers-nimble-pursuit|Triggers Nimble Pursuit.]], effect slot 4 (type 302, rate 100%)
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

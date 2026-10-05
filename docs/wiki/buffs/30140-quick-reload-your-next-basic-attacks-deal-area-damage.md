---
title: "Quick Reload : Your next basic Attacks deal area damage"
type: "buff"
id: 30140
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30140", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10140"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 10124}
icon: {"file": "Skill_Einsel_01.png", "index": 17}
applied_by:
  - {"skill": 10103, "slot": 2, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=c31d97 type=6143a1 id=c6fa3b sources=786f55 name_key=ada59b duration=3d2da5 is_buff=b6589f stack_type=356a19 group=b6589f effects=a62d67 icon=7c2320 applied_by=444611 -->
|  |  |
|---|---|
|  | ![Quick Reload : Your next basic Attacks deal area damage](wiki/assets/buffs/30140.png) |
| **Buff id** | `30140` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 17 |

### Tooltip

> Quick Reload : Your next basic Attacks deal area damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 10,124 ([[wiki/skills/10124\|Skill 10124]]) |

### Applied by

- Skill [[wiki/skills/10103-rapid-reload|Rapid Reload]], effect slot 2 (type 301, rate 100%)
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

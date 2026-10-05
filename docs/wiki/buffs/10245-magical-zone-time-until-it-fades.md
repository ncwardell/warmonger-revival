---
title: "Magical Zone : Time until it fades."
type: "buff"
id: 10245
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10245", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10245"
duration: {"ticks": 5, "seconds": 1.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 10}
  - {"code": 34, "stat": "Mana Regeneration", "value": 10}
icon: {"file": "Policy.png", "index": 32}
applied_by:
  - {"skill": 5202, "slot": 2, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=e06581 type=6143a1 id=bdfceb sources=88d884 name_key=fdcc53 duration=76674f is_buff=b6589f stack_type=356a19 group=b6589f effects=c522ae icon=1bc8e5 applied_by=1ffc7d -->
|  |  |
|---|---|
|  | ![Magical Zone : Time until it fades.](wiki/assets/buffs/10245.png) |
| **Buff id** | `10245` |
| **Duration** | 1 s (5 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 32 |

### Tooltip

> Magical Zone : Time until it fades.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 10 |
| 34 | Mana Regeneration | 10 |

### Applied by

- Skill [[wiki/skills/5202|Skill 5202]], effect slot 2 (type 314, rate 100%)
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

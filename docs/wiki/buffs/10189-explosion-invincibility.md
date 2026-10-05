---
title: "Explosion : Invincibility"
type: "buff"
id: 10189
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10189", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10189"
duration: {"ticks": 10, "seconds": 2.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 6, "stat": "Armor", "value": 500}
  - {"code": 7, "stat": "Magic Resist", "value": 500}
icon: {"file": "Policy.png", "index": 34}
applied_by:
  - {"skill": 5156, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=d8c79a type=6143a1 id=2019d8 sources=420e83 name_key=1c66d4 duration=2a0b1e is_buff=b6589f stack_type=356a19 group=b6589f effects=642b6e icon=9835a6 applied_by=3d3f17 -->
|  |  |
|---|---|
|  | ![Explosion : Invincibility](../assets/buffs/10189.png) |
| **Buff id** | `10189` |
| **Duration** | 2 s (10 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 34 |

### Tooltip

> Explosion : Invincibility

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 6 | Armor | 500 |
| 7 | Magic Resist | 500 |

### Applied by

- Skill [[wiki/skills/5156|Skill 5156]], effect slot 1 (type 301, rate 100%)
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

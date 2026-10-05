---
title: "The Other Side : Increased Armor and Magic Resistance"
type: "buff"
id: 10185
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10185", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10185"
duration: {"ticks": 8000, "seconds": 1600.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 6, "stat": "Armor", "value": 150}
  - {"code": 7, "stat": "Magic Resist", "value": 150}
icon: {"file": "Policy.png", "index": 33}
applied_by:
  - {"skill": 4999, "slot": 1, "type": 314, "rate": 100}
  - {"skill": 5157, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=86a12d type=6143a1 id=b43e41 sources=c6667a name_key=28fc8d duration=c94200 is_buff=b6589f stack_type=356a19 group=b6589f effects=66a274 icon=0392b4 applied_by=590c68 -->
|  |  |
|---|---|
|  | ![The Other Side : Increased Armor and Magic Resistance](wiki/assets/buffs/10185.png) |
| **Buff id** | `10185` |
| **Duration** | 26 min 40 s (8,000 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 33 |

### Tooltip

> The Other Side : Increased Armor and Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 6 | Armor | 150 |
| 7 | Magic Resist | 150 |

### Applied by

- Skill [[wiki/skills/4999|Skill 4999]], effect slot 1 (type 314, rate 100%)
- Skill [[wiki/skills/5157|Skill 5157]], effect slot 1 (type 314, rate 100%)
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

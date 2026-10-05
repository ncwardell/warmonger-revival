---
title: "Stone Guard debuff : Reduces defensive stats."
type: "buff"
id: 2013
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2013", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2013"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 106, "stat": "Armor(%)", "value": -30}
  - {"code": 107, "stat": "Magic Resist(%)", "value": -30}
icon: {"file": "Policy.png", "index": 0}
applied_by:
  - {"skill": 12, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=17fece type=6143a1 id=d08b10 sources=1a12c0 name_key=5203cc duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=3d429a icon=f877b6 applied_by=fbe306 -->
|  |  |
|---|---|
|  | ![Stone Guard debuff : Reduces defensive stats.](../assets/buffs/2013.png) |
| **Buff id** | `2013` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Stone Guard debuff : Reduces defensive stats.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 106 | Armor(%) | -30 |
| 107 | Magic Resist(%) | -30 |

### Applied by

- Skill [[wiki/skills/12|Skill 12]], effect slot 1 (type 314, rate 100%)
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

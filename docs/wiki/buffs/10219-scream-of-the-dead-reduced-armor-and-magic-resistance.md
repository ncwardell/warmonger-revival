---
title: "Scream of the Dead : Reduced Armor and Magic Resistance"
type: "buff"
id: 10219
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10219", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10219"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 6, "stat": "Armor", "value": -30}
  - {"code": 7, "stat": "Magic Resist", "value": -30}
icon: {"file": "Policy.png", "index": 40}
applied_by:
  - {"skill": 5185, "slot": 2, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=02d83b type=6143a1 id=0f42ef sources=61dc17 name_key=763832 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=4768c9 icon=6665b9 applied_by=554693 -->
|  |  |
|---|---|
|  | ![Scream of the Dead : Reduced Armor and Magic Resistance](wiki/assets/buffs/10219.png) |
| **Buff id** | `10219` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 40 |

### Tooltip

> Scream of the Dead : Reduced Armor and Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 6 | Armor | -30 |
| 7 | Magic Resist | -30 |

### Applied by

- Skill [[wiki/skills/5185-scream-of-the-dead|Scream of the Dead]], effect slot 2 (type 314, rate 100%)
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

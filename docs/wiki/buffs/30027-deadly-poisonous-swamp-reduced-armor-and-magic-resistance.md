---
title: "Deadly Poisonous Swamp : Reduced Armor and Magic Resistance"
type: "buff"
id: 30027
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30027", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10027"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10027
effects:
  - {"code": 106, "stat": "Armor(%)", "value": -20}
  - {"code": 107, "stat": "Magic Resist(%)", "value": -20}
icon: {"file": "Skill_Miriam_01.png", "index": 18}
applied_by:
  - {"skill": 10028, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=47eb30 type=6143a1 id=07b8af sources=d96760 name_key=90c73a duration=870e64 is_buff=b6589f stack_type=356a19 group=b9cc0a effects=f8da5d icon=90d3d6 applied_by=f7af73 -->
|  |  |
|---|---|
|  | ![Deadly Poisonous Swamp : Reduced Armor and Magic Resistance](wiki/assets/buffs/30027.png) |
| **Buff id** | `30027` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10027 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 18 |

### Tooltip

> Deadly Poisonous Swamp : Reduced Armor and Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 106 | Armor(%) | -20 |
| 107 | Magic Resist(%) | -20 |

### Applied by

- Skill [[wiki/skills/10028-poisonous-swamp|Poisonous Swamp]], effect slot 3 (type 314, rate 100%)
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

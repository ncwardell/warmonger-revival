---
title: "Energetic Claw : Reduced Armor and Magic Resistance"
type: "buff"
id: 10176
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10176", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10176"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 106, "stat": "Armor(%)", "value": -20}
  - {"code": 107, "stat": "Magic Resist(%)", "value": -20}
icon: {"file": "Skill_Einsel_01.png", "index": 31}
applied_by:
  - {"skill": 5150, "slot": 4, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=42558e type=6143a1 id=308a76 sources=14652b name_key=ffcba6 duration=3d2da5 is_buff=b6589f stack_type=356a19 group=b6589f effects=f8da5d icon=e24f43 applied_by=6fa416 -->
|  |  |
|---|---|
|  | ![Energetic Claw : Reduced Armor and Magic Resistance](../assets/buffs/10176.png) |
| **Buff id** | `10176` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 31 |

### Tooltip

> Energetic Claw : Reduced Armor and Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 106 | Armor(%) | -20 |
| 107 | Magic Resist(%) | -20 |

### Applied by

- Skill [[wiki/skills/5150-skull-king-s-claw|Skull king's Claw]], effect slot 4 (type 314, rate 100%)
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

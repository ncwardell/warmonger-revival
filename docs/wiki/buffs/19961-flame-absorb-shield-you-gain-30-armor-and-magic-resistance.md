---
title: "Flame Absorb shield : You gain 30% Armor and Magic Resistance"
type: "buff"
id: 19961
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 19961", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_19961"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 106, "stat": "Armor(%)", "value": 10}
  - {"code": 107, "stat": "Magic Resist(%)", "value": 10}
icon: {"file": "Skill_Boss_01.dds", "index": 11}
applied_by:
  - {"skill": 19961, "slot": 2, "type": 301, "rate": 100}
  - {"skill": 19961, "slot": 4, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=8c0b10 type=6143a1 id=f4d46d sources=7677ae name_key=3d92d0 duration=3d2da5 is_buff=b6589f stack_type=356a19 group=b6589f effects=a2c63c icon=e77ed7 applied_by=583524 -->
|  |  |
|---|---|
|  | ![Flame Absorb shield : You gain 30% Armor and Magic Resistance](../assets/buffs/19961.png) |
| **Buff id** | `19961` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 11 |

### Tooltip

> Flame Absorb shield : You gain 30% Armor and Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 106 | Armor(%) | 10 |
| 107 | Magic Resist(%) | 10 |

### Applied by

- Skill [[wiki/skills/19961-flame-absorbtion-shield|Flame Absorbtion Shield]], effect slot 2 (type 301, rate 100%)
- Skill [[wiki/skills/19961-flame-absorbtion-shield|Flame Absorbtion Shield]], effect slot 4 (type 314, rate 100%)
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

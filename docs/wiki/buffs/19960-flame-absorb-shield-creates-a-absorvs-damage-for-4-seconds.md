---
title: "Flame Absorb shield : Creates a absorvs damage for 4 seconds"
type: "buff"
id: 19960
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 19960", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_19960"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 19960
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 300}
  - {"code": 101, "stat": "Attack(%)", "value": 10}
icon: {"file": "Skill_Boss_01.dds", "index": 11}
applied_by:
  - {"skill": 19961, "slot": 1, "type": 304, "rate": 100}
  - {"skill": 19961, "slot": 3, "type": 317, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=cee326 type=6143a1 id=98aca3 sources=b73ffc name_key=3fd218 duration=3d2da5 is_buff=b6589f stack_type=356a19 group=98aca3 effects=816ad5 icon=e77ed7 applied_by=077771 -->
|  |  |
|---|---|
|  | ![Flame Absorb shield : Creates a absorvs damage for 4 seconds](wiki/assets/buffs/19960.png) |
| **Buff id** | `19960` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 19960 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 11 |

### Tooltip

> Flame Absorb shield : Creates a absorvs damage for 4 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 300 |
| 101 | Attack(%) | 10 |

### Applied by

- Skill [[wiki/skills/19961-flame-absorbtion-shield|Flame Absorbtion Shield]], effect slot 1 (type 304, rate 100%)
- Skill [[wiki/skills/19961-flame-absorbtion-shield|Flame Absorbtion Shield]], effect slot 3 (type 317, rate 100%)
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

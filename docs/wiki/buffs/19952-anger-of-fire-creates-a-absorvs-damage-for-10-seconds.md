---
title: "Anger of fire : Creates a absorvs damage for 10 seconds"
type: "buff"
id: 19952
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 19952", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_19952"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 19952
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 200}
  - {"code": 101, "stat": "Attack(%)", "value": 10}
icon: {"file": "Skill_Einsel_01.png", "index": 36}
applied_by:
  - {"skill": 19951, "slot": 2, "type": 308, "rate": 100}
  - {"skill": 19952, "slot": 4, "type": 305, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=2bac66 type=6143a1 id=00fc1e sources=4fcd34 name_key=4af062 duration=6c749d is_buff=b6589f stack_type=356a19 group=00fc1e effects=b34cd3 icon=574aef applied_by=fb54dd -->
|  |  |
|---|---|
|  | ![Anger of fire : Creates a absorvs damage for 10 seconds](wiki/assets/buffs/19952.png) |
| **Buff id** | `19952` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 19952 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 36 |

### Tooltip

> Anger of fire : Creates a absorvs damage for 10 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 200 |
| 101 | Attack(%) | 10 |

### Applied by

- Skill [[wiki/skills/19951-fiery-anger|Fiery Anger]], effect slot 2 (type 308, rate 100%)
- Skill [[wiki/skills/19952-fiery-anger|Fiery Anger]], effect slot 4 (type 305, rate 100%)
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

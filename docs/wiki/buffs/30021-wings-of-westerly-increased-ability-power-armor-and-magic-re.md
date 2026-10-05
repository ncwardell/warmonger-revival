---
title: "Wings of Westerly : Increased Ability Power, Armor and Magic Resistance"
type: "buff"
id: 30021
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30021", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10021"
duration: {"ticks": 40, "seconds": 8.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 106, "stat": "Armor(%)", "value": 5}
  - {"code": 107, "stat": "Magic Resist(%)", "value": 5}
  - {"code": 102, "stat": "Ability Power(%)", "value": 20}
icon: {"file": "Skill_Einsel_01.png", "index": 25}
applied_by:
  - {"skill": 10023, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=a964aa type=6143a1 id=ca4ef2 sources=972666 name_key=8811bf duration=8c4b49 is_buff=b6589f stack_type=356a19 group=b6589f effects=6a4769 icon=8f0410 applied_by=bb2b98 -->
|  |  |
|---|---|
|  | ![Wings of Westerly : Increased Ability Power, Armor and Magic Resistance](wiki/assets/buffs/30021.png) |
| **Buff id** | `30021` |
| **Duration** | 8 s (40 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 25 |

### Tooltip

> Wings of Westerly : Increased Ability Power, Armor and Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 106 | Armor(%) | 5 |
| 107 | Magic Resist(%) | 5 |
| 102 | Ability Power(%) | 20 |

### Applied by

- Skill [[wiki/skills/10023-wings-of-fair-wind|Wings of fair wind]], effect slot 1 (type 301, rate 100%)
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

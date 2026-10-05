---
title: "Assassination : Active"
type: "buff"
id: 10343
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10343", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10343"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10343
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 5293}
icon: {"file": "Skill_Miriam_01.png", "index": 25}
applied_by:
  - {"skill": 5289, "slot": 1, "type": 301, "rate": 100}
  - {"skill": 5293, "slot": 2, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=ea5e5f type=6143a1 id=27268e sources=c2b82b name_key=556277 duration=870e64 is_buff=b6589f stack_type=356a19 group=27268e effects=8dfc54 icon=d212e9 applied_by=a3ee2b -->
|  |  |
|---|---|
|  | ![Assassination : Active](wiki/assets/buffs/10343.png) |
| **Buff id** | `10343` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10343 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 25 |

### Tooltip

> Assassination : Active

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 5,293 ([[wiki/skills/5293-assassination\|Assassination]]) |

### Applied by

- Skill [[wiki/skills/5289-assassination|Assassination]], effect slot 1 (type 301, rate 100%)
- Skill [[wiki/skills/5293-assassination|Assassination]], effect slot 2 (type 302, rate 100%)
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

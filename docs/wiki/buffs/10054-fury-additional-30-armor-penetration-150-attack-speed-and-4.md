---
title: "Fury : Additional 30 Armor Penetration, 150 Attack Speed and 4 Health Regeneration"
type: "buff"
id: 10054
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10054", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10054"
duration: {"ticks": 40, "seconds": 8.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 13, "stat": "Armor Penetration", "value": 30}
  - {"code": 16, "stat": "code 16 (unknown)", "value": 150}
  - {"code": 32, "stat": "Health Regeneration", "value": 4}
icon: {"file": "Skill_Dolorece_01.png", "index": 10}
applied_by:
  - {"skill": 5061, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=7980fa type=6143a1 id=3e2ae0 sources=5db5cd name_key=ff0e9f duration=8c4b49 is_buff=b6589f stack_type=356a19 group=b6589f effects=cf5663 icon=3500a1 applied_by=947e11 -->
|  |  |
|---|---|
|  | ![Fury : Additional 30 Armor Penetration, 150 Attack Speed and 4 Health Regeneration](wiki/assets/buffs/10054.png) |
| **Buff id** | `10054` |
| **Duration** | 8 s (40 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 10 |

### Tooltip

> Fury : Additional 30 Armor Penetration, 150 Attack Speed 
>  and 4 Health Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 13 | Armor Penetration | 30 |
| 16 | code 16 (unknown) | 150 |
| 32 | Health Regeneration | 4 |

### Applied by

- Skill [[wiki/skills/5061-fury|Fury]], effect slot 1 (type 301, rate 100%)
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

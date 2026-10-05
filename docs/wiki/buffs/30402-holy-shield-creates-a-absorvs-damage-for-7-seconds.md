---
title: "Holy Shield : Creates a absorvs damage for 7 seconds"
type: "buff"
id: 30402
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30402", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10402"
duration: {"ticks": 35, "seconds": 7.0, "permanent": false}
is_buff: 0
stack_type: 3
group: 10402
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 200}
  - {"code": 131, "stat": "Health(%)", "value": 50}
icon: {"file": "Skill_Dolorece_01.png", "index": 36}
applied_by:
  - {"skill": 10354, "slot": 1, "type": 308, "rate": 100}
  - {"skill": 10354, "slot": 2, "type": 317, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=d22d28 type=6143a1 id=879677 sources=fc442c name_key=3dedca duration=bdf5bf is_buff=b6589f stack_type=77de68 group=74c0ab effects=4213bb icon=7da0f2 applied_by=03fd2f -->
|  |  |
|---|---|
|  | ![Holy Shield : Creates a absorvs damage for 7 seconds](wiki/assets/buffs/30402.png) |
| **Buff id** | `30402` |
| **Duration** | 7 s (35 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 3 (guessed column) |
| **Group** | 10402 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 36 |

### Tooltip

> Holy Shield :  Creates a absorvs damage for 7 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 200 |
| 131 | Health(%) | 50 |

### Applied by

- Skill [[wiki/skills/10354-holy-shield|Holy Shield]], effect slot 1 (type 308, rate 100%)
- Skill [[wiki/skills/10354-holy-shield|Holy Shield]], effect slot 2 (type 317, rate 100%)
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

---
title: "Dark Transformation : Gain 100 Movement Speed"
type: "buff"
id: 30038
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30038", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10038"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 17, "stat": "code 17 (unknown)", "value": 100}
icon: {"file": "Skill_Dolorece_01.png", "index": 7}
applied_by:
  - {"skill": 10041, "slot": 2, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=7b4d72 type=6143a1 id=73b3bc sources=e64040 name_key=62b850 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=48390e icon=3af2a9 applied_by=c0a38f -->
|  |  |
|---|---|
|  | ![Dark Transformation : Gain 100 Movement Speed](wiki/assets/buffs/30038.png) |
| **Buff id** | `30038` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 7 |

### Tooltip

> Dark Transformation : Gain 100 Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 17 | code 17 (unknown) | 100 |

### Applied by

- Skill [[wiki/skills/10041-dark-transformation|Dark Transformation]], effect slot 2 (type 301, rate 100%)
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

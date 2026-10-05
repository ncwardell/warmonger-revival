---
title: "Dark Transformation : Gain 100 Movement Speed"
type: "buff"
id: 10038
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10038", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 Character creation, 1:50 (10 s; matches client duration)"]
name_key: "SkillBuff_10038"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 17, "stat": "code 17 (unknown)", "value": 100}
icon: {"file": "Skill_Dolorece_01.png", "index": 7}
applied_by:
  - {"skill": 5041, "slot": 2, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=7b4d72 type=6143a1 id=2c384a sources=0e2bfa name_key=62b850 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=48390e icon=3af2a9 applied_by=5f4ca6 -->
|  |  |
|---|---|
|  | ![Dark Transformation : Gain 100 Movement Speed](wiki/assets/buffs/10038.png) |
| **Buff id** | `10038` |
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

- Skill [[wiki/skills/5041-dark-transformation|Dark Transformation]], effect slot 2 (type 301, rate 100%)
<!-- generated:end -->

## Notes

- One of the two 10 s buffs of [[wiki/skills/5041-dark-transformation|Dark Transformation]]. The level-1 skill text on the character-creation screen reads "more HP regeneration and movement speed for 10 s", matching this buff's movement speed and its 10 s duration ([[gameplay/video-character-creation-and-tutorial]] §1, [1:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=110s)). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-character-creation-and-tutorial]] §1.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

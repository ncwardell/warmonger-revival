---
title: "Howl of Victory : Increased Health Regeneration"
type: "buff"
id: 10351
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10351", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10351"
duration: {"ticks": 40, "seconds": 8.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 132, "stat": "Health Regeneration(%)", "value": 20}
icon: {"file": "Skill_Dolorece_01.png", "index": 14}
applied_by:
  - {"skill": 5296, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=a905c9 type=6143a1 id=3809f8 sources=a09f10 name_key=906b8a duration=8c4b49 is_buff=b6589f stack_type=356a19 group=b6589f effects=6914b3 icon=384e30 applied_by=da911b -->
|  |  |
|---|---|
|  | ![Howl of Victory : Increased Health Regeneration](wiki/assets/buffs/10351.png) |
| **Buff id** | `10351` |
| **Duration** | 8 s (40 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 14 |

### Tooltip

> Howl of Victory : Increased Health Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 132 | Health Regeneration(%) | 20 |

### Applied by

- Skill [[wiki/skills/5296-howl-of-victory|Howl of Victory]], effect slot 3 (type 314, rate 100%)
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

---
title: "Draw Power: Increases Attack and Movement Speed"
type: "buff"
id: 30017
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30017", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10017"
duration: {"ticks": 70, "seconds": 14.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 116, "stat": "code 116 (unknown)", "value": 15}
  - {"code": 117, "stat": "code 117 (unknown)", "value": 15}
icon: {"file": "Skill_Einsel_01.png", "index": 13}
applied_by:
  - {"skill": 10015, "slot": 1, "type": 301, "rate": 100}
  - {"skill": 10015, "slot": 2, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=48a95f type=6143a1 id=fd3f92 sources=49daaa name_key=4e4acf duration=718052 is_buff=b6589f stack_type=356a19 group=b6589f effects=7ff3e1 icon=6b1db9 applied_by=c2a63d -->
|  |  |
|---|---|
|  | ![Draw Power: Increases Attack and Movement Speed](wiki/assets/buffs/30017.png) |
| **Buff id** | `30017` |
| **Duration** | 14 s (70 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 13 |

### Tooltip

> Draw Power: Increases Attack and Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 116 | code 116 (unknown) | 15 |
| 117 | code 117 (unknown) | 15 |

### Applied by

- Skill [[wiki/skills/10015-bless-of-crystal|Bless of Crystal]], effect slot 1 (type 301, rate 100%)
- Skill [[wiki/skills/10015-bless-of-crystal|Bless of Crystal]], effect slot 2 (type 314, rate 100%)
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

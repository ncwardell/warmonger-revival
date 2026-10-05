---
title: "Smoke Screen : Reduced Movement and Attack Speed"
type: "buff"
id: 10353
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10353", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10353"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 118, "stat": "code 118 (unknown)", "value": -30}
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Skill_Dolorece_01.png", "index": 29}
applied_by:
  - {"skill": 5300, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=e612bd type=6143a1 id=6cd82b sources=9777c7 name_key=a5b12c duration=870e64 is_buff=b6589f stack_type=356a19 group=e3cbba effects=0b8164 icon=54955f applied_by=c1a8e5 -->
|  |  |
|---|---|
|  | ![Smoke Screen : Reduced Movement and Attack Speed](wiki/assets/buffs/10353.png) |
| **Buff id** | `10353` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 29 |

### Tooltip

> Smoke Screen : Reduced Movement and Attack Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 118 | code 118 (unknown) | -30 |
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/5300-smoke-screen|Smoke Screen]], effect slot 3 (type 314, rate 100%)
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

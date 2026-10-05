---
title: "Hail of Arrows : Reduced Movement Speed"
type: "buff"
id: 30114
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30114", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10114"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -40}
icon: {"file": "Skill_Miriam_01.png", "index": 14}
applied_by:
  - {"skill": 10114, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=7cc4ba type=6143a1 id=c7bd7c sources=47c5f0 name_key=fb6258 duration=0aac5a is_buff=b6589f stack_type=356a19 group=e3cbba effects=34f6eb icon=21b456 applied_by=036d6f -->
|  |  |
|---|---|
|  | ![Hail of Arrows : Reduced Movement Speed](wiki/assets/buffs/30114.png) |
| **Buff id** | `30114` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 14 |

### Tooltip

> Hail of Arrows : Reduced Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -40 |

### Applied by

- Skill [[wiki/skills/10114-hail-of-arrows|Hail of Arrows]], effect slot 3 (type 314, rate 100%)
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

---
title: "Roar : Increase Movement speed and Attack speed"
type: "buff"
id: 20252
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20252", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20252"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 118, "stat": "code 118 (unknown)", "value": -30}
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Skill_Boss_01.dds", "index": 47}
applied_by:
  - {"skill": 20252, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=7cdd9c type=6143a1 id=b3189c sources=82f8d7 name_key=717490 duration=3d2da5 is_buff=b6589f stack_type=356a19 group=e3cbba effects=0b8164 icon=3f59d9 applied_by=3f34c1 -->
|  |  |
|---|---|
|  | ![Roar : Increase Movement speed and Attack speed](wiki/assets/buffs/20252.png) |
| **Buff id** | `20252` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 47 |

### Tooltip

> Roar : Increase Movement speed and Attack speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 118 | code 118 (unknown) | -30 |
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/20252-roar|Roar]], effect slot 1 (type 314, rate 100%)
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

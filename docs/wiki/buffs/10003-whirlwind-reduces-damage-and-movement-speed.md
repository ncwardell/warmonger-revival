---
title: "Whirlwind: Reduces Damage and Movement Speed"
type: "buff"
id: 10003
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10003", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10003"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 101, "stat": "Attack(%)", "value": -30}
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Skill_Dolorece_01.png", "index": 2}
applied_by:
  - {"skill": 5002, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=913fcd type=6143a1 id=b27b41 sources=86b1a0 name_key=bbdaa6 duration=3d2da5 is_buff=b6589f stack_type=356a19 group=e3cbba effects=22dadb icon=47a729 applied_by=8c1b92 -->
|  |  |
|---|---|
|  | ![Whirlwind: Reduces Damage and Movement Speed](wiki/assets/buffs/10003.png) |
| **Buff id** | `10003` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 2 |

### Tooltip

> Whirlwind: Reduces Damage and Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 101 | Attack(%) | -30 |
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/5002-whirlwind|Whirlwind]], effect slot 3 (type 314, rate 100%)
- Nation policy 4 `PolicyName_4` (Policy.cdb, server-only; buff_or_skill)
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

---
title: "Blessing of Order: Creates a shield that absorbs Damage for 10 seconds"
type: "buff"
id: 30047
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30047", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10047"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10047
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 100}
  - {"code": 102, "stat": "Ability Power(%)", "value": 10}
  - {"code": 410, "stat": "code 410 (unknown)", "value": 30049}
icon: {"file": "Skill_Einsel_01.png", "index": 22}
applied_by:
  - {"skill": 10052, "slot": 1, "type": 317, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=799380 type=6143a1 id=47087d sources=22a3b2 name_key=92cab9 duration=6c749d is_buff=b6589f stack_type=356a19 group=ad886d effects=4ba6cd icon=6b4fc5 applied_by=c89599 -->
|  |  |
|---|---|
|  | ![Blessing of Order: Creates a shield that absorbs Damage for 10 seconds](wiki/assets/buffs/30047.png) |
| **Buff id** | `30047` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10047 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 22 |

### Tooltip

> Blessing of Order: Creates a shield that absorbs Damage for 10 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 100 |
| 102 | Ability Power(%) | 10 |
| 410 | code 410 (unknown) | 30,049 |

### Applied by

- Skill [[wiki/skills/10052-blessing-of-order|Blessing of Order]], effect slot 1 (type 317, rate 100%)
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

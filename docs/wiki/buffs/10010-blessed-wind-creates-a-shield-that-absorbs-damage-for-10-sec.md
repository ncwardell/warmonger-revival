---
title: "Blessed Wind: Creates a shield that absorbs Damage for 10 seconds"
type: "buff"
id: 10010
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10010", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10010"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10010
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 200}
  - {"code": 102, "stat": "Ability Power(%)", "value": 40}
icon: {"file": "Skill_Einsel_01.png", "index": 2}
applied_by:
  - {"skill": 5010, "slot": 1, "type": 317, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=302751 type=6143a1 id=b66ddc sources=608754 name_key=9e5328 duration=6c749d is_buff=b6589f stack_type=356a19 group=b66ddc effects=a46c67 icon=1fd7a3 applied_by=b4ca2c -->
|  |  |
|---|---|
|  | ![Blessed Wind: Creates a shield that absorbs Damage for 10 seconds](../assets/buffs/10010.png) |
| **Buff id** | `10010` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10010 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 2 |

### Tooltip

> Blessed Wind: Creates a shield that absorbs Damage for 10 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 200 |
| 102 | Ability Power(%) | 40 |

### Applied by

- Skill [[wiki/skills/5010-blessed-wind|Blessed Wind]], effect slot 1 (type 317, rate 100%)
- Nation policy 11 `PolicyName_11` (Policy.cdb, server-only; buff_or_skill)
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

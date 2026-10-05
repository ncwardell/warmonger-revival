---
title: "Eye of the Storm : Increased Movement Speed and defence"
type: "buff"
id: 10013
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10013", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10013"
duration: {"ticks": 10, "seconds": 2.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10013
effects:
  - {"code": 117, "stat": "code 117 (unknown)", "value": 15}
  - {"code": 106, "stat": "Armor(%)", "value": 25}
  - {"code": 107, "stat": "Magic Resist(%)", "value": 25}
icon: {"file": "Skill_Einsel_01.png", "index": 3}
applied_by:
  - {"skill": 5012, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=49a528 type=6143a1 id=c1e866 sources=bf114c name_key=099550 duration=2a0b1e is_buff=b6589f stack_type=356a19 group=c1e866 effects=cddaab icon=fae5ad applied_by=ca535c -->
|  |  |
|---|---|
|  | ![Eye of the Storm : Increased Movement Speed and defence](../assets/buffs/10013.png) |
| **Buff id** | `10013` |
| **Duration** | 2 s (10 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10013 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 3 |

### Tooltip

> Eye of the Storm : Increased Movement Speed and defence

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 117 | code 117 (unknown) | 15 |
| 106 | Armor(%) | 25 |
| 107 | Magic Resist(%) | 25 |

### Applied by

- Skill [[wiki/skills/5012|Skill 5012]], effect slot 1 (type 314, rate 100%)
- Nation policy 14 `PolicyName_14` (Policy.cdb, server-only; buff_or_skill)
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

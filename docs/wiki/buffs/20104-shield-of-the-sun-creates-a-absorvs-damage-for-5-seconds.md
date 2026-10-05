---
title: "Shield of the Sun : Creates a absorvs damage for 5 seconds"
type: "buff"
id: 20104
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20104", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20104"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 20104
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 150}
  - {"code": 102, "stat": "Ability Power(%)", "value": 20}
icon: {"file": "Skill_Boss_01.dds", "index": 18}
applied_by:
  - {"skill": 20108, "slot": 1, "type": 308, "rate": 100}
  - {"skill": 20108, "slot": 3, "type": 366, "rate": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=0e8a39 type=6143a1 id=8cbfd8 sources=f9120a name_key=0c9635 duration=870e64 is_buff=b6589f stack_type=356a19 group=8cbfd8 effects=5558ea icon=7bf15f applied_by=6261d6 -->
|  |  |
|---|---|
|  | ![Shield of the Sun : Creates a absorvs damage for 5 seconds](../assets/buffs/20104.png) |
| **Buff id** | `20104` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 20104 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 18 |

### Tooltip

> Shield of the Sun : Creates a absorvs damage for 5 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 150 |
| 102 | Ability Power(%) | 20 |

### Applied by

- Skill [[wiki/skills/20108-shield-of-the-sun|Shield of the Sun]], effect slot 1 (type 308, rate 100%)
- Skill [[wiki/skills/20108-shield-of-the-sun|Shield of the Sun]], effect slot 3 (type 366, rate 5%)
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

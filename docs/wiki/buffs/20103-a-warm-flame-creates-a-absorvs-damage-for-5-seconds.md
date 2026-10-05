---
title: "A warm flame : Creates a absorvs damage for 5 seconds"
type: "buff"
id: 20103
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20103", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20103"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 20103
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 300}
  - {"code": 102, "stat": "Ability Power(%)", "value": 50}
icon: {"file": "Skill_Boss_01.dds", "index": 15}
applied_by:
  - {"skill": 20105, "slot": 1, "type": 308, "rate": 100}
  - {"skill": 20105, "slot": 2, "type": 317, "rate": 100}
  - {"skill": 20105, "slot": 3, "type": 365, "rate": 5}
  - {"skill": 20105, "slot": 4, "type": 366, "rate": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=bb98f1 type=6143a1 id=55fcbe sources=c95d8c name_key=bbaeec duration=870e64 is_buff=b6589f stack_type=356a19 group=55fcbe effects=8ef2dd icon=660fb1 applied_by=07c96d -->
|  |  |
|---|---|
|  | ![A warm flame : Creates a absorvs damage for 5 seconds](wiki/assets/buffs/20103.png) |
| **Buff id** | `20103` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 20103 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 15 |

### Tooltip

> A warm flame : Creates a absorvs damage for 5 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 300 |
| 102 | Ability Power(%) | 50 |

### Applied by

- Skill [[wiki/skills/20105-a-warm-flame|A warm flame]], effect slot 1 (type 308, rate 100%)
- Skill [[wiki/skills/20105-a-warm-flame|A warm flame]], effect slot 2 (type 317, rate 100%)
- Skill [[wiki/skills/20105-a-warm-flame|A warm flame]], effect slot 3 (type 365, rate 5%)
- Skill [[wiki/skills/20105-a-warm-flame|A warm flame]], effect slot 4 (type 366, rate 5%)
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

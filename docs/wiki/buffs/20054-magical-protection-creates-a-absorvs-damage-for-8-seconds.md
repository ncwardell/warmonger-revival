---
title: "Magical Protection : Creates a absorvs damage for 8 seconds"
type: "buff"
id: 20054
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20054", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10230"
duration: {"ticks": 40, "seconds": 8.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10230
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 300}
  - {"code": 101, "stat": "Attack(%)", "value": 10}
  - {"code": 410, "stat": "code 410 (unknown)", "value": 20055}
icon: {"file": "Skill_Boss_01.dds", "index": 5}
applied_by:
  - {"skill": 20054, "slot": 1, "type": 308, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=1e409a type=6143a1 id=375c11 sources=18fe30 name_key=1aeda4 duration=8c4b49 is_buff=b6589f stack_type=356a19 group=373c73 effects=da063a icon=b3dd37 applied_by=c3f3d9 -->
|  |  |
|---|---|
|  | ![Magical Protection : Creates a absorvs damage for 8 seconds](../assets/buffs/20054.png) |
| **Buff id** | `20054` |
| **Duration** | 8 s (40 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10230 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 5 |

### Tooltip

> Magical Protection : Creates a absorvs damage for 8 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 300 |
| 101 | Attack(%) | 10 |
| 410 | code 410 (unknown) | 20,055 |

### Applied by

- Skill [[wiki/skills/20054-magical-protection|Magical Protection]], effect slot 1 (type 308, rate 100%)
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

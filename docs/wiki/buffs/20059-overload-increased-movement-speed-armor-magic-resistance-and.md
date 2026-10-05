---
title: "Overload : Increased Movement Speed, Armor, Magic Resistance and immune to abilities."
type: "buff"
id: 20059
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20059", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10235"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": 30}
  - {"code": 6, "stat": "Armor", "value": 30}
  - {"code": 7, "stat": "Magic Resist", "value": 30}
icon: {"file": "Skill_Boss_01.dds", "index": 7}
applied_by:
  - {"skill": 20058, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=9dd6fc type=6143a1 id=b7c063 sources=7c8e12 name_key=c95592 duration=6c749d is_buff=b6589f stack_type=356a19 group=356a19 effects=0aa061 icon=914e85 applied_by=c40093 -->
|  |  |
|---|---|
|  | ![Overload : Increased Movement Speed, Armor, Magic Resistance and immune to abilities.](wiki/assets/buffs/20059.png) |
| **Buff id** | `20059` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 7 |

### Tooltip

> Overload : Increased Movement Speed, Armor, Magic Resistance and immune to abilities.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | 30 |
| 6 | Armor | 30 |
| 7 | Magic Resist | 30 |

### Applied by

- Skill [[wiki/skills/20058-overload|Overload]], effect slot 1 (type 301, rate 100%)
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

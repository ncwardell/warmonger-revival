---
title: "Backstab : Increase movement speed"
type: "buff"
id: 10421
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10421", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10421"
duration: {"ticks": 35, "seconds": 7.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 4
effects:
  - {"code": 17, "stat": "code 17 (unknown)", "value": 90}
icon: {"file": "Skill_Miriam_01.png", "index": 29}
applied_by:
  - {"skill": 5461, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=4c9860 type=6143a1 id=f1cf11 sources=1ca467 name_key=3b4456 duration=bdf5bf is_buff=b6589f stack_type=356a19 group=1b6453 effects=b3b8cb icon=c0fb59 applied_by=aa45ec -->
|  |  |
|---|---|
|  | ![Backstab : Increase movement speed](wiki/assets/buffs/10421.png) |
| **Buff id** | `10421` |
| **Duration** | 7 s (35 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 4 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 29 |

### Tooltip

> Backstab : Increase movement speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 17 | code 17 (unknown) | 90 |

### Applied by

- Skill [[wiki/skills/5461-backstab|Backstab]], effect slot 1 (type 301, rate 100%)
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

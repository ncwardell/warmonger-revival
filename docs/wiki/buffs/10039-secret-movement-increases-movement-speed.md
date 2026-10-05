---
title: "Secret Movement: Increases Movement Speed"
type: "buff"
id: 10039
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10039", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10039"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 4
effects:
  - {"code": 17, "stat": "code 17 (unknown)", "value": 90}
icon: {"file": "Skill_Miriam_01.png", "index": 4}
applied_by:
  - {"skill": 5043, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=ce49dc type=6143a1 id=c2bdbf sources=59864b name_key=f09af6 duration=870e64 is_buff=b6589f stack_type=356a19 group=1b6453 effects=b3b8cb icon=a12d2b applied_by=68a1c5 -->
|  |  |
|---|---|
|  | ![Secret Movement: Increases Movement Speed](wiki/assets/buffs/10039.png) |
| **Buff id** | `10039` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 4 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 4 |

### Tooltip

> Secret Movement: Increases Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 17 | code 17 (unknown) | 90 |

### Applied by

- Skill [[wiki/skills/5043-secret-movement|Secret Movement]], effect slot 1 (type 301, rate 100%)
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

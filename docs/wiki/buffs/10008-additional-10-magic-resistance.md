---
title: "Additional 10% Magic Resistance"
type: "buff"
id: 10008
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10008"]
name_key: "SkillBuff_10008"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 7, "stat": "Magic Resist", "value": 15}
icon: {"file": "Items_05.png", "index": 7}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=4d3867 type=6143a1 id=e3a530 sources=6b04fc name_key=749800 duration=6c141f is_buff=b6589f stack_type=356a19 group=b6589f effects=aeb489 icon=ce75c9 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Additional 10% Magic Resistance](wiki/assets/buffs/10008.png) |
| **Buff id** | `10008` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_05.png` cell 7 |

### Tooltip

> Additional 10% Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 7 | Magic Resist | 15 |

### Applied by

- Nation policy 9 `PolicyName_9` (Policy.cdb, server-only; buff_or_skill)
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

---
title: "Improved HP Regeneration"
type: "buff"
id: 10001
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10001"]
name_key: "SkillBuff_10001"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 10001
effects:
  - {"code": 132, "stat": "Health Regeneration(%)", "value": 20}
icon: {"file": "Items_05.png", "index": 0}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=e4391e type=6143a1 id=6c447a sources=3114a0 name_key=9de87b duration=6c141f is_buff=b6589f stack_type=356a19 group=6c447a effects=6914b3 icon=bccb6d applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Improved HP Regeneration](../assets/buffs/10001.png) |
| **Buff id** | `10001` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10001 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_05.png` cell 0 |

### Tooltip

> Improved HP Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 132 | Health Regeneration(%) | 20 |

### Applied by

- Nation policy 2 `PolicyName_2` (Policy.cdb, server-only; buff_or_skill)
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

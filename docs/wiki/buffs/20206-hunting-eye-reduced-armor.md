---
title: "Hunting Eye: Reduced armor"
type: "buff"
id: 20206
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20206"]
name_key: "SkillBuff_20206"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 20216}
icon: {"file": "Skill_Boss_01.dds", "index": 33}
applied_by:
  - {"skill": 20215, "slot": 1, "type": 303, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=cbbc74 type=6143a1 id=8a6394 sources=3b4476 name_key=edd4ad duration=6c141f is_buff=b6589f stack_type=356a19 group=b6589f effects=a6e44a icon=2fe3b0 applied_by=cab7e1 -->
|  |  |
|---|---|
|  | ![Hunting Eye: Reduced armor](wiki/assets/buffs/20206.png) |
| **Buff id** | `20206` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 33 |

### Tooltip

> Hunting Eye: Reduced armor

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 20,216 ([[wiki/skills/20216-hunting-eye\|Hunting Eye]]) |

### Applied by

- Skill [[wiki/skills/20215-hunting-eye|Hunting Eye]], effect slot 1 (type 303, rate 100%)
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

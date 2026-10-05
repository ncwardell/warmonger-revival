---
title: "Transfers 5% points of Mana into Ability Power"
type: "buff"
id: 10006
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10006"]
name_key: "SkillBuff_10006"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 2, "stat": "Ability Power", "value": 0}
  - {"code": 133, "stat": "Mana(%)", "value": 5}
icon: {"file": "Items_05.png", "index": 3}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=ff82ab type=6143a1 id=e86188 sources=16695c name_key=35e3bc duration=6c141f is_buff=b6589f stack_type=356a19 group=b6589f effects=7a8f30 icon=695d02 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Transfers 5% points of Mana into Ability Power](../assets/buffs/10006.png) |
| **Buff id** | `10006` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_05.png` cell 3 |

### Tooltip

> Transfers 5% points of Mana into Ability Power

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 2 | Ability Power | 0 |
| 133 | Mana(%) | 5 |

### Applied by

- Nation policy 7 `PolicyName_7` (Policy.cdb, server-only; buff_or_skill)
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

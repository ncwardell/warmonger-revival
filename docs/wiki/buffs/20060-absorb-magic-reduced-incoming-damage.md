---
title: "Absorb Magic : Reduced incoming damage."
type: "buff"
id: 20060
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20060"]
name_key: "SkillBuff_10236"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 41, "stat": "Life Steal(%)", "value": 30}
icon: {"file": "Skill_Boss_01.dds", "index": 6}
applied_by:
  - {"skill": 20059, "slot": 1, "type": 303, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=1ad06a type=6143a1 id=103caf sources=1d425a name_key=c8cfbe duration=6c141f is_buff=b6589f stack_type=356a19 group=b6589f effects=0ec3a9 icon=26a405 applied_by=418822 -->
|  |  |
|---|---|
|  | ![Absorb Magic : Reduced incoming damage.](../assets/buffs/20060.png) |
| **Buff id** | `20060` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 6 |

### Tooltip

> Absorb Magic : Reduced incoming damage.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 41 | Life Steal(%) | 30 |

### Applied by

- Skill [[wiki/skills/20059-absorbing-magic|Absorbing Magic]], effect slot 1 (type 303, rate 100%)
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

---
title: "Petrification : Stunned for 2 seconds"
type: "buff"
id: 10214
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10214", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10214"
duration: {"ticks": 10, "seconds": 2.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 8
effects:
  - {"code": 360, "stat": "code 360 (unknown)", "value": 144}
  - {"code": 410, "stat": "code 410 (unknown)", "value": 10229}
icon: {"file": "Skill_Einsel_01.png", "index": 33}
applied_by:
  - {"skill": 5180, "slot": 1, "type": 314, "rate": 100}
  - {"skill": 5474, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=be85bb type=6143a1 id=d895f7 sources=b245bf name_key=0716d7 duration=2a0b1e is_buff=b6589f stack_type=356a19 group=fe5dbb effects=1b93c6 icon=072780 applied_by=329fec -->
|  |  |
|---|---|
|  | ![Petrification : Stunned for 2 seconds](../assets/buffs/10214.png) |
| **Buff id** | `10214` |
| **Duration** | 2 s (10 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 8 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 33 |

### Tooltip

> Petrification : Stunned for 2 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 360 | code 360 (unknown) | 144 |
| 410 | code 410 (unknown) | 10,229 |

### Applied by

- Skill [[wiki/skills/5180-petrification|Petrification]], effect slot 1 (type 314, rate 100%)
- Skill [[wiki/skills/5474-petrification|Petrification]], effect slot 1 (type 314, rate 100%)
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

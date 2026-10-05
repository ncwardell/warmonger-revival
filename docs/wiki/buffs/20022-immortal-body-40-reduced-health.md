---
title: "Immortal Body : 40% reduced Health"
type: "buff"
id: 20022
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20022", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10226"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 410, "stat": "code 410 (unknown)", "value": 20020}
  - {"code": 131, "stat": "Health(%)", "value": -40}
icon: {"file": "Policy.png", "index": 37}
applied_by:
  - {"skill": 20000, "slot": 3, "type": 300, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=73dfec type=6143a1 id=59c526 sources=7590ec name_key=059271 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=fa85b0 icon=30f6b2 applied_by=c2ef5d -->
|  |  |
|---|---|
|  | ![Immortal Body : 40% reduced Health](../assets/buffs/20022.png) |
| **Buff id** | `20022` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 37 |

### Tooltip

> Immortal Body : 40% reduced Health

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 410 | code 410 (unknown) | 20,020 |
| 131 | Health(%) | -40 |

### Applied by

- Skill [[wiki/skills/20000-dark-knight-skull-passive|Dark Knight Skull Passive]], effect slot 3 (type 300, rate 100%)
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

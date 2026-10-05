---
title: "Immortal Body : Recovering for 300 seconds"
type: "buff"
id: 20020
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20020", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10224"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 410, "stat": "code 410 (unknown)", "value": 20023}
icon: {"file": "Policy.png", "index": 37}
applied_by:
  - {"skill": 20000, "slot": 1, "type": 300, "rate": 100}
  - {"skill": 20001, "slot": 2, "type": 301, "rate": 100}
  - {"skill": 20049, "slot": 2, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=9db209 type=6143a1 id=ef5cf4 sources=97ce4c name_key=89abf9 duration=995f11 is_buff=b6589f stack_type=356a19 group=b6589f effects=60497a icon=30f6b2 applied_by=db6241 -->
|  |  |
|---|---|
|  | ![Immortal Body : Recovering for 300 seconds](../assets/buffs/20020.png) |
| **Buff id** | `20020` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 37 |

### Tooltip

> Immortal Body : Recovering for 300 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 410 | code 410 (unknown) | 20,023 |

### Applied by

- Skill [[wiki/skills/20000-dark-knight-skull-passive|Dark Knight Skull Passive]], effect slot 1 (type 300, rate 100%)
- Skill [[wiki/skills/20001-dark-knight-skull-transformation|Dark Knight Skull Transformation]], effect slot 2 (type 301, rate 100%)
- Skill [[wiki/skills/20049-dark-knight-skull-transformation|Dark Knight Skull Transformation]], effect slot 2 (type 301, rate 100%)
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

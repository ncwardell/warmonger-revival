---
title: "Non-Aggression"
type: "buff"
id: 10132
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10132", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10132"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 17, "stat": "code 17 (unknown)", "value": 100}
icon: {"file": "Items_02.png", "index": 8}
applied_by:
  - {"skill": 508, "slot": 2, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=06fd89 type=6143a1 id=52fe14 sources=74500a name_key=e3b787 duration=0aac5a is_buff=b6589f stack_type=356a19 group=b6589f effects=48390e icon=871e53 applied_by=af2f12 -->
|  |  |
|---|---|
|  | ![Non-Aggression](wiki/assets/buffs/10132.png) |
| **Buff id** | `10132` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_02.png` cell 8 |

### Tooltip

> Non-Aggression

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 17 | code 17 (unknown) | 100 |

### Applied by

- Skill [[wiki/skills/508-non-aggression|Non-Aggression]], effect slot 2 (type 301, rate 100%)
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

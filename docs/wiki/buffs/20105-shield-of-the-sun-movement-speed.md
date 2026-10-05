---
title: "Shield of the Sun : Movement Speed"
type: "buff"
id: 20105
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20105", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20105"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 117, "stat": "code 117 (unknown)", "value": 30}
icon: {"file": "Skill_Boss_01.dds", "index": 18}
applied_by:
  - {"skill": 20108, "slot": 2, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=d2695d type=6143a1 id=ed6429 sources=3f5668 name_key=433f96 duration=0aac5a is_buff=b6589f stack_type=356a19 group=b6589f effects=53926e icon=7bf15f applied_by=52e753 -->
|  |  |
|---|---|
|  | ![Shield of the Sun : Movement Speed](wiki/assets/buffs/20105.png) |
| **Buff id** | `20105` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 18 |

### Tooltip

> Shield of the Sun : Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 117 | code 117 (unknown) | 30 |

### Applied by

- Skill [[wiki/skills/20108-shield-of-the-sun|Shield of the Sun]], effect slot 2 (type 301, rate 100%)
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

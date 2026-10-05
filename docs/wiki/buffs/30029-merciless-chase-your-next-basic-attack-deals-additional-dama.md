---
title: "Merciless Chase : Your next basic attack deals additional damage"
type: "buff"
id: 30029
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30029", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10029"
duration: {"ticks": 30, "seconds": 6.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 10031}
icon: {"file": "Skill_Miriam_01.png", "index": 0}
applied_by:
  - {"skill": 10031, "slot": 4, "type": 302, "rate": 100}
  - {"skill": 10032, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=e7a5dc type=6143a1 id=ddb0c2 sources=88d10a name_key=603eb9 duration=5d0a7b is_buff=b6589f stack_type=356a19 group=b6589f effects=29228d icon=bfcc89 applied_by=315c5e -->
|  |  |
|---|---|
|  | ![Merciless Chase : Your next basic attack deals additional damage](../assets/buffs/30029.png) |
| **Buff id** | `30029` |
| **Duration** | 6 s (30 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 0 |

### Tooltip

> Merciless Chase : Your next basic attack deals additional damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 10,031 ([[wiki/skills/10031-merciless-chaser\|Merciless Chaser]]) |

### Applied by

- Skill [[wiki/skills/10031-merciless-chaser|Merciless Chaser]], effect slot 4 (type 302, rate 100%)
- Skill [[wiki/skills/10032-merciless-chaser|Merciless Chaser]], effect slot 1 (type 301, rate 100%)
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

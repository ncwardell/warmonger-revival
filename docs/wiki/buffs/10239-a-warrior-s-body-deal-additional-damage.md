---
title: "A Warrior's Body. Deal additional damage."
type: "buff"
id: 10239
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10239", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10239"
duration: {"ticks": 35, "seconds": 7.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 5197}
icon: {"file": "Skill_Boss_01.dds", "index": 2}
applied_by:
  - {"skill": 5196, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=d57dc5 type=6143a1 id=92d379 sources=3244d7 name_key=4b8027 duration=bdf5bf is_buff=b6589f stack_type=356a19 group=b6589f effects=fd7001 icon=1a93f3 applied_by=348087 -->
|  |  |
|---|---|
|  | ![A Warrior's Body. Deal additional damage.](wiki/assets/buffs/10239.png) |
| **Buff id** | `10239` |
| **Duration** | 7 s (35 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 2 |

### Tooltip

> A Warrior's Body. Deal additional damage.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 5,197 ([[wiki/skills/5197-a-warrior-s-body\|A Warrior's Body]]) |

### Applied by

- Skill [[wiki/skills/5196-a-warrior-s-body|A Warrior's Body]], effect slot 1 (type 301, rate 100%)
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

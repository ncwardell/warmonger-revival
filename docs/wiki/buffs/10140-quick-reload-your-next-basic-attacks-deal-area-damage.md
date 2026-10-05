---
title: "Quick Reload : Your next basic Attacks deal area damage"
type: "buff"
id: 10140
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10140", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10140"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 5124}
icon: {"file": "Skill_Einsel_01.png", "index": 17}
applied_by:
  - {"skill": 5103, "slot": 2, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=c31d97 type=6143a1 id=6b3f8d sources=048327 name_key=ada59b duration=3d2da5 is_buff=b6589f stack_type=356a19 group=b6589f effects=0d568c icon=7c2320 applied_by=1eedec -->
|  |  |
|---|---|
|  | ![Quick Reload : Your next basic Attacks deal area damage](../assets/buffs/10140.png) |
| **Buff id** | `10140` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 17 |

### Tooltip

> Quick Reload : Your next basic Attacks deal area damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 5,124 ([[wiki/skills/5124-soul-infestation-you-deal-additional-damage\|Soul Infestation : You deal additional damage]]) |

### Applied by

- Skill [[wiki/skills/5103-rapid-reload|Rapid Reload]], effect slot 2 (type 301, rate 100%)
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

---
title: "Poisonous Blade : Next Attack Stunned"
type: "buff"
id: 10341
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10341", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10341"
duration: {"ticks": 30, "seconds": 6.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 5288}
icon: {"file": "Skill_Miriam_01.png", "index": 24}
applied_by:
  - {"skill": 5287, "slot": 1, "type": 301, "rate": 100}
  - {"skill": 5288, "slot": 4, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=24b1c1 type=6143a1 id=209e7e sources=ec401b name_key=c58ac0 duration=5d0a7b is_buff=b6589f stack_type=356a19 group=b6589f effects=964648 icon=78290d applied_by=b12bf2 -->
|  |  |
|---|---|
|  | ![Poisonous Blade : Next Attack Stunned](../assets/buffs/10341.png) |
| **Buff id** | `10341` |
| **Duration** | 6 s (30 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 24 |

### Tooltip

> Poisonous Blade : Next Attack Stunned

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 5,288 ([[wiki/skills/5288-poisonous-blade-active\|Poisonous Blade : Active]]) |

### Applied by

- Skill [[wiki/skills/5287-poisonous-blade|Poisonous Blade]], effect slot 1 (type 301, rate 100%)
- Skill [[wiki/skills/5288-poisonous-blade-active|Poisonous Blade : Active]], effect slot 4 (type 302, rate 100%)
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

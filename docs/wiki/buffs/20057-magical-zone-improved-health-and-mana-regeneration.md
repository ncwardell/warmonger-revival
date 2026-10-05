---
title: "Magical Zone : Improved Health and Mana Regeneration."
type: "buff"
id: 20057
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20057", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10233"
duration: {"ticks": 5, "seconds": 1.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 6}
  - {"code": 34, "stat": "Mana Regeneration", "value": 6}
icon: {"file": "Skill_Boss_01.dds", "index": 4}
applied_by:
  - {"skill": 20057, "slot": 2, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=d8794f type=6143a1 id=189133 sources=98f8df name_key=15a273 duration=76674f is_buff=b6589f stack_type=356a19 group=b6589f effects=b7cd16 icon=d93629 applied_by=e1187e -->
|  |  |
|---|---|
|  | ![Magical Zone : Improved Health and Mana Regeneration.](../assets/buffs/20057.png) |
| **Buff id** | `20057` |
| **Duration** | 1 s (5 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 4 |

### Tooltip

> Magical Zone : Improved Health and Mana Regeneration.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 6 |
| 34 | Mana Regeneration | 6 |

### Applied by

- Skill [[wiki/skills/20057-magical-zone|Magical Zone]], effect slot 2 (type 314, rate 100%)
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

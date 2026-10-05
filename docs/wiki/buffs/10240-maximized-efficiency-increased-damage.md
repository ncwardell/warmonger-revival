---
title: "Maximized Efficiency: Increased Damage."
type: "buff"
id: 10240
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10240", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10240"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 405, "stat": "code 405 (unknown)", "value": 5}
  - {"code": 101, "stat": "Attack(%)", "value": 10}
icon: {"file": "Skill_Boss_01.dds", "index": 1}
applied_by:
  - {"skill": 5198, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=f499bc type=6143a1 id=d95668 sources=ac231c name_key=cd8992 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=67a7d3 icon=875e75 applied_by=2f1aae -->
|  |  |
|---|---|
|  | ![Maximized Efficiency: Increased Damage.](../assets/buffs/10240.png) |
| **Buff id** | `10240` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 1 |

### Tooltip

> Maximized Efficiency: Increased Damage.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 405 | code 405 (unknown) | 5 |
| 101 | Attack(%) | 10 |

### Applied by

- Skill [[wiki/skills/5198-maximized-efficiency|Maximized Efficiency]], effect slot 1 (type 301, rate 100%)
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

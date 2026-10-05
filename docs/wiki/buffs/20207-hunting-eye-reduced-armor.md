---
title: "Hunting Eye: Reduced armor"
type: "buff"
id: 20207
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20207", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20207"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 405, "stat": "code 405 (unknown)", "value": 5}
  - {"code": 106, "stat": "Armor(%)", "value": -4}
icon: {"file": "Skill_Boss_01.dds", "index": 33}
applied_by:
  - {"skill": 20216, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=cbbc74 type=6143a1 id=2a6042 sources=69585a name_key=4b6ae9 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=a97a10 icon=2fe3b0 applied_by=4d871d -->
|  |  |
|---|---|
|  | ![Hunting Eye: Reduced armor](wiki/assets/buffs/20207.png) |
| **Buff id** | `20207` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 33 |

### Tooltip

> Hunting Eye: Reduced armor

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 405 | code 405 (unknown) | 5 |
| 106 | Armor(%) | -4 |

### Applied by

- Skill [[wiki/skills/20216-hunting-eye|Hunting Eye]], effect slot 3 (type 314, rate 100%)
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

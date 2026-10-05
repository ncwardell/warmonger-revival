---
title: "Crystal Burst : Reduced Armor and Magic Resistance"
type: "buff"
id: 10019
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10019", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10019"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 106, "stat": "Armor(%)", "value": -20}
  - {"code": 107, "stat": "Magic Resist(%)", "value": -20}
icon: {"file": "Skill_Einsel_01.png", "index": 14}
applied_by:
  - {"skill": 5016, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=a1a85e type=6143a1 id=8492e1 sources=0bcfd9 name_key=14190c duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=f8da5d icon=baee3b applied_by=c7a63f -->
|  |  |
|---|---|
|  | ![Crystal Burst : Reduced Armor and Magic Resistance](../assets/buffs/10019.png) |
| **Buff id** | `10019` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 14 |

### Tooltip

> Crystal Burst : Reduced Armor and Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 106 | Armor(%) | -20 |
| 107 | Magic Resist(%) | -20 |

### Applied by

- Skill [[wiki/skills/5016-crystal-nova|Crystal Nova]], effect slot 3 (type 314, rate 100%)
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

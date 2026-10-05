---
title: "Lightning spray : Reduced Armor and Magic Resistance, Movement speed"
type: "buff"
id: 10432
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10432", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10432"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
  - {"code": 106, "stat": "Armor(%)", "value": -30}
  - {"code": 107, "stat": "Magic Resist(%)", "value": -30}
icon: {"file": "Policy.png", "index": 33}
applied_by:
  - {"skill": 5482, "slot": 4, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=f830da type=6143a1 id=104bc1 sources=91eace name_key=94cdda duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=f4309d icon=0392b4 applied_by=b25960 -->
|  |  |
|---|---|
|  | ![Lightning spray : Reduced Armor and Magic Resistance, Movement speed](wiki/assets/buffs/10432.png) |
| **Buff id** | `10432` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 33 |

### Tooltip

> Lightning spray : Reduced Armor and Magic Resistance, Movement speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -30 |
| 106 | Armor(%) | -30 |
| 107 | Magic Resist(%) | -30 |

### Applied by

- Skill [[wiki/skills/5482|Skill 5482]], effect slot 4 (type 314, rate 100%)
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

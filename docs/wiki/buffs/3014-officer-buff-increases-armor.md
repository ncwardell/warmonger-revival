---
title: "Officer Buff: Increases Armor"
type: "buff"
id: 3014
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 3014", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_3014"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 106, "stat": "Armor(%)", "value": 30}
icon: {"file": "Mastery_01.png", "index": 13}
applied_by:
  - {"skill": 3013, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=0d6d40 type=6143a1 id=e11c34 sources=874694 name_key=69a9ae duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=fe0162 icon=e1413d applied_by=9a19c0 -->
|  |  |
|---|---|
|  | ![Officer Buff: Increases Armor](wiki/assets/buffs/3014.png) |
| **Buff id** | `3014` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Mastery_01.png` cell 13 |

### Tooltip

> Officer Buff: Increases Armor

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 106 | Armor(%) | 30 |

### Applied by

- Skill [[wiki/skills/3013|Skill 3013]], effect slot 1 (type 314, rate 100%)
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

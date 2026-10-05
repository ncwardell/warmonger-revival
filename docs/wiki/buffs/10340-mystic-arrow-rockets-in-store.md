---
title: "Mystic Arrow : Rockets in store"
type: "buff"
id: 10340
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10340", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10340"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10340
effects:
  - {"code": 403, "stat": "basic attack override", "value": 2}
icon: {"file": "Skill_Miriam_01.png", "index": 8}
applied_by:
  - {"skill": 5283, "slot": 4, "type": 307, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=f7e476 type=6143a1 id=11b25b sources=4a89ae name_key=dea928 duration=870e64 is_buff=b6589f stack_type=356a19 group=11b25b effects=5e87a3 icon=a11afc applied_by=fd58ec -->
|  |  |
|---|---|
|  | ![Mystic Arrow : Rockets in store](../assets/buffs/10340.png) |
| **Buff id** | `10340` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10340 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 8 |

### Tooltip

> Mystic Arrow : Rockets in store

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 403 | basic attack override | 2 ([[wiki/skills/2\|Skill 2]]) |

### Applied by

- Skill [[wiki/skills/5283-mystic-arrow|Mystic Arrow]], effect slot 4 (type 307, rate 100%)
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

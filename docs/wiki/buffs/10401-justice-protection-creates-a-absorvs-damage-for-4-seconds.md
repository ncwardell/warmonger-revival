---
title: "Justice Protection : Creates a absorvs damage for 4 seconds"
type: "buff"
id: 10401
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10401", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10401"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10401
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 200}
  - {"code": 131, "stat": "Health(%)", "value": 15}
icon: {"file": "Skill_Dolorece_01.png", "index": 34}
applied_by:
  - {"skill": 5352, "slot": 1, "type": 308, "rate": 100}
  - {"skill": 5352, "slot": 2, "type": 317, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=aade1c type=6143a1 id=a73f20 sources=18b072 name_key=405ecb duration=3d2da5 is_buff=b6589f stack_type=356a19 group=a73f20 effects=9ff02c icon=e85470 applied_by=0f745f -->
|  |  |
|---|---|
|  | ![Justice Protection : Creates a absorvs damage for 4 seconds](../assets/buffs/10401.png) |
| **Buff id** | `10401` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10401 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 34 |

### Tooltip

> Justice Protection : Creates a absorvs damage for 4 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 200 |
| 131 | Health(%) | 15 |

### Applied by

- Skill [[wiki/skills/5352-protection-of-justice|Protection of Justice]], effect slot 1 (type 308, rate 100%)
- Skill [[wiki/skills/5352-protection-of-justice|Protection of Justice]], effect slot 2 (type 317, rate 100%)
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

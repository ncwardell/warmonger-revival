---
title: "Battle Cry: Increases HP Regeneration"
type: "buff"
id: 30002
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30002", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10002"
duration: {"ticks": 80, "seconds": 16.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10002
effects:
  - {"code": 132, "stat": "Health Regeneration(%)", "value": 20}
icon: {"file": "Skill_Dolorece_01.png", "index": 1}
applied_by:
  - {"skill": 10001, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=7bce23 type=6143a1 id=1aa3a2 sources=7500d7 name_key=e70407 duration=fba78d is_buff=b6589f stack_type=356a19 group=6918d3 effects=6914b3 icon=2a2087 applied_by=68470e -->
|  |  |
|---|---|
|  | ![Battle Cry: Increases HP Regeneration](wiki/assets/buffs/30002.png) |
| **Buff id** | `30002` |
| **Duration** | 16 s (80 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10002 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 1 |

### Tooltip

> Battle Cry: Increases HP Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 132 | Health Regeneration(%) | 20 |

### Applied by

- Skill [[wiki/skills/10001-battle-cry|Battle Cry]], effect slot 1 (type 314, rate 100%)
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

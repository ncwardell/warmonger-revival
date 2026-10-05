---
title: "Lava Ogre : Attack damage, Ability Power +10%"
type: "buff"
id: 3112
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 3112", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_3112"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 101, "stat": "Attack(%)", "value": 10}
  - {"code": 102, "stat": "Ability Power(%)", "value": 10}
icon: {"file": "Mastery_01.png", "index": 10}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=a64e00 type=6143a1 id=bba423 sources=6ca2c5 name_key=867c76 duration=995f11 is_buff=b6589f stack_type=356a19 group=b6589f effects=2b7bb6 icon=4a83a1 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Lava Ogre : Attack damage, Ability Power +10%](wiki/assets/buffs/3112.png) |
| **Buff id** | `3112` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Mastery_01.png` cell 10 |

### Tooltip

> Lava Ogre : Attack damage, Ability Power +10%

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 101 | Attack(%) | 10 |
| 102 | Ability Power(%) | 10 |
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

---
title: "Bloody anger : Increases Damage"
type: "buff"
id: 20260
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20260", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20260"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 405, "stat": "code 405 (unknown)", "value": 7}
  - {"code": 101, "stat": "Attack(%)", "value": 4}
icon: {"file": "Skill_Boss_01.dds", "index": 49}
applied_by:
  - {"skill": 20254, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=57b8ea type=6143a1 id=ca15ea sources=11884a name_key=0cc392 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=4ef473 icon=5c9a70 applied_by=0ba0c0 -->
|  |  |
|---|---|
|  | ![Bloody anger : Increases Damage](../assets/buffs/20260.png) |
| **Buff id** | `20260` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 49 |

### Tooltip

> Bloody anger : Increases Damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 405 | code 405 (unknown) | 7 |
| 101 | Attack(%) | 4 |

### Applied by

- Skill [[wiki/skills/20254-bloody-anger|Bloody anger]], effect slot 1 (type 301, rate 100%)
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

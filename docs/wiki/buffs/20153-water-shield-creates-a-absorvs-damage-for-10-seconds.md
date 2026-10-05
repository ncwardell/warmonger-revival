---
title: "Water shield : Creates a absorvs damage for 10 seconds"
type: "buff"
id: 20153
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20153", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20153"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 20153
effects:
  - {"code": 405, "stat": "code 405 (unknown)", "value": 10}
  - {"code": 441, "stat": "code 441 (unknown)", "value": 150}
  - {"code": 101, "stat": "Attack(%)", "value": 20}
icon: {"file": "Skill_Boss_01.dds", "index": 24}
applied_by:
  - {"skill": 20153, "slot": 1, "type": 308, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=78f3d3 type=6143a1 id=151704 sources=3217dd name_key=bf4077 duration=6c749d is_buff=b6589f stack_type=356a19 group=151704 effects=01abaf icon=13fce1 applied_by=f9a6f1 -->
|  |  |
|---|---|
|  | ![Water shield : Creates a absorvs damage for 10 seconds](wiki/assets/buffs/20153.png) |
| **Buff id** | `20153` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 20153 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 24 |

### Tooltip

> Water shield : Creates a absorvs damage for 10 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 405 | code 405 (unknown) | 10 |
| 441 | code 441 (unknown) | 150 |
| 101 | Attack(%) | 20 |

### Applied by

- Skill [[wiki/skills/20153-water-shield|Water shield]], effect slot 1 (type 308, rate 100%)
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

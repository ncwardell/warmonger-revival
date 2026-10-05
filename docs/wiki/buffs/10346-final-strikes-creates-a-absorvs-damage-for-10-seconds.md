---
title: "Final Strikes : Creates a absorvs damage for 10 seconds"
type: "buff"
id: 10346
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10346", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10346"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 3
group: 10346
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 300}
  - {"code": 101, "stat": "Attack(%)", "value": 10}
icon: {"file": "Skill_Miriam_01.png", "index": 27}
applied_by:
  - {"skill": 5291, "slot": 3, "type": 308, "rate": 100}
  - {"skill": 5292, "slot": 4, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=5a107a type=6143a1 id=23ae30 sources=503cef name_key=c4516f duration=6c749d is_buff=b6589f stack_type=77de68 group=23ae30 effects=816ad5 icon=b1d574 applied_by=781db0 -->
|  |  |
|---|---|
|  | ![Final Strikes : Creates a absorvs damage for 10 seconds](../assets/buffs/10346.png) |
| **Buff id** | `10346` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 3 (guessed column) |
| **Group** | 10346 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 27 |

### Tooltip

> Final Strikes : Creates a absorvs damage for 10 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 300 |
| 101 | Attack(%) | 10 |

### Applied by

- Skill [[wiki/skills/5291-final-strike|Final Strike]], effect slot 3 (type 308, rate 100%)
- Skill [[wiki/skills/5292-final-strike-silence|Final Strike : Silence]], effect slot 4 (type 302, rate 100%)
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

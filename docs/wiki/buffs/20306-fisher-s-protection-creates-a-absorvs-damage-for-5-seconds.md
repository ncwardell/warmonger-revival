---
title: "Fisher's Protection : Creates a absorvs damage for 5 seconds"
type: "buff"
id: 20306
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20306", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20306"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 20306
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 200}
  - {"code": 133, "stat": "Mana(%)", "value": 5}
icon: {"file": "Skill_Boss_01.dds", "index": 43}
applied_by:
  - {"skill": 20307, "slot": 1, "type": 317, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=af1f25 type=6143a1 id=e9e67b sources=cb0b70 name_key=33dae8 duration=870e64 is_buff=b6589f stack_type=356a19 group=e9e67b effects=309ea8 icon=50b6e5 applied_by=471852 -->
|  |  |
|---|---|
|  | ![Fisher's Protection : Creates a absorvs damage for 5 seconds](wiki/assets/buffs/20306.png) |
| **Buff id** | `20306` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 20306 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 43 |

### Tooltip

> Fisher's Protection : Creates a absorvs damage for 5 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 200 |
| 133 | Mana(%) | 5 |

### Applied by

- Skill [[wiki/skills/20307-fisher-s-protection|Fisher's Protection]], effect slot 1 (type 317, rate 100%)
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

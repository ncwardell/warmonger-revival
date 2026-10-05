---
title: "Fisher's cries : Creates a absorvs damage for 5 seconds"
type: "buff"
id: 20308
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20308", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20308"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 20308
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 200}
  - {"code": 134, "stat": "Mana Regeneration(%)", "value": 20}
icon: {"file": "Skill_Boss_01.dds", "index": 46}
applied_by:
  - {"skill": 20310, "slot": 1, "type": 317, "rate": 100}
  - {"skill": 20310, "slot": 2, "type": 308, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=9b4260 type=6143a1 id=557425 sources=8df00e name_key=cdd1d1 duration=870e64 is_buff=b6589f stack_type=356a19 group=557425 effects=1b7b3a icon=f9031f applied_by=f7b9e9 -->
|  |  |
|---|---|
|  | ![Fisher's cries : Creates a absorvs damage for 5 seconds](../assets/buffs/20308.png) |
| **Buff id** | `20308` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 20308 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 46 |

### Tooltip

> Fisher's cries : Creates a absorvs damage for 5 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 200 |
| 134 | Mana Regeneration(%) | 20 |

### Applied by

- Skill [[wiki/skills/20310-fisher-s-cries|Fisher's cries]], effect slot 1 (type 317, rate 100%)
- Skill [[wiki/skills/20310-fisher-s-cries|Fisher's cries]], effect slot 2 (type 308, rate 100%)
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

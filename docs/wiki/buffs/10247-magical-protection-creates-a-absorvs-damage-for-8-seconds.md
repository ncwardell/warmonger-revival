---
title: "Magical Protection : Creates a absorvs damage for 8 seconds"
type: "buff"
id: 10247
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10247", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10247"
duration: {"ticks": 40, "seconds": 8.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10247
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 1000}
  - {"code": 101, "stat": "Attack(%)", "value": 10}
  - {"code": 410, "stat": "code 410 (unknown)", "value": 10248}
icon: {"file": "Policy.png", "index": 34}
applied_by:
  - {"skill": 5204, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=1e409a type=6143a1 id=9b6d18 sources=6f812a name_key=ab4c8e duration=8c4b49 is_buff=b6589f stack_type=356a19 group=9b6d18 effects=8b8710 icon=9835a6 applied_by=527587 -->
|  |  |
|---|---|
|  | ![Magical Protection : Creates a absorvs damage for 8 seconds](../assets/buffs/10247.png) |
| **Buff id** | `10247` |
| **Duration** | 8 s (40 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10247 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy.png` cell 34 |

### Tooltip

> Magical Protection : Creates a absorvs damage for 8 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 1,000 |
| 101 | Attack(%) | 10 |
| 410 | code 410 (unknown) | 10,248 |

### Applied by

- Skill [[wiki/skills/5204|Skill 5204]], effect slot 1 (type 314, rate 100%)
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

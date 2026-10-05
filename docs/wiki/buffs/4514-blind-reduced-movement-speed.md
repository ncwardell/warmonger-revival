---
title: "Blind : Reduced Movement Speed."
type: "buff"
id: 4514
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 4514", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10280"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Policy_01.png", "index": 36}
applied_by:
  - {"skill": 4515, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=2375b1 type=6143a1 id=5663c4 sources=ad9f12 name_key=88fdb2 duration=3d2da5 is_buff=b6589f stack_type=356a19 group=e3cbba effects=732c70 icon=494d30 applied_by=eb646e -->
|  |  |
|---|---|
|  | ![Blind : Reduced Movement Speed.](wiki/assets/buffs/4514.png) |
| **Buff id** | `4514` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy_01.png` cell 36 |

### Tooltip

> Blind : Reduced Movement Speed.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/4515-blind-attack|Blind Attack]], effect slot 1 (type 314, rate 100%)
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

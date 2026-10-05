---
title: "Curse Explosion : Reduced Movement Speed"
type: "buff"
id: 10205
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10205", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10205"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Skill_Dolorece_01.png", "index": 27}
applied_by:
  - {"skill": 3026, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=31a193 type=6143a1 id=1219a5 sources=dcf31a name_key=c9efdf duration=3d2da5 is_buff=b6589f stack_type=356a19 group=e3cbba effects=732c70 icon=f19f25 applied_by=451134 -->
|  |  |
|---|---|
|  | ![Curse Explosion : Reduced Movement Speed](../assets/buffs/10205.png) |
| **Buff id** | `10205` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 27 |

### Tooltip

> Curse Explosion : Reduced Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/3026|Skill 3026]], effect slot 3 (type 314, rate 100%)
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

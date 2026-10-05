---
title: "Tomb of the Dead : Reduced Movement Speed"
type: "buff"
id: 10221
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10221", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10221"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -20}
icon: {"file": "Policy.png", "index": 42}
applied_by:
  - {"skill": 5187, "slot": 2, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=e3ee6e type=6143a1 id=fadefc sources=444981 name_key=cdb496 duration=0aac5a is_buff=b6589f stack_type=356a19 group=e3cbba effects=a1bf0d icon=5cb950 applied_by=6aa088 -->
|  |  |
|---|---|
|  | ![Tomb of the Dead : Reduced Movement Speed](wiki/assets/buffs/10221.png) |
| **Buff id** | `10221` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy.png` cell 42 |

### Tooltip

> Tomb of the Dead : Reduced Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -20 |

### Applied by

- Skill [[wiki/skills/5187-tomb-of-the-dead|Tomb of the Dead]], effect slot 2 (type 314, rate 100%)
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

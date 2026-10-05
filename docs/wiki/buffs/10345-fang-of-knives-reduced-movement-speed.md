---
title: "Fang of Knives : Reduced Movement Speed"
type: "buff"
id: 10345
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10345", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10345"
duration: {"ticks": 10, "seconds": 2.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -20}
icon: {"file": "Skill_Miriam_01.png", "index": 26}
applied_by:
  - {"skill": 5290, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=7ccea0 type=6143a1 id=681e3e sources=cb59d7 name_key=17b360 duration=2a0b1e is_buff=b6589f stack_type=356a19 group=e3cbba effects=a1bf0d icon=5f1bf5 applied_by=8edf79 -->
|  |  |
|---|---|
|  | ![Fang of Knives : Reduced Movement Speed](wiki/assets/buffs/10345.png) |
| **Buff id** | `10345` |
| **Duration** | 2 s (10 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 26 |

### Tooltip

> Fang of Knives : Reduced Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -20 |

### Applied by

- Skill [[wiki/skills/5290-fang-of-knives|Fang of Knives]], effect slot 3 (type 314, rate 100%)
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

---
title: "Mark of Death : Reduced Armor"
type: "buff"
id: 30042
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30042", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10042"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10042
effects:
  - {"code": 106, "stat": "Armor(%)", "value": -20}
icon: {"file": "Skill_Miriam_01.png", "index": 6}
applied_by:
  - {"skill": 10046, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=82f746 type=6143a1 id=67727e sources=0c79c4 name_key=88a1d2 duration=6c749d is_buff=b6589f stack_type=356a19 group=22cdd7 effects=656ee4 icon=c3bc1a applied_by=0d663c -->
|  |  |
|---|---|
|  | ![Mark of Death : Reduced Armor](../assets/buffs/30042.png) |
| **Buff id** | `30042` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10042 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 6 |

### Tooltip

> Mark of Death : Reduced Armor

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 106 | Armor(%) | -20 |

### Applied by

- Skill [[wiki/skills/10046-mark-of-death|Mark of Death]], effect slot 1 (type 314, rate 100%)
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

---
title: "Wave of Crystals : Reduced Movement Speed"
type: "buff"
id: 10020
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10020", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10020"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1009
effects:
  - {"code": 19, "stat": "code 19 (unknown)", "value": -150}
icon: {"file": "Skill_Einsel_01.png", "index": 15}
applied_by:
  - {"skill": 5017, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=a284b5 type=6143a1 id=122673 sources=0fd88c name_key=f965f9 duration=3d2da5 is_buff=b6589f stack_type=356a19 group=ab68fc effects=f8a4f8 icon=29c012 applied_by=325125 -->
|  |  |
|---|---|
|  | ![Wave of Crystals : Reduced Movement Speed](../assets/buffs/10020.png) |
| **Buff id** | `10020` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1009 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 15 |

### Tooltip

> Wave of Crystals : Reduced Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 19 | code 19 (unknown) | -150 |

### Applied by

- Skill [[wiki/skills/5017-crystal-wave|Crystal Wave]], effect slot 3 (type 314, rate 100%)
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

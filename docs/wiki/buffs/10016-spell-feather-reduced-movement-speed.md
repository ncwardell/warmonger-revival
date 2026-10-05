---
title: "Spell Feather : Reduced Movement Speed"
type: "buff"
id: 10016
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10016", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10016"
duration: {"ticks": 10, "seconds": 2.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1009
effects:
  - {"code": 19, "stat": "code 19 (unknown)", "value": -90}
icon: {"file": "Skill_Einsel_01.png", "index": 12}
applied_by:
  - {"skill": 5014, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=f839ce type=6143a1 id=d5483a sources=d95a12 name_key=aaf4ca duration=2a0b1e is_buff=b6589f stack_type=356a19 group=ab68fc effects=289dcd icon=31f51a applied_by=384798 -->
|  |  |
|---|---|
|  | ![Spell Feather : Reduced Movement Speed](wiki/assets/buffs/10016.png) |
| **Buff id** | `10016` |
| **Duration** | 2 s (10 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1009 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 12 |

### Tooltip

> Spell Feather : Reduced Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 19 | code 19 (unknown) | -90 |

### Applied by

- Skill [[wiki/skills/5014-spell-feather|Spell Feather]], effect slot 3 (type 314, rate 100%)
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

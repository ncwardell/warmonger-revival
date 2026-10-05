---
title: "Indiscriminate Launch: Rockets available in the Store"
type: "buff"
id: 10161
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10161", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10161"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10161
effects:
  - {"code": 403, "stat": "basic attack override", "value": 7}
icon: {"file": "Skill_Dolorece_01.png", "index": 31}
applied_by:
  - {"skill": 5137, "slot": 3, "type": 307, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=cb1ba9 type=6143a1 id=18584a sources=a80142 name_key=18dd47 duration=6c749d is_buff=b6589f stack_type=356a19 group=18584a effects=c4647b icon=14a444 applied_by=2ad82b -->
|  |  |
|---|---|
|  | ![Indiscriminate Launch: Rockets available in the Store](../assets/buffs/10161.png) |
| **Buff id** | `10161` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10161 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 31 |

### Tooltip

> Indiscriminate Launch: Rockets available in the Store

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 403 | basic attack override | 7 |

### Applied by

- Skill [[wiki/skills/5137-wild-launch|Wild Launch]], effect slot 3 (type 307, rate 100%)
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

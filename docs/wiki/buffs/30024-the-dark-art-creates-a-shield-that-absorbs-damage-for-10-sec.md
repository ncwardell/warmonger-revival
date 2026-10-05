---
title: "The Dark Art: Creates a shield that absorbs Damage for 10 seconds."
type: "buff"
id: 30024
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30024", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10024"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 3
group: 10024
effects:
  - {"code": 441, "stat": "code 441 (unknown)", "value": 300}
  - {"code": 101, "stat": "Attack(%)", "value": 10}
icon: {"file": "Skill_Miriam_01.png", "index": 19}
applied_by:
  - {"skill": 10029, "slot": 3, "type": 308, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=b4d426 type=6143a1 id=382388 sources=4dc49c name_key=21ed86 duration=6c749d is_buff=b6589f stack_type=77de68 group=fe762c effects=816ad5 icon=fdf9b8 applied_by=4df90e -->
|  |  |
|---|---|
|  | ![The Dark Art: Creates a shield that absorbs Damage for 10 seconds.](../assets/buffs/30024.png) |
| **Buff id** | `30024` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 3 (guessed column) |
| **Group** | 10024 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 19 |

### Tooltip

> The Dark Art: Creates a shield that absorbs Damage for 10 seconds.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 441 | code 441 (unknown) | 300 |
| 101 | Attack(%) | 10 |

### Applied by

- Skill [[wiki/skills/10029-the-dark-art|The Dark Art]], effect slot 3 (type 308, rate 100%)
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

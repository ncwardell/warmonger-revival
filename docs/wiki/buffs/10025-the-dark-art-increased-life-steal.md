---
title: "The Dark Art : Increased Life Steal"
type: "buff"
id: 10025
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10025", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10025"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10025
effects:
  - {"code": 41, "stat": "Life Steal(%)", "value": 10}
icon: {"file": "Skill_Miriam_01.png", "index": 19}
applied_by:
  - {"skill": 5030, "slot": 4, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=eda016 type=6143a1 id=703386 sources=54b71c name_key=aebaac duration=6c749d is_buff=b6589f stack_type=356a19 group=703386 effects=71fb0a icon=fdf9b8 applied_by=aab33f -->
|  |  |
|---|---|
|  | ![The Dark Art : Increased Life Steal](../assets/buffs/10025.png) |
| **Buff id** | `10025` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10025 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 19 |

### Tooltip

> The Dark Art : Increased Life Steal

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 41 | Life Steal(%) | 10 |

### Applied by

- Skill [[wiki/skills/5030-the-dark-art|The Dark Art]], effect slot 4 (type 301, rate 100%)
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

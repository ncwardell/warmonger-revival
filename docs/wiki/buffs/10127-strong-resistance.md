---
title: "Strong Resistance"
type: "buff"
id: 10127
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10127", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10127"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -25}
icon: {"file": "Items_02.png", "index": 1}
applied_by:
  - {"skill": 509, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=8c7f2e type=6143a1 id=9a2a5f sources=cc8049 name_key=757e3d duration=3d2da5 is_buff=b6589f stack_type=356a19 group=e3cbba effects=07b4f1 icon=703af3 applied_by=629cfc -->
|  |  |
|---|---|
|  | ![Strong Resistance](../assets/buffs/10127.png) |
| **Buff id** | `10127` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_02.png` cell 1 |

### Tooltip

> Strong Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -25 |

### Applied by

- Skill [[wiki/skills/509-strong-resistance|Strong Resistance]], effect slot 1 (type 314, rate 100%)
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

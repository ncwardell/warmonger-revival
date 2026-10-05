---
title: "Scroll of Critical Strikes [A] : Critical Strike +15%"
type: "buff"
id: 2099
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2099", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2099"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 109, "stat": "Critical Strike +(%)", "value": 15}
icon: {"file": "Items_30.png", "index": 16}
applied_by:
  - {"item": 726}
---
<!-- generated:start -->
<!-- generated-keys: title=4964ef type=6143a1 id=b0e922 sources=d4e5ac name_key=47ac35 duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=d61ba3 icon=2410a2 applied_by=c77cc7 -->
|  |  |
|---|---|
|  | ![Scroll of Critical Strikes (A) : Critical Strike +15%](wiki/assets/buffs/2099.png) |
| **Buff id** | `2099` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 16 |

### Tooltip

> Scroll of Critical Strikes [A] : Critical Strike +15%

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 109 | Critical Strike +(%) | 15 |

### Applied by

- Using [[wiki/items/726-tome-of-critical-a|Tome of Critical (A)]] (Item_Base option 301)
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

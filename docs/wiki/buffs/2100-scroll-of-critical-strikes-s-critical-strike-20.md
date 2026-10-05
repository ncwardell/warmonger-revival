---
title: "Scroll of Critical Strikes [S] : Critical Strike +20%"
type: "buff"
id: 2100
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2100", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2100"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 109, "stat": "Critical Strike +(%)", "value": 20}
icon: {"file": "Items_30.png", "index": 20}
applied_by:
  - {"item": 727}
---
<!-- generated:start -->
<!-- generated-keys: title=bf0679 type=6143a1 id=89b98f sources=854f5b name_key=799624 duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=0e5707 icon=7f2f86 applied_by=52229f -->
|  |  |
|---|---|
|  | ![Scroll of Critical Strikes (S) : Critical Strike +20%](../assets/buffs/2100.png) |
| **Buff id** | `2100` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 20 |

### Tooltip

> Scroll of Critical Strikes [S] : Critical Strike +20%

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 109 | Critical Strike +(%) | 20 |

### Applied by

- Using [[wiki/items/727-tome-of-critical-s|Tome of Critical (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 58): Tome · Tome of Critical · 724–727 · 2097–2100 · Crit chance +5 / 10 / 15 / 20%
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 77): Tome S · Crit 20%, less AoE 20%, Cooldown 12%, Attack speed 40 · Critical Strikes +20% (2100), Reduced Area Damage 20% (2096), Cooldown Reduction 12% (2092),...
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

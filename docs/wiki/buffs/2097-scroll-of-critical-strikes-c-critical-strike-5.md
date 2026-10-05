---
title: "Scroll of Critical Strikes [C] : Critical Strike +5%"
type: "buff"
id: 2097
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2097", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2097"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 109, "stat": "Critical Strike +(%)", "value": 5}
icon: {"file": "Items_30.png", "index": 8}
applied_by:
  - {"item": 724}
---
<!-- generated:start -->
<!-- generated-keys: title=949f50 type=6143a1 id=c18430 sources=f18333 name_key=df65cb duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=d3a436 icon=beca6f applied_by=ecffb2 -->
|  |  |
|---|---|
|  | ![Scroll of Critical Strikes (C) : Critical Strike +5%](wiki/assets/buffs/2097.png) |
| **Buff id** | `2097` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 8 |

### Tooltip

> Scroll of Critical Strikes [C] : Critical Strike +5%

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 109 | Critical Strike +(%) | 5 |

### Applied by

- Using [[wiki/items/724-tome-of-critical-c|Tome of Critical (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 58): Tome · Tome of Critical · 724–727 · 2097–2100 · Crit chance +5 / 10 / 15 / 20%
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

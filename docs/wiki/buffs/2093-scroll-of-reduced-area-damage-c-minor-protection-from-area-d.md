---
title: "Scroll of Reduced Area Damage [C] : Minor protection from Area Damage."
type: "buff"
id: 2093
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2093", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2093"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 270, "stat": "Reduced Area Damage(%)", "value": 5}
icon: {"file": "Items_30.png", "index": 7}
applied_by:
  - {"item": 720}
---
<!-- generated:start -->
<!-- generated-keys: title=978bbe type=6143a1 id=3f1e66 sources=05ee41 name_key=41646d duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=da8e95 icon=dd3139 applied_by=f3f745 -->
|  |  |
|---|---|
|  | ![Scroll of Reduced Area Damage (C) : Minor protection from Area Damage.](../assets/buffs/2093.png) |
| **Buff id** | `2093` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 7 |

### Tooltip

> Scroll of Reduced Area Damage [C] : Minor protection from Area Damage.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 270 | Reduced Area Damage(%) | 5 |

### Applied by

- Using [[wiki/items/720-tome-of-patience-c|Tome of Patience (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 57): Tome · Tome of Patience · 720–723 · 2093–2096 · Area damage taken −5 / 10 / 15 / 20% (opt 270)
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

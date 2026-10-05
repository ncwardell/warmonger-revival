---
title: "Scroll of Cooldown Reduction [C] : 3% Cooldown Reduction"
type: "buff"
id: 2089
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2089", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2089"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 3}
icon: {"file": "Items_30.png", "index": 9}
applied_by:
  - {"item": 716}
---
<!-- generated:start -->
<!-- generated-keys: title=13041d type=6143a1 id=1a95ad sources=f6e41f name_key=61d023 duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=09fc3d icon=d94cf0 applied_by=8a0f71 -->
|  |  |
|---|---|
|  | ![Scroll of Cooldown Reduction (C) : 3% Cooldown Reduction](wiki/assets/buffs/2089.png) |
| **Buff id** | `2089` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 9 |

### Tooltip

> Scroll of Cooldown Reduction [C] : 3% Cooldown Reduction

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 212 | Cooldown Reduction(%) | 3 |

### Applied by

- Using [[wiki/items/716-tome-of-cooldown-c|Tome of Cooldown (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 56): Tome · Tome of Cooldown · 716–719 · 2089–2092 · Cooldown reduction 3 / 6 / 9 / 12%
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

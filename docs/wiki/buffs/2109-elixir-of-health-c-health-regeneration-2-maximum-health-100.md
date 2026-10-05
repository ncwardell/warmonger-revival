---
title: "Elixir of Health [C] : Health Regeneration +2, Maximum Health +100"
type: "buff"
id: 2109
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2109", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2109"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 2}
  - {"code": 31, "stat": "Health", "value": 100}
icon: {"file": "Items_03.png", "index": 28}
applied_by:
  - {"item": 736}
---
<!-- generated:start -->
<!-- generated-keys: title=90d5b0 type=6143a1 id=27b0e6 sources=4d3a48 name_key=4c8df3 duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=590a2f icon=dcd62b applied_by=4afd0a -->
|  |  |
|---|---|
|  | ![Elixir of Health (C) : Health Regeneration +2, Maximum Health +100](wiki/assets/buffs/2109.png) |
| **Buff id** | `2109` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 28 |

### Tooltip

> Elixir of Health [C] : Health Regeneration +2, Maximum Health +100

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 2 |
| 31 | Health | 100 |

### Applied by

- Using [[wiki/items/736-elixir-of-health-c|Elixir of Health (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 59): Elixir · Elixir of Health · 736–739 · 2109–2112 · HP regen +2 / 4 / 6 / 8 and max HP +100 / 200 / 300 / 400
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

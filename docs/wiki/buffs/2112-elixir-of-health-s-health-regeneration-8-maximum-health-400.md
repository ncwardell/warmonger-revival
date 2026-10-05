---
title: "Elixir of Health [S] : Health Regeneration +8, Maximum Health 400"
type: "buff"
id: 2112
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2112", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2112"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 8}
  - {"code": 31, "stat": "Health", "value": 400}
icon: {"file": "Items_03.png", "index": 31}
applied_by:
  - {"item": 739}
---
<!-- generated:start -->
<!-- generated-keys: title=bc8f16 type=6143a1 id=612d9e sources=406179 name_key=963518 duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=659568 icon=49820a applied_by=5a3e10 -->
|  |  |
|---|---|
|  | ![Elixir of Health (S) : Health Regeneration +8, Maximum Health 400](../assets/buffs/2112.png) |
| **Buff id** | `2112` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 31 |

### Tooltip

> Elixir of Health [S] : Health Regeneration +8, Maximum Health 400

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 8 |
| 31 | Health | 400 |

### Applied by

- Using [[wiki/items/739-elixir-of-health-s|Elixir of Health (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 59): Elixir · Elixir of Health · 736–739 · 2109–2112 · HP regen +2 / 4 / 6 / 8 and max HP +100 / 200 / 300 / 400
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 81): Elixir 3 · HP 200, HP regen 20 · Health: HP 400, HP regen 8 (2112) · no
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

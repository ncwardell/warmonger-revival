---
title: "Elixir of Vampirism [S] : 12 Life Steal with each attack. Maximum Health +400"
type: "buff"
id: 2120
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2120", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2120"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 41, "stat": "Life Steal(%)", "value": 12}
  - {"code": 31, "stat": "Health", "value": 400}
icon: {"file": "Items_03.png", "index": 35}
applied_by:
  - {"item": 747}
---
<!-- generated:start -->
<!-- generated-keys: title=7c7ea9 type=6143a1 id=7513f9 sources=332a70 name_key=27191d duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=8807d1 icon=6680cb applied_by=e76325 -->
|  |  |
|---|---|
|  | ![Elixir of Vampirism (S) : 12 Life Steal with each attack. Maximum Health +400](wiki/assets/buffs/2120.png) |
| **Buff id** | `2120` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 35 |

### Tooltip

> Elixir of Vampirism [S] : 12 Life Steal with each attack. 
> Maximum Health +400

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 41 | Life Steal(%) | 12 |
| 31 | Health | 400 |

### Applied by

- Using [[wiki/items/747-elixir-of-vampirism-s|Elixir of Vampirism (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 60): Elixir · Elixir of Vampirism · 744–747 · 2117–2120 · Life steal per hit 3 / 6 / 9 / 12 and max HP +100 / 200 / 300 / 400
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 79): Elixir 1 · HP on hit 12, HP 200 · Vampirism: Life steal 12, HP 400 (2120) · life steal yes, HP no
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

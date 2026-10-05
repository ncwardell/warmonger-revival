---
title: "Elixir of Tenacity [S] : Tenacity +40, Life Steal with each attack +12"
type: "buff"
id: 2128
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2128", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2128"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 41, "stat": "Life Steal(%)", "value": 12}
  - {"code": 269, "stat": "Toughness(%)", "value": 40}
icon: {"file": "Items_03.png", "index": 47}
applied_by:
  - {"item": 755}
---
<!-- generated:start -->
<!-- generated-keys: title=8d4f25 type=6143a1 id=78c217 sources=c7dba7 name_key=3d9f12 duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=ad0273 icon=bf581f applied_by=5fd883 -->
|  |  |
|---|---|
|  | ![Elixir of Tenacity (S) : Tenacity +40, Life Steal with each attack +12](wiki/assets/buffs/2128.png) |
| **Buff id** | `2128` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 47 |

### Tooltip

> Elixir of Tenacity [S] : Tenacity +40, Life Steal with each attack +12

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 41 | Life Steal(%) | 12 |
| 269 | Toughness(%) | 40 |

### Applied by

- Using [[wiki/items/755-elixir-of-tenacity-s|Elixir of Tenacity (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 61): Elixir · Elixir of Tenacity · 752–755 · 2125–2128 · Life steal per hit 3 / 6 / 9 / 12 and Tenacity +10 / 20 / 30 / 40
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 80): Elixir 2 · HP on hit 12, Tenacity 40 · Tenacity: Life steal 12, Tenacity 40 (2128) · yes
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

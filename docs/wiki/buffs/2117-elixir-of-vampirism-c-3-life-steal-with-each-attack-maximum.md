---
title: "Elixir of Vampirism [C]: 3 Life Steal with each attack. Maximum Health +100"
type: "buff"
id: 2117
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2117", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2117"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 41, "stat": "Life Steal(%)", "value": 3}
  - {"code": 31, "stat": "Health", "value": 100}
icon: {"file": "Items_03.png", "index": 32}
applied_by:
  - {"item": 744}
---
<!-- generated:start -->
<!-- generated-keys: title=387daa type=6143a1 id=924235 sources=2e5573 name_key=edc4dc duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=26b546 icon=eac09a applied_by=a16ef9 -->
|  |  |
|---|---|
|  | ![Elixir of Vampirism (C): 3 Life Steal with each attack. Maximum Health +100](wiki/assets/buffs/2117.png) |
| **Buff id** | `2117` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 32 |

### Tooltip

> Elixir of Vampirism [C]: 3 Life Steal with each attack. 
> Maximum Health +100

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 41 | Life Steal(%) | 3 |
| 31 | Health | 100 |

### Applied by

- Using [[wiki/items/744-elixir-of-vampirism-c|Elixir of Vampirism (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 60): Elixir · Elixir of Vampirism · 744–747 · 2117–2120 · Life steal per hit 3 / 6 / 9 / 12 and max HP +100 / 200 / 300 / 400
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

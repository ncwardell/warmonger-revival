---
title: "Elixir of Tenacity [C] : Tenacity +10, Life Steal with each attack +3"
type: "buff"
id: 2125
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2125", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2125"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 41, "stat": "Life Steal(%)", "value": 3}
  - {"code": 269, "stat": "Toughness(%)", "value": 10}
icon: {"file": "Items_03.png", "index": 44}
applied_by:
  - {"item": 752}
---
<!-- generated:start -->
<!-- generated-keys: title=eb328d type=6143a1 id=e8e44b sources=228ed4 name_key=f85e85 duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=6b7072 icon=9eb0f9 applied_by=02aa4f -->
|  |  |
|---|---|
|  | ![Elixir of Tenacity (C) : Tenacity +10, Life Steal with each attack +3](wiki/assets/buffs/2125.png) |
| **Buff id** | `2125` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 44 |

### Tooltip

> Elixir of Tenacity [C] : Tenacity +10, Life Steal with each attack +3

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 41 | Life Steal(%) | 3 |
| 269 | Toughness(%) | 10 |

### Applied by

- Using [[wiki/items/752-elixir-of-tenacity-c|Elixir of Tenacity (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 61): Elixir · Elixir of Tenacity · 752–755 · 2125–2128 · Life steal per hit 3 / 6 / 9 / 12 and Tenacity +10 / 20 / 30 / 40
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

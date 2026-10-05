---
title: "Elixir of Vampirism [A] : 9 Life Steal with each attack. Maximum Health +300"
type: "buff"
id: 2119
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2119", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2119"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 41, "stat": "Life Steal(%)", "value": 9}
  - {"code": 31, "stat": "Health", "value": 300}
icon: {"file": "Items_03.png", "index": 34}
applied_by:
  - {"item": 746}
---
<!-- generated:start -->
<!-- generated-keys: title=4a5882 type=6143a1 id=74c921 sources=82d44a name_key=128a34 duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=efd192 icon=7e443a applied_by=d8cb3c -->
|  |  |
|---|---|
|  | ![Elixir of Vampirism (A) : 9 Life Steal with each attack. Maximum Health +300](wiki/assets/buffs/2119.png) |
| **Buff id** | `2119` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 34 |

### Tooltip

> Elixir of Vampirism [A] : 9 Life Steal with each attack. 
> Maximum Health +300

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 41 | Life Steal(%) | 9 |
| 31 | Health | 300 |

### Applied by

- Using [[wiki/items/746-elixir-of-vampirism-a|Elixir of Vampirism (A)]] (Item_Base option 301)
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

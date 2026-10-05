---
title: "Elixir of Tenacity [A] : Tenacity +30, Life Steal with each attack +9"
type: "buff"
id: 2127
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2127", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2127"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 41, "stat": "Life Steal(%)", "value": 9}
  - {"code": 269, "stat": "Toughness(%)", "value": 30}
icon: {"file": "Items_03.png", "index": 46}
applied_by:
  - {"item": 754}
---
<!-- generated:start -->
<!-- generated-keys: title=981b4e type=6143a1 id=82915e sources=09b951 name_key=8f9794 duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=54e029 icon=da602f applied_by=a52932 -->
|  |  |
|---|---|
|  | ![Elixir of Tenacity (A) : Tenacity +30, Life Steal with each attack +9](wiki/assets/buffs/2127.png) |
| **Buff id** | `2127` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 46 |

### Tooltip

> Elixir of Tenacity [A] : Tenacity +30, Life Steal with each attack +9

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 41 | Life Steal(%) | 9 |
| 269 | Toughness(%) | 30 |

### Applied by

- Using [[wiki/items/754-elixir-of-tenacity-a|Elixir of Tenacity (A)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Elixir of Tenacity [A] (item 754), a Elixir clickable: 9, +30 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row life steal 3 per hit, Tenacity +10 / 6, +20 / 9, +30 / 12, +40). *client*
- One active per family: it shares exclusive group 2109 (Health, Vampirism, Tenacity), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §1–§4, [[gameplay/items-and-crafting]].

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

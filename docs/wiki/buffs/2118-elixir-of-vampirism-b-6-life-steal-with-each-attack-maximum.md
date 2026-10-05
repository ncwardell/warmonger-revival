---
title: "Elixir of Vampirism [B] : 6 Life Steal with each attack. Maximum Health +200"
type: "buff"
id: 2118
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2118", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2118"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 41, "stat": "Life Steal(%)", "value": 6}
  - {"code": 31, "stat": "Health", "value": 200}
icon: {"file": "Items_03.png", "index": 33}
applied_by:
  - {"item": 745}
---
<!-- generated:start -->
<!-- generated-keys: title=095bf9 type=6143a1 id=aaabd0 sources=6899c5 name_key=3f2fbf duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=567ffa icon=cf6997 applied_by=d6830f -->
|  |  |
|---|---|
|  | ![Elixir of Vampirism (B) : 6 Life Steal with each attack. Maximum Health +200](wiki/assets/buffs/2118.png) |
| **Buff id** | `2118` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 33 |

### Tooltip

> Elixir of Vampirism [B] : 6 Life Steal with each attack. 
> Maximum Health +200

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 41 | Life Steal(%) | 6 |
| 31 | Health | 200 |

### Applied by

- Using [[wiki/items/745-elixir-of-vampirism-b|Elixir of Vampirism (B)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Elixir of Vampirism [B] (item 745), a Elixir clickable: 6, +200 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row life steal 3 per hit, max HP +100 / 6, +200 / 9, +300 / 12, +400). *client*
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

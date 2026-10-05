---
title: "Flask of Tenacity [A] : Tenacity +30, Mana Steal with each attack +6"
type: "buff"
id: 2131
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2131", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2131"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 42, "stat": "Devour(%)", "value": 6}
  - {"code": 269, "stat": "Toughness(%)", "value": 30}
icon: {"file": "Items_30.png", "index": 28}
applied_by:
  - {"item": 758}
---
<!-- generated:start -->
<!-- generated-keys: title=31b9a3 type=6143a1 id=7dd1c7 sources=b1a670 name_key=962c0e duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=3c8177 icon=d885bb applied_by=27fc28 -->
|  |  |
|---|---|
|  | ![Flask of Tenacity (A) : Tenacity +30, Mana Steal with each attack +6](wiki/assets/buffs/2131.png) |
| **Buff id** | `2131` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 28 |

### Tooltip

> Flask of Tenacity [A] : Tenacity +30, Mana Steal with each attack +6

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 42 | Devour(%) | 6 |
| 269 | Toughness(%) | 30 |

### Applied by

- Using [[wiki/items/758-flask-of-tenacity-a|Flask of Tenacity (A)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Flask of Tenacity [A] (item 758), a Flask clickable: 6, +30 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row mana steal 2 per hit, Tenacity +10 / 4, +20 / 6, +30 / 8, +40). *client*
- One active per family: it shares exclusive group 2113 (Mana, Devour, Tenacity), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
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

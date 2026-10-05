---
title: "Flask of Devour [B] : 4 Mana Steal with each attack. Maximum Mana +100"
type: "buff"
id: 2122
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2122", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2122"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 42, "stat": "Devour(%)", "value": 4}
  - {"code": 33, "stat": "Mana", "value": 100}
icon: {"file": "Items_30.png", "index": 27}
applied_by:
  - {"item": 749}
---
<!-- generated:start -->
<!-- generated-keys: title=37e770 type=6143a1 id=ce1d36 sources=bbf837 name_key=2f7c26 duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=50314f icon=401415 applied_by=0facb2 -->
|  |  |
|---|---|
|  | ![Flask of Devour (B) : 4 Mana Steal with each attack. Maximum Mana +100](../assets/buffs/2122.png) |
| **Buff id** | `2122` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 27 |

### Tooltip

> Flask of Devour [B] : 4 Mana Steal with each attack. 
> Maximum Mana +100

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 42 | Devour(%) | 4 |
| 33 | Mana | 100 |

### Applied by

- Using [[wiki/items/749-flask-of-devour-b|Flask of Devour (B)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Flask of Devour [B] (item 749), a Flask clickable: 4, +100 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row mana steal 2 per hit, max MP +50 / 4, +100 / 6, +150 / 8, +200). *client*
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

---
title: "Scroll of Reduced Area Damage [A] : Major protection from Area Damage."
type: "buff"
id: 2095
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2095", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2095"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 270, "stat": "Reduced Area Damage(%)", "value": 15}
icon: {"file": "Items_30.png", "index": 15}
applied_by:
  - {"item": 722}
---
<!-- generated:start -->
<!-- generated-keys: title=4bd518 type=6143a1 id=4a1b77 sources=99496c name_key=4c667c duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=c3e20b icon=77c9cc applied_by=d69d2d -->
|  |  |
|---|---|
|  | ![Scroll of Reduced Area Damage (A) : Major protection from Area Damage.](../assets/buffs/2095.png) |
| **Buff id** | `2095` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 15 |

### Tooltip

> Scroll of Reduced Area Damage [A] : Major protection from Area Damage.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 270 | Reduced Area Damage(%) | 15 |

### Applied by

- Using [[wiki/items/722-tome-of-patience-a|Tome of Patience (A)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Tome of Patience [A] (item 722), a Tome clickable: −15 % for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Area damage taken −5 % / −10 % / −15 % / −20 %). *client*
- One active per family: it shares exclusive group 2085 (Attack SPD, Cooldown, Patience, Critical), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The client names the buff the other way round from the item (Scroll ↔ Tome); [[gameplay/consumables]] says to use the item names. *client*

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

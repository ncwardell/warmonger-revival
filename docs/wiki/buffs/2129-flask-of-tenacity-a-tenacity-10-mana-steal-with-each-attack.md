---
title: "Flask of Tenacity [A] : Tenacity +10, Mana Steal with each attack +2"
type: "buff"
id: 2129
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2129", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2129"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 42, "stat": "Devour(%)", "value": 2}
  - {"code": 269, "stat": "Toughness(%)", "value": 10}
icon: {"file": "Items_30.png", "index": 22}
applied_by:
  - {"item": 756}
---
<!-- generated:start -->
<!-- generated-keys: title=62816f type=6143a1 id=a40eb3 sources=871fed name_key=204485 duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=d96241 icon=25b590 applied_by=7a7b73 -->
|  |  |
|---|---|
|  | ![Flask of Tenacity (A) : Tenacity +10, Mana Steal with each attack +2](../assets/buffs/2129.png) |
| **Buff id** | `2129` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 22 |

### Tooltip

> Flask of Tenacity [A] : Tenacity +10, Mana Steal with each attack +2

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 42 | Devour(%) | 2 |
| 269 | Toughness(%) | 10 |

### Applied by

- Using [[wiki/items/756-flask-of-tenacity-c|Flask of Tenacity (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 64): Flask · Flask of Tenacity · 756–759 · 2129–2132 · Mana steal per hit 2 / 4 / 6 / 8 and Tenacity +10 / 20 / 30 / 40
<!-- generated:end -->

## Notes

- Buff of Flask of Tenacity [C] (item 756), a Flask clickable: mana steal 2 per hit, Tenacity +10 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row mana steal 2 per hit, Tenacity +10 / 4, +20 / 6, +30 / 8, +40). *client*
- One active per family: it shares exclusive group 2113 (Mana, Devour, Tenacity), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §1–§4, [[gameplay/items-and-crafting]].

## Open questions

- The client buff name says "[A]" but this is the C-grade row (client typo, [[gameplay/consumables]] §1).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

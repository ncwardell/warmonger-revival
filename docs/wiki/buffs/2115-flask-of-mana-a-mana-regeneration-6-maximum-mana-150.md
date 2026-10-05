---
title: "Flask of Mana [A] : Mana Regeneration +6, Maximum Mana +150"
type: "buff"
id: 2115
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2115", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "notes: [[gameplay/reinforce-and-runes]] §7, WM 0124 (regen 1/2/3/4 → 2/4/6/8; matches client)"]
name_key: "SkillBuff_2115"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 34, "stat": "Mana Regeneration", "value": 6}
  - {"code": 33, "stat": "Mana", "value": 150}
icon: {"file": "Items_30.png", "index": 29}
applied_by:
  - {"item": 742}
---
<!-- generated:start -->
<!-- generated-keys: title=4b74a5 type=6143a1 id=e928dc sources=c1257f name_key=52727b duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=bffb63 icon=ab8647 applied_by=4f3dd5 -->
|  |  |
|---|---|
|  | ![Flask of Mana (A) : Mana Regeneration +6, Maximum Mana +150](../assets/buffs/2115.png) |
| **Buff id** | `2115` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 29 |

### Tooltip

> Flask of Mana [A] : Mana Regeneration +6, Maximum Mana +150

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 34 | Mana Regeneration | 6 |
| 33 | Mana | 150 |

### Applied by

- Using [[wiki/items/742-flask-of-mana-a|Flask of Mana (A)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Flask of Mana [A] (item 742), a Flask clickable: MP regen +6, max MP +150 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row MP regen +2, max MP +50 / MP regen +4, max MP +100 / MP regen +6, max MP +150 / MP regen +8, max MP +200). *client*
- One active per family: it shares exclusive group 2113 (Mana, Devour, Tenacity), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- Patch history: [WM 0124](https://steamcommunity.com/games/718790/announcements/detail/2425653583381829617) doubled the regen part, MP regen 1/2/3/4 → 2/4/6/8; the client buffs match the new values ([[gameplay/reinforce-and-runes]] §7). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §1–§4, [[gameplay/items-and-crafting]], [[gameplay/reinforce-and-runes]] §7.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

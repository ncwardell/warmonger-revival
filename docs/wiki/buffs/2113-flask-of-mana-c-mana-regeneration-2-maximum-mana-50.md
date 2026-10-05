---
title: "Flask of Mana [C] : Mana Regeneration +2, Maximum Mana +50"
type: "buff"
id: 2113
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2113", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "notes: [[gameplay/reinforce-and-runes]] §7, WM 0124 (regen 1/2/3/4 → 2/4/6/8; matches client)"]
name_key: "SkillBuff_2113"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 34, "stat": "Mana Regeneration", "value": 2}
  - {"code": 33, "stat": "Mana", "value": 50}
icon: {"file": "Items_30.png", "index": 23}
applied_by:
  - {"item": 740}
---
<!-- generated:start -->
<!-- generated-keys: title=3563d0 type=6143a1 id=88b726 sources=0cf3f5 name_key=f36b3e duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=2f668f icon=40f6b8 applied_by=7a20df -->
|  |  |
|---|---|
|  | ![Flask of Mana (C) : Mana Regeneration +2, Maximum Mana +50](../assets/buffs/2113.png) |
| **Buff id** | `2113` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 23 |

### Tooltip

> Flask of Mana [C] : Mana Regeneration +2, Maximum Mana +50

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 34 | Mana Regeneration | 2 |
| 33 | Mana | 50 |

### Applied by

- Using [[wiki/items/740-flask-of-mana-c|Flask of Mana (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 62): Flask · Flask of Mana · 740–743 · 2113–2116 · MP regen +2 / 4 / 6 / 8 and max MP +50 / 100 / 150 / 200
<!-- generated:end -->

## Notes

- Buff of Flask of Mana [C] (item 740), a Flask clickable: MP regen +2, max MP +50 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row MP regen +2, max MP +50 / MP regen +4, max MP +100 / MP regen +6, max MP +150 / MP regen +8, max MP +200). *client*
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

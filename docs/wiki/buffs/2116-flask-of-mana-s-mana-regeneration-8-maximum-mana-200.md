---
title: "Flask of Mana [S] : Mana Regeneration +8, Maximum Mana +200"
type: "buff"
id: 2116
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2116", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "sheet: [[gameplay/stat-values]] §5 Sheet3 (Crush-era S values; history)", "notes: [[gameplay/reinforce-and-runes]] §7, WM 0124 (regen 1/2/3/4 → 2/4/6/8; matches client)"]
name_key: "SkillBuff_2116"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 34, "stat": "Mana Regeneration", "value": 8}
  - {"code": 33, "stat": "Mana", "value": 200}
icon: {"file": "Items_30.png", "index": 32}
applied_by:
  - {"item": 743}
---
<!-- generated:start -->
<!-- generated-keys: title=e9c3fc type=6143a1 id=397423 sources=20f526 name_key=974c76 duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=5748d3 icon=16039e applied_by=0c6030 -->
|  |  |
|---|---|
|  | ![Flask of Mana (S) : Mana Regeneration +8, Maximum Mana +200](../assets/buffs/2116.png) |
| **Buff id** | `2116` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 32 |

### Tooltip

> Flask of Mana [S] : Mana Regeneration +8, Maximum Mana +200

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 34 | Mana Regeneration | 8 |
| 33 | Mana | 200 |

### Applied by

- Using [[wiki/items/743-flask-of-mana-s|Flask of Mana (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 62): Flask · Flask of Mana · 740–743 · 2113–2116 · MP regen +2 / 4 / 6 / 8 and max MP +50 / 100 / 150 / 200
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 84): Flask 3 · MP 120, MP regen 16 · Mana: MP 200, MP regen 8 (2116) · no
<!-- generated:end -->

## Notes

- Buff of Flask of Mana [S] (item 743), a Flask clickable: MP regen +8, max MP +200 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row MP regen +2, max MP +50 / MP regen +4, max MP +100 / MP regen +6, max MP +150 / MP regen +8, max MP +200). *client*
- One active per family: it shares exclusive group 2113 (Mana, Devour, Tenacity), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The Crush-era Crush Share sheet (Sheet3) lists Flask 3: MP 120, MP regen 16 (client 200 / 8; disagrees) ([[gameplay/stat-values]] §5). *sheet*
- Patch history: [WM 0124](https://steamcommunity.com/games/718790/announcements/detail/2425653583381829617) doubled the regen part, MP regen 1/2/3/4 → 2/4/6/8; the client buffs match the new values ([[gameplay/reinforce-and-runes]] §7). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §1–§4, [[gameplay/items-and-crafting]], [[gameplay/stat-values]] §5, [[gameplay/reinforce-and-runes]] §7.

## Open questions

- Crush-era sheet values differ from the client (see Notes); the client value is kept.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

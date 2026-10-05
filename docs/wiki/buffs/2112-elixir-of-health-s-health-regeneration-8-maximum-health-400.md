---
title: "Elixir of Health [S] : Health Regeneration +8, Maximum Health 400"
type: "buff"
id: 2112
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2112", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "sheet: [[gameplay/stat-values]] §5 Sheet3 (Crush-era S values; history)", "notes: [[gameplay/reinforce-and-runes]] §7, WM 0124 (regen 1/2/3/4 → 2/4/6/8; matches client)"]
name_key: "SkillBuff_2112"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 8}
  - {"code": 31, "stat": "Health", "value": 400}
icon: {"file": "Items_03.png", "index": 31}
applied_by:
  - {"item": 739}
---
<!-- generated:start -->
<!-- generated-keys: title=bc8f16 type=6143a1 id=612d9e sources=406179 name_key=963518 duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=659568 icon=49820a applied_by=5a3e10 -->
|  |  |
|---|---|
|  | ![Elixir of Health (S) : Health Regeneration +8, Maximum Health 400](wiki/assets/buffs/2112.png) |
| **Buff id** | `2112` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 31 |

### Tooltip

> Elixir of Health [S] : Health Regeneration +8, Maximum Health 400

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 8 |
| 31 | Health | 400 |

### Applied by

- Using [[wiki/items/739-elixir-of-health-s|Elixir of Health (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 59): Elixir · Elixir of Health · 736–739 · 2109–2112 · HP regen +2 / 4 / 6 / 8 and max HP +100 / 200 / 300 / 400
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 81): Elixir 3 · HP 200, HP regen 20 · Health: HP 400, HP regen 8 (2112) · no
<!-- generated:end -->

## Notes

- Buff of Elixir of Health [S] (item 739), a Elixir clickable: HP regen +8, max HP +400 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row HP regen +2, max HP +100 / HP regen +4, max HP +200 / HP regen +6, max HP +300 / HP regen +8, max HP +400). *client*
- One active per family: it shares exclusive group 2109 (Health, Vampirism, Tenacity), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The Crush-era Crush Share sheet (Sheet3) lists Elixir 3: HP 200, HP regen 20 (client 400 / 8; disagrees) ([[gameplay/stat-values]] §5). *sheet*
- Patch history: [WM 0124](https://steamcommunity.com/games/718790/announcements/detail/2425653583381829617) doubled the regen part, HP regen 1/2/3/4 → 2/4/6/8; the client buffs match the new values ([[gameplay/reinforce-and-runes]] §7). *notes*

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

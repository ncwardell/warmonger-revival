---
title: "Flask of Tenacity [S] : Tenacity +40, Mana Steal with each attack +8"
type: "buff"
id: 2132
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2132", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "sheet: [[gameplay/stat-values]] §5 Sheet3 (Crush-era S values; history)"]
name_key: "SkillBuff_2132"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 42, "stat": "Devour(%)", "value": 8}
  - {"code": 269, "stat": "Toughness(%)", "value": 40}
icon: {"file": "Items_30.png", "index": 31}
applied_by:
  - {"item": 759}
---
<!-- generated:start -->
<!-- generated-keys: title=340f2c type=6143a1 id=b6859e sources=9134be name_key=16445d duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=948ad8 icon=4f0d42 applied_by=2eec5d -->
|  |  |
|---|---|
|  | ![Flask of Tenacity (S) : Tenacity +40, Mana Steal with each attack +8](wiki/assets/buffs/2132.png) |
| **Buff id** | `2132` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 31 |

### Tooltip

> Flask of Tenacity [S] : Tenacity +40, Mana Steal with each attack +8

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 42 | Devour(%) | 8 |
| 269 | Toughness(%) | 40 |

### Applied by

- Using [[wiki/items/759-flask-of-tenacity-s|Flask of Tenacity (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 64): Flask · Flask of Tenacity · 756–759 · 2129–2132 · Mana steal per hit 2 / 4 / 6 / 8 and Tenacity +10 / 20 / 30 / 40
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 83): Flask 2 · Tenacity 40, MP on hit 8 · Tenacity: Mana steal 8, Tenacity 40 (2132) · yes
<!-- generated:end -->

## Notes

- Buff of Flask of Tenacity [S] (item 759), a Flask clickable: 8, +40 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row mana steal 2 per hit, Tenacity +10 / 4, +20 / 6, +30 / 8, +40). *client*
- One active per family: it shares exclusive group 2113 (Mana, Devour, Tenacity), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The Crush-era Crush Share sheet (Sheet3) lists Flask 2: Tenacity 40, MP on hit 8 (agrees) ([[gameplay/stat-values]] §5). *sheet*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §1–§4, [[gameplay/items-and-crafting]], [[gameplay/stat-values]] §5.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

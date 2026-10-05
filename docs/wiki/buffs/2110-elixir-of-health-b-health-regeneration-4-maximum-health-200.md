---
title: "Elixir of Health [B] : Health Regeneration +4, Maximum Health +200"
type: "buff"
id: 2110
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2110", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "notes: [[gameplay/reinforce-and-runes]] §7, WM 0124 (regen 1/2/3/4 → 2/4/6/8; matches client)"]
name_key: "SkillBuff_2110"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2109
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 4}
  - {"code": 31, "stat": "Health", "value": 200}
icon: {"file": "Items_03.png", "index": 29}
applied_by:
  - {"item": 737}
---
<!-- generated:start -->
<!-- generated-keys: title=676a88 type=6143a1 id=086e89 sources=1a4561 name_key=debe8c duration=995f11 is_buff=b6589f stack_type=356a19 group=27b0e6 effects=af9cf8 icon=43e444 applied_by=373e83 -->
|  |  |
|---|---|
|  | ![Elixir of Health (B) : Health Regeneration +4, Maximum Health +200](wiki/assets/buffs/2110.png) |
| **Buff id** | `2110` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2109 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 29 |

### Tooltip

> Elixir of Health [B] : Health Regeneration +4, Maximum Health +200

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 4 |
| 31 | Health | 200 |

### Applied by

- Using [[wiki/items/737-elixir-of-health-b|Elixir of Health (B)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Elixir of Health [B] (item 737), a Elixir clickable: HP regen +4, max HP +200 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row HP regen +2, max HP +100 / HP regen +4, max HP +200 / HP regen +6, max HP +300 / HP regen +8, max HP +400). *client*
- One active per family: it shares exclusive group 2109 (Health, Vampirism, Tenacity), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- Patch history: [WM 0124](https://steamcommunity.com/games/718790/announcements/detail/2425653583381829617) doubled the regen part, HP regen 1/2/3/4 → 2/4/6/8; the client buffs match the new values ([[gameplay/reinforce-and-runes]] §7). *notes*

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

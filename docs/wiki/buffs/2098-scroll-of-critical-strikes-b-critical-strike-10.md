---
title: "Scroll of Critical Strikes [B] : Critical Strike +10%"
type: "buff"
id: 2098
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2098", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2098"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 109, "stat": "Critical Strike +(%)", "value": 10}
icon: {"file": "Items_30.png", "index": 12}
applied_by:
  - {"item": 725}
---
<!-- generated:start -->
<!-- generated-keys: title=f613df type=6143a1 id=cb2302 sources=c8d2a0 name_key=dddd98 duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=866346 icon=7d3ec0 applied_by=2c98b9 -->
|  |  |
|---|---|
|  | ![Scroll of Critical Strikes (B) : Critical Strike +10%](wiki/assets/buffs/2098.png) |
| **Buff id** | `2098` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 12 |

### Tooltip

> Scroll of Critical Strikes [B] : Critical Strike +10%

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 109 | Critical Strike +(%) | 10 |

### Applied by

- Using [[wiki/items/725-tome-of-critical-b|Tome of Critical (B)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Tome of Critical [B] (item 725), a Tome clickable: +10 % for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Crit chance +5 % / +10 % / +15 % / +20 %). *client*
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

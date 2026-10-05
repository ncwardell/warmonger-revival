---
title: "Scroll of Critical Strikes [S] : Critical Strike +20%"
type: "buff"
id: 2100
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2100", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "sheet: [[gameplay/stat-values]] §5 Sheet3 (Crush-era S values; history)", "image: [[gameplay/reinforce-and-runes]] §7 (Tome of Critical blog image; matches client)"]
name_key: "SkillBuff_2100"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 109, "stat": "Critical Strike +(%)", "value": 20}
icon: {"file": "Items_30.png", "index": 20}
applied_by:
  - {"item": 727}
---
<!-- generated:start -->
<!-- generated-keys: title=bf0679 type=6143a1 id=89b98f sources=854f5b name_key=799624 duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=0e5707 icon=7f2f86 applied_by=52229f -->
|  |  |
|---|---|
|  | ![Scroll of Critical Strikes (S) : Critical Strike +20%](../assets/buffs/2100.png) |
| **Buff id** | `2100` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 20 |

### Tooltip

> Scroll of Critical Strikes [S] : Critical Strike +20%

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 109 | Critical Strike +(%) | 20 |

### Applied by

- Using [[wiki/items/727-tome-of-critical-s|Tome of Critical (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 58): Tome · Tome of Critical · 724–727 · 2097–2100 · Crit chance +5 / 10 / 15 / 20%
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 77): Tome S · Crit 20%, less AoE 20%, Cooldown 12%, Attack speed 40 · Critical Strikes +20% (2100), Reduced Area Damage 20% (2096), Cooldown Reduction 12% (2092),...
<!-- generated:end -->

## Notes

- Buff of Tome of Critical [S] (item 727), a Tome clickable: +20 % for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Crit chance +5 % / +10 % / +15 % / +20 %). *client*
- One active per family: it shares exclusive group 2085 (Attack SPD, Cooldown, Patience, Critical), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The client names the buff the other way round from the item (Scroll ↔ Tome); [[gameplay/consumables]] says to use the item names. *client*
- The Crush-era Crush Share sheet (Sheet3) lists Tome S: Crit 20 % (agrees) ([[gameplay/stat-values]] §5). *sheet*
- A Spanish guide image shows Tome of Critical [S] at +20 % crit chance for 5 min, matching the client ([[gameplay/reinforce-and-runes]] §7). *image*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §1–§4, [[gameplay/items-and-crafting]], [[gameplay/stat-values]] §5, [[gameplay/reinforce-and-runes]] §7.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

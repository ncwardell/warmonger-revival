---
title: "Scroll of Cooldown Reduction [S] : 12% Cooldown Reduction"
type: "buff"
id: 2092
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2092", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "sheet: [[gameplay/stat-values]] §5 Sheet3 (Crush-era S values; history)"]
name_key: "SkillBuff_2092"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 12}
icon: {"file": "Items_30.png", "index": 21}
applied_by:
  - {"item": 719}
---
<!-- generated:start -->
<!-- generated-keys: title=15d521 type=6143a1 id=3895a2 sources=b83419 name_key=0e5431 duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=b8d801 icon=a5d2ad applied_by=7b8e9e -->
|  |  |
|---|---|
|  | ![Scroll of Cooldown Reduction (S) : 12% Cooldown Reduction](wiki/assets/buffs/2092.png) |
| **Buff id** | `2092` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 21 |

### Tooltip

> Scroll of Cooldown Reduction [S] : 12%  Cooldown Reduction

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 212 | Cooldown Reduction(%) | 12 |

### Applied by

- Using [[wiki/items/719-tome-of-cooldown-s|Tome of Cooldown (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 56): Tome · Tome of Cooldown · 716–719 · 2089–2092 · Cooldown reduction 3 / 6 / 9 / 12%
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 77): Tome S · Crit 20%, less AoE 20%, Cooldown 12%, Attack speed 40 · Critical Strikes +20% (2100), Reduced Area Damage 20% (2096), Cooldown Reduction 12% (2092),...
<!-- generated:end -->

## Notes

- Buff of Tome of Cooldown [S] (item 719), a Tome clickable: 12 % for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Cooldown reduction 3 % / 6 % / 9 % / 12 %). *client*
- One active per family: it shares exclusive group 2085 (Attack SPD, Cooldown, Patience, Critical), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The client names the buff the other way round from the item (Scroll ↔ Tome); [[gameplay/consumables]] says to use the item names. *client*
- The Crush-era Crush Share sheet (Sheet3) lists Tome S: Cooldown 12 % (agrees) ([[gameplay/stat-values]] §5). *sheet*

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

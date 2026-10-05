---
title: "Scroll of Attack Speed [S] : Attack Speed +40"
type: "buff"
id: 2088
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2088", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "sheet: [[gameplay/stat-values]] §5 Sheet3 (Crush-era S values; history)"]
name_key: "SkillBuff_2088"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 16, "stat": "code 16 (unknown)", "value": 40}
icon: {"file": "Items_30.png", "index": 18}
applied_by:
  - {"item": 715}
---
<!-- generated:start -->
<!-- generated-keys: title=c26a7e type=6143a1 id=8ab828 sources=0b07df name_key=cdf0c3 duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=5867cd icon=0ef731 applied_by=7f584e -->
|  |  |
|---|---|
|  | ![Scroll of Attack Speed (S) : Attack Speed +40](wiki/assets/buffs/2088.png) |
| **Buff id** | `2088` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 18 |

### Tooltip

> Scroll of Attack Speed [S] : Attack Speed +40

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 16 | code 16 (unknown) | 40 |

### Applied by

- Using [[wiki/items/715-tome-of-attack-spd-s|Tome of Attack SPD (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 55): Tome · Tome of Attack SPD · 712–715 · 2085–2088 · Attack speed (opt 16) +10 / 20 / 30 / 40
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 77): Tome S · Crit 20%, less AoE 20%, Cooldown 12%, Attack speed 40 · Critical Strikes +20% (2100), Reduced Area Damage 20% (2096), Cooldown Reduction 12% (2092),...
<!-- generated:end -->

## Notes

- Buff of Tome of Attack SPD [S] (item 715), a Tome clickable: +40 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Attack speed +10 / +20 / +30 / +40). *client*
- One active per family: it shares exclusive group 2085 (Attack SPD, Cooldown, Patience, Critical), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The client names the buff the other way round from the item (Scroll ↔ Tome); [[gameplay/consumables]] says to use the item names. *client*
- The Crush-era Crush Share sheet (Sheet3) lists Tome S: Attack speed 40 (agrees) ([[gameplay/stat-values]] §5). *sheet*

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

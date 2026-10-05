---
title: "Tome of the Magician [S] : Ability Power +120"
type: "buff"
id: 2084
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2084", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "sheet: [[gameplay/stat-values]] §5 Sheet3 (Crush-era S values; history)"]
name_key: "SkillBuff_2084"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2077
effects:
  - {"code": 2, "stat": "Ability Power", "value": 120}
icon: {"file": "Items_03.png", "index": 59}
applied_by:
  - {"item": 711}
---
<!-- generated:start -->
<!-- generated-keys: title=7fff69 type=6143a1 id=4a6798 sources=b621ff name_key=0c9af8 duration=995f11 is_buff=b6589f stack_type=356a19 group=009cf5 effects=ad3782 icon=98592e applied_by=109b00 -->
|  |  |
|---|---|
|  | ![Tome of the Magician (S) : Ability Power +120](wiki/assets/buffs/2084.png) |
| **Buff id** | `2084` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2077 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 59 |

### Tooltip

> Tome of the Magician [S] : Ability Power +120

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 2 | Ability Power | 120 |

### Applied by

- Using [[wiki/items/711-scroll-of-the-magician-s|Scroll of the Magician (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 52): Scroll · Scroll of the Magician · 708–711 · 2081–2084 · Ability Power +24 / 48 / 72 / 120
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 78): Scroll S · Attack 35, Ability 35, Armor pen 16, Magic pen 16 · Warrior +160 Attack (2080), Magician +120 AP (2084), Armor Pen +8 (2104), Magic Pen +8 (2108)...
<!-- generated:end -->

## Notes

- Buff of Scroll of the Magician [S] (item 711), a Scroll clickable: +120 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Ability Power +24 / +48 / +72 / +120). *client*
- One active per family: it shares exclusive group 2077 (Warrior, Magician, Armor PNT, Magic PNT), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The client names the buff the other way round from the item (Scroll ↔ Tome); [[gameplay/consumables]] says to use the item names. *client*
- The Crush-era Crush Share sheet (Sheet3) lists Scroll S: Ability 35 (client 120; disagrees) ([[gameplay/stat-values]] §5). *sheet*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §1–§4, [[gameplay/items-and-crafting]], [[gameplay/stat-values]] §5.

## Open questions

- Crush-era sheet values differ from the client (see Notes); the client value is kept.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

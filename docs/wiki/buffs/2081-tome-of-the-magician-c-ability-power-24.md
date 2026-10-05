---
title: "Tome of the Magician [C] : Ability Power +24"
type: "buff"
id: 2081
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2081", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2081"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2077
effects:
  - {"code": 2, "stat": "Ability Power", "value": 24}
icon: {"file": "Items_03.png", "index": 56}
applied_by:
  - {"item": 708}
---
<!-- generated:start -->
<!-- generated-keys: title=a0a427 type=6143a1 id=ba6191 sources=404171 name_key=791462 duration=995f11 is_buff=b6589f stack_type=356a19 group=009cf5 effects=705140 icon=ba2a0d applied_by=7e62fd -->
|  |  |
|---|---|
|  | ![Tome of the Magician (C) : Ability Power +24](../assets/buffs/2081.png) |
| **Buff id** | `2081` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2077 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 56 |

### Tooltip

> Tome of the Magician [C] : Ability Power +24

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 2 | Ability Power | 24 |

### Applied by

- Using [[wiki/items/708-scroll-of-the-magician-c|Scroll of the Magician (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 52): Scroll · Scroll of the Magician · 708–711 · 2081–2084 · Ability Power +24 / 48 / 72 / 120
<!-- generated:end -->

## Notes

- Buff of Scroll of the Magician [C] (item 708), a Scroll clickable: Ability Power +24 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Ability Power +24 / +48 / +72 / +120). *client*
- One active per family: it shares exclusive group 2077 (Warrior, Magician, Armor PNT, Magic PNT), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
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

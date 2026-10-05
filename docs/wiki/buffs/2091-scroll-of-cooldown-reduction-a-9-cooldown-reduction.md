---
title: "Scroll of Cooldown Reduction [A] : 9% Cooldown Reduction"
type: "buff"
id: 2091
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2091", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2091"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 212, "stat": "Cooldown Reduction(%)", "value": 9}
icon: {"file": "Items_30.png", "index": 17}
applied_by:
  - {"item": 718}
  - {"item": 2599}
---
<!-- generated:start -->
<!-- generated-keys: title=18352c type=6143a1 id=2d7cf6 sources=11f2f0 name_key=e33304 duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=ca9d12 icon=7809ef applied_by=922631 -->
|  |  |
|---|---|
|  | ![Scroll of Cooldown Reduction (A) : 9% Cooldown Reduction](wiki/assets/buffs/2091.png) |
| **Buff id** | `2091` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 17 |

### Tooltip

> Scroll of Cooldown Reduction [A] : 9%  Cooldown Reduction

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 212 | Cooldown Reduction(%) | 9 |

### Applied by

- Using [[wiki/items/718-tome-of-cooldown-a|Tome of Cooldown (A)]] (Item_Base option 301)
- Using [[wiki/items/2599-tome-of-cooldown-quest|Tome of Cooldown (Quest)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 3. Potions and other clickables (line 91): 2598 / 2599 · Potion of Health [Quest] / Tome of Cooldown [Quest] · 2062 / 2091 · Same as Health [A] / Cooldown [A] · 17 s / 5 min · quest recipes 749 / 599
<!-- generated:end -->

## Notes

- Buff of Tome of Cooldown [A] (item 718), a Tome clickable: 9 % for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Cooldown reduction 3 % / 6 % / 9 % / 12 %). *client*
- One active per family: it shares exclusive group 2085 (Attack SPD, Cooldown, Patience, Critical), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The client names the buff the other way round from the item (Scroll ↔ Tome); [[gameplay/consumables]] says to use the item names. *client*
- Also applied by Tome of Cooldown [Quest] (item 2599), crafted in the alchemy tutorial quest ([[gameplay/consumables]] §3). *client*

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

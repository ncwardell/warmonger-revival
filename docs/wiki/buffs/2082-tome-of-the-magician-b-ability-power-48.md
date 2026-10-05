---
title: "Tome of the Magician [B] : Ability Power +48"
type: "buff"
id: 2082
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2082", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2082"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2077
effects:
  - {"code": 2, "stat": "Ability Power", "value": 48}
icon: {"file": "Items_03.png", "index": 57}
applied_by:
  - {"item": 709}
---
<!-- generated:start -->
<!-- generated-keys: title=4a6882 type=6143a1 id=dc229a sources=8810bd name_key=493094 duration=995f11 is_buff=b6589f stack_type=356a19 group=009cf5 effects=faa4d7 icon=dac448 applied_by=6c14bd -->
|  |  |
|---|---|
|  | ![Tome of the Magician (B) : Ability Power +48](../assets/buffs/2082.png) |
| **Buff id** | `2082` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2077 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 57 |

### Tooltip

> Tome of the Magician [B] : Ability Power +48

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 2 | Ability Power | 48 |

### Applied by

- Using [[wiki/items/709-scroll-of-the-magician-b|Scroll of the Magician (B)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Scroll of the Magician [B] (item 709), a Scroll clickable: +48 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Ability Power +24 / +48 / +72 / +120). *client*
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

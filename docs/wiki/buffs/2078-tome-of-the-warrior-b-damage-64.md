---
title: "Tome of the Warrior [B]: Damage +64"
type: "buff"
id: 2078
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2078", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)"]
name_key: "SkillBuff_2078"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2077
effects:
  - {"code": 1, "stat": "Attack", "value": 64}
icon: {"file": "Items_03.png", "index": 53}
applied_by:
  - {"item": 705}
---
<!-- generated:start -->
<!-- generated-keys: title=9c64c6 type=6143a1 id=bcc3fe sources=f34e3d name_key=a9b9d1 duration=995f11 is_buff=b6589f stack_type=356a19 group=009cf5 effects=8661e9 icon=082161 applied_by=7f1553 -->
|  |  |
|---|---|
|  | ![Tome of the Warrior (B): Damage +64](../assets/buffs/2078.png) |
| **Buff id** | `2078` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2077 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 53 |

### Tooltip

> Tome of the Warrior [B]: Damage +64

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 1 | Attack | 64 |

### Applied by

- Using [[wiki/items/705-scroll-of-the-warrior-b|Scroll of the Warrior (B)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Scroll of the Warrior [B] (item 705), a Scroll clickable: Attack +64 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Attack +32 / Attack +64 / Attack +96 / Attack +160). *client*
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

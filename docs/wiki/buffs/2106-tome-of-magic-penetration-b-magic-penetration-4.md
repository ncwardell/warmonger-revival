---
title: "Tome of Magic Penetration [B] : Magic Penetration +4"
type: "buff"
id: 2106
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2106", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "notes: [[gameplay/reinforce-and-runes]] §7, WM 0420 (penetration scrolls removed)"]
name_key: "SkillBuff_2106"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2077
effects:
  - {"code": 14, "stat": "Magic resist Penetration", "value": 4}
icon: {"file": "Items_04.png", "index": 17}
applied_by:
  - {"item": 733}
---
<!-- generated:start -->
<!-- generated-keys: title=df8fdb type=6143a1 id=02e0a5 sources=cc16d1 name_key=8515c5 duration=995f11 is_buff=b6589f stack_type=356a19 group=009cf5 effects=2d528d icon=88e6a0 applied_by=5081b5 -->
|  |  |
|---|---|
|  | ![Tome of Magic Penetration (B) : Magic Penetration +4](../assets/buffs/2106.png) |
| **Buff id** | `2106` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2077 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_04.png` cell 17 |

### Tooltip

> Tome of Magic Penetration [B] : Magic Penetration +4

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 14 | Magic resist Penetration | 4 |

### Applied by

- Using [[wiki/items/733-scroll-of-magic-pnt-b|Scroll of Magic PNT (B)]] (Item_Base option 301)
<!-- generated:end -->

## Notes

- Buff of Scroll of Magic PNT [B] (item 733), a Scroll clickable: +4 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Magic penetration +2 / +4 / +6 / +8). *client*
- One active per family: it shares exclusive group 2077 (Warrior, Magician, Armor PNT, Magic PNT), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The client names the buff the other way round from the item (Scroll ↔ Tome); [[gameplay/consumables]] says to use the item names. *client*
- [WM 0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397) says the Scrolls of Armor/MR Penetration were removed from the game ([[gameplay/reinforce-and-runes]] §7). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §1–§4, [[gameplay/items-and-crafting]], [[gameplay/reinforce-and-runes]] §7.

## Open questions

- Removed in WM 0420 by the patch note, but the buff and its items are still in the final client. Whether a server should offer them is open.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

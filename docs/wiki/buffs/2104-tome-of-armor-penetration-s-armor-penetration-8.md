---
title: "Tome of Armor Penetration [S] : Armor Penetration +8"
type: "buff"
id: 2104
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2104", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §2 (value, 5 min, exclusive group, recipe)", "sheet: [[gameplay/stat-values]] §5 Sheet3 (Crush-era S values; history)", "notes: [[gameplay/reinforce-and-runes]] §7, WM 0420 (penetration scrolls removed)"]
name_key: "SkillBuff_2104"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2077
effects:
  - {"code": 13, "stat": "Armor Penetration", "value": 8}
icon: {"file": "Items_04.png", "index": 15}
applied_by:
  - {"item": 731}
---
<!-- generated:start -->
<!-- generated-keys: title=e96c40 type=6143a1 id=a8c97e sources=7a99f7 name_key=deafc5 duration=995f11 is_buff=b6589f stack_type=356a19 group=009cf5 effects=4b598f icon=a68b30 applied_by=68d641 -->
|  |  |
|---|---|
|  | ![Tome of Armor Penetration (S) : Armor Penetration +8](../assets/buffs/2104.png) |
| **Buff id** | `2104` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2077 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_04.png` cell 15 |

### Tooltip

> Tome of Armor Penetration [S] : Armor Penetration +8

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 13 | Armor Penetration | 8 |

### Applied by

- Using [[wiki/items/731-scroll-of-armor-pnt-s|Scroll of Armor PNT (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 53): Scroll · Scroll of Armor PNT · 728–731 · 2101–2104 · Armor penetration +2 / 4 / 6 / 8
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 78): Scroll S · Attack 35, Ability 35, Armor pen 16, Magic pen 16 · Warrior +160 Attack (2080), Magician +120 AP (2084), Armor Pen +8 (2104), Magic Pen +8 (2108)...
<!-- generated:end -->

## Notes

- Buff of Scroll of Armor PNT [S] (item 731), a Scroll clickable: +8 for 5 min (1,500 ticks) ([[gameplay/consumables]] §2; per-grade row Armor penetration +2 / +4 / +6 / +8). *client*
- One active per family: it shares exclusive group 2077 (Warrior, Magician, Armor PNT, Magic PNT), so using another of the group replaces it and restarts the timer ([[gameplay/consumables]] §1, buffs guide §3; [[gameplay/items-and-crafting]]). *client + guide*
- C grade is bought from Lewellyn; B, A and S are only crafted at Owen (1 container + powder + secondary → 10), and A / S need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables]] §1, §2, §4). *client*
- The client names the buff the other way round from the item (Scroll ↔ Tome); [[gameplay/consumables]] says to use the item names. *client*
- The Crush-era Crush Share sheet (Sheet3) lists Scroll S: Armor pen 16 (client 8; disagrees) ([[gameplay/stat-values]] §5). *sheet*
- [WM 0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397) says the Scrolls of Armor/MR Penetration were removed from the game ([[gameplay/reinforce-and-runes]] §7). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §1–§4, [[gameplay/items-and-crafting]], [[gameplay/stat-values]] §5, [[gameplay/reinforce-and-runes]] §7.

## Open questions

- Crush-era sheet values differ from the client (see Notes); the client value is kept.
- Removed in WM 0420 by the patch note, but the buff and its items are still in the final client. Whether a server should offer them is open.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

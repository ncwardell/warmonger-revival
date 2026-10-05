---
title: "Blessing of Shaia [Donation +30%] Movement speed increases in non-combat state, increases mana. Points are wasted during combat or hunting and additional effects are gained. War : medal acquisition and fame acquisition increased by 130% Hunting : Drop rate and EXP increased by 60%"
type: "buff"
id: 19
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 19", "notes: [[gameplay/events-and-schedules]] §6 Shaia Blessing (WM 0809/0817/1107)", "notes: [[gameplay/events-and-schedules]] §6 Shaia Legion donations, WM 1128"]
name_key: "SkillBuff_19"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 20, "stat": "code 20 (unknown)", "value": 150}
  - {"code": 33, "stat": "Mana", "value": 200}
icon: {"file": "Items_15.png", "index": 56}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=16b568 type=6143a1 id=b3f0c7 sources=ce5f72 name_key=bc51c7 duration=6c141f is_buff=b6589f stack_type=356a19 group=b6589f effects=f76543 icon=4037b4 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Blessing of Shaia (Donation +30%) Movement speed increases in non-combat state, increases mana. Points are wasted during combat or hunting and additional effects are gained. War : medal acquisition and fame acquisition increased by 130% Hunting : Drop rate and EXP increased by 60%](../assets/buffs/19.png) |
| **Buff id** | `19` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_15.png` cell 56 |

### Tooltip

> Blessing of Shaia [Donation +30%]
>
> Movement speed increases in non-combat state, increases mana.
> Points are wasted during combat or hunting and additional effects are gained.
> War : medal acquisition and fame acquisition increased by 130%
> Hunting : Drop rate and EXP increased by 60%

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 20 | code 20 (unknown) | 150 |
| 33 | Mana | 200 |
<!-- generated:end -->

## Notes

- Shaia Blessing point buff ([WM 0809](https://steamcommunity.com/games/718790/announcements/detail/2454911758739952435), changed in [WM 0817](https://steamcommunity.com/games/718790/announcements/detail/2444779293764867295) and [WM 1107](https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770)): a point pool up to 10,000; the buff is active while the player has points. Points come from a starting amount, time in a village/fortress/castle/training camp or offline 30+ min (5 per minute, capped at 2,000 → 1,000 from 1107) and the Blessing of Shaia item (1,000 → 2,000 points from 1107). Each normal monster kill spends 5 (→ 10) and each boss 100; in Gaia wars the cost depends on fame and medals. Normal tier (1–2,000 points): 100 % fame and medal points, monster EXP and drop +20 %; Gold tier (2,001–10,000): 130 %, +30 % ([[gameplay/events-and-schedules]] §6). *notes + image*
- The "[Donation +N %]" rows match the Shaia legion donations of [WM 1128](https://steamcommunity.com/games/718790/announcements/detail/2415515408464895311): each member may give 200,000 gold a day; the legion's weekly reward raises Shaia by 10 % (tiers 1–3, 3–10 M gold), 20 % (tiers 4–6, 15–35 M) or 30 % (tier 7, 45 M) ([[gameplay/events-and-schedules]] §6). *notes + image*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/events-and-schedules]] §6.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

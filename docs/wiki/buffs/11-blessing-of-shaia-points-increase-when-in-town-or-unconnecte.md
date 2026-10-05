---
title: "Blessing of Shaia Points increase when in town or unconnected state."
type: "buff"
id: 11
status: "partial"
missing: ["effects"]
sources: ["client: Skill_Buff.cdb id 11", "notes: [[gameplay/events-and-schedules]] §6 Shaia Blessing (WM 0809/0817/1107)"]
name_key: "SkillBuff_11"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 0
effects: []
icon: {"file": "Items_15.png", "index": 48}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=d325e4 type=6143a1 id=17ba07 sources=6170ec name_key=727946 duration=6c141f is_buff=b6589f stack_type=356a19 group=b6589f effects=97d170 icon=abcd01 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Blessing of Shaia Points increase when in town or unconnected state.](../assets/buffs/11.png) |
| **Buff id** | `11` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_15.png` cell 48 |

### Tooltip

> Blessing of Shaia
>
> Points increase when in town or unconnected state.

### Effects

No effect codes in the client: what this buff does (a stun, a mark, a status) is server-side. Add `effects:` by hand when known.
<!-- generated:end -->

## Notes

- Shaia Blessing point buff ([WM 0809](https://steamcommunity.com/games/718790/announcements/detail/2454911758739952435), changed in [WM 0817](https://steamcommunity.com/games/718790/announcements/detail/2444779293764867295) and [WM 1107](https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770)): a point pool up to 10,000; the buff is active while the player has points. Points come from a starting amount, time in a village/fortress/castle/training camp or offline 30+ min (5 per minute, capped at 2,000 → 1,000 from 1107) and the Blessing of Shaia item (1,000 → 2,000 points from 1107). Each normal monster kill spends 5 (→ 10) and each boss 100; in Gaia wars the cost depends on fame and medals. Normal tier (1–2,000 points): 100 % fame and medal points, monster EXP and drop +20 %; Gold tier (2,001–10,000): 130 %, +30 % ([[gameplay/events-and-schedules]] §6). *notes + image*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/events-and-schedules]] §6.

## Open questions

- Effects: the point-gain row has no stat effect in the client or any source.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

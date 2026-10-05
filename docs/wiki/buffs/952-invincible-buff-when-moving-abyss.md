---
title: "Invincible buff when moving Abyss"
type: "buff"
id: 952
status: "partial"
missing: ["effects"]
sources: ["client: Skill_Buff.cdb id 952", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "notes: [[gameplay/events-and-schedules]] §9 and [[gameplay/patch-history]], WM 0404 (5 s; matches client)"]
name_key: "SkillBuff_952"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 11
effects: []
icon: {"file": "Items_05.png", "index": 22}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=f2d053 type=6143a1 id=da5e05 sources=844613 name_key=81f0a7 duration=870e64 is_buff=b6589f stack_type=356a19 group=17ba07 effects=97d170 icon=a9a294 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Invincible buff when moving Abyss](../assets/buffs/952.png) |
| **Buff id** | `952` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 11 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_05.png` cell 22 |

### Tooltip

> Invincible buff when moving Abyss

### Effects

No effect codes in the client: what this buff does (a stun, a mark, a status) is server-side. Add `effects:` by hand when known.
<!-- generated:end -->

## Notes

- [WM 0404](https://steamcommunity.com/games/718790/announcements/detail/2394101748794304355) gave players **5 s** of immunity on moving in the Abyss ([[gameplay/events-and-schedules]] §9; [[gameplay/patch-history]] Dungeons and world). The client buff lasts 25 ticks = 5 s. *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]].

## Open questions

- Effects: the client row has no effect code and no source names one; invulnerability is implied by the name only.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

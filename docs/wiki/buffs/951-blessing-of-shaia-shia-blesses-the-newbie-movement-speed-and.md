---
title: "Blessing of Shaia Shia blesses the newbie. Movement speed and mana increase."
type: "buff"
id: 951
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 951", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "notes: [[gameplay/reinforce-and-runes]] §7, WM 0705 / 0802 (move +150, mana +200; matches client)"]
name_key: "SkillBuff_951"
duration: {"ticks": 18000, "seconds": 3600.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 20, "stat": "code 20 (unknown)", "value": 150}
  - {"code": 33, "stat": "Mana", "value": 200}
icon: {"file": "Items_15.png", "index": 9}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=21bf87 type=6143a1 id=69fa65 sources=67a18b name_key=c714cd duration=23bd3e is_buff=b6589f stack_type=356a19 group=b6589f effects=f76543 icon=c0e73b applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Blessing of Shaia Shia blesses the newbie. Movement speed and mana increase.](../assets/buffs/951.png) |
| **Buff id** | `951` |
| **Duration** | 60 min (18,000 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_15.png` cell 9 |

### Tooltip

> Blessing of Shaia
>
> Shia blesses the newbie.
> Movement speed and mana increase.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 20 | code 20 (unknown) | 150 |
| 33 | Mana | 200 |
<!-- generated:end -->

## Notes

- Matches the Mystical Potion renamed "Blessing of Shaia" (item 905): out-of-combat movement speed +150 and mana +200, only one active, no stacking ([WM 0705](https://steamcommunity.com/games/718790/announcements/detail/2499943313680174373), [WM 0802](https://steamcommunity.com/games/718790/announcements/detail/2451533424634152745); [[gameplay/reinforce-and-runes]] §7). The client buff has the same two values. *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/reinforce-and-runes]] §7.

## Open questions

- Item 905 is not linked to this buff in `Item_Base` (no option 301); the match is by values and name only.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

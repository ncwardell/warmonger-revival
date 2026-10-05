---
title: "Increases drop rate and EXP by 20%."
type: "buff"
id: 2136
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2136", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §3", "notes: [[gameplay/reinforce-and-runes]] §7 and [[gameplay/patch-history]] Dungeons, WM 0726 (matches client)"]
name_key: "SkillBuff_2136"
duration: {"ticks": 3000, "seconds": 600.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2135
effects:
  - {"code": 273, "stat": "Drop Chance(%)", "value": 20}
  - {"code": 271, "stat": "code 271 (unknown)", "value": 20}
icon: {"file": "Items_15.png", "index": 17}
applied_by:
  - {"item": 690}
---
<!-- generated:start -->
<!-- generated-keys: title=2d52ee type=6143a1 id=ac5c09 sources=2c855d name_key=258334 duration=dc6a42 is_buff=b6589f stack_type=356a19 group=ff075d effects=d3c7da icon=2fba78 applied_by=ed6b60 -->
|  |  |
|---|---|
|  | ![Increases drop rate and EXP by 20%.](../assets/buffs/2136.png) |
| **Buff id** | `2136` |
| **Duration** | 10 min (3,000 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2135 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_15.png` cell 17 |

### Tooltip

> Increases drop rate and EXP by 20%.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 273 | Drop Chance(%) | 20 |
| 271 | code 271 (unknown) | 20 |

### Applied by

- Using [[wiki/items/690-tier-2-time-energy|Tier 2 : Time energy]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 3. Potions and other clickables (line 87): 689 / 690 / 691 · Tier 1 / 2 / 3 : Time energy · 2135 / 2136 / 2137 · Drop chance and EXP +10 / 20 / 30% (opts 273, 271) · 10 min (3000) · currency 10 / 11 /...
<!-- generated:end -->

## Notes

- Buff of Tier 2 : Time energy (item 690): drop chance and EXP +20 % for 10 min (3,000 ticks) ([[gameplay/consumables]] §3). From [WM 0726](https://steamcommunity.com/games/718790/announcements/detail/2462791699369817744) Time Energy became these buffs (it was the dungeon entry fee before) ([[gameplay/reinforce-and-runes]] §7; [[gameplay/patch-history]] Dungeons). Exclusive group 2135 ([[gameplay/consumables]] §1). *client + notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §3, [[gameplay/reinforce-and-runes]] §7, [[gameplay/patch-history]].

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

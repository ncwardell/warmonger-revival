---
title: "Transformation : Slime"
type: "buff"
id: 910
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 910", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/consumables]] §1, §3", "notes: [[gameplay/reinforce-and-runes]] §7, WM 0503 (3 → 5 min; matches client)", "video: [[gameplay/video-early-quests]] Wren shop, 16:54 (7,920 gold)"]
name_key: "SkillBuff_910"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1150
effects:
  - {"code": 361, "stat": "code 361 (unknown)", "value": 0}
  - {"code": 360, "stat": "code 360 (unknown)", "value": 627}
  - {"code": 302, "stat": "code 302 (unknown)", "value": 1150}
icon: {"file": "Items_07.png", "index": 35}
applied_by:
  - {"item": 762}
---
<!-- generated:start -->
<!-- generated-keys: title=5ca377 type=6143a1 id=c70dfb sources=3bc802 name_key=cbc839 duration=995f11 is_buff=b6589f stack_type=356a19 group=e9a20a effects=67f83c icon=d402c6 applied_by=0a3da3 -->
|  |  |
|---|---|
|  | ![Transformation : Slime](../assets/buffs/910.png) |
| **Buff id** | `910` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1150 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_07.png` cell 35 |

### Tooltip

> Transformation : Slime

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 361 | code 361 (unknown) | 0 |
| 360 | code 360 (unknown) | 627 |
| 302 | code 302 (unknown) | 1,150 |

### Applied by

- Using [[wiki/items/762-scroll-of-transform-slime|Scroll of Transform : (Slime)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 3. Potions and other clickables (line 89): 760 / 761 / 762 · Scroll of Transform: Golem / Demon / Slime · 1150 / 1152 / 910 · Turn into unit 613 / 741 / 627 · 5 min · 1,000 gold base (kind 19)
<!-- generated:end -->

## Notes

- Buff of Scroll of Transform: Slime (item 762): turns the user into unit 627 for 5 min ([[gameplay/consumables]] §3). [WM 0503](https://steamcommunity.com/games/718790/announcements/detail/2394104285094559240) raised the transformation scroll duration 3 → **5 min** ([[gameplay/reinforce-and-runes]] §7). Exclusive group 1150 (Transform) ([[gameplay/consumables]] §1). *client + notes*
- Wren in the Training Camp sold the Golem, Demon and Slime scrolls for 7,920 gold each ([[gameplay/video-early-quests]], [16:54](https://www.youtube.com/watch?v=s04CSN16w1s&t=1014s)). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/consumables]] §3, [[gameplay/reinforce-and-runes]] §7, [[gameplay/video-early-quests]].

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

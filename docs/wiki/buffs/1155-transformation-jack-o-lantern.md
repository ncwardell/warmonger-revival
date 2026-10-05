---
title: "Transformation : Jack O' Lantern"
type: "buff"
id: 1155
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 1155", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_1155"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1150
effects:
  - {"code": 361, "stat": "code 361 (unknown)", "value": 0}
  - {"code": 360, "stat": "code 360 (unknown)", "value": 2000}
  - {"code": 302, "stat": "code 302 (unknown)", "value": 1150}
icon: {"file": "Items_07.png", "index": 54}
applied_by:
  - {"item": 763}
---
<!-- generated:start -->
<!-- generated-keys: title=7aefb1 type=6143a1 id=1955bf sources=e513ea name_key=21fcfa duration=995f11 is_buff=b6589f stack_type=356a19 group=e9a20a effects=2a4686 icon=c7a58c applied_by=720273 -->
|  |  |
|---|---|
|  | ![Transformation : Jack O' Lantern](../assets/buffs/1155.png) |
| **Buff id** | `1155` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1150 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_07.png` cell 54 |

### Tooltip

> Transformation  : Jack O' Lantern

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 361 | code 361 (unknown) | 0 |
| 360 | code 360 (unknown) | 2,000 |
| 302 | code 302 (unknown) | 1,150 |

### Applied by

- Using [[wiki/items/763-scroll-of-transform-jack|Scroll of Transform : (Jack)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 3. Potions and other clickables (line 90): 763 · Scroll of Transform: Jack · 1155 · Turn into unit 2000 (pumpkin) · 5 min · 10 gold base (event item, guess)
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

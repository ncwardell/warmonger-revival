---
title: "Flask of Tenacity [A] : Tenacity +10, Mana Steal with each attack +2"
type: "buff"
id: 2129
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2129", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2129"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 42, "stat": "Devour(%)", "value": 2}
  - {"code": 269, "stat": "Toughness(%)", "value": 10}
icon: {"file": "Items_30.png", "index": 22}
applied_by:
  - {"item": 756}
---
<!-- generated:start -->
<!-- generated-keys: title=62816f type=6143a1 id=a40eb3 sources=871fed name_key=204485 duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=d96241 icon=25b590 applied_by=7a7b73 -->
|  |  |
|---|---|
|  | ![Flask of Tenacity (A) : Tenacity +10, Mana Steal with each attack +2](wiki/assets/buffs/2129.png) |
| **Buff id** | `2129` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 22 |

### Tooltip

> Flask of Tenacity [A] : Tenacity +10, Mana Steal with each attack +2

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 42 | Devour(%) | 2 |
| 269 | Toughness(%) | 10 |

### Applied by

- Using [[wiki/items/756-flask-of-tenacity-c|Flask of Tenacity (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 64): Flask · Flask of Tenacity · 756–759 · 2129–2132 · Mana steal per hit 2 / 4 / 6 / 8 and Tenacity +10 / 20 / 30 / 40
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

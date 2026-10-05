---
title: "Flask of Devour [S] : 8 Mana Steal with each attack. Maximum Mana +200"
type: "buff"
id: 2124
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2124", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2124"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 42, "stat": "Devour(%)", "value": 8}
  - {"code": 33, "stat": "Mana", "value": 200}
icon: {"file": "Items_30.png", "index": 33}
applied_by:
  - {"item": 751}
---
<!-- generated:start -->
<!-- generated-keys: title=9d3a3a type=6143a1 id=59a121 sources=288613 name_key=d895f4 duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=00f0e7 icon=881255 applied_by=4f1e17 -->
|  |  |
|---|---|
|  | ![Flask of Devour (S) : 8 Mana Steal with each attack. Maximum Mana +200](wiki/assets/buffs/2124.png) |
| **Buff id** | `2124` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 33 |

### Tooltip

> Flask of Devour [S] : 8 Mana Steal with each attack. 
> Maximum Mana +200

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 42 | Devour(%) | 8 |
| 33 | Mana | 200 |

### Applied by

- Using [[wiki/items/751-flask-of-devour-s|Flask of Devour (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 63): Flask · Flask of Devour · 748–751 · 2121–2124 · Mana steal per hit 2 / 4 / 6 / 8 and max MP +50 / 100 / 150 / 200
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 82): Flask 1 · MP on hit 8, MP 120 · Devour: Mana steal 8, MP 200 (2124) · steal yes, MP no
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

---
title: "Flask of Tenacity [B] : Tenacity +20, Mana Steal with each attack +4"
type: "buff"
id: 2130
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2130", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2130"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2113
effects:
  - {"code": 42, "stat": "Devour(%)", "value": 4}
  - {"code": 269, "stat": "Toughness(%)", "value": 20}
icon: {"file": "Items_30.png", "index": 25}
applied_by:
  - {"item": 757}
---
<!-- generated:start -->
<!-- generated-keys: title=2184d9 type=6143a1 id=9fb005 sources=85f3e3 name_key=e563fc duration=995f11 is_buff=b6589f stack_type=356a19 group=88b726 effects=5c8db4 icon=e80c37 applied_by=0069bf -->
|  |  |
|---|---|
|  | ![Flask of Tenacity (B) : Tenacity +20, Mana Steal with each attack +4](../assets/buffs/2130.png) |
| **Buff id** | `2130` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2113 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 25 |

### Tooltip

> Flask of Tenacity [B] : Tenacity +20, Mana Steal with each attack +4

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 42 | Devour(%) | 4 |
| 269 | Toughness(%) | 20 |

### Applied by

- Using [[wiki/items/757-flask-of-tenacity-b|Flask of Tenacity (B)]] (Item_Base option 301)
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

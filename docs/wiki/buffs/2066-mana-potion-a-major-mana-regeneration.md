---
title: "Mana Potion [A] : Major Mana regeneration"
type: "buff"
id: 2066
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2066", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2066"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 34, "stat": "Mana Regeneration", "value": 16}
icon: {"file": "Items_01.png", "index": 8}
applied_by:
  - {"item": 891}
---
<!-- generated:start -->
<!-- generated-keys: title=020ff3 type=6143a1 id=2dfa38 sources=32f1c3 name_key=aee417 duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=c63e2d icon=a120a7 applied_by=4368a8 -->
|  |  |
|---|---|
|  | ![Mana Potion (A) : Major Mana regeneration](../assets/buffs/2066.png) |
| **Buff id** | `2066` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 8 |

### Tooltip

> Mana Potion [A] : Major Mana regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 34 | Mana Regeneration | 16 |

### Applied by

- Using [[wiki/items/891-potion-of-mana-a|Potion of Mana (A)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 28): 891 · Potion of Mana [A] · 135 · 40 · 2066 · – · 16
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

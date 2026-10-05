---
title: "Omni Potion [A] : Major Omni Regeneration"
type: "buff"
id: 2071
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2071", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2071"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 31}
  - {"code": 34, "stat": "Mana Regeneration", "value": 6}
icon: {"file": "Items_01.png", "index": 13}
applied_by:
  - {"item": 896}
---
<!-- generated:start -->
<!-- generated-keys: title=4c6576 type=6143a1 id=739adc sources=67a4c3 name_key=97b8fd duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=6459a5 icon=16e1b9 applied_by=9e7ef0 -->
|  |  |
|---|---|
|  | ![Omni Potion (A) : Major Omni Regeneration](../assets/buffs/2071.png) |
| **Buff id** | `2071` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 13 |

### Tooltip

> Omni Potion [A] : Major Omni Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 31 |
| 34 | Mana Regeneration | 6 |

### Applied by

- Using [[wiki/items/896-health-mana-potion-a|Health Mana Potion (A)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 33): 896 · Health Mana Potion [A] · 151 · 40 · 2071 · 31 · 6
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

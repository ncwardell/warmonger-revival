---
title: "Omni Potion [D] : Weak Omni Regeneration"
type: "buff"
id: 2068
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2068", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2068"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 13}
  - {"code": 34, "stat": "Mana Regeneration", "value": 3}
icon: {"file": "Items_01.png", "index": 10}
applied_by:
  - {"item": 893}
---
<!-- generated:start -->
<!-- generated-keys: title=bf2eef type=6143a1 id=274438 sources=ef82e9 name_key=d6f630 duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=dee64b icon=258247 applied_by=4834ca -->
|  |  |
|---|---|
|  | ![Omni Potion (D) : Weak Omni Regeneration](wiki/assets/buffs/2068.png) |
| **Buff id** | `2068` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 10 |

### Tooltip

> Omni Potion [D] : Weak Omni Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 13 |
| 34 | Mana Regeneration | 3 |

### Applied by

- Using [[wiki/items/893-health-mana-potion-d|Health Mana Potion (D)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 30): 893 · Health Mana Potion [D] · 25 · 10 · 2068 · 13 · 3
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

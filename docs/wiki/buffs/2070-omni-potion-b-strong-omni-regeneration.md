---
title: "Omni Potion [B] : Strong Omni Regeneration"
type: "buff"
id: 2070
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2070", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2070"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 25}
  - {"code": 34, "stat": "Mana Regeneration", "value": 5}
icon: {"file": "Items_01.png", "index": 12}
applied_by:
  - {"item": 895}
---
<!-- generated:start -->
<!-- generated-keys: title=bc0a06 type=6143a1 id=0164a5 sources=8810b4 name_key=ada4dc duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=7c2214 icon=be594a applied_by=99e02b -->
|  |  |
|---|---|
|  | ![Omni Potion (B) : Strong Omni Regeneration](../assets/buffs/2070.png) |
| **Buff id** | `2070` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 12 |

### Tooltip

> Omni Potion [B] : Strong Omni Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 25 |
| 34 | Mana Regeneration | 5 |

### Applied by

- Using [[wiki/items/895-health-mana-potion-b|Health Mana Potion (B)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 32): 895 · Health Mana Potion [B] · 100 · 30 · 2070 · 25 · 5
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

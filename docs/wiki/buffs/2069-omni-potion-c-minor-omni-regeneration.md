---
title: "Omni Potion [C] : Minor Omni Regeneration"
type: "buff"
id: 2069
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2069", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2069"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 19}
  - {"code": 34, "stat": "Mana Regeneration", "value": 4}
icon: {"file": "Items_01.png", "index": 11}
applied_by:
  - {"item": 894}
---
<!-- generated:start -->
<!-- generated-keys: title=f266d0 type=6143a1 id=100b22 sources=08c29c name_key=f5d1a0 duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=113826 icon=f46d20 applied_by=8d6443 -->
|  |  |
|---|---|
|  | ![Omni Potion (C) : Minor Omni Regeneration](wiki/assets/buffs/2069.png) |
| **Buff id** | `2069` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 11 |

### Tooltip

> Omni Potion [C] : Minor Omni Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 19 |
| 34 | Mana Regeneration | 4 |

### Applied by

- Using [[wiki/items/894-health-mana-potion-c|Health Mana Potion (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 31): 894 · Health Mana Potion [C] · 80 · 20 · 2069 · 19 · 4
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

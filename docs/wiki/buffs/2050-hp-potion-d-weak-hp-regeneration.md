---
title: "HP Potion [D]: Weak HP Regeneration"
type: "buff"
id: 2050
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2050", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2050"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 25}
icon: {"file": "Items_01.png", "index": 0}
applied_by:
  - {"item": 883}
---
<!-- generated:start -->
<!-- generated-keys: title=6563e8 type=6143a1 id=cb58c3 sources=9a0ca6 name_key=eec714 duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=04d34b icon=e23161 applied_by=8f43b1 -->
|  |  |
|---|---|
|  | ![HP Potion (D): Weak HP Regeneration](../assets/buffs/2050.png) |
| **Buff id** | `2050` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 0 |

### Tooltip

> HP Potion [D]: Weak HP Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 25 |

### Applied by

- Using [[wiki/items/883-potion-of-health-d|Potion of Health (D)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 20): 883 · Potion of Health [D] · 10 · 10 · 2050 · 25 · –
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

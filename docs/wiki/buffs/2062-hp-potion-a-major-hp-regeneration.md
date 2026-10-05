---
title: "HP Potion [A]: Major HP Regeneration"
type: "buff"
id: 2062
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2062", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2062"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 63}
icon: {"file": "Items_01.png", "index": 3}
applied_by:
  - {"item": 887}
  - {"item": 2598}
---
<!-- generated:start -->
<!-- generated-keys: title=24899d type=6143a1 id=329bcc sources=4f5b96 name_key=fb0ff2 duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=6a3780 icon=966ff7 applied_by=d8980d -->
|  |  |
|---|---|
|  | ![HP Potion (A): Major HP Regeneration](wiki/assets/buffs/2062.png) |
| **Buff id** | `2062` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 3 |

### Tooltip

> HP Potion [A]: Major HP Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 63 |

### Applied by

- Using [[wiki/items/887-potion-of-health-a|Potion of Health (A)]] (Item_Base option 301)
- Using [[wiki/items/2598-potion-of-health-quest|Potion of Health (Quest)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 3. Potions and other clickables (line 91): 2598 / 2599 · Potion of Health [Quest] / Tome of Cooldown [Quest] · 2062 / 2091 · Same as Health [A] / Cooldown [A] · 17 s / 5 min · quest recipes 749 / 599
- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 23): 887 · Potion of Health [A] · 135 · 40 · 2062 · 63 · –
- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 35): 2598 · Potion of Health [Quest] · 135 · 40 · 2062 · 63 · –
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

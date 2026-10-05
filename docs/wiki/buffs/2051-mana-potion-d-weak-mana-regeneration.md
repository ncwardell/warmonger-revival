---
title: "Mana Potion [D] : Weak Mana Regeneration"
type: "buff"
id: 2051
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2051", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2051"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 34, "stat": "Mana Regeneration", "value": 6}
icon: {"file": "Items_01.png", "index": 5}
applied_by:
  - {"item": 884}
---
<!-- generated:start -->
<!-- generated-keys: title=799cbf type=6143a1 id=33b82c sources=d3aac0 name_key=ec185b duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=52b377 icon=7bc914 applied_by=741af8 -->
|  |  |
|---|---|
|  | ![Mana Potion (D) : Weak Mana Regeneration](../assets/buffs/2051.png) |
| **Buff id** | `2051` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 5 |

### Tooltip

> Mana Potion [D] : Weak Mana Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 34 | Mana Regeneration | 6 |

### Applied by

- Using [[wiki/items/884-potion-of-mana-d|Potion of Mana (D)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 25): 884 · Potion of Mana [D] · 10 · 10 · 2051 · – · 6
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

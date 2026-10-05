---
title: "Mana Potion [B] : Strong Mana regeneration"
type: "buff"
id: 2065
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2065", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2065"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 34, "stat": "Mana Regeneration", "value": 13}
icon: {"file": "Items_01.png", "index": 7}
applied_by:
  - {"item": 890}
---
<!-- generated:start -->
<!-- generated-keys: title=2becae type=6143a1 id=aa9127 sources=d7de20 name_key=2e1b29 duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=a665b4 icon=33f4fc applied_by=e75755 -->
|  |  |
|---|---|
|  | ![Mana Potion (B) : Strong Mana regeneration](../assets/buffs/2065.png) |
| **Buff id** | `2065` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 7 |

### Tooltip

> Mana Potion [B] : Strong Mana regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 34 | Mana Regeneration | 13 |

### Applied by

- Using [[wiki/items/890-potion-of-mana-b|Potion of Mana (B)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 27): 890 · Potion of Mana [B] · 90 · 30 · 2065 · – · 13
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

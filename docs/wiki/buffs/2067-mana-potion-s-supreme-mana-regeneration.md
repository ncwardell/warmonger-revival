---
title: "Mana Potion [S] : Supreme Mana regeneration"
type: "buff"
id: 2067
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2067", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2067"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 34, "stat": "Mana Regeneration", "value": 19}
icon: {"file": "Items_01.png", "index": 9}
applied_by:
  - {"item": 892}
---
<!-- generated:start -->
<!-- generated-keys: title=cf12d0 type=6143a1 id=14e7c3 sources=2c34ec name_key=bd20b2 duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=43677d icon=8f8284 applied_by=aae0e0 -->
|  |  |
|---|---|
|  | ![Mana Potion (S) : Supreme Mana regeneration](wiki/assets/buffs/2067.png) |
| **Buff id** | `2067` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 9 |

### Tooltip

> Mana Potion [S] : Supreme Mana regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 34 | Mana Regeneration | 19 |

### Applied by

- Using [[wiki/items/892-potion-of-mana-s|Potion of Mana (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 29): 892 · Potion of Mana [S] · 182 · 50 · 2067 · – · 19
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

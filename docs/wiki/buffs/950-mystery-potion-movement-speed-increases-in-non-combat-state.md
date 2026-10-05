---
title: "Mystery Potion Movement speed increases in non-combat state, increases mana."
type: "buff"
id: 950
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 950", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_950"
duration: {"ticks": 18000, "seconds": 3600.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 20, "stat": "code 20 (unknown)", "value": 150}
  - {"code": 33, "stat": "Mana", "value": 200}
icon: {"file": "Items_15.png", "index": 9}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=691314 type=6143a1 id=b63c6a sources=eaf7e4 name_key=0e275a duration=23bd3e is_buff=b6589f stack_type=356a19 group=b6589f effects=f76543 icon=c0e73b applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Mystery Potion Movement speed increases in non-combat state, increases mana.](../assets/buffs/950.png) |
| **Buff id** | `950` |
| **Duration** | 60 min (18,000 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_15.png` cell 9 |

### Tooltip

> Mystery Potion
>
> Movement speed increases in non-combat state, increases mana.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 20 | code 20 (unknown) | 150 |
| 33 | Mana | 200 |
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

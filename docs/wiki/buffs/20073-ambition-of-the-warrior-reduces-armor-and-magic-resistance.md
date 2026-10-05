---
title: "Ambition of the Warrior : Reduces Armor and Magic Resistance"
type: "buff"
id: 20073
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20073", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10238"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 106, "stat": "Armor(%)", "value": -20}
  - {"code": 107, "stat": "Magic Resist(%)", "value": -20}
icon: {"file": "Items_20.png", "index": 27}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=8856a2 type=6143a1 id=02888c sources=cd2fba name_key=1d350a duration=0aac5a is_buff=b6589f stack_type=356a19 group=b6589f effects=f8da5d icon=13db30 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Ambition of the Warrior : Reduces Armor and Magic Resistance](wiki/assets/buffs/20073.png) |
| **Buff id** | `20073` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_20.png` cell 27 |

### Tooltip

> Ambition of the Warrior : Reduces Armor and Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 106 | Armor(%) | -20 |
| 107 | Magic Resist(%) | -20 |
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

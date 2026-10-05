---
title: "Ambition of the Warrior : Reduces Armor and Magic Resistance by 30%."
type: "buff"
id: 10250
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10250", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10250"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 6, "stat": "Armor", "value": -30}
  - {"code": 7, "stat": "Magic Resist", "value": -30}
icon: {"file": "Policy.png", "index": 32}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=5f1057 type=6143a1 id=893dbd sources=4f9a87 name_key=aabc4e duration=0aac5a is_buff=b6589f stack_type=356a19 group=b6589f effects=4768c9 icon=1bc8e5 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Ambition of the Warrior : Reduces Armor and Magic Resistance by 30%.](../assets/buffs/10250.png) |
| **Buff id** | `10250` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 32 |

### Tooltip

> Ambition of the Warrior : Reduces Armor and Magic Resistance by 30%.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 6 | Armor | -30 |
| 7 | Magic Resist | -30 |
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

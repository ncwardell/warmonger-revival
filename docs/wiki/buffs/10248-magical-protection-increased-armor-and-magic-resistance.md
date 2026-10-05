---
title: "Magical Protection : Increased Armor and Magic Resistance."
type: "buff"
id: 10248
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10248", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10248"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10248
effects:
  - {"code": 6, "stat": "Armor", "value": 80}
  - {"code": 7, "stat": "Magic Resist", "value": 80}
icon: {"file": "Policy.png", "index": 34}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=7a743c type=6143a1 id=3264ab sources=44f4e9 name_key=b45c6d duration=870e64 is_buff=b6589f stack_type=356a19 group=3264ab effects=f0fa3f icon=9835a6 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Magical Protection : Increased Armor and Magic Resistance.](../assets/buffs/10248.png) |
| **Buff id** | `10248` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10248 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy.png` cell 34 |

### Tooltip

> Magical Protection : Increased Armor and Magic Resistance.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 6 | Armor | 80 |
| 7 | Magic Resist | 80 |
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

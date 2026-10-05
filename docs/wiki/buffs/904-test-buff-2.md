---
title: "Test Buff 2"
type: "buff"
id: 904
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 904", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_901"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 15
effects:
  - {"code": 231, "stat": "level? (char+0x657)", "value": 5}
icon: {"file": "Policy.png", "index": 0}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=0e036f type=6143a1 id=6f2c73 sources=08de33 name_key=55d920 duration=6c749d is_buff=b6589f stack_type=356a19 group=f1abd6 effects=5cfa52 icon=f877b6 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Test Buff 2](../assets/buffs/904.png) |
| **Buff id** | `904` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 15 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Test Buff 2

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 231 | level? (char+0x657) | 5 |
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

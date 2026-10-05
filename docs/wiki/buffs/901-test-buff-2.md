---
title: "Test Buff 2"
type: "buff"
id: 901
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 901", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_901"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 1, "stat": "Attack", "value": 30}
  - {"code": 6, "stat": "Armor", "value": 10}
icon: {"file": "Policy.png", "index": 0}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=0e036f type=6143a1 id=a071f3 sources=c6a163 name_key=55d920 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=aea35f icon=f877b6 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Test Buff 2](../assets/buffs/901.png) |
| **Buff id** | `901` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Test Buff 2

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 1 | Attack | 30 |
| 6 | Armor | 10 |
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

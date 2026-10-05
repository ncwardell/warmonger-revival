---
title: "Deals an additional 10% Attack Damage."
type: "buff"
id: 100
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 100", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_100"
duration: {"ticks": 150, "seconds": 30.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 101, "stat": "Attack(%)", "value": 10}
  - {"code": 102, "stat": "Ability Power(%)", "value": 10}
icon: {"file": "Policy.png", "index": 0}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=f3eec8 type=6143a1 id=310b86 sources=7c4beb name_key=8ca41a duration=faac5c is_buff=b6589f stack_type=356a19 group=b6589f effects=2b7bb6 icon=f877b6 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Deals an additional 10% Attack Damage.](wiki/assets/buffs/100.png) |
| **Buff id** | `100` |
| **Duration** | 30 s (150 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Deals an additional 10% Attack Damage.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 101 | Attack(%) | 10 |
| 102 | Ability Power(%) | 10 |
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

---
title: "Elixir of Agility : 3% Critical Strike Rating and 5% Movement Speed."
type: "buff"
id: 2018
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2018", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2018"
duration: {"ticks": 3000, "seconds": 600.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 9, "stat": "Critical Strike", "value": 10}
  - {"code": 110, "stat": "Critical Strike Deal(%)", "value": 5}
icon: {"file": "Policy.png", "index": 0}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=d9669d type=6143a1 id=66efd9 sources=60fea2 name_key=53aebb duration=dc6a42 is_buff=b6589f stack_type=356a19 group=b6589f effects=cb6374 icon=f877b6 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Elixir of Agility : 3% Critical Strike Rating and 5% Movement Speed.](wiki/assets/buffs/2018.png) |
| **Buff id** | `2018` |
| **Duration** | 10 min (3,000 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Elixir of Agility : 3% Critical Strike Rating and 5% Movement Speed.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 9 | Critical Strike | 10 |
| 110 | Critical Strike Deal(%) | 5 |
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

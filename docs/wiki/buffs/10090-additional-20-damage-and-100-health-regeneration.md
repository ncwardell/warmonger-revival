---
title: "Additional 20% damage and 100% Health Regeneration"
type: "buff"
id: 10090
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10090", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10090"
duration: {"ticks": 900, "seconds": 180.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 136, "stat": "Damage(%)+", "value": 20}
  - {"code": 132, "stat": "Health Regeneration(%)", "value": 100}
icon: {"file": "Mastery_01.png", "index": 5}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=e5b1df type=6143a1 id=759a10 sources=052e24 name_key=6e85cc duration=e0cd66 is_buff=b6589f stack_type=356a19 group=b6589f effects=f91aaa icon=eb907e applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Additional 20% damage and 100% Health Regeneration](wiki/assets/buffs/10090.png) |
| **Buff id** | `10090` |
| **Duration** | 3 min (900 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Mastery_01.png` cell 5 |

### Tooltip

> Additional 20% damage and 100% Health Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 136 | Damage(%)+ | 20 |
| 132 | Health Regeneration(%) | 100 |
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

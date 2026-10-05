---
title: "Magic Heart : Stun"
type: "buff"
id: 3025
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 3025", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_3025"
duration: {"ticks": 900, "seconds": 180.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": -3000}
icon: {"file": "Policy.png", "index": 0}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=cb3506 type=6143a1 id=eb24ed sources=7ba7a0 name_key=032715 duration=e0cd66 is_buff=b6589f stack_type=356a19 group=b6589f effects=70cd03 icon=f877b6 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Magic Heart : Stun](../assets/buffs/3025.png) |
| **Buff id** | `3025` |
| **Duration** | 3 min (900 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Magic Heart : Stun

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | -3,000 |
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

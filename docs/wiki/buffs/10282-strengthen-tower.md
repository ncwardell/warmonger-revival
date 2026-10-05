---
title: "Strengthen Tower"
type: "buff"
id: 10282
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10282", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10282"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 402, "stat": "basic attack override", "value": 5229}
  - {"code": 1, "stat": "Attack", "value": 50}
  - {"code": 6, "stat": "Armor", "value": 50}
icon: {"file": "Policy_01.png", "index": 39}
applied_by:
  - {"skill": 5228, "slot": 1, "type": 452, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=43bbc8 type=6143a1 id=d3c830 sources=1a9fba name_key=bc4d6a duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=ee94f5 icon=30da17 applied_by=04315e -->
|  |  |
|---|---|
|  | ![Strengthen Tower](../assets/buffs/10282.png) |
| **Buff id** | `10282` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy_01.png` cell 39 |

### Tooltip

> Strengthen Tower

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 402 | basic attack override | 5,229 ([[wiki/skills/5229-improved-fortification\|Improved Fortification]]) |
| 1 | Attack | 50 |
| 6 | Armor | 50 |

### Applied by

- Skill [[wiki/skills/5228-fortified|Fortified]], effect slot 1 (type 452, rate 100%)
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

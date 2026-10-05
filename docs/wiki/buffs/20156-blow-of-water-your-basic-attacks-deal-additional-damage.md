---
title: "Blow of water : Your basic Attacks deal additional damage"
type: "buff"
id: 20156
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20156", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_20156"
duration: {"ticks": 30, "seconds": 6.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 20159}
icon: {"file": "Skill_Boss_01.dds", "index": 28}
applied_by:
  - {"skill": 20158, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=d7c4f9 type=6143a1 id=c5d9e5 sources=7769da name_key=8f4d94 duration=5d0a7b is_buff=b6589f stack_type=356a19 group=b6589f effects=6dbc6d icon=e4f418 applied_by=a0fcd7 -->
|  |  |
|---|---|
|  | ![Blow of water : Your basic Attacks deal additional damage](../assets/buffs/20156.png) |
| **Buff id** | `20156` |
| **Duration** | 6 s (30 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 28 |

### Tooltip

> Blow of water : Your basic Attacks deal additional damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 20,159 ([[wiki/skills/20159-blow-of-water\|Blow of water]]) |

### Applied by

- Skill [[wiki/skills/20158-blow-of-water|Blow of water]], effect slot 1 (type 301, rate 100%)
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

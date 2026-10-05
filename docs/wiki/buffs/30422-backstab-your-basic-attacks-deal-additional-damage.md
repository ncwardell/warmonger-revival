---
title: "Backstab : Your basic Attacks deal additional damage"
type: "buff"
id: 30422
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30422", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10422"
duration: {"ticks": 35, "seconds": 7.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 10462}
icon: {"file": "Skill_Miriam_01.png", "index": 29}
applied_by:
  - {"skill": 10461, "slot": 2, "type": 301, "rate": 100}
  - {"skill": 10462, "slot": 4, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=350c46 type=6143a1 id=945a43 sources=69c7a8 name_key=5b4df4 duration=bdf5bf is_buff=b6589f stack_type=356a19 group=b6589f effects=0f7fb1 icon=c0fb59 applied_by=717bae -->
|  |  |
|---|---|
|  | ![Backstab : Your basic Attacks deal additional damage](../assets/buffs/30422.png) |
| **Buff id** | `30422` |
| **Duration** | 7 s (35 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 29 |

### Tooltip

> Backstab : Your basic Attacks deal additional damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 10,462 ([[wiki/skills/10462-backstab\|Backstab]]) |

### Applied by

- Skill [[wiki/skills/10461-backstab|Backstab]], effect slot 2 (type 301, rate 100%)
- Skill [[wiki/skills/10462-backstab|Backstab]], effect slot 4 (type 302, rate 100%)
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

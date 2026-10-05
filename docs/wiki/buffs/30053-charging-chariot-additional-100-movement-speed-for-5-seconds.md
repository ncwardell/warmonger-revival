---
title: "Charging Chariot : Additional 100 Movement Speed for 5 seconds"
type: "buff"
id: 30053
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30053", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10053"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 17, "stat": "code 17 (unknown)", "value": 100}
icon: {"file": "Skill_Dolorece_01.png", "index": 9}
applied_by:
  - {"skill": 10060, "slot": 3, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=6d66b5 type=6143a1 id=a3f926 sources=cb9a8f name_key=de5a46 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=48390e icon=aa3f54 applied_by=41cc1f -->
|  |  |
|---|---|
|  | ![Charging Chariot : Additional 100 Movement Speed for 5 seconds](wiki/assets/buffs/30053.png) |
| **Buff id** | `30053` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 9 |

### Tooltip

> Charging Chariot : Additional 100 Movement Speed for 5 seconds

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 17 | code 17 (unknown) | 100 |

### Applied by

- Skill [[wiki/skills/10060-charging-chariot|Charging Chariot]], effect slot 3 (type 301, rate 100%)
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

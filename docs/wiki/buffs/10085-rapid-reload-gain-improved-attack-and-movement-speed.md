---
title: "Rapid Reload : Gain improved Attack and Movement Speed"
type: "buff"
id: 10085
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10085", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10085"
duration: {"ticks": 20, "seconds": 4.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 116, "stat": "code 116 (unknown)", "value": 40}
  - {"code": 117, "stat": "code 117 (unknown)", "value": 40}
icon: {"file": "Skill_Einsel_01.png", "index": 17}
applied_by:
  - {"skill": 5103, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=dbbd9e type=6143a1 id=cc96cf sources=a2841b name_key=5c858f duration=3d2da5 is_buff=b6589f stack_type=356a19 group=b6589f effects=6e7a6d icon=7c2320 applied_by=0d069e -->
|  |  |
|---|---|
|  | ![Rapid Reload : Gain improved Attack and Movement Speed](wiki/assets/buffs/10085.png) |
| **Buff id** | `10085` |
| **Duration** | 4 s (20 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 17 |

### Tooltip

> Rapid Reload : Gain improved Attack and Movement Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 116 | code 116 (unknown) | 40 |
| 117 | code 117 (unknown) | 40 |

### Applied by

- Skill [[wiki/skills/5103-rapid-reload|Rapid Reload]], effect slot 1 (type 314, rate 100%)
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

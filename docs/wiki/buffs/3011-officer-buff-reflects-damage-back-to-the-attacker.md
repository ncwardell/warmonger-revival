---
title: "Officer Buff: Reflects damage back to the attacker"
type: "buff"
id: 3011
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 3011", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_3011"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 443, "stat": "code 443 (unknown)", "value": 40}
icon: {"file": "Mastery_01.png", "index": 10}
applied_by:
  - {"skill": 3010, "slot": 1, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=0fd374 type=6143a1 id=1d25ca sources=05e570 name_key=e24359 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=ad21dc icon=4a83a1 applied_by=4aa562 -->
|  |  |
|---|---|
|  | ![Officer Buff: Reflects damage back to the attacker](../assets/buffs/3011.png) |
| **Buff id** | `3011` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Mastery_01.png` cell 10 |

### Tooltip

> Officer Buff: Reflects damage back to the attacker

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 443 | code 443 (unknown) | 40 |

### Applied by

- Skill [[wiki/skills/3010|Skill 3010]], effect slot 1 (type 314, rate 100%)
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

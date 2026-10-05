---
title: "Mystic Arrow : Increased Attack Speed"
type: "buff"
id: 10443
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10443", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10443"
duration: {"ticks": 30, "seconds": 6.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 103, "stat": "Attack Speed(%)", "value": 20}
icon: {"file": "Skill_Miriam_01.png", "index": 34}
applied_by:
  - {"skill": 5491, "slot": 4, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=15c953 type=6143a1 id=03dd8d sources=462654 name_key=0fcc7a duration=5d0a7b is_buff=b6589f stack_type=356a19 group=b6589f effects=9c3f21 icon=744c36 applied_by=dd0567 -->
|  |  |
|---|---|
|  | ![Mystic Arrow : Increased Attack Speed](wiki/assets/buffs/10443.png) |
| **Buff id** | `10443` |
| **Duration** | 6 s (30 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 34 |

### Tooltip

> Mystic Arrow : Increased Attack Speed

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 103 | Attack Speed(%) | 20 |

### Applied by

- Skill [[wiki/skills/5491-mystic-arrow|Mystic Arrow]], effect slot 4 (type 301, rate 100%)
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

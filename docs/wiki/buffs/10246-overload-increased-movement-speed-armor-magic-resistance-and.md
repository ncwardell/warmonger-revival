---
title: "Overload : Increased Movement Speed, Armor, Magic Resistance and immune to abilities."
type: "buff"
id: 10246
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10246", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10246"
duration: {"ticks": 50, "seconds": 10.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": 30}
  - {"code": 6, "stat": "Armor", "value": 50}
  - {"code": 7, "stat": "Magic Resist", "value": 50}
icon: {"file": "Policy.png", "index": 33}
applied_by:
  - {"skill": 5203, "slot": 1, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=9dd6fc type=6143a1 id=96de60 sources=454a93 name_key=3dc6e3 duration=6c749d is_buff=b6589f stack_type=356a19 group=b6589f effects=e134a0 icon=0392b4 applied_by=813e25 -->
|  |  |
|---|---|
|  | ![Overload : Increased Movement Speed, Armor, Magic Resistance and immune to abilities.](wiki/assets/buffs/10246.png) |
| **Buff id** | `10246` |
| **Duration** | 10 s (50 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Policy.png` cell 33 |

### Tooltip

> Overload : Increased Movement Speed, Armor, Magic Resistance and immune to abilities.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | 30 |
| 6 | Armor | 50 |
| 7 | Magic Resist | 50 |

### Applied by

- Skill [[wiki/skills/5203|Skill 5203]], effect slot 1 (type 301, rate 100%)
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

---
title: "Assassination : Active"
type: "buff"
id: 10169
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10169", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10169"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10169
effects:
  - {"code": 404, "stat": "basic attack override", "value": 1}
  - {"code": 402, "stat": "basic attack override", "value": 5144}
icon: {"file": "Skill_Miriam_01.png", "index": 25}
applied_by:
  - {"skill": 5140, "slot": 1, "type": 301, "rate": 100}
  - {"skill": 5144, "slot": 3, "type": 302, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=ea5e5f type=6143a1 id=084c34 sources=eeac85 name_key=5326ba duration=870e64 is_buff=b6589f stack_type=356a19 group=084c34 effects=261d5d icon=d212e9 applied_by=abf19f -->
|  |  |
|---|---|
|  | ![Assassination : Active](../assets/buffs/10169.png) |
| **Buff id** | `10169` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10169 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 25 |

### Tooltip

> Assassination : Active

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 404 | basic attack override | 1 |
| 402 | basic attack override | 5,144 ([[wiki/skills/5144\|Skill 5144]]) |

### Applied by

- Skill [[wiki/skills/5140-assassination|Assassination]], effect slot 1 (type 301, rate 100%)
- Skill [[wiki/skills/5144|Skill 5144]], effect slot 3 (type 302, rate 100%)
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

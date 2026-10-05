---
title: "Aura of Death : Kills and assists heal you"
type: "buff"
id: 20011
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 20011"]
name_key: "SkillBuff_10223"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 16
effects:
  - {"code": 131, "stat": "Health(%)", "value": 3}
icon: {"file": "Policy.png", "index": 41}
applied_by:
  - {"skill": 20012, "slot": 1, "type": 303, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=164627 type=6143a1 id=95e708 sources=190885 name_key=324a94 duration=6c141f is_buff=b6589f stack_type=356a19 group=1574bd effects=3c70a8 icon=4e653c applied_by=73aa92 -->
|  |  |
|---|---|
|  | ![Aura of Death : Kills and assists heal you](../assets/buffs/20011.png) |
| **Buff id** | `20011` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 16 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy.png` cell 41 |

### Tooltip

> Aura of Death : Kills and assists heal you

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 131 | Health(%) | 3 |

### Applied by

- Skill [[wiki/skills/20012-aura-of-death|Aura of Death]], effect slot 1 (type 303, rate 100%)
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

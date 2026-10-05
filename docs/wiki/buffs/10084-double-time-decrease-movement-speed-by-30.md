---
title: "Double Time : Decrease Movement Speed by 30%"
type: "buff"
id: 10084
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10084", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10084"
duration: {"ticks": 10, "seconds": 2.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 1000
effects:
  - {"code": 119, "stat": "code 119 (unknown)", "value": -30}
icon: {"file": "Skill_Einsel_01.png", "index": 16}
applied_by:
  - {"skill": 5102, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=70c3ef type=6143a1 id=f3cf8f sources=d242d0 name_key=8467d3 duration=2a0b1e is_buff=b6589f stack_type=356a19 group=e3cbba effects=732c70 icon=3b602b applied_by=d26daf -->
|  |  |
|---|---|
|  | ![Double Time : Decrease Movement Speed by 30%](wiki/assets/buffs/10084.png) |
| **Buff id** | `10084` |
| **Duration** | 2 s (10 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 1000 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 16 |

### Tooltip

> Double Time : Decrease Movement Speed by 30%

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 119 | code 119 (unknown) | -30 |

### Applied by

- Skill [[wiki/skills/5102-ankle-aim|Ankle Aim]], effect slot 3 (type 314, rate 100%)
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

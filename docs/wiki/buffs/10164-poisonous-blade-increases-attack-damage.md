---
title: "Poisonous Blade: Increases Attack Damage"
type: "buff"
id: 10164
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10164", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10164"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 116, "stat": "code 116 (unknown)", "value": 10}
  - {"code": 101, "stat": "Attack(%)", "value": 10}
icon: {"file": "Skill_Miriam_01.png", "index": 24}
applied_by:
  - {"skill": 5139, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=b8eefb type=6143a1 id=1a9dee sources=dc0af2 name_key=55bf80 duration=870e64 is_buff=b6589f stack_type=356a19 group=b6589f effects=73556b icon=78290d applied_by=16ba9e -->
|  |  |
|---|---|
|  | ![Poisonous Blade: Increases Attack Damage](wiki/assets/buffs/10164.png) |
| **Buff id** | `10164` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 24 |

### Tooltip

> Poisonous Blade: Increases Attack Damage

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 116 | code 116 (unknown) | 10 |
| 101 | Attack(%) | 10 |

### Applied by

- Skill [[wiki/skills/5139-poisonous-blade|Poisonous Blade]], effect slot 3 (type 314, rate 100%)
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

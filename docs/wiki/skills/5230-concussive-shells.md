---
title: "Concussive Shells"
type: "skill"
id: 5230
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5230"]
name_key: "Skill_5230"
desc_key: "SkillComment_5230"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["player", "structure"], "max_targets": 3}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 255.0, "width_or_angle": 255.0}
cost: {"type": 14, "type_name": "TP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 453, "value": 10283, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10283, "rate": 100}]}
icon: {"file": "Policy_01.png", "index": 41}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=5d8c5a type=86a754 id=8eef6a sources=8388a8 name_key=79c999 desc_key=f7ff82 kind=356a19 kind_name=9bc378 target=879c59 range=3028f5 area=febbd1 cost=29fd72 cooldown=7d0c8c effect_kind=b6589f effects=6a70e4 damage_or_effect=6619a2 icon=6e5b1d used_by=97d170 -->
|  |  |
|---|---|
|  | ![Concussive Shells](wiki/assets/skills/5230.png) |
| **Skill id** | `5230` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: player, structure; up to 3 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 255, width/angle 255 |
| **Cost** | 340 TP |
| **Cooldown** | 60 s |
| **Icon** | `ui/icons/Policy_01.png` cell 41 |

### Tooltip

> Stops the enemy Attack.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 453 | applies buff (variant 453) | [[wiki/buffs/10283-concussive-shells\|Concussive Shells]] | 100 |

**Reading:** applies [[wiki/buffs/10283-concussive-shells|Concussive Shells]] (100%).
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

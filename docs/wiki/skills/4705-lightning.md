---
title: "Lightning"
type: "skill"
id: 4705
status: "stub"
missing: ["damage_or_effect", "cooldown"]
sources: ["client: Skill_Base.cdb id 4705", "client: Skill_TP.cdb row 53"]
name_key: "Skill_4705"
desc_key: "SkillComment_4705"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: {"type": 14, "type_name": "TP", "amount": 0, "from": "Skill_TP"}
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 324, "value": 10045, "rate": 100}
damage_or_effect: {}
icon: {"file": "Policy_01.png", "index": 24}
used_by: []
tp: {"row": 53, "tp_cost": 0, "cooldown_s": 0, "need_flags": 396, "c7": 0}
---
<!-- generated:start -->
<!-- generated-keys: title=5cd14f type=86a754 id=2593eb sources=2f16cb name_key=61ef12 desc_key=2da273 kind=356a19 kind_name=9bc378 target=cacd0a range=3028f5 area=950fc9 cost=15f43a cooldown=2be88c effect_kind=356a19 effects=076914 damage_or_effect=bf21a9 icon=ae8ff0 used_by=97d170 tp=4c817a -->
|  |  |
|---|---|
|  | ![Lightning](wiki/assets/skills/4705.png) |
| **Skill id** | `4705` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Cost** | 0 TP |
| **Effect kind** | damage (physical?) (1) |
| **TP skill** | 0 TP, 0 s cooldown (Skill_TP row 53) |
| **Icon** | `ui/icons/Policy_01.png` cell 24 |

### Tooltip

> Click on a field or mini-map to inflict 300 (+ 5% of your maximum HP) damage per second to enemies within a certain radius.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 10,045 | 100 |
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

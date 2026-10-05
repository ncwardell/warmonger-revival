---
title: "Iron Will"
type: "skill"
id: 505
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 505"]
name_key: "Skill_505"
desc_key: "SkillComment_505"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 0.0}
cost: null
cooldown: null
effect_kind: 31
effects:
  - {"slot": 1, "type": 131, "value": 3, "rate": 0}
damage_or_effect: {"kind": "heal HP", "stats": [{"code": 131, "value": 3}]}
icon: null
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=4f662e type=86a754 id=3ead28 sources=30b95f name_key=dd0406 desc_key=36b204 kind=356a19 kind_name=9bc378 target=d99f6c range=77de68 area=c0807e cost=2be88c cooldown=2be88c effect_kind=632667 effects=51c322 damage_or_effect=2d77ae icon=2be88c used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `505` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 3, width/angle 0 |
| **Effect kind** | heal HP (31) |

### Tooltip

> Rapid Regeneration

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 3 | 0 |

**Reading:** heal HP.
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

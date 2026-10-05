---
title: "Fame Item : Warsong"
type: "skill"
id: 5123
status: "stub"
missing: ["damage_or_effect", "cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 5123"]
name_key: "Skill_5123"
desc_key: "SkillComment_5123"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 0.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 309, "value": 8, "rate": 100}
damage_or_effect: {}
visual: 354
icon: null
used_by:
  - {"item_use": 2908}
---
<!-- generated:start -->
<!-- generated-keys: title=711060 type=86a754 id=105940 sources=dbaed4 name_key=0227ac desc_key=9190f8 kind=356a19 kind_name=9bc378 target=aabe0a range=ac3478 area=500aa4 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=42f246 damage_or_effect=bf21a9 visual=1a1162 icon=2be88c used_by=9619e2 -->
|  |  |
|---|---|
| **Skill id** | `5123` |
| **Kind** | active (1) |
| **Target** | self; self, ally; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 0 |
| **Visual** | skillVisual 354 `정화의 귀걸이 이펙트` |

### Tooltip

> Warsong

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 309 | unknown | 8 | 100 |

### Used by

- Cast when [[wiki/items/2908-purifying|Purifying]] is used (Item_Base option 210)
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

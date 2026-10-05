---
title: "Fame Item : March"
type: "skill"
id: 5121
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 5121"]
name_key: "Skill_5121"
desc_key: "SkillComment_5121"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 6
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 0.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10138, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10138, "rate": 100}]}
icon: null
used_by:
  - {"item_use": 2906}
---
<!-- generated:start -->
<!-- generated-keys: title=911fef type=86a754 id=1a4624 sources=9268a7 name_key=78efc2 desc_key=7c9ed3 kind=356a19 kind_name=9bc378 target=aabe0a range=c1dfd9 area=e9876d cost=2be88c cooldown=2be88c effect_kind=b6589f effects=33c633 damage_or_effect=a8a908 icon=2be88c used_by=f525e0 -->
|  |  |
|---|---|
| **Skill id** | `5121` |
| **Kind** | active (1) |
| **Target** | self; self, ally; units: monster, player; up to 5 |
| **Range** | 6 (world units) |
| **Area** | circle, radius 6, width/angle 0 |

### Tooltip

> March

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10138-fame-item-march\|Fame item: March]] | 100 |

**Reading:** applies [[wiki/buffs/10138-fame-item-march|Fame item: March]] (100%).

### Used by

- Cast when [[wiki/items/2906-celerity|Celerity]] is used (Item_Base option 210)
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

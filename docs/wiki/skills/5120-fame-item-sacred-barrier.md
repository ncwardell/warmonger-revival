---
title: "Fame Item : Sacred Barrier"
type: "skill"
id: 5120
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 5120"]
name_key: "Skill_5120"
desc_key: "SkillComment_5120"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 0.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10137, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10137, "rate": 100}]}
icon: null
used_by:
  - {"item_use": 2905}
---
<!-- generated:start -->
<!-- generated-keys: title=049279 type=86a754 id=ec7aea sources=4c9d4f name_key=2af73e desc_key=2c176b kind=356a19 kind_name=9bc378 target=33cc09 range=ac3478 area=500aa4 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=54b75c damage_or_effect=4bea27 icon=2be88c used_by=df1f9e -->
|  |  |
|---|---|
| **Skill id** | `5120` |
| **Kind** | active (1) |
| **Target** | self; self, ally; units: monster, player; up to 1 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 0 |

### Tooltip

> Sacred Barrier

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10137-fame-item-sacred-barrier\|Fame item: Sacred Barrier]] | 100 |

**Reading:** applies [[wiki/buffs/10137-fame-item-sacred-barrier|Fame item: Sacred Barrier]] (100%).

### Used by

- Cast when [[wiki/items/2905-invincible|Invincible]] is used (Item_Base option 210)
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

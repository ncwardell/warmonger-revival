---
title: "Fame Item : Dark shadow"
type: "skill"
id: 5122
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 5122"]
name_key: "Skill_5122"
desc_key: "SkillComment_5122"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 0.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10139, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10139, "rate": 100}]}
icon: null
used_by:
  - {"item_use": 2907}
---
<!-- generated:start -->
<!-- generated-keys: title=13a94b type=86a754 id=36c48a sources=b5b823 name_key=4df468 desc_key=d4b265 kind=356a19 kind_name=9bc378 target=33cc09 range=ac3478 area=500aa4 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=e93a9b damage_or_effect=c4d676 icon=2be88c used_by=306834 -->
|  |  |
|---|---|
| **Skill id** | `5122` |
| **Kind** | active (1) |
| **Target** | self; self, ally; units: monster, player; up to 1 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 0 |

### Tooltip

> Dark shadow

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10139-fame-item-dark-shadow\|Fame item: Dark shadow]] | 100 |

**Reading:** applies [[wiki/buffs/10139-fame-item-dark-shadow|Fame item: Dark shadow]] (100%).

### Used by

- Cast when [[wiki/items/2907-ghost|Ghost]] is used (Item_Base option 210)
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

---
title: "Hunting Eye"
type: "skill"
id: 20215
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20215"]
name_key: "Skill_20215"
desc_key: "SkillComment_20215"
kind: 2
kind_name: "passive"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 7.0, "width_or_angle": 7.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20206, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20206, "rate": 100}]}
requirements:
  - {"type": 20206, "a": 5, "b": 20216}
icon: {"file": "Skill_Boss_01.dds", "index": 33}
used_by:
  - {"weapon_base": 73, "slot": 3, "items": [8004, 8504]}
---
<!-- generated:start -->
<!-- generated-keys: title=64c9d2 type=86a754 id=f5f2eb sources=c66c7e name_key=babd59 desc_key=5df5bb kind=da4b92 kind_name=3844d5 target=ad4b90 range=902ba3 area=1bac4b cost=2be88c cooldown=2be88c effect_kind=b6589f effects=0ca83a damage_or_effect=15fa3c requirements=323d24 icon=2fe3b0 used_by=387eae -->
|  |  |
|---|---|
|  | ![Hunting Eye](../assets/skills/20215.png) |
| **Skill id** | `20215` |
| **Kind** | passive (2) |
| **Target** | self; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 7, width/angle 7 |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 33 |

### Tooltip

> [Passive] When an enemy is hit by a basic attack, the enemy's Defense decreases by 4% for a certain amount of time. (Up to 5 times.)

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20206-hunting-eye-reduced-armor\|Hunting Eye: Reduced armor]] | 100 |

**Reading:** applies [[wiki/buffs/20206-hunting-eye-reduced-armor|Hunting Eye: Reduced armor]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 20206 | 5 | 20216 |

### Used by

- Weapon skill **E** of WeaponBase 73: [[wiki/items/8004-artamos|Artamos]], [[wiki/items/8504-crystal-artamos|Crystal : Artamos]]
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

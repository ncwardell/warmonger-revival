---
title: "Quick attack"
type: "skill"
id: 20258
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20258"]
name_key: "Skill_20258"
desc_key: "SkillComment_20258"
kind: 2
kind_name: "passive"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20255, "rate": 100}
  - {"slot": 2, "type": 303, "value": 20257, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20255, "rate": 100}, {"buff": 20257, "rate": 100}]}
icon: {"file": "Skill_Boss_01.dds", "index": 53}
used_by:
  - {"weapon_base": 75, "slot": 7, "items": [8006, 8506]}
---
<!-- generated:start -->
<!-- generated-keys: title=67e85a type=86a754 id=0717f7 sources=d16aff name_key=e02dc3 desc_key=36cf86 kind=da4b92 kind_name=3844d5 target=ad4b90 range=77de68 area=344636 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=490ca4 damage_or_effect=96a20b icon=e8b5ca used_by=41fc12 -->
|  |  |
|---|---|
|  | ![Quick attack](../assets/skills/20258.png) |
| **Skill id** | `20258` |
| **Kind** | passive (2) |
| **Target** | self; enemy; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 53 |

### Tooltip

> [Passive] A stack is created during a basic attack and your Attack Speed is increased when you reach 5 stacks.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20255\|Buff 20255]] | 100 |
| 2 | 303 | applies buff (variant 303) | [[wiki/buffs/20257-quick-attack-increase-attack-speed-when-reaching-5-stack\|Quick attack : Increase attack speed when reaching 5 stack]] | 100 |

**Reading:** applies [[wiki/buffs/20255|Buff 20255]] (100%); applies [[wiki/buffs/20257-quick-attack-increase-attack-speed-when-reaching-5-stack|Quick attack : Increase attack speed when reaching 5 stack]] (100%).

### Used by

- Weapon skill **hero set 3** of WeaponBase 75: [[wiki/items/8006-king-deathhead|King Deathhead]], [[wiki/items/8506-crystal-king-deathhead|Crystal : King Deathhead]]
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

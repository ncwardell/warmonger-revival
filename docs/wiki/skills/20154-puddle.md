---
title: "Puddle"
type: "skill"
id: 20154
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 20154"]
name_key: "Skill_20154"
desc_key: "SkillComment_20154"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
delivery: {"type": 4, "field_tick": 0.1}
effect_kind: 1
effects:
  - {"slot": 1, "type": 324, "value": 14003, "rate": 100}
damage_or_effect: {}
visual: 423
icon: {"file": "Skill_Boss_01.dds", "index": 25}
used_by:
  - {"weapon_base": 72, "slot": 3, "items": [8003, 8503]}
---
<!-- generated:start -->
<!-- generated-keys: title=def61d type=86a754 id=c3733c sources=c8856e name_key=0f4c26 desc_key=fdb4ec kind=356a19 kind_name=9bc378 target=cacd0a range=fe5dbb area=6d01a6 cost=911ade cooldown=628d31 delivery=8af2f4 effect_kind=356a19 effects=30c39d damage_or_effect=bf21a9 visual=a785bd icon=f7179c used_by=35fe02 -->
|  |  |
|---|---|
|  | ![Puddle](../assets/skills/20154.png) |
| **Skill id** | `20154` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Delivery** | projectile / SFX (4), tick 0.1 |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 423 `사라스바티_웅덩이_소환몹` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 25 |

### Tooltip

> [Active]Summons a puddle at a designated location, and enemies on the puddle have a significantly reduced movement speed.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 14,003 | 100 |

### Used by

- Weapon skill **E** of WeaponBase 72: [[wiki/items/8003-sarasvati|Sarasvati]], [[wiki/items/8503-crystal-sarasvati|Crystal : Sarasvati]]
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

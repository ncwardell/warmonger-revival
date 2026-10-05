---
title: "Invisible prison"
type: "skill"
id: 20209
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 20209"]
name_key: "Skill_20209"
desc_key: "SkillComment_20209"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 324, "value": 14004, "rate": 100}
damage_or_effect: {}
visual: 434
icon: {"file": "Skill_Boss_01.dds", "index": 36}
used_by:
  - {"weapon_base": 73, "slot": 6, "items": [8004, 8504]}
---
<!-- generated:start -->
<!-- generated-keys: title=db02bb type=86a754 id=b6599c sources=b53aeb name_key=063434 desc_key=7084d3 kind=356a19 kind_name=9bc378 target=cacd0a range=fe5dbb area=6d01a6 cost=911ade cooldown=628d31 effect_kind=b6589f effects=7185a2 damage_or_effect=bf21a9 visual=8949eb icon=da8658 used_by=6214c7 -->
|  |  |
|---|---|
|  | ![Invisible prison](wiki/assets/skills/20209.png) |
| **Skill id** | `20209` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Visual** | skillVisual 434 `아르타모스_보이지 않는 감옥` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 36 |

### Tooltip

> [Active]Summons an invisible prison at a designated location and hides the enemy's field of view for 5 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 14,004 | 100 |

### Used by

- Weapon skill **hero set 2** of WeaponBase 73: [[wiki/items/8004-artamos|Artamos]], [[wiki/items/8504-crystal-artamos|Crystal : Artamos]]
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

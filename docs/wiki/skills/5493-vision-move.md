---
title: "Vision Move"
type: "skill"
id: 5493
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5493"]
name_key: "Skill_5493"
desc_key: "SkillComment_5493"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 0.0}
cost: {"type": 5, "type_name": "MP", "amount": 125}
cooldown: {"ms": 15000, "group": 0}
movement: "blink / teleport"
effect_kind: 1
effects:
  - {"slot": 1, "type": 303, "value": 10441, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10441, "rate": 100}]}
visual: 483
icon: {"file": "Skill_Miriam_01.png", "index": 36}
used_by:
  - {"weapon_base": 86, "slot": 3, "items": [15005]}
---
<!-- generated:start -->
<!-- generated-keys: title=be7862 type=86a754 id=d764b9 sources=95a9fb name_key=491a79 desc_key=fb9f9e kind=356a19 kind_name=9bc378 target=c9e051 range=b1d578 area=3b02d8 cost=f67772 cooldown=e3989d movement=953fcf effect_kind=356a19 effects=2976b2 damage_or_effect=12ffed visual=9ee0df icon=dc4741 used_by=1f3611 -->
|  |  |
|---|---|
|  | ![Vision Move](../assets/skills/5493.png) |
| **Skill id** | `5493` |
| **Kind** | active (1) |
| **Target** | ground; ally, enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 1, width/angle 0 |
| **Cost** | 125 MP |
| **Cooldown** | 15 s |
| **Movement** | blink / teleport |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 483 `해골왕의 비젼 활_비전 이동` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 36 |

### Tooltip

> [Active] Teleport to the designated location.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/10441\|Buff 10441]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/10441|Buff 10441]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 86: [[wiki/items/15005-skeleton-king-s-vision-bow|Skeleton king's Vision Bow]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 114): E · Vision Move · 15 s · 125 · teleport to target point
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

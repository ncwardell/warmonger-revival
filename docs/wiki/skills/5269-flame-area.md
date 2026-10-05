---
title: "Flame area"
type: "skill"
id: 5269
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 5269"]
name_key: "Skill_5269"
desc_key: "SkillComment_5269"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 6
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 5, "type_name": "MP", "amount": 415}
cooldown: {"ms": 75000, "group": 0}
delivery: {"type": 4, "field_tick": 0.1}
effect_kind: 1
effects:
  - {"slot": 1, "type": 324, "value": 10041, "rate": 100}
damage_or_effect: {}
visual: 389
icon: {"file": "Skill_Einsel_01.png", "index": 39}
used_by:
  - {"weapon_base": 6, "slot": 4, "items": [10005]}
---
<!-- generated:start -->
<!-- generated-keys: title=d01485 type=86a754 id=1de731 sources=69d349 name_key=c613b5 desc_key=30abbc kind=356a19 kind_name=9bc378 target=cacd0a range=c1dfd9 area=d82541 cost=d55bc7 cooldown=cf1f8c delivery=8af2f4 effect_kind=356a19 effects=535cd0 damage_or_effect=bf21a9 visual=1ed862 icon=56e68a used_by=ea9df7 -->
|  |  |
|---|---|
|  | ![Flame area](../assets/skills/5269.png) |
| **Skill id** | `5269` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 6 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 415 MP |
| **Cooldown** | 75 s |
| **Delivery** | projectile / SFX (4), tick 0.1 |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 389 `PCE_SwordShd_01_R_화염 지역` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 39 |

### Tooltip

> [Active] Lasts for 6 seconds and deals Damage worth 6% of the enemy's max HP per second.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 10,041 | 100 |

### Used by

- Weapon skill **R** of WeaponBase 6: [[wiki/items/10005-magical-blade-shield-flame|Magical Blade Shield : Flame]]
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

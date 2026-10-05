---
title: "Flame area"
type: "skill"
id: 19954
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 19954"]
name_key: "Skill_19954"
desc_key: "SkillComment_19954"
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
  - {"slot": 1, "type": 324, "value": 10042, "rate": 100}
damage_or_effect: {}
visual: 405
icon: {"file": "Skill_Einsel_01.png", "index": 39}
used_by:
  - {"weapon_base": 74, "slot": 4, "items": [8005, 8505]}
---
<!-- generated:start -->
<!-- generated-keys: title=d01485 type=86a754 id=7ce2a3 sources=e51c8f name_key=55a845 desc_key=8415f6 kind=356a19 kind_name=9bc378 target=cacd0a range=c1dfd9 area=d82541 cost=d55bc7 cooldown=cf1f8c delivery=8af2f4 effect_kind=356a19 effects=3e7f8e damage_or_effect=bf21a9 visual=7ee51d icon=56e68a used_by=6a096c -->
|  |  |
|---|---|
|  | ![Flame area](../assets/skills/19954.png) |
| **Skill id** | `19954` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 6 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 415 MP |
| **Cooldown** | 75 s |
| **Delivery** | projectile / SFX (4), tick 0.1 |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 405 `모리온_화염 지역` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 39 |

### Tooltip

> [Active] Lasts for 6 seconds and deals Damage worth 6% of the enemy's max HP per second.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 10,042 | 100 |

### Used by

- Weapon skill **R** of WeaponBase 74: [[wiki/items/8005-morion|Morion]], [[wiki/items/8505-crystal-morion|Crystal : Morion]]
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

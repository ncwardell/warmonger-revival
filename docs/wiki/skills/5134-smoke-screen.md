---
title: "Smoke Screen"
type: "skill"
id: 5134
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 5134", "client: StringAll_Eng SkillComment_5134 (tooltip value tags)"]
name_key: "Skill_5134"
desc_key: "SkillComment_5134"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 10.0}
cost: {"type": 5, "type_name": "MP", "amount": 150}
cooldown: {"ms": 22000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 324, "value": 404, "rate": 100}
damage_or_effect: {}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 200}
  - {"tag": "EF_R_DAM", "value": 110}
  - {"tag": "EF_R_MDAM", "value": 90}
visual: 277
icon: {"file": "Skill_Dolorece_01.png", "index": 29}
used_by:
  - {"weapon_base": 56, "slot": 2, "items": [40014]}
---
<!-- generated:start -->
<!-- generated-keys: title=567d08 type=86a754 id=036c28 sources=cfd686 name_key=fff4d8 desc_key=3ef5fe kind=356a19 kind_name=9bc378 target=cacd0a range=b1d578 area=9876f1 cost=95c2ed cooldown=ba8361 delivery=93a212 effect_kind=356a19 effects=419bb9 damage_or_effect=bf21a9 tooltip_formula=a0e324 visual=f33316 icon=54955f used_by=c9587d -->
|  |  |
|---|---|
|  | ![Smoke Screen](wiki/assets/skills/5134.png) |
| **Skill id** | `5134` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 4, width/angle 10 |
| **Cost** | 150 MP |
| **Cooldown** | 22 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 277 `PCD_Cannon_05_W_연막탄 발사` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 29 |

### Tooltip

> [Active] Fires a Smoke Screen into the designated area, that inflicts `{EF_STATIC 200}``{EF_R_DAM 110}``{EF_R_MDAM 90}` Damage per second. The smoke clears after 5 seconds.

Tooltip formula: **200 + 110% Attack + 90% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 404 | 100 |

### Used by

- Weapon skill **W** of WeaponBase 56: [[wiki/items/40014-skeleton-king-s-magic-cannon|Skeleton King's Magic Cannon]]
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

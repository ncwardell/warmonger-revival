---
title: "Suppressing Fire"
type: "skill"
id: 10105
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 10105", "client: StringAll_Eng SkillComment_10105 (tooltip value tags)"]
name_key: "Skill_10105"
desc_key: "SkillComment_10105"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 12
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 415}
cooldown: {"ms": 75000, "group": 0}
delivery: {"type": 4, "field_tick": 1.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 324, "value": 15003, "rate": 100}
damage_or_effect: {}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 90}
  - {"tag": "EF_R_MDAM", "value": 125}
visual: 238
icon: {"file": "Skill_Einsel_01.png", "index": 19}
used_by:
  - {"weapon_base": 112, "slot": 4, "items": [11011]}
---
<!-- generated:start -->
<!-- generated-keys: title=a5ade2 type=86a754 id=d496a3 sources=d0db46 name_key=ffe7cc desc_key=8cfde9 kind=356a19 kind_name=9bc378 target=cacd0a range=7b5200 area=6d01a6 cost=d55bc7 cooldown=cf1f8c delivery=15a656 effect_kind=da4b92 effects=bf1d25 damage_or_effect=bf21a9 tooltip_formula=5b3301 visual=5b7d26 icon=52a60d used_by=350451 -->
|  |  |
|---|---|
|  | ![Suppressing Fire](wiki/assets/skills/10105.png) |
| **Skill id** | `10105` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 12 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 415 MP |
| **Cooldown** | 75 s |
| **Delivery** | projectile / SFX (4), tick 1 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 238 `PCE_Gun_01_R 쌍권총소나기` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 19 |

### Tooltip

> [Active] This hail of bullets inflicts `{EF_STATIC 90}``{EF_R_MDAM 125}` Damage. Decreases their Attack and Movement Speed by 30 for 5 seconds.

Tooltip formula: **90 + 125% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 15,003 | 100 |

### Used by

- Weapon skill **R** of WeaponBase 112: [[wiki/items/11011-magical-adapted-dual-gun|Magical adapted Dual Gun]]
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

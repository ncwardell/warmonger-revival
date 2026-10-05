---
title: "Dark Matter"
type: "skill"
id: 5473
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5473", "client: StringAll_Eng SkillComment_5473 (tooltip value tags)"]
name_key: "Skill_5473"
desc_key: "SkillComment_5473"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 200, "rate": 100}
  - {"slot": 2, "type": 102, "value": 70, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 200, "ability_pct": 70}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 200}
  - {"tag": "EF_R_MDAM", "value": 70}
visual: 316
icon: {"file": "Skill_Einsel_01.png", "index": 35}
used_by:
  - {"weapon_base": 85, "slot": 4, "items": [30020]}
---
<!-- generated:start -->
<!-- generated-keys: title=b3792a type=86a754 id=d633bb sources=50ed60 name_key=35556b desc_key=4f103e kind=356a19 kind_name=9bc378 target=04e8ed range=902ba3 area=344636 cost=ff5a60 cooldown=ad2ac8 delivery=93a212 effect_kind=da4b92 effects=b2e60f damage_or_effect=5249fb tooltip_formula=bf0019 visual=81c692 icon=c23d4b used_by=c3a7c2 -->
|  |  |
|---|---|
|  | ![Dark Matter](wiki/assets/skills/5473.png) |
| **Skill id** | `5473` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 5 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 316 `PCE_Staff_08_R_멈춰!` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 35 |

### Tooltip

> [Active] Causese an explosion that deals `{EF_STATIC 200}``{EF_R_MDAM 70}` Damage.

Tooltip formula: **200 + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 200 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |

**Reading:** amount **200 + 70% Ability Power**; damage (magic?).

### Used by

- Weapon skill **R** of WeaponBase 85: [[wiki/items/30020-magical-devil-wand|Magical Devil Wand]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 96): 0420 · Magical Devil Wand (10020) · R cooldown 70 → 60 s, AP 70 → 100 (the client still has Dark Matter at 70 s)
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

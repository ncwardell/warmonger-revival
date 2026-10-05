---
title: "Explosion"
type: "skill"
id: 20102
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20102", "client: StringAll_Eng SkillComment_20102 (tooltip value tags)"]
name_key: "Skill_20102"
desc_key: "SkillComment_20102"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 2.0, "width_or_angle": 2.0}
cost: {"type": 5, "type_name": "MP", "amount": 50}
cooldown: {"ms": 2000, "group": 0}
delivery: {"type": 4, "field_tick": 0.5}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 50, "rate": 0}
  - {"slot": 3, "type": 362, "value": 1, "rate": 10}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 50}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 50}
requirements:
  - {"type": 20108, "a": 6, "b": 20107}
visual: 413
icon: {"file": "Skill_Boss_01.dds", "index": 12}
used_by:
  - {"weapon_base": 71, "slot": 1, "items": [8002, 8502]}
---
<!-- generated:start -->
<!-- generated-keys: title=472ab8 type=86a754 id=d8f4d2 sources=9217d2 name_key=a47854 desc_key=4a0256 kind=356a19 kind_name=9bc378 target=e84f24 range=fe5dbb area=644dff cost=7e5cd4 cooldown=367d78 delivery=6a22dc effect_kind=da4b92 effects=df90f3 damage_or_effect=25c130 tooltip_formula=df5a8b requirements=3a72c4 visual=5715aa icon=8f7203 used_by=fa168e -->
|  |  |
|---|---|
|  | ![Explosion](../assets/skills/20102.png) |
| **Skill id** | `20102` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 2, width/angle 2 |
| **Cost** | 50 MP |
| **Cooldown** | 2 s |
| **Delivery** | projectile / SFX (4), tick 0.5 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 413 `아마테라스_익스플로젼` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 12 |

### Tooltip

> [Active]Summons a sphere to a specified location. Deals damage to nearby enemies by `{EF_STATIC 70}``{EF_R_MDAM 50}`.
> Tura Sun Stack +1 
> When using stack : Damage increases.

Tooltip formula: **70 + 50% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 50 | 0 |
| 3 | 362 | unknown | 1 | 10 |

**Reading:** amount **70 + 50% Ability Power**; damage (magic?).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 20108 | 6 | 20107 |

### Used by

- Weapon skill **Q** of WeaponBase 71: [[wiki/items/8002-amaterasu|Amaterasu]], [[wiki/items/8502-crystal-amaterasu|Crystal : Amaterasu]]
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

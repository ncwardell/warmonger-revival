---
title: "Flame pillar"
type: "skill"
id: 20106
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20106", "client: StringAll_Eng SkillComment_20106 (tooltip value tags)"]
name_key: "Skill_20106"
desc_key: "SkillComment_20106"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
delivery: {"type": 4, "field_tick": 0.5}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
  - {"slot": 3, "type": 362, "value": 1, "rate": 10}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 80}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 80}
requirements:
  - {"type": 20107, "a": 6, "b": 20108}
visual: 417
icon: {"file": "Skill_Boss_01.dds", "index": 16}
used_by:
  - {"weapon_base": 71, "slot": 5, "items": [8002, 8502]}
---
<!-- generated:start -->
<!-- generated-keys: title=b5cb60 type=86a754 id=cf487f sources=6221f7 name_key=6a6924 desc_key=2655b3 kind=356a19 kind_name=9bc378 target=e84f24 range=fe5dbb area=6d01a6 cost=e4e7cf cooldown=e3989d delivery=6a22dc effect_kind=da4b92 effects=8eb2d8 damage_or_effect=5aaec0 tooltip_formula=e4dbdd requirements=adeac3 visual=4dc778 icon=c2f732 used_by=8dc4f7 -->
|  |  |
|---|---|
|  | ![Flame pillar](../assets/skills/20106.png) |
| **Skill id** | `20106` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Delivery** | projectile / SFX (4), tick 0.5 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 417 `아마테라스_화염기둥` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 16 |

### Tooltip

> [Active]A circular fire pillar is created at the designated location and deals damage to nearby enemies by `{EF_STATIC 70}``{EF_R_MDAM 80}`.
> Kra Sun Stack +1 
> When using Stack : Damage increases.

Tooltip formula: **70 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |
| 3 | 362 | unknown | 1 | 10 |

**Reading:** amount **70 + 80% Ability Power**; damage (magic?).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 20107 | 6 | 20108 |

### Used by

- Weapon skill **hero set 1** of WeaponBase 71: [[wiki/items/8002-amaterasu|Amaterasu]], [[wiki/items/8502-crystal-amaterasu|Crystal : Amaterasu]]
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

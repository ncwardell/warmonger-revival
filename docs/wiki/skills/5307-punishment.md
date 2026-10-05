---
title: "Punishment"
type: "skill"
id: 5307
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5307", "client: StringAll_Eng SkillComment_5307 (tooltip value tags)"]
name_key: "Skill_5307"
desc_key: "SkillComment_5307"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
delivery: {"type": 4, "field_tick": 1.2}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 102, "value": 120, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 120, "ability_pct": 120}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_MDAM", "value": 120}
visual: 396
icon: {"file": "Skill_Einsel_01.png", "index": 7}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=5ad6d5 type=86a754 id=3edc3d sources=6f1845 name_key=830093 desc_key=6abd2e kind=356a19 kind_name=9bc378 target=7056fd range=902ba3 area=e8b0ea cost=ff5a60 cooldown=ad2ac8 delivery=9e15a4 effect_kind=da4b92 effects=3ca132 damage_or_effect=5ccadc tooltip_formula=bb1008 visual=2bc4a9 icon=62f758 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Punishment](../assets/skills/5307.png) |
| **Skill id** | `5307` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 7 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Delivery** | projectile / SFX (4), tick 1.2 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 396 `시즌2_PCE_Staff_01_R_천벌_02` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 7 |

### Tooltip

> [Active] All enemy located in the area are hit by thunder and receive `{EF_STATIC 120}``{EF_R_MDAM 120}` Magic Damage.

Tooltip formula: **120 + 120% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 120 | 0 |

**Reading:** amount **120 + 120% Ability Power**; damage (magic?).
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

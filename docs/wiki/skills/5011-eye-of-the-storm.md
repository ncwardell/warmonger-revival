---
title: "Eye of the Storm"
type: "skill"
id: 5011
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 5011"]
name_key: "Skill_5011"
desc_key: "SkillComment_5011"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 0
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 324, "value": 402, "rate": 100}
damage_or_effect: {}
visual: 88
icon: {"file": "Skill_Einsel_01.png", "index": 3}
used_by:
  - {"weapon_base": 1, "slot": 4, "items": [10000]}
---
<!-- generated:start -->
<!-- generated-keys: title=5ed432 type=86a754 id=0c24fb sources=8ca7a0 name_key=541c38 desc_key=9758ba kind=356a19 kind_name=9bc378 target=c18e1a range=b6589f cost=ff5a60 cooldown=ad2ac8 effect_kind=b6589f effects=fb5f4a damage_or_effect=bf21a9 visual=b37f6d icon=fae5ad used_by=b26ec5 -->
|  |  |
|---|---|
|  | ![Eye of the Storm](wiki/assets/skills/5011.png) |
| **Skill id** | `5011` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 1 |
| **Range** | 0 (world units) |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Visual** | skillVisual 88 `PCE_Staff_01_R_폭풍의 근원` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 3 |

### Tooltip

> [Active] Increases the nearby allie's Movement Speed by 15%, Armor and Magic Resistance by 25%. Decreases the nearby enemie's Movement Speed by 30% and Attack Speed by 150.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 402 | 100 |

### Used by

- Weapon skill **R** of WeaponBase 1: [[wiki/items/10000-magical-storm-wand|Magical Storm Wand]]
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

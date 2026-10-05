---
title: "Snow of the Sun"
type: "skill"
id: 20103
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 20103"]
name_key: "Skill_20103"
desc_key: "SkillComment_20103"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 255
cost: {"type": 5, "type_name": "MP", "amount": 190}
cooldown: {"ms": 30000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 363, "value": 14002, "rate": 10}
damage_or_effect: {}
requirements:
  - {"type": 20108, "a": 6, "b": 20107}
visual: 414
icon: {"file": "Skill_Boss_01.dds", "index": 13}
used_by:
  - {"weapon_base": 71, "slot": 2, "items": [8002, 8502]}
---
<!-- generated:start -->
<!-- generated-keys: title=9a5cf6 type=86a754 id=55fcbe sources=3b01a6 name_key=e43ebc desc_key=e8ac06 kind=356a19 kind_name=9bc378 target=cacd0a range=3028f5 cost=9b32a5 cooldown=6963fe effect_kind=da4b92 effects=bf2189 damage_or_effect=bf21a9 requirements=3a72c4 visual=4396c2 icon=20ae02 used_by=1877bd -->
|  |  |
|---|---|
|  | ![Snow of the Sun](../assets/skills/20103.png) |
| **Skill id** | `20103` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 255 (world units) |
| **Cost** | 190 MP |
| **Cooldown** | 30 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 414 `아마테라스_태양의 눈` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 13 |

### Tooltip

> [Active]Summons the eyes of the sun to the specified location and illuminates the surrounding area for a certain period of time.
> Tura Sun Stack +1 
> When using stack : Duration increases.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 363 | unknown | 14,002 | 10 |

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 20108 | 6 | 20107 |

### Used by

- Weapon skill **W** of WeaponBase 71: [[wiki/items/8002-amaterasu|Amaterasu]], [[wiki/items/8502-crystal-amaterasu|Crystal : Amaterasu]]
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

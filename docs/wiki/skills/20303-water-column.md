---
title: "Water column"
type: "skill"
id: 20303
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20303", "client: StringAll_Eng SkillComment_20303 (tooltip value tags)"]
name_key: "Skill_20303"
desc_key: "SkillComment_20303"
kind: 3
kind_name: "kind 3"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 6
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 50}
cooldown: {"ms": 2000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 301, "value": 20303, "rate": 100}
  - {"slot": 2, "type": 321, "value": 20303, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20303, "rate": 100}, {"buff": 20303, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 60}
  - {"tag": "EF_R_MDAM", "value": 20}
  - {"tag": "EF_R_MAXMANA", "value": 5}
requirements:
  - {"type": 20303, "a": 4, "b": 0}
icon: {"file": "Skill_Boss_01.dds", "index": 40}
used_by:
  - {"weapon_base": 76, "slot": 2, "items": [8007, 8507]}
---
<!-- generated:start -->
<!-- generated-keys: title=78605e type=86a754 id=da7762 sources=681b4d name_key=9d7c13 desc_key=3ac99b kind=77de68 kind_name=78ea43 target=d1cc1b range=c1dfd9 area=e8b0ea cost=7e5cd4 cooldown=367d78 effect_kind=da4b92 effects=3a179d damage_or_effect=0f4bcb tooltip_formula=389900 requirements=8fe77a icon=2eeddb used_by=97263e -->
|  |  |
|---|---|
|  | ![Water column](wiki/assets/skills/20303.png) |
| **Skill id** | `20303` |
| **Kind** | kind 3 (3) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 6 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 50 MP |
| **Cooldown** | 2 s |
| **Effect kind** | damage (magic?) (2) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 40 |

### Tooltip

> [Active] Consumes Mana per second, and deals Magic Damage to enemies around you `{EF_STATIC 60}``{EF_R_MDAM 20}``{EF_R_MAXMANA 5}` continuously.

Tooltip formula: **60 + 20% Ability Power + 5% max Mana** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/20303\|Buff 20303]] | 100 |
| 2 | 321 | applies buff (variant 321) | [[wiki/buffs/20303\|Buff 20303]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20303|Buff 20303]] (100%); applies [[wiki/buffs/20303|Buff 20303]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 20303 | 4 | 0 |

### Used by

- Weapon skill **W** of WeaponBase 76: [[wiki/items/8007-tempest-fisher|Tempest Fisher]], [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]]
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

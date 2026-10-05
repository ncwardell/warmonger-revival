---
title: "A warm flame"
type: "skill"
id: 20105
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20105", "client: StringAll_Eng SkillComment_20105 (tooltip value tags)"]
name_key: "Skill_20105"
desc_key: "SkillComment_20105"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: {"type": 5, "type_name": "MP", "amount": 490}
cooldown: {"ms": 90000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 308, "value": 20103, "rate": 100}
  - {"slot": 2, "type": 317, "value": 20103, "rate": 100}
  - {"slot": 3, "type": 365, "value": 20103, "rate": 5}
  - {"slot": 4, "type": 366, "value": 20103, "rate": 5}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20103, "rate": 100}, {"buff": 20103, "rate": 100}, {"buff": 20103, "rate": 5}, {"buff": 20103, "rate": 5}]}
tooltip_formula:
  - {"tag": "EF_R_MDAM", "value": 50}
requirements:
  - {"type": 20108, "a": 6, "b": 20107}
visual: 416
icon: {"file": "Skill_Boss_01.dds", "index": 15}
used_by:
  - {"weapon_base": 71, "slot": 4, "items": [8002, 8502]}
---
<!-- generated:start -->
<!-- generated-keys: title=49ce1e type=86a754 id=ed6429 sources=f7636a name_key=79217e desc_key=383b48 kind=356a19 kind_name=9bc378 target=55b685 range=1b6453 area=950fc9 cost=cb4f2a cooldown=bc9744 effect_kind=da4b92 effects=bdc644 damage_or_effect=351a15 tooltip_formula=f662a9 requirements=3a72c4 visual=279e90 icon=660fb1 used_by=850273 -->
|  |  |
|---|---|
|  | ![A warm flame](wiki/assets/skills/20105.png) |
| **Skill id** | `20105` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Cost** | 490 MP |
| **Cooldown** | 90 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 416 `아마테라스_따듯한 불꽃` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 15 |

### Tooltip

> [Active]Provides shields to nearby party when using.300`{EF_R_MDAM 50}`
> Tura Sun Stack +1 
> When using stack : The shield increases.

Tooltip formula: **50% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 308 | applies buff (variant 308) | [[wiki/buffs/20103-a-warm-flame-creates-a-absorvs-damage-for-5-seconds\|A warm flame : Creates a absorvs damage for 5 seconds]] | 100 |
| 2 | 317 | applies buff (variant 317) | [[wiki/buffs/20103-a-warm-flame-creates-a-absorvs-damage-for-5-seconds\|A warm flame : Creates a absorvs damage for 5 seconds]] | 100 |
| 3 | 365 | applies buff (variant 365) | [[wiki/buffs/20103-a-warm-flame-creates-a-absorvs-damage-for-5-seconds\|A warm flame : Creates a absorvs damage for 5 seconds]] | 5 |
| 4 | 366 | applies buff (variant 366) | [[wiki/buffs/20103-a-warm-flame-creates-a-absorvs-damage-for-5-seconds\|A warm flame : Creates a absorvs damage for 5 seconds]] | 5 |

**Reading:** damage (magic?); applies [[wiki/buffs/20103-a-warm-flame-creates-a-absorvs-damage-for-5-seconds|A warm flame : Creates a absorvs damage for 5 seconds]] (100%); applies [[wiki/buffs/20103-a-warm-flame-creates-a-absorvs-damage-for-5-seconds|A warm flame : Creates a absorvs damage for 5 seconds]] (100%); applies [[wiki/buffs/20103-a-warm-flame-creates-a-absorvs-damage-for-5-seconds|A warm flame : Creates a absorvs damage for 5 seconds]] (5%); applies [[wiki/buffs/20103-a-warm-flame-creates-a-absorvs-damage-for-5-seconds|A warm flame : Creates a absorvs damage for 5 seconds]] (5%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 20108 | 6 | 20107 |

### Used by

- Weapon skill **R** of WeaponBase 71: [[wiki/items/8002-amaterasu|Amaterasu]], [[wiki/items/8502-crystal-amaterasu|Crystal : Amaterasu]]
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

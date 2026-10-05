---
title: "Shield of the Sun"
type: "skill"
id: 20108
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20108", "client: StringAll_Eng SkillComment_20108 (tooltip value tags)"]
name_key: "Skill_20108"
desc_key: "SkillComment_20108"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 4
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 308, "value": 20104, "rate": 100}
  - {"slot": 2, "type": 301, "value": 20105, "rate": 100}
  - {"slot": 3, "type": 366, "value": 20104, "rate": 5}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20104, "rate": 100}, {"buff": 20105, "rate": 100}, {"buff": 20104, "rate": 5}]}
tooltip_formula:
  - {"tag": "EF_R_MDAM", "value": 20}
requirements:
  - {"type": 20107, "a": 6, "b": 20108}
visual: 419
icon: {"file": "Skill_Boss_01.dds", "index": 18}
used_by:
  - {"weapon_base": 71, "slot": 7, "items": [8002, 8502]}
---
<!-- generated:start -->
<!-- generated-keys: title=8bbee7 type=86a754 id=2804f9 sources=322274 name_key=c04af2 desc_key=015677 kind=356a19 kind_name=9bc378 target=d99f6c range=1b6453 cost=e4e7cf cooldown=e3989d effect_kind=da4b92 effects=aed4ca damage_or_effect=776b0b tooltip_formula=a8a2ef requirements=adeac3 visual=1f0037 icon=7bf15f used_by=c23978 -->
|  |  |
|---|---|
|  | ![Shield of the Sun](../assets/skills/20108.png) |
| **Skill id** | `20108` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 4 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 419 `아마테라스_태양의 방패` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 18 |

### Tooltip

> [Active]Creates a 150`{EF_R_MDAM 20}` shield for yourself, increases movement speed for 3 seconds 
> Kra Sun Stack +1 
> When using Stack : The shield increases.

Tooltip formula: **20% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 308 | applies buff (variant 308) | [[wiki/buffs/20104-shield-of-the-sun-creates-a-absorvs-damage-for-5-seconds\|Shield of the Sun : Creates a absorvs damage for 5 seconds]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/20105-shield-of-the-sun-movement-speed\|Shield of the Sun : Movement Speed]] | 100 |
| 3 | 366 | applies buff (variant 366) | [[wiki/buffs/20104-shield-of-the-sun-creates-a-absorvs-damage-for-5-seconds\|Shield of the Sun : Creates a absorvs damage for 5 seconds]] | 5 |

**Reading:** damage (magic?); applies [[wiki/buffs/20104-shield-of-the-sun-creates-a-absorvs-damage-for-5-seconds|Shield of the Sun : Creates a absorvs damage for 5 seconds]] (100%); applies [[wiki/buffs/20105-shield-of-the-sun-movement-speed|Shield of the Sun : Movement Speed]] (100%); applies [[wiki/buffs/20104-shield-of-the-sun-creates-a-absorvs-damage-for-5-seconds|Shield of the Sun : Creates a absorvs damage for 5 seconds]] (5%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 20107 | 6 | 20108 |

### Used by

- Weapon skill **hero set 3** of WeaponBase 71: [[wiki/items/8002-amaterasu|Amaterasu]], [[wiki/items/8502-crystal-amaterasu|Crystal : Amaterasu]]
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

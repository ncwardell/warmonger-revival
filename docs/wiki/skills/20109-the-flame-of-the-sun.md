---
title: "The Flame of the Sun"
type: "skill"
id: 20109
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20109", "client: StringAll_Eng SkillComment_20109 (tooltip value tags)"]
name_key: "Skill_20109"
desc_key: "SkillComment_20109"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 5, "type_name": "MP", "amount": 490}
cooldown: {"ms": 90000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 100}
  - {"slot": 2, "type": 102, "value": 100, "rate": 0}
  - {"slot": 3, "type": 362, "value": 1, "rate": 10}
damage_or_effect: {"kind": "damage (magic?)", "base": 100, "ability_pct": 100}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 100}
  - {"tag": "EF_R_MDAM", "value": 100}
requirements:
  - {"type": 20107, "a": 6, "b": 20108}
visual: 420
icon: {"file": "Skill_Boss_01.dds", "index": 19}
used_by:
  - {"weapon_base": 71, "slot": 8, "items": [8002, 8502]}
---
<!-- generated:start -->
<!-- generated-keys: title=779f54 type=86a754 id=0bb788 sources=eff054 name_key=024052 desc_key=94ae56 kind=356a19 kind_name=9bc378 target=9dc90e range=1b6453 area=d82541 cost=cb4f2a cooldown=bc9744 effect_kind=da4b92 effects=86ff8f damage_or_effect=844296 tooltip_formula=a8acf5 requirements=adeac3 visual=7a9556 icon=40f7db used_by=8a1b0f -->
|  |  |
|---|---|
|  | ![The Flame of the Sun](wiki/assets/skills/20109.png) |
| **Skill id** | `20109` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 10 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 490 MP |
| **Cooldown** | 90 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 420 `아마테라스_태양의 불꽃` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 19 |

### Tooltip

> [Active]Deals damage to nearby enemies by `{EF_STATIC 100}``{EF_R_MDAM 100}`
> Kra Sun Stack +1 
> When using Stack : The shield increases.

Tooltip formula: **100 + 100% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 100 | 0 |
| 3 | 362 | unknown | 1 | 10 |

**Reading:** amount **100 + 100% Ability Power**; damage (magic?).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 20107 | 6 | 20108 |

### Used by

- Weapon skill **hero set 4** of WeaponBase 71: [[wiki/items/8002-amaterasu|Amaterasu]], [[wiki/items/8502-crystal-amaterasu|Crystal : Amaterasu]]
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

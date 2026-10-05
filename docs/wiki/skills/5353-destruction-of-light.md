---
title: "Destruction of light"
type: "skill"
id: 5353
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5353", "client: StringAll_Eng SkillComment_5353 (tooltip value tags)"]
name_key: "Skill_5353"
desc_key: "SkillComment_5353"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 90}
cooldown: {"ms": 10000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 75, "rate": 100}
  - {"slot": 2, "type": 102, "value": 50, "rate": 0}
  - {"slot": 3, "type": 106, "value": 70, "rate": 0}
  - {"slot": 4, "type": 314, "value": 10403, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 75, "ability_pct": 50, "stats": [{"code": 106, "value": 70}], "buffs": [{"buff": 10403, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 75}
  - {"tag": "EF_R_MDAM", "value": 50}
  - {"tag": "EF_R_DEF", "value": 70}
visual: 464
icon: {"file": "Skill_Dolorece_01.png", "index": 35}
used_by:
  - {"weapon_base": 57, "slot": 3, "items": [20015]}
---
<!-- generated:start -->
<!-- generated-keys: title=371ca8 type=86a754 id=bf76ed sources=a21121 name_key=b4c0cc desc_key=0975f9 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=da6e22 cooldown=4aa5a5 effect_kind=da4b92 effects=cc3f64 damage_or_effect=07fd5a tooltip_formula=663dd5 visual=6f946e icon=dd90a4 used_by=5b49ed -->
|  |  |
|---|---|
|  | ![Destruction of light](wiki/assets/skills/5353.png) |
| **Skill id** | `5353` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 90 MP |
| **Cooldown** | 10 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 464 `수호의 마력 메이스_빛의 섬멸` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 35 |

### Tooltip

> [Active] Inflicts `{EF_STATIC 75}``{EF_R_MDAM 50}``{EF_R_DEF 70}` Damage to nearby enemies. Reduces Movement Speed.

Tooltip formula: **75 + 50% Ability Power + 70% Armor** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 50 | 0 |
| 3 | 106 | stat? Armor(%) | 70 | 0 |
| 4 | 314 | applies buff (variant 314) | [[wiki/buffs/10403-destruction-of-light-decreased-move-speed\|Destruction of light : Decreased Move Speed]] | 100 |

**Reading:** amount **75 + 50% Ability Power**; damage (magic?); applies [[wiki/buffs/10403-destruction-of-light-decreased-move-speed|Destruction of light : Decreased Move Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 57: [[wiki/items/20015-magical-protect-mace|Magical Protect Mace]]
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

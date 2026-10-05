---
title: "Destruction of light"
type: "skill"
id: 10353
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10353", "client: StringAll_Eng SkillComment_10353 (tooltip value tags)"]
name_key: "Skill_10353"
desc_key: "SkillComment_10353"
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
  - {"slot": 2, "type": 102, "value": 55, "rate": 0}
  - {"slot": 3, "type": 106, "value": 75, "rate": 0}
  - {"slot": 4, "type": 314, "value": 30403, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 75, "ability_pct": 55, "stats": [{"code": 106, "value": 75}], "buffs": [{"buff": 30403, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 75}
  - {"tag": "EF_R_MDAM", "value": 55}
  - {"tag": "EF_R_DEF", "value": 75}
visual: 464
icon: {"file": "Skill_Dolorece_01.png", "index": 35}
used_by:
  - {"weapon_base": 157, "slot": 3, "items": [21015]}
---
<!-- generated:start -->
<!-- generated-keys: title=371ca8 type=86a754 id=6cd82b sources=fd9751 name_key=87523a desc_key=af20b6 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=da6e22 cooldown=4aa5a5 effect_kind=da4b92 effects=d56f1c damage_or_effect=5bf726 tooltip_formula=c14a32 visual=6f946e icon=dd90a4 used_by=619ff5 -->
|  |  |
|---|---|
|  | ![Destruction of light](wiki/assets/skills/10353.png) |
| **Skill id** | `10353` |
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

> [Active] Inflicts `{EF_STATIC 75}``{EF_R_MDAM 55}``{EF_R_DEF 75}` Damage to nearby enemies. Reduces Movement Speed.

Tooltip formula: **75 + 55% Ability Power + 75% Armor** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 55 | 0 |
| 3 | 106 | stat? Armor(%) | 75 | 0 |
| 4 | 314 | applies buff (variant 314) | [[wiki/buffs/30403-destruction-of-light-decreased-move-speed\|Destruction of light : Decreased Move Speed]] | 100 |

**Reading:** amount **75 + 55% Ability Power**; damage (magic?); applies [[wiki/buffs/30403-destruction-of-light-decreased-move-speed|Destruction of light : Decreased Move Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 157: [[wiki/items/21015-magical-protect-mace|Magical Protect Mace]]
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

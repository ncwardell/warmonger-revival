---
title: "Wave of water"
type: "skill"
id: 20161
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20161", "client: StringAll_Eng SkillComment_20161 (tooltip value tags)"]
name_key: "Skill_20161"
desc_key: "SkillComment_20161"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 5, "type_name": "MP", "amount": 590}
cooldown: {"ms": 110000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 364, "value": 100, "rate": 5}
damage_or_effect: {"kind": "damage (physical?)", "base": 100, "attack_pct": 100}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 100}
  - {"tag": "EF_R_DAM", "value": 100}
visual: 429
icon: {"file": "Skill_Boss_01.dds", "index": 30}
used_by:
  - {"weapon_base": 72, "slot": 8, "items": [8003, 8503]}
---
<!-- generated:start -->
<!-- generated-keys: title=b1d687 type=86a754 id=d77b12 sources=cef068 name_key=db461c desc_key=f59ff0 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=d82541 cost=5baaf6 cooldown=e0e4dd effect_kind=356a19 effects=8a7f61 damage_or_effect=c76639 tooltip_formula=16f859 visual=75988f icon=63ba9c used_by=e222c4 -->
|  |  |
|---|---|
|  | ![Wave of water](wiki/assets/skills/20161.png) |
| **Skill id** | `20161` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 590 MP |
| **Cooldown** | 110 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 429 `사라스바티_물의 파동` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 30 |

### Tooltip

> [Active]When used, it loses `{EF_STATIC 100}``{EF_R_DAM 100}` damage to enemies nearby. 
>  When a shield is created, it inflicts damage on the enemy with an increased number of shields.

Tooltip formula: **100 + 100% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 364 | unknown | 100 | 5 |

**Reading:** amount **100 + 100% Attack**; damage (physical?).

### Used by

- Weapon skill **hero set 4** of WeaponBase 72: [[wiki/items/8003-sarasvati|Sarasvati]], [[wiki/items/8503-crystal-sarasvati|Crystal : Sarasvati]]
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

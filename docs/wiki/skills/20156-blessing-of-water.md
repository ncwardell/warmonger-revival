---
title: "Blessing of water"
type: "skill"
id: 20156
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20156"]
name_key: "Skill_20156"
desc_key: "SkillComment_20156"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 1
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 5, "type_name": "MP", "amount": 590}
cooldown: {"ms": 110000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 100}
  - {"slot": 2, "type": 102, "value": 30, "rate": 0}
  - {"slot": 3, "type": 364, "value": 100, "rate": 5}
damage_or_effect: {"kind": "heal HP", "base": 100, "ability_pct": 30}
visual: 425
icon: {"file": "Skill_Boss_01.dds", "index": 26}
used_by:
  - {"weapon_base": 72, "slot": 4, "items": [8003, 8503]}
---
<!-- generated:start -->
<!-- generated-keys: title=b331de type=86a754 id=c5d9e5 sources=9279a0 name_key=a08f30 desc_key=333b54 kind=356a19 kind_name=9bc378 target=55b685 range=356a19 area=d82541 cost=5baaf6 cooldown=e0e4dd effect_kind=632667 effects=dbc7f6 damage_or_effect=45639c visual=7a6986 icon=771dfc used_by=44e0e1 -->
|  |  |
|---|---|
|  | ![Blessing of water](../assets/skills/20156.png) |
| **Skill id** | `20156` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 590 MP |
| **Cooldown** | 110 s |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 425 `사라스바티_물의 축복` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 26 |

### Tooltip

> [Active]When you use it restores the party around you. 
>  When a shield is created, it restores the party to an increased number of shields.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 30 | 0 |
| 3 | 364 | unknown | 100 | 5 |

**Reading:** amount **100 + 30% Ability Power**; heal HP.

### Used by

- Weapon skill **R** of WeaponBase 72: [[wiki/items/8003-sarasvati|Sarasvati]], [[wiki/items/8503-crystal-sarasvati|Crystal : Sarasvati]]
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

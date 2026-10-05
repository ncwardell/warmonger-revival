---
title: "Divine Recovery"
type: "skill"
id: 10351
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10351"]
name_key: "Skill_10351"
desc_key: "SkillComment_10351"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 1
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 131, "value": 7, "rate": 0}
damage_or_effect: {"kind": "heal HP", "stats": [{"code": 131, "value": 7}]}
visual: 462
icon: {"file": "Skill_Dolorece_01.png", "index": 33}
used_by:
  - {"weapon_base": 157, "slot": 1, "items": [21015]}
---
<!-- generated:start -->
<!-- generated-keys: title=7c78e1 type=86a754 id=3809f8 sources=2bab13 name_key=cc8777 desc_key=3b55ac kind=356a19 kind_name=9bc378 target=55b685 range=356a19 area=344636 cost=e4e7cf cooldown=e3989d effect_kind=632667 effects=23a4e2 damage_or_effect=5f90fb visual=5a73b7 icon=c8aa0b used_by=186c19 -->
|  |  |
|---|---|
|  | ![Divine Recovery](../assets/skills/10351.png) |
| **Skill id** | `10351` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 462 `수호의 마력 메이스_신성한 회복` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 33 |

### Tooltip

> [Active] Restores 7% HP of your nearby allies total HP.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 7 | 0 |

**Reading:** heal HP.

### Used by

- Weapon skill **Q** of WeaponBase 157: [[wiki/items/21015-magical-protect-mace|Magical Protect Mace]]
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

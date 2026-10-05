---
title: "Holy Shield"
type: "skill"
id: 10354
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10354"]
name_key: "Skill_10354"
desc_key: "SkillComment_10354"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 1
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 440}
cooldown: {"ms": 80000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 308, "value": 30402, "rate": 100}
  - {"slot": 2, "type": 317, "value": 30402, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 30402, "rate": 100}, {"buff": 30402, "rate": 100}]}
visual: 465
icon: {"file": "Skill_Dolorece_01.png", "index": 36}
used_by:
  - {"weapon_base": 157, "slot": 4, "items": [21015]}
---
<!-- generated:start -->
<!-- generated-keys: title=8834af type=86a754 id=f456ed sources=cfe616 name_key=686dd8 desc_key=cac58d kind=356a19 kind_name=9bc378 target=55b685 range=356a19 area=6d01a6 cost=15d513 cooldown=dceb3e effect_kind=b6589f effects=d60914 damage_or_effect=e2c2ff visual=f8b5f6 icon=7da0f2 used_by=1f6082 -->
|  |  |
|---|---|
|  | ![Holy Shield](wiki/assets/skills/10354.png) |
| **Skill id** | `10354` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 440 MP |
| **Cooldown** | 80 s |
| **Visual** | skillVisual 465 `수호의 마력 메이스_신성한 보호막` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 36 |

### Tooltip

> [Active] Creates a Shield worth 50% of your total Stamina to your nearby allies.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 308 | applies buff (variant 308) | [[wiki/buffs/30402-holy-shield-creates-a-absorvs-damage-for-7-seconds\|Holy Shield : Creates a absorvs damage for 7 seconds]] | 100 |
| 2 | 317 | applies buff (variant 317) | [[wiki/buffs/30402-holy-shield-creates-a-absorvs-damage-for-7-seconds\|Holy Shield : Creates a absorvs damage for 7 seconds]] | 100 |

**Reading:** applies [[wiki/buffs/30402-holy-shield-creates-a-absorvs-damage-for-7-seconds|Holy Shield : Creates a absorvs damage for 7 seconds]] (100%); applies [[wiki/buffs/30402-holy-shield-creates-a-absorvs-damage-for-7-seconds|Holy Shield : Creates a absorvs damage for 7 seconds]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 157: [[wiki/items/21015-magical-protect-mace|Magical Protect Mace]]
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

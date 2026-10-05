---
title: "Breeze"
type: "skill"
id: 5009
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5009"]
name_key: "Skill_5009"
desc_key: "SkillComment_5009"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 6
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10012, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10012, "rate": 100}]}
visual: 86
icon: {"file": "Skill_Einsel_01.png", "index": 1}
used_by:
  - {"weapon_base": 1, "slot": 2, "items": [10000]}
---
<!-- generated:start -->
<!-- generated-keys: title=ad0da9 type=86a754 id=3ebcce sources=0edc34 name_key=416c1c desc_key=50e919 kind=356a19 kind_name=9bc378 target=55b685 range=c1dfd9 area=d82541 cost=e4e7cf cooldown=e3989d effect_kind=b6589f effects=8ce1b3 damage_or_effect=fce8cf visual=3c26df icon=86c28e used_by=8aa568 -->
|  |  |
|---|---|
|  | ![Breeze](wiki/assets/skills/5009.png) |
| **Skill id** | `5009` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 6 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Visual** | skillVisual 86 `PCE_Staff_01_W_산들 바람` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 1 |

### Tooltip

> [Active] Send out a breeze, increasing the nearby party's Ability Power by 20% and Movement Speed by 50 for 5 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10012-breeze-increased-ability-power-and-movement-speed\|Breeze : Increased Ability Power and Movement Speed]] | 100 |

**Reading:** applies [[wiki/buffs/10012-breeze-increased-ability-power-and-movement-speed|Breeze : Increased Ability Power and Movement Speed]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 1: [[wiki/items/10000-magical-storm-wand|Magical Storm Wand]]
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

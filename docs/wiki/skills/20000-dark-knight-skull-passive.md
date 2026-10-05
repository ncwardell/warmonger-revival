---
title: "Dark Knight Skull Passive"
type: "skill"
id: 20000
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20000"]
name_key: "Skill_20000"
desc_key: "SkillComment_20000"
kind: 2
kind_name: "passive"
target: {"type": 3, "type_name": "self", "relation": [], "unit_classes": [], "max_targets": 1}
range: 0
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 300, "value": 20020, "rate": 100}
  - {"slot": 2, "type": 300, "value": 20023, "rate": 100}
  - {"slot": 3, "type": 300, "value": 20022, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20020, "rate": 100}, {"buff": 20023, "rate": 100}, {"buff": 20022, "rate": 100}]}
visual: 352
icon: {"file": "Policy.png", "index": 37}
used_by:
  - {"weapon_base": 69, "slot": 3, "items": [8000, 8500]}
---
<!-- generated:start -->
<!-- generated-keys: title=ee81e2 type=86a754 id=352bc7 sources=d2a9eb name_key=1ed34f desc_key=cbf080 kind=da4b92 kind_name=3844d5 target=17c4ad range=b6589f area=344636 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=e969da damage_or_effect=35efea visual=efbc08 icon=30f6b2 used_by=bd3a9e -->
|  |  |
|---|---|
|  | ![Dark Knight Skull Passive](wiki/assets/skills/20000.png) |
| **Skill id** | `20000` |
| **Kind** | passive (2) |
| **Target** | self; -; units: -; up to 1 |
| **Range** | 0 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Visual** | skillVisual 352 `화염 구슬 이펙트` |
| **Icon** | `ui/icons/Policy.png` cell 37 |

### Tooltip

> [Passive] Resurrection within in 5 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 300 | applies buff (variant 300) | [[wiki/buffs/20020-immortal-body-recovering-for-300-seconds\|Immortal Body : Recovering for 300 seconds]] | 100 |
| 2 | 300 | applies buff (variant 300) | [[wiki/buffs/20023-immortal-body-revival\|Immortal Body : Revival]] | 100 |
| 3 | 300 | applies buff (variant 300) | [[wiki/buffs/20022-immortal-body-40-reduced-health\|Immortal Body : 40% reduced Health]] | 100 |

**Reading:** applies [[wiki/buffs/20020-immortal-body-recovering-for-300-seconds|Immortal Body : Recovering for 300 seconds]] (100%); applies [[wiki/buffs/20023-immortal-body-revival|Immortal Body : Revival]] (100%); applies [[wiki/buffs/20022-immortal-body-40-reduced-health|Immortal Body : 40% reduced Health]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 69: [[wiki/items/8000-dark-knight-skull|Dark knight Skull]], [[wiki/items/8500-crystal-dark-knight-skull|Crystal : Dark knight Skull]]
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

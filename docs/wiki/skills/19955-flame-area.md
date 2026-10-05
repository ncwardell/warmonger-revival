---
title: "Flame area"
type: "skill"
id: 19955
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 19955"]
name_key: "Skill_19955"
desc_key: "SkillComment_19955"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 6
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: null
cooldown: {"ms": 75000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 131, "value": 6, "rate": 1}
  - {"slot": 2, "type": 314, "value": 19956, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "stats": [{"code": 131, "value": 6}], "buffs": [{"buff": 19956, "rate": 100}]}
visual: 406
icon: {"file": "Skill_Einsel_01.png", "index": 39}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=d01485 type=86a754 id=0675ed sources=37201f name_key=54eecd desc_key=67265e kind=356a19 kind_name=9bc378 target=d1cc1b range=c1dfd9 area=d82541 cost=2be88c cooldown=cf1f8c effect_kind=356a19 effects=962491 damage_or_effect=2a7c09 visual=b20297 icon=56e68a used_by=97d170 -->
|  |  |
|---|---|
|  | ![Flame area](wiki/assets/skills/19955.png) |
| **Skill id** | `19955` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 6 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cooldown** | 75 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 406 `모리온_화염 지역_피격` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 39 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 6 | 1 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/19956-flame-area-movement-25-3-secs\|Flame area : Movement -25% (3 Secs)]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/19956-flame-area-movement-25-3-secs|Flame area : Movement -25% (3 Secs)]] (100%).
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

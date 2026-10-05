---
title: "Puddle"
type: "skill"
id: 20155
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 20155"]
name_key: "Skill_20155"
desc_key: "SkillComment_20155"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: null
cooldown: {"ms": 20000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 314, "value": 20155, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 20155, "rate": 100}]}
visual: 424
icon: {"file": "Skill_Boss_01.dds", "index": 25}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=def61d type=86a754 id=232bb1 sources=1777cb name_key=5f3186 desc_key=9c96a7 kind=356a19 kind_name=9bc378 target=9dc90e range=fe5dbb area=6d01a6 cost=2be88c cooldown=628d31 effect_kind=356a19 effects=173227 damage_or_effect=9eec18 visual=778736 icon=f7179c used_by=97d170 -->
|  |  |
|---|---|
|  | ![Puddle](wiki/assets/skills/20155.png) |
| **Skill id** | `20155` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 10 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cooldown** | 20 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 424 `사라스바티_웅덩이` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 25 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/20155-puddle-reduced-movement-speed\|Puddle : Reduced Movement Speed]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/20155-puddle-reduced-movement-speed|Puddle : Reduced Movement Speed]] (100%).
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

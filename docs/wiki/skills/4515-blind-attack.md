---
title: "Blind Attack"
type: "skill"
id: 4515
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 4515"]
name_key: "Skill_4515"
desc_key: "SkillComment_4515"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["player"], "max_targets": 15}
range: 6
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 4514, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 4514, "rate": 100}]}
icon: {"file": "Policy_01.png", "index": 36}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=fb42b2 type=86a754 id=53e0c2 sources=c4f1b7 name_key=0d9210 desc_key=7c5faa kind=356a19 kind_name=9bc378 target=e0ddef range=c1dfd9 area=d82541 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=8a4205 damage_or_effect=24970a icon=494d30 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Blind Attack](wiki/assets/skills/4515.png) |
| **Skill id** | `4515` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: player; up to 15 |
| **Range** | 6 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Icon** | `ui/icons/Policy_01.png` cell 36 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/4514-blind-reduced-movement-speed\|Blind : Reduced Movement Speed.]] | 100 |

**Reading:** applies [[wiki/buffs/4514-blind-reduced-movement-speed|Blind : Reduced Movement Speed.]] (100%).
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

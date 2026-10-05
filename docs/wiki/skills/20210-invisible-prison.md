---
title: "Invisible prison"
type: "skill"
id: 20210
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 20210"]
name_key: "Skill_20210"
desc_key: "SkillComment_20210"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["player"], "max_targets": 15}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: null
cooldown: {"ms": 1000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 20211, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20211, "rate": 100}]}
icon: {"file": "Skill_Boss_01.dds", "index": 36}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=db02bb type=86a754 id=666687 sources=048e65 name_key=4d66b1 desc_key=8af6f9 kind=356a19 kind_name=9bc378 target=e0ddef range=1b6453 area=6d01a6 cost=2be88c cooldown=4a6a0b effect_kind=b6589f effects=412fcb damage_or_effect=b16c17 icon=da8658 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Invisible prison](../assets/skills/20210.png) |
| **Skill id** | `20210` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: player; up to 15 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cooldown** | 1 s |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 36 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/20211-invisible-prison\|Invisible prison]] | 100 |

**Reading:** applies [[wiki/buffs/20211-invisible-prison|Invisible prison]] (100%).
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

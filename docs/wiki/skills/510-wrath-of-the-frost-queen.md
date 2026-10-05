---
title: "Wrath of the Frost Queen"
type: "skill"
id: 510
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 510"]
name_key: "Skill_510"
desc_key: "SkillComment_510"
kind: 2
kind_name: "passive"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 10.0, "width_or_angle": 10.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10115, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10115, "rate": 100}]}
icon: {"file": "Skill_MagicScholar_17.png", "index": 0}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=07d4aa type=86a754 id=2d3fbc sources=8ec04c name_key=332adc desc_key=e7d06b kind=da4b92 kind_name=3844d5 target=d1cc1b range=b1d578 area=40b3f5 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=59e7bb damage_or_effect=7ed97b icon=826275 used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `510` |
| **Kind** | passive (2) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 10, width/angle 10 |
| **Icon** | `ui/icons/Skill_MagicScholar_17.png` cell 0 |

### Tooltip

> Wrath of the Frost Queen

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10115-wrath\|Wrath]] | 100 |

**Reading:** applies [[wiki/buffs/10115-wrath|Wrath]] (100%).
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

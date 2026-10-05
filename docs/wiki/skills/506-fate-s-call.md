---
title: "Fate's Call"
type: "skill"
id: 506
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 506"]
name_key: "Skill_506"
desc_key: "SkillComment_506"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 10.0, "width_or_angle": 10.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10133, "rate": 100}
  - {"slot": 2, "type": 136, "value": 30, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10133, "rate": 100}], "stats": [{"code": 136, "value": 30}]}
visual: 353
icon: {"file": "Skill_MagicScholar_17.png", "index": 0}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=081501 type=86a754 id=e408d8 sources=172ea9 name_key=7c59d3 desc_key=52cb6a kind=356a19 kind_name=9bc378 target=d1cc1b range=b1d578 area=40b3f5 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=725ce7 damage_or_effect=ff78ee visual=8ada66 icon=826275 used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `506` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 10, width/angle 10 |
| **Visual** | skillVisual 353 `파멸의반지 이펙트` |
| **Icon** | `ui/icons/Skill_MagicScholar_17.png` cell 0 |

### Tooltip

> Fate's Call

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10133-fate-s-call\|Fate's Call]] | 100 |
| 2 | 136 | stat? Damage(%)+ | 30 | 100 |

**Reading:** applies [[wiki/buffs/10133-fate-s-call|Fate's Call]] (100%).
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

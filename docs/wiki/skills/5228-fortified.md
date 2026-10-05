---
title: "Fortified"
type: "skill"
id: 5228
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5228"]
name_key: "Skill_5228"
desc_key: "SkillComment_5228"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally"], "unit_classes": ["player", "structure"], "max_targets": 3}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 255.0, "width_or_angle": 255.0}
cost: {"type": 14, "type_name": "TP", "amount": 190}
cooldown: {"ms": 30000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 452, "value": 10282, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10282, "rate": 100}]}
icon: {"file": "Policy_01.png", "index": 39}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=ce9b19 type=86a754 id=fad948 sources=a996f9 name_key=e0164b desc_key=d8dd55 kind=356a19 kind_name=9bc378 target=5eb991 range=3028f5 area=febbd1 cost=6750b6 cooldown=6963fe effect_kind=b6589f effects=aa964f damage_or_effect=4b9f15 icon=30da17 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Fortified](../assets/skills/5228.png) |
| **Skill id** | `5228` |
| **Kind** | active (1) |
| **Target** | self; self, ally; units: player, structure; up to 3 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 255, width/angle 255 |
| **Cost** | 190 TP |
| **Cooldown** | 30 s |
| **Icon** | `ui/icons/Policy_01.png` cell 39 |

### Tooltip

> Increases the offensive and defensive potential of all 
> your towers on the map.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 452 | applies buff (variant 452) | [[wiki/buffs/10282-strengthen-tower\|Strengthen Tower]] | 100 |

**Reading:** applies [[wiki/buffs/10282-strengthen-tower|Strengthen Tower]] (100%).

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 180): Fortified · 2,000 / 180 · 2,000 / 120
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

---
title: "Hungry arrows"
type: "skill"
id: 20205
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20205"]
name_key: "Skill_20205"
desc_key: "SkillComment_20205"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 1.0}
cost: {"type": 5, "type_name": "MP", "amount": 50}
cooldown: {"ms": 2000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 304, "value": 20205, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20205, "rate": 100}]}
icon: {"file": "Skill_Boss_01.dds", "index": 32}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=1de249 type=86a754 id=570f73 sources=e55565 name_key=4cc11c desc_key=81cf22 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 area=394af4 cost=7e5cd4 cooldown=367d78 effect_kind=b6589f effects=ce55b3 damage_or_effect=cde9e5 icon=6834b3 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Hungry arrows](wiki/assets/skills/20205.png) |
| **Skill id** | `20205` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 1, width/angle 1 |
| **Cost** | 50 MP |
| **Cooldown** | 2 s |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 32 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 304 | applies buff (variant 304) | [[wiki/buffs/20205-hungry-arrows-increased-life-steal\|Hungry arrows: increased Life Steal]] | 100 |

**Reading:** applies [[wiki/buffs/20205-hungry-arrows-increased-life-steal|Hungry arrows: increased Life Steal]] (100%).
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

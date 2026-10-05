---
title: "Lightning"
type: "skill"
id: 4706
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 4706"]
name_key: "Skill_4706"
desc_key: "SkillComment_4706"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: null
cooldown: null
effect_kind: 15
effects:
  - {"slot": 1, "type": 330, "value": 300, "rate": 100}
  - {"slot": 2, "type": 131, "value": 5, "rate": 1}
  - {"slot": 3, "type": 314, "value": 4706, "rate": 100}
damage_or_effect: {"kind": "effect kind 15", "base": 300, "stats": [{"code": 131, "value": 5}], "buffs": [{"buff": 4706, "rate": 100}]}
icon: {"file": "Policy_01.png", "index": 24}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=5cd14f type=86a754 id=925de5 sources=160a0f name_key=a6dab9 desc_key=f51bda kind=356a19 kind_name=9bc378 target=9dc90e range=fe5dbb area=950fc9 cost=2be88c cooldown=2be88c effect_kind=f1abd6 effects=7ac8e9 damage_or_effect=6f45e0 icon=ae8ff0 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Lightning](wiki/assets/skills/4706.png) |
| **Skill id** | `4706` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 10 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Effect kind** | ? (15) |
| **Icon** | `ui/icons/Policy_01.png` cell 24 |

### Tooltip

> Click on a field or mini-map to inflict 300 (+ 5% of your maximum HP) damage per second to enemies within a certain radius.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 300 | 100 |
| 2 | 131 | stat? Health(%) | 5 | 1 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/4706\|Buff 4706]] | 100 |

**Reading:** amount **300**; effect kind 15; applies [[wiki/buffs/4706|Buff 4706]] (100%).
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

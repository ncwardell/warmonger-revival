---
title: "Flaming fire"
type: "skill"
id: 19967
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 19967"]
name_key: "Skill_19967"
desc_key: "SkillComment_19967"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 0.0}
cost: null
cooldown: null
effect_kind: 31
effects:
  - {"slot": 1, "type": 131, "value": 2, "rate": 0}
  - {"slot": 2, "type": 302, "value": 19969, "rate": 100}
damage_or_effect: {"kind": "heal HP", "stats": [{"code": 131, "value": 2}], "buffs": [{"buff": 19969, "rate": 100}]}
icon: {"file": "Items_20.png", "index": 28}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=7ac68a type=86a754 id=94e5af sources=5fd5ed name_key=76d895 desc_key=57bd58 kind=356a19 kind_name=9bc378 target=d99f6c range=77de68 area=c0807e cost=2be88c cooldown=2be88c effect_kind=632667 effects=eb1718 damage_or_effect=e79d64 icon=23f487 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Flaming fire](../assets/skills/19967.png) |
| **Skill id** | `19967` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 3, width/angle 0 |
| **Effect kind** | heal HP (31) |
| **Icon** | `ui/icons/Items_20.png` cell 28 |

### Tooltip

> [Passive]Flaming fire : When you drop below 25% health you recover 20% of your total health over 10 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 2 | 0 |
| 2 | 302 | applies buff (variant 302) | [[wiki/buffs/19969-flaming-fire\|Flaming fire]] | 100 |

**Reading:** heal HP; applies [[wiki/buffs/19969-flaming-fire|Flaming fire]] (100%).
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

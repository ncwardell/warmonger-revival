---
title: "Savior's Gift"
type: "skill"
id: 10282
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 10282"]
name_key: "Skill_10282"
desc_key: "SkillComment_10282"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: null
cooldown: {"ms": 80000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 131, "value": 5, "rate": 1}
damage_or_effect: {"kind": "heal HP", "stats": [{"code": 131, "value": 5}]}
visual: 367
icon: {"file": "Skill_Einsel_01.png", "index": 11}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=eee00b type=86a754 id=d3c830 sources=00fa98 name_key=85fd7d desc_key=52e3b2 kind=356a19 kind_name=9bc378 target=55b685 range=fe5dbb area=d82541 cost=2be88c cooldown=dceb3e effect_kind=632667 effects=9223b3 damage_or_effect=9e6559 visual=f09093 icon=5095da used_by=97d170 -->
|  |  |
|---|---|
|  | ![Savior's Gift](wiki/assets/skills/10282.png) |
| **Skill id** | `10282` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cooldown** | 80 s |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 367 `시즌1_PCE_Staff_03_R_구원의 선물_피격` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 11 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 5 | 1 |

**Reading:** heal HP.
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

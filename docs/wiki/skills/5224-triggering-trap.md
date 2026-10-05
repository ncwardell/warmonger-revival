---
title: "Triggering Trap"
type: "skill"
id: 5224
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 5224"]
name_key: "Skill_5224"
desc_key: "SkillComment_5224"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["player"], "max_targets": 5}
range: 2
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 2.0}
cost: null
cooldown: {"ms": 1000, "group": 0}
effect_kind: 15
effects:
  - {"slot": 1, "type": 330, "value": 200, "rate": 100}
damage_or_effect: {"kind": "effect kind 15", "base": 200}
visual: 359
icon: {"file": "Policy_01.png", "index": 34}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=95c691 type=86a754 id=68ecbf sources=663e41 name_key=7a3a61 desc_key=dcbc9f kind=356a19 kind_name=9bc378 target=b7c52c range=da4b92 area=0c52f0 cost=2be88c cooldown=4a6a0b effect_kind=f1abd6 effects=68d1ef damage_or_effect=1ad5e8 visual=2a5ac5 icon=c4012e used_by=97d170 -->
|  |  |
|---|---|
|  | ![Triggering Trap](wiki/assets/skills/5224.png) |
| **Skill id** | `5224` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: player; up to 5 |
| **Range** | 2 (world units) |
| **Area** | circle, radius 5, width/angle 2 |
| **Cooldown** | 1 s |
| **Effect kind** | ? (15) |
| **Visual** | skillVisual 359 `TP스킬_부비트랩` |
| **Icon** | `ui/icons/Policy_01.png` cell 34 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 200 | 100 |

**Reading:** amount **200**; effect kind 15.
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

---
title: "Highly Concentrated Bomb"
type: "skill"
id: 4520
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 4520"]
name_key: "Skill_4520"
desc_key: "SkillComment_4520"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["player", "structure"], "max_targets": 1}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: null
cooldown: null
effect_kind: 15
effects:
  - {"slot": 1, "type": 330, "value": 10000, "rate": 100}
  - {"slot": 2, "type": 131, "value": 60, "rate": 1}
damage_or_effect: {"kind": "effect kind 15", "base": 10000, "stats": [{"code": 131, "value": 60}]}
visual: 443
icon: {"file": "Policy_01.png", "index": 16}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=31d608 type=86a754 id=b2d754 sources=7c4e08 name_key=1bbad8 desc_key=d97ba0 kind=356a19 kind_name=9bc378 target=49c148 range=1b6453 area=6d01a6 cost=2be88c cooldown=2be88c effect_kind=f1abd6 effects=735872 damage_or_effect=8a0bac visual=ac3e7b icon=51436c used_by=97d170 -->
|  |  |
|---|---|
|  | ![Highly Concentrated Bomb](wiki/assets/skills/4520.png) |
| **Skill id** | `4520` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: player, structure; up to 1 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Effect kind** | ? (15) |
| **Visual** | skillVisual 443 `TP 스킬_포격` |
| **Icon** | `ui/icons/Policy_01.png` cell 16 |

### Tooltip

> Attack the middle boss and the boss. If there is an Middle boss, attack the middle boss first

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 10,000 | 100 |
| 2 | 131 | stat? Health(%) | 60 | 1 |

**Reading:** amount **10,000**; effect kind 15.
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

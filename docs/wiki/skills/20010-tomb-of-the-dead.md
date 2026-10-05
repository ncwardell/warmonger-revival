---
title: "Tomb of the Dead"
type: "skill"
id: 20010
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 20010"]
name_key: "Skill_5187"
desc_key: "SkillComment_5187"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 5.0}
cost: null
cooldown: {"ms": 120000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 131, "value": 5, "rate": 1}
  - {"slot": 2, "type": 314, "value": 20009, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "stats": [{"code": 131, "value": 5}], "buffs": [{"buff": 20009, "rate": 100}]}
visual: 323
icon: {"file": "Policy.png", "index": 42}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=25fe5b type=86a754 id=9e1af8 sources=136f70 name_key=c078b7 desc_key=9693ae kind=356a19 kind_name=9bc378 target=d1cc1b range=ac3478 area=ec7019 cost=2be88c cooldown=a7242f effect_kind=da4b92 effects=bd64bc damage_or_effect=2be8af visual=cb4dd5 icon=5cb950 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Tomb of the Dead](wiki/assets/skills/20010.png) |
| **Skill id** | `20010` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 6, width/angle 5 |
| **Cooldown** | 120 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 323 `Skeleton_King_변신스킬_06_망자의 무덤_장판 피격` |
| **Icon** | `ui/icons/Policy.png` cell 42 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 5 | 1 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/20009-tomb-of-the-dead-reduced-movement-speed\|Tomb of the Dead : Reduced Movement Speed]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20009-tomb-of-the-dead-reduced-movement-speed|Tomb of the Dead : Reduced Movement Speed]] (100%).
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

---
title: "Guardian Passive"
type: "skill"
id: 20050
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20050"]
name_key: "Skill_20050"
desc_key: "SkillComment_20050"
kind: 2
kind_name: "passive"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: null
cooldown: null
effect_kind: 2
effects:
  - {"slot": 1, "type": 303, "value": 10237, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 10237, "rate": 100}]}
visual: 352
icon: {"file": "Items_20.png", "index": 27}
used_by:
  - {"hero": 2, "slot": 1}
  - {"hero": 52, "slot": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=7ca66a type=86a754 id=c001f7 sources=f863ed name_key=65f911 desc_key=1b617f kind=da4b92 kind_name=3844d5 target=d1cc1b range=77de68 area=344636 cost=2be88c cooldown=2be88c effect_kind=da4b92 effects=bd4dec damage_or_effect=1044ac visual=efbc08 icon=13db30 used_by=c98cf7 -->
|  |  |
|---|---|
|  | ![Guardian Passive](wiki/assets/skills/20050.png) |
| **Skill id** | `20050` |
| **Kind** | passive (2) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 352 `화염 구슬 이펙트` |
| **Icon** | `ui/icons/Items_20.png` cell 27 |

### Tooltip

> [Passive]Ambition of the Warrior : Reduces enemy armor and resistances by 5% when inflicting damage with a base attack.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/10237-ambition-of-the-warrior\|Ambition of the Warrior]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/10237-ambition-of-the-warrior|Ambition of the Warrior]] (100%).

### Used by

- Hero [[wiki/heroes/2-guardian|Guardian]], skill 1
- Hero [[wiki/heroes/52-guardian-crystal|Guardian (Crystal)]], skill 1
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

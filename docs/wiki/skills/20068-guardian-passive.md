---
title: "Guardian Passive"
type: "skill"
id: 20068
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20068"]
name_key: "Skill_20068"
desc_key: "SkillComment_20068"
kind: 2
kind_name: "passive"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: null
cooldown: null
effect_kind: 2
effects:
  - {"slot": 1, "type": 303, "value": 20072, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20072, "rate": 100}]}
visual: 352
icon: {"file": "Items_20.png", "index": 27}
used_by:
  - {"hero": 2, "slot": 6}
  - {"hero": 2, "slot": 7}
  - {"hero": 2, "slot": 8}
  - {"hero": 2, "slot": 9}
  - {"hero": 2, "slot": 10}
  - {"hero": 52, "slot": 6}
  - {"hero": 52, "slot": 7}
  - {"hero": 52, "slot": 8}
  - {"hero": 52, "slot": 9}
  - {"hero": 52, "slot": 10}
---
<!-- generated:start -->
<!-- generated-keys: title=7ca66a type=86a754 id=e7fa0d sources=9b08d8 name_key=8c5fd4 desc_key=2b380c kind=da4b92 kind_name=3844d5 target=d1cc1b range=77de68 area=344636 cost=2be88c cooldown=2be88c effect_kind=da4b92 effects=c3cc7b damage_or_effect=e3240c visual=efbc08 icon=13db30 used_by=d4d198 -->
|  |  |
|---|---|
|  | ![Guardian Passive](wiki/assets/skills/20068.png) |
| **Skill id** | `20068` |
| **Kind** | passive (2) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 352 `화염 구슬 이펙트` |
| **Icon** | `ui/icons/Items_20.png` cell 27 |

### Tooltip

> [Passive]Ambition of the Warrior : Reduces enemy armor and resistances by 20% when inflicting damage with a base attack.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20072-ambition-of-the-warrior\|Ambition of the Warrior]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20072-ambition-of-the-warrior|Ambition of the Warrior]] (100%).

### Used by

- Hero Guardian, skill 6
- Hero Guardian, skill 7
- Hero Guardian, skill 8
- Hero Guardian, skill 9
- Hero Guardian, skill 10
- Hero Guardian, skill 6
- Hero Guardian, skill 7
- Hero Guardian, skill 8
- Hero Guardian, skill 9
- Hero Guardian, skill 10
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

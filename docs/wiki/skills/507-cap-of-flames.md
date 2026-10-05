---
title: "Cap of Flames"
type: "skill"
id: 507
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 507"]
name_key: "Skill_507"
desc_key: "SkillComment_507"
kind: 2
kind_name: "passive"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: null
cooldown: null
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 25, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 25}
visual: 352
icon: {"file": "Skill_MagicScholar_17.png", "index": 0}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=d872ed type=86a754 id=118540 sources=a24cb1 name_key=42c304 desc_key=20772d kind=da4b92 kind_name=3844d5 target=d1cc1b range=77de68 area=344636 cost=2be88c cooldown=2be88c effect_kind=da4b92 effects=7dcb7f damage_or_effect=26d662 visual=efbc08 icon=826275 used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `507` |
| **Kind** | passive (2) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 352 `화염 구슬 이펙트` |
| **Icon** | `ui/icons/Skill_MagicScholar_17.png` cell 0 |

### Tooltip

> Angry Demon

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 25 | 100 |

**Reading:** amount **25**; damage (magic?).
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

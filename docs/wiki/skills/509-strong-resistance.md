---
title: "Strong Resistance"
type: "skill"
id: 509
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 509"]
name_key: "Skill_509"
desc_key: "SkillComment_509"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["player"], "max_targets": 5}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 10.0, "width_or_angle": 10.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10127, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10127, "rate": 100}]}
visual: 267
icon: {"file": "Skill_MagicScholar_17.png", "index": 0}
used_by:
  - {"item_use": 2901}
---
<!-- generated:start -->
<!-- generated-keys: title=8c7f2e type=86a754 id=6d5db0 sources=2074c5 name_key=11691b desc_key=1d7b88 kind=356a19 kind_name=9bc378 target=b7c52c range=b1d578 area=40b3f5 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=38972d damage_or_effect=702e16 visual=81ecfd icon=826275 used_by=8d5a59 -->
|  |  |
|---|---|
| **Skill id** | `509` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: player; up to 5 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 10, width/angle 10 |
| **Visual** | skillVisual 267 `거센 저항의 갑옷 - 범위` |
| **Icon** | `ui/icons/Skill_MagicScholar_17.png` cell 0 |

### Tooltip

> Strong Resistance

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10127-strong-resistance\|Strong Resistance]] | 100 |

**Reading:** applies [[wiki/buffs/10127-strong-resistance|Strong Resistance]] (100%).

### Used by

- Cast when [[wiki/items/2901-strong-resistance|Strong Resistance]] is used (Item_Base option 210)
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

---
title: "Explosion"
type: "skill"
id: 5053
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 5053"]
name_key: "Skill_5053"
desc_key: "SkillComment_5053"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: null
cooldown: {"ms": 15000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 30, "rate": 100}
  - {"slot": 2, "type": 102, "value": 90, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 30, "ability_pct": 90}
visual: 174
icon: null
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=472ab8 type=86a754 id=852ad7 sources=78eefa name_key=f07940 desc_key=350f70 kind=356a19 kind_name=9bc378 target=d1cc1b range=ac3478 area=d82541 cost=2be88c cooldown=e3989d effect_kind=da4b92 effects=693048 damage_or_effect=814b29 visual=d09470 icon=2be88c used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `5053` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cooldown** | 15 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 174 `PCE_Knife_01_E 폭발 (질서의 가호)` |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 30 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 90 | 0 |

**Reading:** amount **30 + 90% Ability Power**; damage (magic?).
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

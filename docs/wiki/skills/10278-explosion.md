---
title: "Explosion"
type: "skill"
id: 10278
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 10278"]
name_key: "Skill_10278"
desc_key: "SkillComment_10278"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: null
cooldown: {"ms": 8000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 105, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 105}
visual: 363
icon: {"file": "Skill_Einsel_01.png", "index": 8}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=472ab8 type=86a754 id=d3ea5d sources=b1d53e name_key=a17db5 desc_key=c9f360 kind=356a19 kind_name=9bc378 target=d1cc1b range=ac3478 area=d82541 cost=2be88c cooldown=9ded33 effect_kind=da4b92 effects=896aa6 damage_or_effect=7688b4 visual=15a17a icon=1aeac2 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Explosion](wiki/assets/skills/10278.png) |
| **Skill id** | `10278` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cooldown** | 8 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 363 `시즌1_PCE_Staff_03_Q_대자연의 가호 폭발` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 8 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 105 | 0 |

**Reading:** amount **70 + 105% Ability Power**; damage (magic?).
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

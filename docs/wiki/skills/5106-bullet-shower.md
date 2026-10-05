---
title: "Bullet shower"
type: "skill"
id: 5106
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 5106"]
name_key: "Skill_5106"
desc_key: "SkillComment_5106"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: null
cooldown: {"ms": 75000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 90, "rate": 100}
  - {"slot": 2, "type": 102, "value": 120, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10088, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 90, "ability_pct": 120, "buffs": [{"buff": 10088, "rate": 100}]}
visual: 265
icon: null
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=9cb8c3 type=86a754 id=515767 sources=2df855 name_key=e348ff desc_key=9ddbc9 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=2be88c cooldown=cf1f8c effect_kind=da4b92 effects=c61c9d damage_or_effect=0da838 visual=25250e icon=2be88c used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `5106` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cooldown** | 75 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 265 `PCE_Gun_01_R 쌍권총소나기 장판피격` |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 90 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 120 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10088-suppressive-fire-reduced-attack-and-movement-speed-for-3-sec\|Suppressive Fire : Reduced Attack and Movement Speed for 3 seconds]] | 100 |

**Reading:** amount **90 + 120% Ability Power**; damage (magic?); applies [[wiki/buffs/10088-suppressive-fire-reduced-attack-and-movement-speed-for-3-sec|Suppressive Fire : Reduced Attack and Movement Speed for 3 seconds]] (100%).
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

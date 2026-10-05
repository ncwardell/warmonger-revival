---
title: "Flame armor"
type: "skill"
id: 19957
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 19957", "client: StringAll_Eng SkillComment_19957 (tooltip value tags)"]
name_key: "Skill_19957"
desc_key: "SkillComment_19957"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 50}
cooldown: {"ms": 2000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 90}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 407
icon: {"file": "Skill_Einsel_01.png", "index": 37}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=3b8f74 type=86a754 id=fd25a5 sources=9e999c name_key=b2034c desc_key=269934 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=7e5cd4 cooldown=367d78 effect_kind=356a19 effects=db4d14 damage_or_effect=75d6a2 tooltip_formula=0fc93d visual=e6de89 icon=04a3fd used_by=97d170 -->
|  |  |
|---|---|
|  | ![Flame armor](wiki/assets/skills/19957.png) |
| **Skill id** | `19957` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 50 MP |
| **Cooldown** | 2 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 407 `모리온_불의 갑옷` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 37 |

### Tooltip

> [Active] Use Mana per second and deal `{EF_STATIC 80}``{EF_R_DAM 90}` Damage to all nearby enemies.

Tooltip formula: **80 + 90% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |

**Reading:** amount **80 + 90% Attack**; damage (physical?).
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

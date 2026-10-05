---
title: "Flame armor"
type: "skill"
id: 5272
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5272", "client: StringAll_Eng SkillComment_5272 (tooltip value tags)"]
name_key: "Skill_5272"
desc_key: "SkillComment_5272"
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
  - {"slot": 2, "type": 101, "value": 30, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 30}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 30}
visual: 391
icon: {"file": "Skill_Einsel_01.png", "index": 37}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=3b8f74 type=86a754 id=57d7de sources=bacd30 name_key=11e1c5 desc_key=52fd13 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=7e5cd4 cooldown=367d78 effect_kind=356a19 effects=a7f8c2 damage_or_effect=26c33f tooltip_formula=4e7b45 visual=4c629c icon=04a3fd used_by=97d170 -->
|  |  |
|---|---|
|  | ![Flame armor](../assets/skills/5272.png) |
| **Skill id** | `5272` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 50 MP |
| **Cooldown** | 2 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 391 `PCE_SwordShd_01_W 불의 갑옷` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 37 |

### Tooltip

> [Active] Use Mana per second and deal `{EF_STATIC 80}``{EF_R_DAM 30}` Damage to all nearby enemies.

Tooltip formula: **80 + 30% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 30 | 0 |

**Reading:** amount **80 + 30% Attack**; damage (physical?).
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

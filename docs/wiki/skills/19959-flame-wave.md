---
title: "Flame wave"
type: "skill"
id: 19959
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 19959", "client: StringAll_Eng SkillComment_19959 (tooltip value tags)"]
name_key: "Skill_19959"
desc_key: "SkillComment_19959"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 130}
cooldown: {"ms": 18000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 90}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 409
icon: {"file": "Skill_Boss_01.dds", "index": 9}
used_by:
  - {"weapon_base": 74, "slot": 6, "items": [8005, 8505]}
---
<!-- generated:start -->
<!-- generated-keys: title=f4884a type=86a754 id=be82e6 sources=f4f246 name_key=1c3062 desc_key=25e2a7 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=58a4ca cooldown=133145 effect_kind=356a19 effects=db4d14 damage_or_effect=75d6a2 tooltip_formula=0fc93d visual=3352d0 icon=797c87 used_by=65459e -->
|  |  |
|---|---|
|  | ![Flame wave](wiki/assets/skills/19959.png) |
| **Skill id** | `19959` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 130 MP |
| **Cooldown** | 18 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 409 `모리온_불의 파동` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 9 |

### Tooltip

> [Active] Deals `{EF_STATIC 80}``{EF_R_DAM 90}` Physical Damage to nearby enemies.

Tooltip formula: **80 + 90% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |

**Reading:** amount **80 + 90% Attack**; damage (physical?).

### Used by

- Weapon skill **hero set 2** of WeaponBase 74: [[wiki/items/8005-morion|Morion]], [[wiki/items/8505-crystal-morion|Crystal : Morion]]
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

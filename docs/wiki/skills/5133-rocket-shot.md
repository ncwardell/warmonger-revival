---
title: "Rocket Shot"
type: "skill"
id: 5133
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5133", "client: StringAll_Eng SkillComment_5133 (tooltip value tags)"]
name_key: "Skill_5133"
desc_key: "SkillComment_5133"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 11
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 12.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 100}
cooldown: {"ms": 12000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 70}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 70}
visual: 276
icon: {"file": "Skill_Dolorece_01.png", "index": 28}
used_by:
  - {"weapon_base": 56, "slot": 1, "items": [40014]}
---
<!-- generated:start -->
<!-- generated-keys: title=021f7d type=86a754 id=2c650d sources=65a671 name_key=788277 desc_key=779267 kind=356a19 kind_name=9bc378 target=aa5d92 range=17ba07 area=855a17 cost=4e8ae0 cooldown=d1c73e delivery=93a212 effect_kind=356a19 effects=15a9c3 damage_or_effect=6fa7d1 tooltip_formula=321def visual=6d3634 icon=b0d762 used_by=a7e0b3 -->
|  |  |
|---|---|
|  | ![Rocket Shot](wiki/assets/skills/5133.png) |
| **Skill id** | `5133` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 11 (world units) |
| **Area** | line / rectangle?, radius 12, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 100 MP |
| **Cooldown** | 12 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 276 `PCD_Cannon_05_Q_캐논발사` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 28 |

### Tooltip

> [Active] Fires a rocket that deals `{EF_STATIC 80}``{EF_R_DAM 70}` Damage.

Tooltip formula: **80 + 70% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |

**Reading:** amount **80 + 70% Attack**; damage (physical?).

### Used by

- Weapon skill **Q** of WeaponBase 56: [[wiki/items/40014-skeleton-king-s-magic-cannon|Skeleton King's Magic Cannon]]
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

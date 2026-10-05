---
title: "Empowered Shot"
type: "skill"
id: 10117
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10117", "client: StringAll_Eng SkillComment_10117 (tooltip value tags)"]
name_key: "Skill_10117"
desc_key: "SkillComment_10117"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 13
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 14.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 100}
cooldown: {"ms": 12000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 85, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30117, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 85, "buffs": [{"buff": 30117, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 85}
visual: 250
icon: {"file": "Skill_Dolorece_01.png", "index": 21}
used_by:
  - {"weapon_base": 153, "slot": 2, "items": [21011]}
---
<!-- generated:start -->
<!-- generated-keys: title=f96cc9 type=86a754 id=5ecabe sources=62934b name_key=1c8369 desc_key=686bfc kind=356a19 kind_name=9bc378 target=e84f24 range=bd307a area=efd331 cost=4e8ae0 cooldown=d1c73e delivery=93a212 effect_kind=356a19 effects=c41557 damage_or_effect=423d37 tooltip_formula=de4d81 visual=ba30fd icon=ac6851 used_by=d665ba -->
|  |  |
|---|---|
|  | ![Empowered Shot](wiki/assets/skills/10117.png) |
| **Skill id** | `10117` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 13 (world units) |
| **Area** | line / rectangle?, radius 14, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 100 MP |
| **Cooldown** | 12 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 250 `PCD_Cannon_02_W 관통탄` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 21 |

### Tooltip

> [Active] Fire an empowered bullet at your enemies dealing `{EF_STATIC 80}``{EF_R_DAM 85}` Damage to the first target it hits. Decreases their Damage and Movement Speed by 30% for 3 seconds.

Tooltip formula: **80 + 85% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 85 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30117-empowered-shot-increases-movement-speed\|Empowered Shot: Increases Movement Speed]] | 100 |

**Reading:** amount **80 + 85% Attack**; damage (physical?); applies [[wiki/buffs/30117-empowered-shot-increases-movement-speed|Empowered Shot: Increases Movement Speed]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 153: [[wiki/items/21011-magical-blast-cannon|Magical Blast Cannon]]
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

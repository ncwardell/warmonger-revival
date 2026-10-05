---
title: "Rocket Shot"
type: "skill"
id: 5298
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5298", "client: StringAll_Eng SkillComment_5298 (tooltip value tags)"]
name_key: "Skill_5298"
desc_key: "SkillComment_5298"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 11
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 14.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 100}
cooldown: {"ms": 12000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 102, "value": 70, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "attack_pct": 80, "ability_pct": 70}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 70}
visual: 383
icon: {"file": "Skill_Dolorece_01.png", "index": 28}
used_by:
  - {"weapon_base": 68, "slot": 1, "items": [20014]}
---
<!-- generated:start -->
<!-- generated-keys: title=021f7d type=86a754 id=b5f175 sources=25e21f name_key=24316f desc_key=3d3836 kind=356a19 kind_name=9bc378 target=e84f24 range=17ba07 area=efd331 cost=4e8ae0 cooldown=d1c73e delivery=93a212 effect_kind=da4b92 effects=8004a9 damage_or_effect=1a84c7 tooltip_formula=0a6707 visual=8c4a0a icon=b0d762 used_by=3ca25e -->
|  |  |
|---|---|
|  | ![Rocket Shot](wiki/assets/skills/5298.png) |
| **Skill id** | `5298` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 11 (world units) |
| **Area** | line / rectangle?, radius 14, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 100 MP |
| **Cooldown** | 12 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 383 `시즌1_PCD_Cannon_05_Q_캐논발사` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 28 |

### Tooltip

> [Active] Fires a rocket that deals `{EF_STATIC 80}``{EF_R_DAM 80}``{EF_R_MDAM 70}` Damage.

Tooltip formula: **80 + 80% Attack + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |

**Reading:** amount **80 + 80% Attack + 70% Ability Power**; damage (magic?).

### Used by

- Weapon skill **Q** of WeaponBase 68: [[wiki/items/20014-skeleton-king-s-magic-cannon|Skeleton King's Magic Cannon]]
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

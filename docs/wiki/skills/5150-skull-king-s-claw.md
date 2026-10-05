---
title: "Skull king's Claw"
type: "skill"
id: 5150
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5150", "client: StringAll_Eng SkillComment_5150 (tooltip value tags)"]
name_key: "Skill_5150"
desc_key: "SkillComment_5150"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 465}
cooldown: {"ms": 85000, "group": 0}
delivery: {"type": 4, "field_tick": 1.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 110, "rate": 100}
  - {"slot": 2, "type": 102, "value": 100, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10175, "rate": 100}
  - {"slot": 4, "type": 314, "value": 10176, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 110, "ability_pct": 100, "buffs": [{"buff": 10175, "rate": 100}, {"buff": 10176, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 110}
  - {"tag": "EF_R_MDAM", "value": 100}
visual: 293
icon: {"file": "Skill_Einsel_01.png", "index": 31}
used_by:
  - {"weapon_base": 15, "slot": 4, "items": [10014]}
---
<!-- generated:start -->
<!-- generated-keys: title=ec91e7 type=86a754 id=505e83 sources=1d5d19 name_key=09fad5 desc_key=73b8f8 kind=356a19 kind_name=9bc378 target=47c86e range=b1d578 area=6d01a6 cost=7fa4df cooldown=a1ede3 delivery=15a656 effect_kind=da4b92 effects=24509f damage_or_effect=17714a tooltip_formula=2ed782 visual=05580c icon=e24f43 used_by=4ed818 -->
|  |  |
|---|---|
|  | ![Skull king's Claw](wiki/assets/skills/5150.png) |
| **Skill id** | `5150` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 10 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 465 MP |
| **Cooldown** | 85 s |
| **Delivery** | projectile / SFX (4), tick 1 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 293 `PCE_Gun_05_R_해골왕의 갈퀴손` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 31 |

### Tooltip

> [Active] Shoot the claw missile to the designated area inflicting `{EF_STATIC 110}``{EF_R_MDAM 100}` Damage. Reduces the Armor and Magic Resistance of all enemies trapped inside.

Tooltip formula: **110 + 100% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 110 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 100 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10175-energetic-claw-restricted\|Energetic Claw : Restricted]] | 100 |
| 4 | 314 | applies buff (variant 314) | [[wiki/buffs/10176-energetic-claw-reduced-armor-and-magic-resistance\|Energetic Claw : Reduced Armor and Magic Resistance]] | 100 |

**Reading:** amount **110 + 100% Ability Power**; damage (magic?); applies [[wiki/buffs/10175-energetic-claw-restricted|Energetic Claw : Restricted]] (100%); applies [[wiki/buffs/10176-energetic-claw-reduced-armor-and-magic-resistance|Energetic Claw : Reduced Armor and Magic Resistance]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 15: [[wiki/items/10014-skeleton-king-s-magic-gun|Skeleton king's Magic Gun]]
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

---
title: "Flash Bang"
type: "skill"
id: 5147
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5147", "client: StringAll_Eng SkillComment_5147 (tooltip value tags)"]
name_key: "Skill_5147"
desc_key: "SkillComment_5147"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 11
area: {"shape": 1, "shape_name": "circle", "radius": 2.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 125}
cooldown: {"ms": 17000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10171, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 80, "buffs": [{"buff": 10171, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 290
icon: {"file": "Skill_Einsel_01.png", "index": 29}
used_by:
  - {"weapon_base": 15, "slot": 2, "items": [10014]}
---
<!-- generated:start -->
<!-- generated-keys: title=23d743 type=86a754 id=9920a5 sources=5a3bbb name_key=9dde86 desc_key=c8ff3b kind=356a19 kind_name=9bc378 target=7056fd range=17ba07 area=8aa5fb cost=f67772 cooldown=c9c532 delivery=93a212 effect_kind=da4b92 effects=44cea6 damage_or_effect=684ef9 tooltip_formula=c2e772 visual=9d3237 icon=bd7250 used_by=224d66 -->
|  |  |
|---|---|
|  | ![Flash Bang](wiki/assets/skills/5147.png) |
| **Skill id** | `5147` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 7 |
| **Range** | 11 (world units) |
| **Area** | circle, radius 2, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 125 MP |
| **Cooldown** | 17 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 290 `PCE_Gun_05_W_암흑 섬광탄` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 29 |

### Tooltip

> [Active] Throw a Flash Bang that deals `{EF_STATIC 80}``{EF_R_MDAM 80}` Damage. The Movement Speed of all targets is reduced.

Tooltip formula: **80 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10171-flash-bang-reduced-movement-speed\|Flash Bang : Reduced Movement Speed]] | 100 |

**Reading:** amount **80 + 80% Ability Power**; damage (magic?); applies [[wiki/buffs/10171-flash-bang-reduced-movement-speed|Flash Bang : Reduced Movement Speed]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 15: [[wiki/items/10014-skeleton-king-s-magic-gun|Skeleton king's Magic Gun]]
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

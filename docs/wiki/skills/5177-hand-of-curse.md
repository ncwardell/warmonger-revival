---
title: "Hand of Curse"
type: "skill"
id: 5177
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5177", "client: StringAll_Eng SkillComment_5177 (tooltip value tags)"]
name_key: "Skill_5177"
desc_key: "SkillComment_5177"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 8
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 11.0, "width_or_angle": 3.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 80}
cooldown: {"ms": 8000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 60, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10212, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 60, "ability_pct": 80, "buffs": [{"buff": 10212, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 60}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 314
icon: {"file": "Skill_Einsel_01.png", "index": 32}
used_by:
  - {"weapon_base": 21, "slot": 1, "items": [10020]}
---
<!-- generated:start -->
<!-- generated-keys: title=b0deb2 type=86a754 id=c14f19 sources=b3f214 name_key=3c4802 desc_key=e25d4e kind=356a19 kind_name=9bc378 target=7056fd range=fe5dbb area=3d2256 cost=e01d1d cooldown=9ded33 delivery=93a212 effect_kind=da4b92 effects=35d358 damage_or_effect=a05769 tooltip_formula=2440c3 visual=6e21fc icon=8a093a used_by=9dcb23 -->
|  |  |
|---|---|
|  | ![Hand of Curse](wiki/assets/skills/5177.png) |
| **Skill id** | `5177` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 7 |
| **Range** | 8 (world units) |
| **Area** | line / rectangle?, radius 11, width/angle 3 (indicator `stick256x512.png`) |
| **Cost** | 80 MP |
| **Cooldown** | 8 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 314 `PCE_Staff_08_Q_느려져!` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 32 |

### Tooltip

> [Active] Launches a wave that deals `{EF_STATIC 60}``{EF_R_MDAM 80}` Damage to everyone in its path. Decreases the Movement Speed of all enemies hit.

Tooltip formula: **60 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 60 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10212-wave-of-mutilation-reduced-movement-speed-for-3-seconds\|Wave of Mutilation : Reduced Movement Speed for 3 seconds]] | 100 |

**Reading:** amount **60 + 80% Ability Power**; damage (magic?); applies [[wiki/buffs/10212-wave-of-mutilation-reduced-movement-speed-for-3-seconds|Wave of Mutilation : Reduced Movement Speed for 3 seconds]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 21: [[wiki/items/10020-magical-devil-wand|Magical Devil Wand]]
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

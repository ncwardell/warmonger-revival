---
title: "Essence Manipulation"
type: "skill"
id: 10064
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10064", "client: StringAll_Eng SkillComment_10064 (tooltip value tags)"]
name_key: "Skill_10064"
desc_key: "SkillComment_10064"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 9
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 10.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 85}
cooldown: {"ms": 9000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 102, "value": 65, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 85, "ability_pct": 65}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_MDAM", "value": 65}
visual: 77
icon: {"file": "Skill_Miriam_01.png", "index": 9}
used_by:
  - {"weapon_base": 124, "slot": 2, "items": [16002]}
---
<!-- generated:start -->
<!-- generated-keys: title=142858 type=86a754 id=272a88 sources=8ec8fd name_key=8ac67e desc_key=9e72f9 kind=356a19 kind_name=9bc378 target=e84f24 range=0ade7c area=728214 cost=4921ef cooldown=db479b delivery=93a212 effect_kind=da4b92 effects=cf7ea1 damage_or_effect=bc1873 tooltip_formula=3d6572 visual=d321d6 icon=dd1ff3 used_by=f2f7cd -->
|  |  |
|---|---|
|  | ![Essence Manipulation](wiki/assets/skills/10064.png) |
| **Skill id** | `10064` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 9 (world units) |
| **Area** | line / rectangle?, radius 10, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 85 MP |
| **Cooldown** | 9 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 77 `PCM_Bow_03_W_정수의 흐름` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 9 |

### Tooltip

> [Active] Shoots an energy wave that deals `{EF_STATIC 85}``{EF_R_MDAM 65}` Damage to all enemies it passes.

Tooltip formula: **85 + 65% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 65 | 0 |

**Reading:** amount **85 + 65% Ability Power**; damage (magic?).

### Used by

- Weapon skill **W** of WeaponBase 124: [[wiki/items/16002-magical-vision-bow|Magical Vision Bow]]
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

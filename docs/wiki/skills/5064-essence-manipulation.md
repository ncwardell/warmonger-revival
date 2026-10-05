---
title: "Essence Manipulation"
type: "skill"
id: 5064
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5064", "client: StringAll_Eng SkillComment_5064 (tooltip value tags)"]
name_key: "Skill_5064"
desc_key: "SkillComment_5064"
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
  - {"slot": 2, "type": 102, "value": 60, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 85, "ability_pct": 60}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_MDAM", "value": 60}
visual: 77
icon: {"file": "Skill_Miriam_01.png", "index": 9}
used_by:
  - {"weapon_base": 24, "slot": 2, "items": [15002]}
---
<!-- generated:start -->
<!-- generated-keys: title=142858 type=86a754 id=a66121 sources=04f95b name_key=57026c desc_key=c0770d kind=356a19 kind_name=9bc378 target=e84f24 range=0ade7c area=728214 cost=4921ef cooldown=db479b delivery=93a212 effect_kind=da4b92 effects=24cace damage_or_effect=8b204e tooltip_formula=97a359 visual=d321d6 icon=dd1ff3 used_by=bc42ed -->
|  |  |
|---|---|
|  | ![Essence Manipulation](../assets/skills/5064.png) |
| **Skill id** | `5064` |
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

> [Active] Shoots an energy wave that deals `{EF_STATIC 85}``{EF_R_MDAM 60}` Damage to all enemies it passes.

Tooltip formula: **85 + 60% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 60 | 0 |

**Reading:** amount **85 + 60% Ability Power**; damage (magic?).

### Used by

- Weapon skill **W** of WeaponBase 24: [[wiki/items/15002-magical-vision-bow|Magical Vision Bow]]
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

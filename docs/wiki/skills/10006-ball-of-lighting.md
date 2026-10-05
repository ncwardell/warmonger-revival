---
title: "Ball of Lighting"
type: "skill"
id: 10006
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10006", "client: StringAll_Eng SkillComment_10006 (tooltip value tags)"]
name_key: "Skill_10006"
desc_key: "SkillComment_10006"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 11.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 90}
cooldown: {"ms": 10000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 90, "rate": 100}
  - {"slot": 2, "type": 102, "value": 85, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 90, "ability_pct": 85}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 90}
  - {"tag": "EF_R_MDAM", "value": 85}
visual: 105
icon: {"file": "Skill_Einsel_01.png", "index": 6}
used_by:
  - {"weapon_base": 102, "slot": 3, "items": [11001]}
---
<!-- generated:start -->
<!-- generated-keys: title=79944f type=86a754 id=e86188 sources=9d9e40 name_key=f0dcce desc_key=06286a kind=356a19 kind_name=9bc378 target=aa5d92 range=b1d578 area=2a66b8 cost=da6e22 cooldown=4aa5a5 delivery=93a212 effect_kind=da4b92 effects=88fa41 damage_or_effect=7df25c tooltip_formula=2b5b19 visual=e114c4 icon=ade420 used_by=a78377 -->
|  |  |
|---|---|
|  | ![Ball of Lighting](../assets/skills/10006.png) |
| **Skill id** | `10006` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | line / rectangle?, radius 11, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 90 MP |
| **Cooldown** | 10 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 105 `PCE_Staff_02_E_섬광탄` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 6 |

### Tooltip

> [Active] Shoot a ball of lightning dealing `{EF_STATIC 90}``{EF_R_MDAM 85}`damage to the first target it hits.

Tooltip formula: **90 + 85% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 90 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 85 | 0 |

**Reading:** amount **90 + 85% Ability Power**; damage (magic?).

### Used by

- Weapon skill **E** of WeaponBase 102: [[wiki/items/11001-magical-thunder-wand|Magical Thunder Wand]]
- Nation policy 7 `PolicyName_7` (Policy.cdb, server-only; buff_or_skill)
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

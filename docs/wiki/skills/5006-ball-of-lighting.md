---
title: "Ball of Lighting"
type: "skill"
id: 5006
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5006", "client: StringAll_Eng SkillComment_5006 (tooltip value tags)"]
name_key: "Skill_5006"
desc_key: "SkillComment_5006"
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
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 90, "ability_pct": 80}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 90}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 105
icon: {"file": "Skill_Einsel_01.png", "index": 6}
used_by:
  - {"weapon_base": 2, "slot": 3, "items": [10001]}
---
<!-- generated:start -->
<!-- generated-keys: title=79944f type=86a754 id=5de340 sources=35b59e name_key=291cd3 desc_key=912188 kind=356a19 kind_name=9bc378 target=aa5d92 range=b1d578 area=2a66b8 cost=da6e22 cooldown=4aa5a5 delivery=93a212 effect_kind=da4b92 effects=cf8ce8 damage_or_effect=8a64f8 tooltip_formula=e14aa6 visual=e114c4 icon=ade420 used_by=1563bb -->
|  |  |
|---|---|
|  | ![Ball of Lighting](../assets/skills/5006.png) |
| **Skill id** | `5006` |
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

> [Active] Shoot a ball of lightning dealing `{EF_STATIC 90}``{EF_R_MDAM 80}`damage to the first target it hits.

Tooltip formula: **90 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 90 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |

**Reading:** amount **90 + 80% Ability Power**; damage (magic?).

### Used by

- Weapon skill **E** of WeaponBase 2: [[wiki/items/10001-magical-thunder-wand|Magical Thunder Wand]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot E for [[wiki/items/10001-magical-thunder-wand|Magical Thunder Wand]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.
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

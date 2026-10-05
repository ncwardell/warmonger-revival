---
title: "Entangling Bullet"
type: "skill"
id: 10104
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10104", "client: StringAll_Eng SkillComment_10104 (tooltip value tags)"]
name_key: "Skill_10104"
desc_key: "SkillComment_10104"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 10.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 130}
cooldown: {"ms": 18000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 102, "value": 105, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30087, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 85, "ability_pct": 105, "buffs": [{"buff": 30087, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_MDAM", "value": 105}
visual: 242
icon: {"file": "Skill_Einsel_01.png", "index": 18}
used_by:
  - {"weapon_base": 112, "slot": 3, "items": [11011]}
---
<!-- generated:start -->
<!-- generated-keys: title=fd1912 type=86a754 id=6163cc sources=1bb561 name_key=4a3d6c desc_key=510464 kind=356a19 kind_name=9bc378 target=aa5d92 range=b1d578 area=728214 cost=58a4ca cooldown=133145 delivery=93a212 effect_kind=da4b92 effects=873f88 damage_or_effect=b79d71 tooltip_formula=bcdca5 visual=851cd0 icon=d9b35f used_by=d92bcf -->
|  |  |
|---|---|
|  | ![Entangling Bullet](wiki/assets/skills/10104.png) |
| **Skill id** | `10104` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | line / rectangle?, radius 10, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 130 MP |
| **Cooldown** | 18 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 242 `PCE_Gun_01_E` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 18 |

### Tooltip

> [Active] Deals `{EF_STATIC 85}``{EF_R_MDAM 105}` Damage and holds the enemy in place for 2 seconds.

Tooltip formula: **85 + 105% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 105 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30087-entangling-shot-rooted-for-2-seconds\|Entangling Shot : Rooted for 2 seconds]] | 100 |

**Reading:** amount **85 + 105% Ability Power**; damage (magic?); applies [[wiki/buffs/30087-entangling-shot-rooted-for-2-seconds|Entangling Shot : Rooted for 2 seconds]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 112: [[wiki/items/11011-magical-adapted-dual-gun|Magical adapted Dual Gun]]
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

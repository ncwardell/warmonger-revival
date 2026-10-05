---
title: "Ball of Lighting"
type: "skill"
id: 5305
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5305", "client: StringAll_Eng SkillComment_5305 (tooltip value tags)"]
name_key: "Skill_5305"
desc_key: "SkillComment_5305"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 11.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 90, "rate": 100}
  - {"slot": 2, "type": 102, "value": 90, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10358, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 90, "ability_pct": 90, "buffs": [{"buff": 10358, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 90}
  - {"tag": "EF_R_MDAM", "value": 90}
visual: 394
icon: {"file": "Skill_Einsel_01.png", "index": 6}
used_by:
  - {"weapon_base": 5, "slot": 3, "items": [10004]}
---
<!-- generated:start -->
<!-- generated-keys: title=79944f type=86a754 id=3d4a44 sources=609193 name_key=37aa93 desc_key=4c2f49 kind=356a19 kind_name=9bc378 target=aa5d92 range=b1d578 area=2a66b8 cost=e4e7cf cooldown=e3989d delivery=93a212 effect_kind=da4b92 effects=26b59e damage_or_effect=491d71 tooltip_formula=ac573a visual=bc6230 icon=ade420 used_by=b2eef2 -->
|  |  |
|---|---|
|  | ![Ball of Lighting](wiki/assets/skills/5305.png) |
| **Skill id** | `5305` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | line / rectangle?, radius 11, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 394 `시즌2_PCE_Staff_01_E_섬광탄` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 6 |

### Tooltip

> [Active] Shoot a ball of lightning, dealing `{EF_STATIC 90}``{EF_R_MDAM 90}` Damage to the first target it hits, stunning it for 2 seconds.

Tooltip formula: **90 + 90% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 90 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 90 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10358-ball-of-lighting-stun-2-secs\|Ball of Lighting : Stun (2 Secs)]] | 100 |

**Reading:** amount **90 + 90% Ability Power**; damage (magic?); applies [[wiki/buffs/10358-ball-of-lighting-stun-2-secs|Ball of Lighting : Stun (2 Secs)]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 5: [[wiki/items/10004-tempest-s-magical-wand|Tempest's magical wand]]
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

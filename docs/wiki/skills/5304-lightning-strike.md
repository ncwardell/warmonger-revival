---
title: "Lightning Strike"
type: "skill"
id: 5304
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5304", "client: StringAll_Eng SkillComment_5304 (tooltip value tags)"]
name_key: "Skill_5304"
desc_key: "SkillComment_5304"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 120}
cooldown: {"ms": 16000, "group": 0}
delivery: {"type": 4, "field_tick": 0.9}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10357, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 85, "ability_pct": 80, "buffs": [{"buff": 10357, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 393
icon: {"file": "Skill_Einsel_01.png", "index": 5}
used_by:
  - {"weapon_base": 5, "slot": 2, "items": [10004]}
---
<!-- generated:start -->
<!-- generated-keys: title=b22690 type=86a754 id=a381cf sources=ff217b name_key=eba05a desc_key=c3ed49 kind=356a19 kind_name=9bc378 target=7056fd range=902ba3 area=6d01a6 cost=deac18 cooldown=a93f07 delivery=4fe5f3 effect_kind=da4b92 effects=942aab damage_or_effect=4d6a41 tooltip_formula=b1a00d visual=b0c689 icon=eb1101 used_by=8362bd -->
|  |  |
|---|---|
|  | ![Lightning Strike](wiki/assets/skills/5304.png) |
| **Skill id** | `5304` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 7 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 120 MP |
| **Cooldown** | 16 s |
| **Delivery** | projectile / SFX (4), tick 0.9 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 393 `시즌2_PCE_Staff_01_W_낙뢰` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 5 |

### Tooltip

> [Active] Thunder strikes the targeted area, dealing `{EF_STATIC 85}``{EF_R_MDAM 80}` Damage.

Tooltip formula: **85 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10357-lightning-strike-silence-2-secs\|Lightning Strike : Silence (2 Secs)]] | 100 |

**Reading:** amount **85 + 80% Ability Power**; damage (magic?); applies [[wiki/buffs/10357-lightning-strike-silence-2-secs|Lightning Strike : Silence (2 Secs)]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 5: [[wiki/items/10004-tempest-s-magical-wand|Tempest's magical wand]]
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

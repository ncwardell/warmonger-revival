---
title: "Light of Judgement"
type: "skill"
id: 5054
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5054", "client: StringAll_Eng SkillComment_5054 (tooltip value tags)"]
name_key: "Skill_5054"
desc_key: "SkillComment_5054"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
delivery: {"type": 4, "field_tick": 1.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 1}
  - {"slot": 2, "type": 102, "value": 110, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10050, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 120, "ability_pct": 110, "buffs": [{"buff": 10050, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_MDAM", "value": 110}
visual: 175
icon: {"file": "Skill_Einsel_01.png", "index": 23}
used_by:
  - {"weapon_base": 16, "slot": 4, "items": [10015]}
---
<!-- generated:start -->
<!-- generated-keys: title=1a20ac type=86a754 id=9382da sources=80a72c name_key=0451be desc_key=bad4d7 kind=356a19 kind_name=9bc378 target=e84f24 range=b1d578 area=6d01a6 cost=ff5a60 cooldown=ad2ac8 delivery=15a656 effect_kind=da4b92 effects=3e6e54 damage_or_effect=b0e8a0 tooltip_formula=42e57b visual=04f124 icon=1431e5 used_by=a81eca -->
|  |  |
|---|---|
|  | ![Light of Judgement](../assets/skills/5054.png) |
| **Skill id** | `5054` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Delivery** | projectile / SFX (4), tick 1 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 175 `PCE_Knife_01_R 시전 (심판의 빛)` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 23 |

### Tooltip

> [Active] Judge the enemies in the targeted area, dealing `{EF_STATIC 120}``{EF_R_MDAM 110}` Damage and stunning them for 2 seconds.

Tooltip formula: **120 + 110% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 1 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 110 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10050-judgement-stunned-for-2-seconds\|Judgement : Stunned for 2 seconds]] | 100 |

**Reading:** amount **120 + 110% Ability Power**; damage (magic?); applies [[wiki/buffs/10050-judgement-stunned-for-2-seconds|Judgement : Stunned for 2 seconds]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 16: [[wiki/items/10015-magical-dash-blade|Magical Dash Blade]]
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

---
title: "Light of Judgement"
type: "skill"
id: 10054
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10054", "client: StringAll_Eng SkillComment_10054 (tooltip value tags)"]
name_key: "Skill_10054"
desc_key: "SkillComment_10054"
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
  - {"slot": 2, "type": 102, "value": 115, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30050, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 120, "ability_pct": 115, "buffs": [{"buff": 30050, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_MDAM", "value": 115}
visual: 175
icon: {"file": "Skill_Einsel_01.png", "index": 23}
used_by:
  - {"weapon_base": 116, "slot": 4, "items": [11015]}
---
<!-- generated:start -->
<!-- generated-keys: title=1a20ac type=86a754 id=3e2ae0 sources=bbb579 name_key=3bc014 desc_key=47eabc kind=356a19 kind_name=9bc378 target=e84f24 range=b1d578 area=6d01a6 cost=ff5a60 cooldown=ad2ac8 delivery=15a656 effect_kind=da4b92 effects=dce85d damage_or_effect=cd5e18 tooltip_formula=b9e136 visual=04f124 icon=1431e5 used_by=250b3b -->
|  |  |
|---|---|
|  | ![Light of Judgement](wiki/assets/skills/10054.png) |
| **Skill id** | `10054` |
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

> [Active] Judge the enemies in the targeted area, dealing `{EF_STATIC 120}``{EF_R_MDAM 115}` Damage and stunning them for 2 seconds.

Tooltip formula: **120 + 115% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 1 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 115 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30050-judgement-stunned-for-2-seconds\|Judgement : Stunned for 2 seconds]] | 100 |

**Reading:** amount **120 + 115% Ability Power**; damage (magic?); applies [[wiki/buffs/30050-judgement-stunned-for-2-seconds|Judgement : Stunned for 2 seconds]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 116: [[wiki/items/11015-magical-dash-blade|Magical Dash Blade]]
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

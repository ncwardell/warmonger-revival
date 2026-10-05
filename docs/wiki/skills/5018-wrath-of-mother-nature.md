---
title: "Wrath of Mother Nature"
type: "skill"
id: 5018
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5018", "client: StringAll_Eng SkillComment_5018 (tooltip value tags)"]
name_key: "Skill_5018"
desc_key: "SkillComment_5018"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 5, "type_name": "MP", "amount": 90}
cooldown: {"ms": 10000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 75, "rate": 100}
  - {"slot": 2, "type": 102, "value": 70, "rate": 0}
  - {"slot": 3, "type": 131, "value": 3, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 75, "ability_pct": 70, "stats": [{"code": 131, "value": 3}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 75}
  - {"tag": "EF_R_MDAM", "value": 70}
visual: 206
icon: {"file": "Skill_Einsel_01.png", "index": 8}
used_by:
  - {"weapon_base": 3, "slot": 1, "items": [30002]}
---
<!-- generated:start -->
<!-- generated-keys: title=ac7a52 type=86a754 id=9d0ad0 sources=5c3e1b name_key=796939 desc_key=8cb5cb kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=d82541 cost=da6e22 cooldown=4aa5a5 effect_kind=da4b92 effects=c4c504 damage_or_effect=a12746 tooltip_formula=e2e031 visual=4afa8f icon=1aeac2 used_by=bcd0e5 -->
|  |  |
|---|---|
|  | ![Wrath of Mother Nature](wiki/assets/skills/5018.png) |
| **Skill id** | `5018` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 90 MP |
| **Cooldown** | 10 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 206 `PCE_Staff_03_Q_대지의 진노` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 8 |

### Tooltip

> [Active] Damages all enemies around you with `{EF_STATIC 75}``{EF_R_MDAM 70}` The damage is increased by 3% of your maximum HP.

Tooltip formula: **75 + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |
| 3 | 131 | stat? Health(%) | 3 | 0 |

**Reading:** amount **75 + 70% Ability Power**; damage (magic?).

### Used by

- Weapon skill **Q** of WeaponBase 3: [[wiki/items/30002-magical-life-wand|Magical Life Wand]]
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

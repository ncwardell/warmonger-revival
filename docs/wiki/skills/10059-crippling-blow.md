---
title: "Crippling Blow"
type: "skill"
id: 10059
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10059", "client: StringAll_Eng SkillComment_10059 (tooltip value tags)"]
name_key: "Skill_10059"
desc_key: "SkillComment_10059"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 60}
cooldown: {"ms": 4000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 101, "value": 75, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30055, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 70, "attack_pct": 75, "buffs": [{"buff": 30055, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_DAM", "value": 75}
visual: 113
icon: {"file": "Skill_Dolorece_01.png", "index": 8}
used_by:
  - {"weapon_base": 144, "slot": 1, "items": [21002]}
---
<!-- generated:start -->
<!-- generated-keys: title=a5422f type=86a754 id=9e6431 sources=c8eac6 name_key=27ac20 desc_key=8d13d1 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=7b288b cooldown=e61764 effect_kind=356a19 effects=f2c594 damage_or_effect=ad4948 tooltip_formula=e37e0c visual=e99321 icon=6547b0 used_by=a34ce8 -->
|  |  |
|---|---|
|  | ![Crippling Blow](wiki/assets/skills/10059.png) |
| **Skill id** | `10059` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 60 MP |
| **Cooldown** | 4 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 113 `PCD_Hammer_03_Q_끈적이는 마그마` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 8 |

### Tooltip

> [Active] You spin your hammer, damaging all enemies with `{EF_STATIC 70}``{EF_R_DAM 75}`. Decreases their Movement Speed by 20% for 2 seconds.

Tooltip formula: **70 + 75% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 75 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30055-crippling-blow-decreased-movement-speed\|Crippling Blow : Decreased Movement Speed]] | 100 |

**Reading:** amount **70 + 75% Attack**; damage (physical?); applies [[wiki/buffs/30055-crippling-blow-decreased-movement-speed|Crippling Blow : Decreased Movement Speed]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 144: [[wiki/items/21002-magical-dash-hammer|Magical Dash Hammer]]
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

---
title: "Aim of water"
type: "skill"
id: 20152
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20152", "client: StringAll_Eng SkillComment_20152 (tooltip value tags)"]
name_key: "Skill_20152"
desc_key: "SkillComment_20152"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 3}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 7.0}
cost: {"type": 5, "type_name": "MP", "amount": 155}
cooldown: {"ms": 23000, "group": 0}
movement: "dash"
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 70, "rate": 0}
  - {"slot": 3, "type": 314, "value": 20152, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 70, "buffs": [{"buff": 20152, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 70}
visual: 421
icon: {"file": "Skill_Boss_01.dds", "index": 23}
used_by:
  - {"weapon_base": 72, "slot": 1, "items": [8003, 8503]}
---
<!-- generated:start -->
<!-- generated-keys: title=11841f type=86a754 id=6fd491 sources=4fb202 name_key=cb28e2 desc_key=0afdc6 kind=356a19 kind_name=9bc378 target=b42027 range=fe5dbb area=c8f1f4 cost=88d6b6 cooldown=7745e9 movement=5f1488 effect_kind=da4b92 effects=4b2c51 damage_or_effect=71a538 tooltip_formula=7fd566 visual=1c76c4 icon=4cd48d used_by=a0178b -->
|  |  |
|---|---|
|  | ![Aim of water](../assets/skills/20152.png) |
| **Skill id** | `20152` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 3 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 3, width/angle 7 |
| **Cost** | 155 MP |
| **Cooldown** | 23 s |
| **Movement** | dash |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 421 `사라스바티_물의 조준` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 23 |

### Tooltip

> [Active]It rushes to the selected enemy, hits enemies nearby, and inflicts damage by `{EF_STATIC 70}``{EF_R_MDAM 70}`.

Tooltip formula: **70 + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/20152-aim-of-water-silenced\|Aim of water : Silenced]] | 100 |

**Reading:** amount **70 + 70% Ability Power**; damage (magic?); applies [[wiki/buffs/20152-aim-of-water-silenced|Aim of water : Silenced]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 72: [[wiki/items/8003-sarasvati|Sarasvati]], [[wiki/items/8503-crystal-sarasvati|Crystal : Sarasvati]]
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

---
title: "Earthquake"
type: "skill"
id: 20308
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20308", "client: StringAll_Eng SkillComment_20308 (tooltip value tags)"]
name_key: "Skill_20308"
desc_key: "SkillComment_20308"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 130}
cooldown: {"ms": 18000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 70, "rate": 0}
  - {"slot": 3, "type": 314, "value": 20307, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 70, "buffs": [{"buff": 20307, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 70}
visual: 449
icon: {"file": "Skill_Boss_01.dds", "index": 44}
used_by:
  - {"weapon_base": 76, "slot": 6, "items": [8007, 8507]}
---
<!-- generated:start -->
<!-- generated-keys: title=b5f38e type=86a754 id=557425 sources=a8b04b name_key=19ff70 desc_key=4bf357 kind=356a19 kind_name=9bc378 target=9dc90e range=1b6453 area=6d01a6 cost=58a4ca cooldown=133145 effect_kind=da4b92 effects=75086a damage_or_effect=a12173 tooltip_formula=7fd566 visual=5fd7e3 icon=bf44a9 used_by=ce1a4a -->
|  |  |
|---|---|
|  | ![Earthquake](../assets/skills/20308.png) |
| **Skill id** | `20308` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 10 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 130 MP |
| **Cooldown** | 18 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 449 `피셔_지진` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 44 |

### Tooltip

> [Active] Deals `{EF_STATIC 70}``{EF_R_MDAM 70}` Magical Damage to nearby enemies, stunning them.

Tooltip formula: **70 + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/20307-earthquake-stun-2-secs\|Earthquake : Stun (2 Secs)]] | 100 |

**Reading:** amount **70 + 70% Ability Power**; damage (magic?); applies [[wiki/buffs/20307-earthquake-stun-2-secs|Earthquake : Stun (2 Secs)]] (100%).

### Used by

- Weapon skill **hero set 2** of WeaponBase 76: [[wiki/items/8007-tempest-fisher|Tempest Fisher]], [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]]
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

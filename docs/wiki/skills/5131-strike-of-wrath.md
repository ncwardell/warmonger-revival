---
title: "Strike of Wrath"
type: "skill"
id: 5131
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5131", "client: StringAll_Eng SkillComment_5131 (tooltip value tags)"]
name_key: "Skill_5131"
desc_key: "SkillComment_5131"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10154, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 80, "buffs": [{"buff": 10154, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 270
icon: {"file": "Skill_Dolorece_01.png", "index": 26}
used_by:
  - {"weapon_base": 46, "slot": 3, "items": [20004]}
---
<!-- generated:start -->
<!-- generated-keys: title=37826a type=86a754 id=5155d2 sources=f4c197 name_key=4685c3 desc_key=e242a0 kind=356a19 kind_name=9bc378 target=d1cc1b range=ac3478 area=6d01a6 cost=911ade cooldown=628d31 effect_kind=356a19 effects=3c1b28 damage_or_effect=c3e9f6 tooltip_formula=4709a0 visual=293508 icon=b4ae95 used_by=0a5e22 -->
|  |  |
|---|---|
|  | ![Strike of Wrath](../assets/skills/5131.png) |
| **Skill id** | `5131` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 270 `PCD_Hammer_05_E_진노의일격` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 26 |

### Tooltip

> [Active] Spin in a circle inflicting `{EF_STATIC 80}``{EF_R_DAM 80}` damage to all enemies hit. Decreases their Damage by 30% and Movement Speed by 70% for 4 seconds.

Tooltip formula: **80 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10154-wrath-strike-reduces-damage-and-movement-speed\|Wrath Strike: Reduces Damage and Movement Speed]] | 100 |

**Reading:** amount **80 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10154-wrath-strike-reduces-damage-and-movement-speed|Wrath Strike: Reduces Damage and Movement Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 46: [[wiki/items/20004-skeleton-king-s-magic-hammer|Skeleton King's Magic Hammer]]
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

---
title: "Whirlwind"
type: "skill"
id: 10002
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10002", "client: StringAll_Eng SkillComment_10002 (tooltip value tags)"]
name_key: "Skill_10002"
desc_key: "SkillComment_10002"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 130}
cooldown: {"ms": 18000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 65, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30003, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 65, "buffs": [{"buff": 30003, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 65}
visual: 101
icon: {"file": "Skill_Dolorece_01.png", "index": 2}
used_by:
  - {"weapon_base": 162, "slot": 3, "items": [21020]}
---
<!-- generated:start -->
<!-- generated-keys: title=88ccea type=86a754 id=6918d3 sources=de17ae name_key=b0d369 desc_key=d3a6ed kind=356a19 kind_name=9bc378 target=d1cc1b range=ac3478 area=6d01a6 cost=58a4ca cooldown=133145 effect_kind=356a19 effects=e77240 damage_or_effect=fbcd88 tooltip_formula=8a26f3 visual=dbc0f0 icon=47a729 used_by=3fe556 -->
|  |  |
|---|---|
|  | ![Whirlwind](wiki/assets/skills/10002.png) |
| **Skill id** | `10002` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 130 MP |
| **Cooldown** | 18 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 101 `PCD_Hammer_01_E_징벌의 일격` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 2 |

### Tooltip

> [Active] Spins in a circle inflicting `{EF_STATIC 80}``{EF_R_DAM 65}` Damage to all enemies that are hit. Decreases their Damage by 30% and Movement Speed by 30% for 4 seconds.

Tooltip formula: **80 + 65% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 65 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30003-whirlwind-reduces-damage-and-movement-speed\|Whirlwind: Reduces Damage and Movement Speed]] | 100 |

**Reading:** amount **80 + 65% Attack**; damage (physical?); applies [[wiki/buffs/30003-whirlwind-reduces-damage-and-movement-speed|Whirlwind: Reduces Damage and Movement Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 162: [[wiki/items/21020-magical-protect-hammer|Magical Protect Hammer]]
- Nation policy 3 `PolicyName_3` (Policy.cdb, server-only; buff_or_skill)
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

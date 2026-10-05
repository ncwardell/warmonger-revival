---
title: "Protection of Justice"
type: "skill"
id: 10352
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10352"]
name_key: "Skill_10352"
desc_key: "SkillComment_10352"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 2}
range: 6
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 308, "value": 30401, "rate": 100}
  - {"slot": 2, "type": 317, "value": 30401, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 30401, "rate": 100}, {"buff": 30401, "rate": 100}]}
visual: 463
icon: {"file": "Skill_Dolorece_01.png", "index": 34}
used_by:
  - {"weapon_base": 157, "slot": 2, "items": [21015]}
---
<!-- generated:start -->
<!-- generated-keys: title=a823c7 type=86a754 id=fb8af9 sources=9ddc2e name_key=bde56a desc_key=8e3e4e kind=356a19 kind_name=9bc378 target=0c4810 range=c1dfd9 cost=911ade cooldown=628d31 effect_kind=b6589f effects=2b31e4 damage_or_effect=e95899 visual=07fd89 icon=e85470 used_by=2d7510 -->
|  |  |
|---|---|
|  | ![Protection of Justice](../assets/skills/10352.png) |
| **Skill id** | `10352` |
| **Kind** | active (1) |
| **Target** | unit; self, ally; units: monster, player; up to 2 |
| **Range** | 6 (world units) |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Visual** | skillVisual 463 `수호의 마력 메이스_정의로운 보호` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 34 |

### Tooltip

> [Active] Create a Shield for you and your allies worth 15% of your total HP.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 308 | applies buff (variant 308) | [[wiki/buffs/30401-justice-protection-creates-a-absorvs-damage-for-4-seconds\|Justice Protection : Creates a absorvs damage for 4 seconds]] | 100 |
| 2 | 317 | applies buff (variant 317) | [[wiki/buffs/30401-justice-protection-creates-a-absorvs-damage-for-4-seconds\|Justice Protection : Creates a absorvs damage for 4 seconds]] | 100 |

**Reading:** applies [[wiki/buffs/30401-justice-protection-creates-a-absorvs-damage-for-4-seconds|Justice Protection : Creates a absorvs damage for 4 seconds]] (100%); applies [[wiki/buffs/30401-justice-protection-creates-a-absorvs-damage-for-4-seconds|Justice Protection : Creates a absorvs damage for 4 seconds]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 157: [[wiki/items/21015-magical-protect-mace|Magical Protect Mace]]
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

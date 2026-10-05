---
title: "Fisher's Protection"
type: "skill"
id: 20307
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20307", "client: StringAll_Eng SkillComment_20307 (tooltip value tags)"]
name_key: "Skill_20307"
desc_key: "SkillComment_20307"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 317, "value": 20306, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20306, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_R_MAXMANA", "value": 5}
visual: 448
icon: {"file": "Skill_Boss_01.dds", "index": 43}
used_by:
  - {"weapon_base": 76, "slot": 5, "items": [8007, 8507]}
---
<!-- generated:start -->
<!-- generated-keys: title=a5c0c0 type=86a754 id=c1f002 sources=ec0a1b name_key=3703d8 desc_key=74d8db kind=356a19 kind_name=9bc378 target=644925 range=fe5dbb cost=911ade cooldown=628d31 effect_kind=b6589f effects=1a023b damage_or_effect=64f1a5 tooltip_formula=173d91 visual=f04b1d icon=50b6e5 used_by=90ba45 -->
|  |  |
|---|---|
|  | ![Fisher's Protection](wiki/assets/skills/20307.png) |
| **Skill id** | `20307` |
| **Kind** | active (1) |
| **Target** | unit; self, ally; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Visual** | skillVisual 448 `피셔_피셔의 보호` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 43 |

### Tooltip

> [Active] Creates a 200 `{EF_R_MAXMANA 5}` shield for you or your allies.

Tooltip formula: **5% max Mana** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 317 | applies buff (variant 317) | [[wiki/buffs/20306-fisher-s-protection-creates-a-absorvs-damage-for-5-seconds\|Fisher's Protection : Creates a absorvs damage for 5 seconds]] | 100 |

**Reading:** applies [[wiki/buffs/20306-fisher-s-protection-creates-a-absorvs-damage-for-5-seconds|Fisher's Protection : Creates a absorvs damage for 5 seconds]] (100%).

### Used by

- Weapon skill **hero set 1** of WeaponBase 76: [[wiki/items/8007-tempest-fisher|Tempest Fisher]], [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]]
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

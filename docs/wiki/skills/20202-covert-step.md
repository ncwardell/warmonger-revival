---
title: "Covert Step"
type: "skill"
id: 20202
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20202", "client: StringAll_Eng SkillComment_20202 (tooltip value tags)"]
name_key: "Skill_20202"
desc_key: "SkillComment_20202"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 20202, "rate": 100}
  - {"slot": 2, "type": 301, "value": 20203, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 20202, "rate": 100}, {"buff": 20203, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 100}
visual: 438
icon: {"file": "Skill_Boss_01.dds", "index": 31}
used_by:
  - {"weapon_base": 73, "slot": 1, "items": [8004, 8504]}
---
<!-- generated:start -->
<!-- generated-keys: title=4164ff type=86a754 id=a45180 sources=ca346e name_key=74bb43 desc_key=01563b kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=e4e7cf cooldown=e3989d effect_kind=356a19 effects=2a8090 damage_or_effect=2ddc01 tooltip_formula=28fad8 visual=06cb3f icon=10f839 used_by=18feeb -->
|  |  |
|---|---|
|  | ![Covert Step](wiki/assets/skills/20202.png) |
| **Skill id** | `20202` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 438 `아르타모스_은밀한 발걸음` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 31 |

### Tooltip

> [Active] Movement Speed increases and you are hidden. It inflicts `{EF_STATIC 80}``{EF_R_DAM 100}` Physical Damage during a basic attack. Increases the target's Physical Damage by 5%.

Tooltip formula: **80 + 100% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/20202-covert-steps-increase-movement-speed\|Covert Steps: Increase movement speed]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/20203-covert-steps-your-basic-attacks-deal-additional-damage\|Covert Steps: Your basic Attacks deal additional damage]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/20202-covert-steps-increase-movement-speed|Covert Steps: Increase movement speed]] (100%); applies [[wiki/buffs/20203-covert-steps-your-basic-attacks-deal-additional-damage|Covert Steps: Your basic Attacks deal additional damage]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 73: [[wiki/items/8004-artamos|Artamos]], [[wiki/items/8504-crystal-artamos|Crystal : Artamos]]
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

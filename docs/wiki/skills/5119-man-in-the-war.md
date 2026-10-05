---
title: "Man in the war"
type: "skill"
id: 5119
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5119", "client: StringAll_Eng SkillComment_5119 (tooltip value tags)"]
name_key: "Skill_5119"
desc_key: "SkillComment_5119"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 308, "value": 10118, "rate": 100}
  - {"slot": 2, "type": 314, "value": 10119, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10118, "rate": 100}, {"buff": 10119, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_R_DAM", "value": 10}
visual: 252
icon: {"file": "Skill_Dolorece_01.png", "index": 23}
used_by:
  - {"weapon_base": 53, "slot": 4, "items": [20011]}
---
<!-- generated:start -->
<!-- generated-keys: title=045ceb type=86a754 id=df66df sources=65a4ab name_key=ee99be desc_key=884fef kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=9e049c cooldown=7d0c8c effect_kind=b6589f effects=b5742b damage_or_effect=113038 tooltip_formula=c66bd8 visual=98fcc3 icon=60dd2b used_by=47c2a3 -->
|  |  |
|---|---|
|  | ![Man in the war](../assets/skills/5119.png) |
| **Skill id** | `5119` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Visual** | skillVisual 252 `PCD_Cannon_02_R 전장돌진` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 23 |

### Tooltip

> [Active] Channel the power within your weapon increasing your Attack and Movement Speed. You gain a Shield that absorbs some Damage. 300`{EF_R_DAM 10}`

Tooltip formula: **10% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 308 | applies buff (variant 308) | [[wiki/buffs/10118-rapid-fire-creates-a-shield-that-absorbs-damage-for-10-secon\|Rapid Fire: Creates a shield that absorbs Damage for 10 seconds]] | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/10119-rapid-fire-increases-movement-speed\|Rapid Fire: Increases Movement Speed]] | 100 |

**Reading:** applies [[wiki/buffs/10118-rapid-fire-creates-a-shield-that-absorbs-damage-for-10-secon|Rapid Fire: Creates a shield that absorbs Damage for 10 seconds]] (100%); applies [[wiki/buffs/10119-rapid-fire-increases-movement-speed|Rapid Fire: Increases Movement Speed]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 53: [[wiki/items/20011-magical-blast-cannon|Magical Blast Cannon]]
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

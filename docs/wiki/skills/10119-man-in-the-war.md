---
title: "Man in the war"
type: "skill"
id: 10119
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10119", "client: StringAll_Eng SkillComment_10119 (tooltip value tags)"]
name_key: "Skill_10119"
desc_key: "SkillComment_10119"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 308, "value": 30118, "rate": 100}
  - {"slot": 2, "type": 314, "value": 30119, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 30118, "rate": 100}, {"buff": 30119, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_R_DAM", "value": 10}
visual: 252
icon: {"file": "Skill_Dolorece_01.png", "index": 23}
used_by:
  - {"weapon_base": 153, "slot": 4, "items": [21011]}
---
<!-- generated:start -->
<!-- generated-keys: title=045ceb type=86a754 id=bc2af3 sources=77353f name_key=bcc064 desc_key=5be504 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=9e049c cooldown=7d0c8c effect_kind=b6589f effects=4fbaa2 damage_or_effect=1de01d tooltip_formula=c66bd8 visual=98fcc3 icon=60dd2b used_by=ef759a -->
|  |  |
|---|---|
|  | ![Man in the war](wiki/assets/skills/10119.png) |
| **Skill id** | `10119` |
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
| 1 | 308 | applies buff (variant 308) | [[wiki/buffs/30118-rapid-fire-creates-a-shield-that-absorbs-damage-for-10-secon\|Rapid Fire: Creates a shield that absorbs Damage for 10 seconds]] | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/30119-rapid-fire-increases-movement-speed\|Rapid Fire: Increases Movement Speed]] | 100 |

**Reading:** applies [[wiki/buffs/30118-rapid-fire-creates-a-shield-that-absorbs-damage-for-10-secon|Rapid Fire: Creates a shield that absorbs Damage for 10 seconds]] (100%); applies [[wiki/buffs/30119-rapid-fire-increases-movement-speed|Rapid Fire: Increases Movement Speed]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 153: [[wiki/items/21011-magical-blast-cannon|Magical Blast Cannon]]
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

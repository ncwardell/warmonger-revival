---
title: "Battle Cry"
type: "skill"
id: 5001
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5001"]
name_key: "Skill_5001"
desc_key: "SkillComment_5001"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 0.0}
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 314, "value": 10002, "rate": 100}
damage_or_effect: {"kind": "heal HP", "buffs": [{"buff": 10002, "rate": 100}]}
visual: 100
icon: {"file": "Skill_Dolorece_01.png", "index": 1}
used_by:
  - {"weapon_base": 62, "slot": 2, "items": [20020]}
---
<!-- generated:start -->
<!-- generated-keys: title=e7637a type=86a754 id=7b61de sources=2e1919 name_key=5ea498 desc_key=78057c kind=356a19 kind_name=9bc378 target=55b685 range=ac3478 area=e9876d cost=e4e7cf cooldown=e3989d effect_kind=632667 effects=a54d76 damage_or_effect=ca4fb0 visual=310b86 icon=2a2087 used_by=1f64a2 -->
|  |  |
|---|---|
|  | ![Battle Cry](wiki/assets/skills/5001.png) |
| **Skill id** | `5001` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 6, width/angle 0 |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 100 `PCD_Hammer_01_W_전장의 함성` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 1 |

### Tooltip

> [Active] Unleashes a battle cry, increasing Health Regeneration of nearby party by 20%.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10002-battle-cry-increases-hp-regeneration\|Battle Cry: Increases HP Regeneration]] | 100 |

**Reading:** heal HP; applies [[wiki/buffs/10002-battle-cry-increases-hp-regeneration|Battle Cry: Increases HP Regeneration]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 62: [[wiki/items/20020-magical-protect-hammer|Magical Protect Hammer]]
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

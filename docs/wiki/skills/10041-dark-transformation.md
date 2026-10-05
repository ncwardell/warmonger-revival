---
title: "Dark Transformation"
type: "skill"
id: 10041
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10041"]
name_key: "Skill_10041"
desc_key: "SkillComment_10041"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 301, "value": 30037, "rate": 100}
  - {"slot": 2, "type": 301, "value": 30038, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 30037, "rate": 100}, {"buff": 30038, "rate": 100}]}
visual: 213
icon: {"file": "Skill_Dolorece_01.png", "index": 7}
used_by:
  - {"weapon_base": 143, "slot": 4, "items": [21001]}
---
<!-- generated:start -->
<!-- generated-keys: title=128bcd type=86a754 id=6486ab sources=26cae5 name_key=57b547 desc_key=7b1391 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=9e049c cooldown=7d0c8c effect_kind=da4b92 effects=874f49 damage_or_effect=e43da0 visual=19187d icon=3af2a9 used_by=570477 -->
|  |  |
|---|---|
|  | ![Dark Transformation](wiki/assets/skills/10041.png) |
| **Skill id** | `10041` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 213 `PCD_Hammer_02_R_독각 대왕` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 7 |

### Tooltip

> [Active] During the state of transformation you gain increased HP Regeneration and Movement Speed for 10 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/30037-dark-transformation-gain-40-health-regeneration\|Dark Transformation : Gain 40% Health Regeneration]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/30038-dark-transformation-gain-100-movement-speed\|Dark Transformation : Gain 100 Movement Speed]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/30037-dark-transformation-gain-40-health-regeneration|Dark Transformation : Gain 40% Health Regeneration]] (100%); applies [[wiki/buffs/30038-dark-transformation-gain-100-movement-speed|Dark Transformation : Gain 100 Movement Speed]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 143: [[wiki/items/21001-magical-demolition-hammer|Magical Demolition Hammer]]

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 47): Dark Transformation · 60 s · 340 · More HP regeneration and movement speed for 10 s
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps (line 27, at 1:38, 3:20, 3:15): 1. Character creation 1:38–3:20. The nation is chosen first (Arslan). Then the class: Guardian, Saint, Punisher, each with a weapon picked from the class's l...
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

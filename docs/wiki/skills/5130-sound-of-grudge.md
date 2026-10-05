---
title: "Sound of Grudge"
type: "skill"
id: 5130
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5130"]
name_key: "Skill_5130"
desc_key: "SkillComment_5130"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 0
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 301, "value": 10153, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10153, "rate": 100}]}
visual: 269
icon: {"file": "Skill_Dolorece_01.png", "index": 25}
used_by:
  - {"weapon_base": 46, "slot": 2, "items": [20004]}
---
<!-- generated:start -->
<!-- generated-keys: title=bf04a1 type=86a754 id=38a676 sources=f13fee name_key=b02cb3 desc_key=9dc1e3 kind=356a19 kind_name=9bc378 target=d99f6c range=b6589f cost=911ade cooldown=628d31 effect_kind=b6589f effects=47c64c damage_or_effect=a75644 visual=9a61b8 icon=f0762b used_by=5034ba -->
|  |  |
|---|---|
|  | ![Sound of Grudge](wiki/assets/skills/5130.png) |
| **Skill id** | `5130` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 0 (world units) |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Visual** | skillVisual 269 `PCD_Hammer_05_W_원한의소리` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 25 |

### Tooltip

> [Active] Unleashes a Sound of Grudge, increasing HP Regeneration, Armor Penetration and Movement Speed for 5 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10153-sound-of-grudge-gain-30-armor-penetration-movement-speed-and\|Sound of Grudge : Gain 30 Armor Penetration, Movement Speed and 4 Health Regeneration.]] | 100 |

**Reading:** applies [[wiki/buffs/10153-sound-of-grudge-gain-30-armor-penetration-movement-speed-and|Sound of Grudge : Gain 30 Armor Penetration, Movement Speed and 4 Health Regeneration.]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 46: [[wiki/items/20004-skeleton-king-s-magic-hammer|Skeleton King's Magic Hammer]]
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

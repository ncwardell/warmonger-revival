---
title: "Bloody anger"
type: "skill"
id: 20254
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20254"]
name_key: "Skill_20254"
desc_key: "SkillComment_20254"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 4, "type_name": "HP %", "amount": 3}
cooldown: {"ms": 5000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 301, "value": 20260, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20260, "rate": 100}]}
visual: 460
icon: {"file": "Skill_Boss_01.dds", "index": 49}
used_by:
  - {"weapon_base": 75, "slot": 3, "items": [8006, 8506]}
---
<!-- generated:start -->
<!-- generated-keys: title=50dc1b type=86a754 id=38891c sources=bb7179 name_key=007c60 desc_key=384d09 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=e65f66 cooldown=752bf3 effect_kind=b6589f effects=15be46 damage_or_effect=0c0a29 visual=e973a6 icon=5c9a70 used_by=27e6ea -->
|  |  |
|---|---|
|  | ![Bloody anger](wiki/assets/skills/20254.png) |
| **Skill id** | `20254` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 3 HP % |
| **Cooldown** | 5 s |
| **Visual** | skillVisual 460 `데스헤드_피의 분노` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 49 |

### Tooltip

> [Active] Increases Damage. Stacks up to 7 times.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/20260-bloody-anger-increases-damage\|Bloody anger : Increases Damage]] | 100 |

**Reading:** applies [[wiki/buffs/20260-bloody-anger-increases-damage|Bloody anger : Increases Damage]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 75: [[wiki/items/8006-king-deathhead|King Deathhead]], [[wiki/items/8506-crystal-king-deathhead|Crystal : King Deathhead]]
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

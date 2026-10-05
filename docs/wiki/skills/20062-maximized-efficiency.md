---
title: "Maximized Efficiency"
type: "skill"
id: 20062
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20062"]
name_key: "Skill_5198"
desc_key: "SkillComment_5198"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 4, "type_name": "HP %", "amount": 2}
cooldown: {"ms": 5000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 301, "value": 20062, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20062, "rate": 100}]}
visual: 325
icon: {"file": "Skill_Boss_01.dds", "index": 1}
used_by:
  - {"weapon_base": 70, "slot": 2, "items": [8001, 8501]}
---
<!-- generated:start -->
<!-- generated-keys: title=932c50 type=86a754 id=a9be2b sources=6f5a90 name_key=c68cd0 desc_key=6ff9f5 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=89f997 cooldown=752bf3 effect_kind=b6589f effects=88fd92 damage_or_effect=92a43e visual=4551b2 icon=875e75 used_by=bdf526 -->
|  |  |
|---|---|
|  | ![Maximized Efficiency](wiki/assets/skills/20062.png) |
| **Skill id** | `20062` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 2 HP % |
| **Cooldown** | 5 s |
| **Visual** | skillVisual 325 `수호신장_변신스킬_02_마력극대화` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 1 |

### Tooltip

> [Active] Increases your Damage dealt. Stacks up to 5 times.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/20062-maximized-efficiency-increased-damage\|Maximized Efficiency: Increased Damage.]] | 100 |

**Reading:** applies [[wiki/buffs/20062-maximized-efficiency-increased-damage|Maximized Efficiency: Increased Damage.]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 70: [[wiki/items/8001-guardian|Guardian]], [[wiki/items/8501-crystal-guardian|Crystal : Guardian]]
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

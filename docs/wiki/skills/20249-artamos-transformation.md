---
title: "Artamos Transformation"
type: "skill"
id: 20249
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20249"]
name_key: "Skill_20249"
desc_key: "SkillComment_20249"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 20, "type_name": "cost type 20 (unknown)", "amount": 0}
cooldown: {"ms": 120000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20201, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20201, "rate": 100}]}
visual: 442
icon: {"file": "Items_20.png", "index": 44}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=7fa476 type=86a754 id=244de1 sources=e8e3bf name_key=2e365d desc_key=8abe20 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=68d2b6 cooldown=a7242f effect_kind=da4b92 effects=e29d16 damage_or_effect=d601a3 visual=e076fa icon=0288a0 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Artamos Transformation](wiki/assets/skills/20249.png) |
| **Skill id** | `20249` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 cost type 20 (unknown) |
| **Cooldown** | 120 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 442 `아르타모스_변신` |
| **Icon** | `ui/icons/Items_20.png` cell 44 |

### Tooltip

> [Active]Artamos Transformation. 
> Consumes durability when transforming.
> When all durability is exhausted, the item is destroyed.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/20201-transformation-120-seconds\|Transformation : 120 Seconds]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20201-transformation-120-seconds|Transformation : 120 Seconds]] (100%).
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

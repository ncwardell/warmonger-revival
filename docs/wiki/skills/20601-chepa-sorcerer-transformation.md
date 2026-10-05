---
title: "Chepa Sorcerer Transformation"
type: "skill"
id: 20601
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20601"]
name_key: "Skill_20601"
desc_key: "SkillComment_20601"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 6, "type_name": "EXP", "amount": 0}
cooldown: {"ms": 10000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20601, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20601, "rate": 100}]}
visual: 442
icon: {"file": "Items_20.png", "index": 31}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=74155c type=86a754 id=175991 sources=d51697 name_key=f4c26b desc_key=853207 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=b1d441 cooldown=4aa5a5 effect_kind=da4b92 effects=f1a6a3 damage_or_effect=5c9829 visual=e076fa icon=e5f8ba used_by=97d170 -->
|  |  |
|---|---|
|  | ![Chepa Sorcerer Transformation](wiki/assets/skills/20601.png) |
| **Skill id** | `20601` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 EXP |
| **Cooldown** | 10 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 442 `아르타모스_변신` |
| **Icon** | `ui/icons/Items_20.png` cell 31 |

### Tooltip

> [Active] Chepa Sorcerer Transformation transformed.
> It consumes experience when transforming

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/20601\|Buff 20601]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20601|Buff 20601]] (100%).
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

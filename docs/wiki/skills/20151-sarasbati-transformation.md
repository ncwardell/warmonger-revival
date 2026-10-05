---
title: "Sarasbati Transformation"
type: "skill"
id: 20151
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20151"]
name_key: "Skill_20151"
desc_key: "SkillComment_20151"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 6, "type_name": "EXP", "amount": 0}
cooldown: {"ms": 120000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20151, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20151, "rate": 100}]}
visual: 441
icon: {"file": "Items_20.png", "index": 30}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=8dabc7 type=86a754 id=571985 sources=2e7f89 name_key=fc5117 desc_key=8dfa59 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=b1d441 cooldown=a7242f effect_kind=da4b92 effects=cd39a4 damage_or_effect=2d6f47 visual=5dd8b5 icon=e9f376 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Sarasbati Transformation](wiki/assets/skills/20151.png) |
| **Skill id** | `20151` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 EXP |
| **Cooldown** | 120 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 441 `사라스바티_변신` |
| **Icon** | `ui/icons/Items_20.png` cell 30 |

### Tooltip

> [Active] Sarasbati Transformation. 
> Consumes EXP when transforming.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/20151-transformation-120-seconds\|Transformation : 120 Seconds]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20151-transformation-120-seconds|Transformation : 120 Seconds]] (100%).
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

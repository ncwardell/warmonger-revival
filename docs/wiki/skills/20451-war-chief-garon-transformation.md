---
title: "War chief Garon Transformation"
type: "skill"
id: 20451
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20451"]
name_key: "Skill_20451"
desc_key: "SkillComment_20451"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 6, "type_name": "EXP", "amount": 0}
cooldown: {"ms": 10000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20451, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20451, "rate": 100}]}
visual: 442
icon: {"file": "Items_20.png", "index": 23}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=c7fe77 type=86a754 id=f561c2 sources=a62a4e name_key=c1c17c desc_key=e3a7e8 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=b1d441 cooldown=4aa5a5 effect_kind=da4b92 effects=8fb1e3 damage_or_effect=cb0813 visual=e076fa icon=140b66 used_by=97d170 -->
|  |  |
|---|---|
|  | ![War chief Garon Transformation](wiki/assets/skills/20451.png) |
| **Skill id** | `20451` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 EXP |
| **Cooldown** | 10 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 442 `아르타모스_변신` |
| **Icon** | `ui/icons/Items_20.png` cell 23 |

### Tooltip

> [Active] War chief Garon Transformation transformed.
> It consumes experience when transforming

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/20451\|Buff 20451]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20451|Buff 20451]] (100%).
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

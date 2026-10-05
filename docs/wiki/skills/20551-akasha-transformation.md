---
title: "Akasha Transformation"
type: "skill"
id: 20551
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20551"]
name_key: "Skill_20551"
desc_key: "SkillComment_20551"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 6, "type_name": "EXP", "amount": 0}
cooldown: {"ms": 10000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20551, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20551, "rate": 100}]}
visual: 442
icon: {"file": "Items_20.png", "index": 31}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=57da51 type=86a754 id=ff974f sources=1fb7fa name_key=7ab7cd desc_key=d4d9d4 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=b1d441 cooldown=4aa5a5 effect_kind=da4b92 effects=dd3945 damage_or_effect=9de065 visual=e076fa icon=e5f8ba used_by=97d170 -->
|  |  |
|---|---|
|  | ![Akasha Transformation](../assets/skills/20551.png) |
| **Skill id** | `20551` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 EXP |
| **Cooldown** | 10 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 442 `아르타모스_변신` |
| **Icon** | `ui/icons/Items_20.png` cell 31 |

### Tooltip

> [Active] Akasha Transformation transformed.
> It consumes experience when transforming

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/20551\|Buff 20551]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20551|Buff 20551]] (100%).
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

---
title: "Non-Aggression"
type: "skill"
id: 508
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 508"]
name_key: "Skill_508"
desc_key: "SkillComment_508"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["player"], "max_targets": 1}
range: 1
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 309, "value": 8, "rate": 100}
  - {"slot": 2, "type": 301, "value": 10132, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10132, "rate": 100}]}
icon: {"file": "Skill_MagicScholar_17.png", "index": 0}
used_by:
  - {"item_use": 2902}
---
<!-- generated:start -->
<!-- generated-keys: title=06fd89 type=86a754 id=07a85b sources=bc7c7e name_key=9abefd desc_key=eaf819 kind=356a19 kind_name=9bc378 target=1feeb6 range=356a19 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=6e3a07 damage_or_effect=04191f icon=826275 used_by=5f6ef1 -->
|  |  |
|---|---|
| **Skill id** | `508` |
| **Kind** | active (1) |
| **Target** | self; self; units: player; up to 1 |
| **Range** | 1 (world units) |
| **Icon** | `ui/icons/Skill_MagicScholar_17.png` cell 0 |

### Tooltip

> Non-Aggression

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 309 | unknown | 8 | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/10132-non-aggression\|Non-Aggression]] | 100 |

**Reading:** applies [[wiki/buffs/10132-non-aggression|Non-Aggression]] (100%).

### Used by

- Cast when [[wiki/items/2902-invalidity|Invalidity]] is used (Item_Base option 210)
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

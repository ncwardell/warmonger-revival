---
title: "Fisher's essence"
type: "skill"
id: 20312
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20312"]
name_key: "Skill_20312"
desc_key: "SkillComment_20312"
kind: 2
kind_name: "passive"
target: {"type": 0, "type_name": "none", "relation": [], "unit_classes": [], "max_targets": 0}
range: 0
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20311, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20311, "rate": 100}]}
icon: {"file": "Items_20.png", "index": 20}
used_by:
  - {"hero": 8, "slot": 2}
  - {"hero": 58, "slot": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=54132f type=86a754 id=4bfa54 sources=cc4ac5 name_key=76d249 desc_key=208718 kind=da4b92 kind_name=3844d5 target=2771a9 range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=922d16 damage_or_effect=6f1f82 icon=ebd420 used_by=b9e2f3 -->
|  |  |
|---|---|
|  | ![Fisher's essence](wiki/assets/skills/20312.png) |
| **Skill id** | `20312` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 0 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Items_20.png` cell 20 |

### Tooltip

> [Passive]Fisher's essence : Increases the magical penetration by 5.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20311-fisher-s-essence-increases-magic-penetration\|Fisher's essence : Increases Magic Penetration]] | 100 |

**Reading:** applies [[wiki/buffs/20311-fisher-s-essence-increases-magic-penetration|Fisher's essence : Increases Magic Penetration]] (100%).

### Used by

- Hero [[wiki/heroes/8-tempest-fisher|Tempest Fisher]], skill 2
- Hero [[wiki/heroes/58-tempest-fisher-crystal|Tempest Fisher (Crystal)]], skill 2
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

---
title: "Power of the ax"
type: "skill"
id: 20266
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20266"]
name_key: "Skill_20266"
desc_key: "SkillComment_20266"
kind: 2
kind_name: "passive"
target: {"type": 0, "type_name": "none", "relation": [], "unit_classes": [], "max_targets": 0}
range: 0
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20264, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20264, "rate": 100}]}
icon: {"file": "Items_20.png", "index": 18}
used_by:
  - {"hero": 7, "slot": 5}
  - {"hero": 57, "slot": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=fc558d type=86a754 id=aca189 sources=5fd21e name_key=656370 desc_key=76d309 kind=da4b92 kind_name=3844d5 target=2771a9 range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=5010d4 damage_or_effect=64cf7e icon=ff62ba used_by=3d8ad0 -->
|  |  |
|---|---|
|  | ![Power of the ax](wiki/assets/skills/20266.png) |
| **Skill id** | `20266` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 0 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Items_20.png` cell 18 |

### Tooltip

> [Passive]Power of the ax : Increases Critical Strike(%) by 5.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20264-power-of-the-ax-increase-critical-strike\|Power of the ax : Increase Critical Strike(%)]] | 100 |

**Reading:** applies [[wiki/buffs/20264-power-of-the-ax-increase-critical-strike|Power of the ax : Increase Critical Strike(%)]] (100%).

### Used by

- Hero [[wiki/heroes/7-king-deathhead|King Deathhead]], skill 5
- Hero [[wiki/heroes/57-king-deathhead-crystal|King Deathhead (Crystal)]], skill 5
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

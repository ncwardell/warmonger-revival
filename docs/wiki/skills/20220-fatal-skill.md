---
title: "Fatal skill"
type: "skill"
id: 20220
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20220"]
name_key: "Skill_20220"
desc_key: "SkillComment_20220"
kind: 2
kind_name: "passive"
target: {"type": 0, "type_name": "none", "relation": [], "unit_classes": [], "max_targets": 0}
range: 0
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20224, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20224, "rate": 100}]}
icon: {"file": "Items_20.png", "index": 31}
used_by:
  - {"hero": 5, "slot": 5}
  - {"hero": 55, "slot": 5}
---
<!-- generated:start -->
<!-- generated-keys: title=d7f35c type=86a754 id=0351c7 sources=595c7e name_key=1cac1f desc_key=5d0d71 kind=da4b92 kind_name=3844d5 target=2771a9 range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=838f95 damage_or_effect=d18df4 icon=e5f8ba used_by=fc671e -->
|  |  |
|---|---|
|  | ![Fatal skill](../assets/skills/20220.png) |
| **Skill id** | `20220` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 0 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Items_20.png` cell 31 |

### Tooltip

> [Passive]Fatal skill : Increased Critical Strike(%) by 7

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20224-fatal-skill-increased-critical-strike\|Fatal skill: Increased Critical Strike(%)]] | 100 |

**Reading:** applies [[wiki/buffs/20224-fatal-skill-increased-critical-strike|Fatal skill: Increased Critical Strike(%)]] (100%).

### Used by

- Hero Artamos, skill 5
- Hero Artamos, skill 5
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

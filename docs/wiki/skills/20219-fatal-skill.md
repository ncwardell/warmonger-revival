---
title: "Fatal skill"
type: "skill"
id: 20219
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20219"]
name_key: "Skill_20219"
desc_key: "SkillComment_20219"
kind: 2
kind_name: "passive"
target: {"type": 0, "type_name": "none", "relation": [], "unit_classes": [], "max_targets": 0}
range: 0
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20223, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20223, "rate": 100}]}
icon: {"file": "Items_20.png", "index": 31}
used_by:
  - {"hero": 5, "slot": 4}
  - {"hero": 55, "slot": 4}
---
<!-- generated:start -->
<!-- generated-keys: title=d7f35c type=86a754 id=109c1a sources=21d5c6 name_key=9d7faa desc_key=427cf1 kind=da4b92 kind_name=3844d5 target=2771a9 range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=952cda damage_or_effect=ffa207 icon=e5f8ba used_by=9c2eaf -->
|  |  |
|---|---|
|  | ![Fatal skill](../assets/skills/20219.png) |
| **Skill id** | `20219` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 0 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Items_20.png` cell 31 |

### Tooltip

> [Passive]Fatal skill : Increased Critical Strike(%) by 6

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20223-fatal-skill-increased-critical-strike\|Fatal skill: Increased Critical Strike(%)]] | 100 |

**Reading:** applies [[wiki/buffs/20223-fatal-skill-increased-critical-strike|Fatal skill: Increased Critical Strike(%)]] (100%).

### Used by

- Hero Artamos, skill 4
- Hero Artamos, skill 4
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

---
title: "Guardian Avenger"
type: "skill"
id: 20013
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20013"]
name_key: "Skill_20013"
desc_key: "SkillComment_20013"
kind: 2
kind_name: "passive"
target: {"type": 0, "type_name": "none", "relation": [], "unit_classes": [], "max_targets": 1}
range: 0
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20012, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20012, "rate": 100}]}
icon: {"file": "Items_20.png", "index": 19}
used_by:
  - {"hero": 1, "slot": 2}
  - {"hero": 51, "slot": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=a05746 type=86a754 id=ab7680 sources=653338 name_key=0c0706 desc_key=be8e36 kind=da4b92 kind_name=3844d5 target=6d698f range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=56243a damage_or_effect=77b743 icon=a71171 used_by=0def54 -->
|  |  |
|---|---|
|  | ![Guardian Avenger](../assets/skills/20013.png) |
| **Skill id** | `20013` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 1 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Items_20.png` cell 19 |

### Tooltip

> [Passive] Increases your damage by 8% of your current Armor.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20012-group-of-guardians-increased-damage\|Group of Guardians : Increased damage]] | 100 |

**Reading:** applies [[wiki/buffs/20012-group-of-guardians-increased-damage|Group of Guardians : Increased damage]] (100%).

### Used by

- Hero Dark Knight Skull, skill 2
- Hero Dark Knight Skull, skill 2
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

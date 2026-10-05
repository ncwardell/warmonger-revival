---
title: "Guardian Avenger"
type: "skill"
id: 20011
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20011"]
name_key: "Skill_5188"
desc_key: "SkillComment_5188"
kind: 2
kind_name: "passive"
target: {"type": 0, "type_name": "none", "relation": [], "unit_classes": [], "max_targets": 1}
range: 0
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20010, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20010, "rate": 100}]}
icon: {"file": "Items_20.png", "index": 19}
used_by:
  - {"hero": 1, "slot": 1}
  - {"hero": 51, "slot": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=a05746 type=86a754 id=95e708 sources=93101b name_key=f92498 desc_key=012b6a kind=da4b92 kind_name=3844d5 target=6d698f range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=076785 damage_or_effect=d0c079 icon=a71171 used_by=510e44 -->
|  |  |
|---|---|
|  | ![Guardian Avenger](../assets/skills/20011.png) |
| **Skill id** | `20011` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 1 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Items_20.png` cell 19 |

### Tooltip

> [Passive] Increases your Damage by 5% of your current Armor.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20010-group-of-guardians-increased-damage\|Group of Guardians : Increased damage]] | 100 |

**Reading:** applies [[wiki/buffs/20010-group-of-guardians-increased-damage|Group of Guardians : Increased damage]] (100%).

### Used by

- Hero Dark Knight Skull, skill 1
- Hero Dark Knight Skull, skill 1
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

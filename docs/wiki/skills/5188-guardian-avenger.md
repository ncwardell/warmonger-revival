---
title: "Guardian Avenger"
type: "skill"
id: 5188
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5188"]
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
  - {"slot": 1, "type": 303, "value": 10222, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10222, "rate": 100}]}
icon: {"file": "Policy.png", "index": 37}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=a05746 type=86a754 id=29f0a1 sources=fe3486 name_key=f92498 desc_key=012b6a kind=da4b92 kind_name=3844d5 target=6d698f range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=da990a damage_or_effect=4147c7 icon=30f6b2 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Guardian Avenger](wiki/assets/skills/5188.png) |
| **Skill id** | `5188` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 1 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Policy.png` cell 37 |

### Tooltip

> [Passive] Increases your Damage by 5% of your current Armor.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/10222-group-of-guardians-increased-damage\|Group of Guardians : Increased damage]] | 100 |

**Reading:** applies [[wiki/buffs/10222-group-of-guardians-increased-damage|Group of Guardians : Increased damage]] (100%).
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

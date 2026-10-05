---
title: "Aura of Death"
type: "skill"
id: 5189
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5189"]
name_key: "Skill_5189"
desc_key: "SkillComment_5189"
kind: 2
kind_name: "passive"
target: {"type": 0, "type_name": "none", "relation": [], "unit_classes": [], "max_targets": 1}
range: 0
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 10223, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10223, "rate": 100}]}
icon: {"file": "Policy.png", "index": 41}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=d266c7 type=86a754 id=b26817 sources=de0e3e name_key=ba91d8 desc_key=1a11c7 kind=da4b92 kind_name=3844d5 target=6d698f range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=4c63b2 damage_or_effect=6d754e icon=4e653c used_by=97d170 -->
|  |  |
|---|---|
|  | ![Aura of Death](../assets/skills/5189.png) |
| **Skill id** | `5189` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 1 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Policy.png` cell 41 |

### Tooltip

> [Passive] Restores 3% of your Health for every kill or assist.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/10223-aura-of-death-kills-and-assists-heal-you\|Aura of Death : Kills and assists heal you]] | 100 |

**Reading:** applies [[wiki/buffs/10223-aura-of-death-kills-and-assists-heal-you|Aura of Death : Kills and assists heal you]] (100%).
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

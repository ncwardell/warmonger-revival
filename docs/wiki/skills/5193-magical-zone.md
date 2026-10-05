---
title: "Magical Zone"
type: "skill"
id: 5193
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 5193"]
name_key: "Skill_5193"
desc_key: "SkillComment_5193"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: null
cooldown: {"ms": 16000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10232, "rate": 100}
  - {"slot": 2, "type": 314, "value": 10233, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10232, "rate": 100}, {"buff": 10233, "rate": 100}]}
visual: 330
icon: {"file": "Skill_Boss_01.dds", "index": 4}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=324252 type=86a754 id=eccf8e sources=f1d877 name_key=10e6d7 desc_key=566683 kind=356a19 kind_name=9bc378 target=71d399 range=fe5dbb area=950fc9 cost=2be88c cooldown=a93f07 effect_kind=b6589f effects=353173 damage_or_effect=a1a235 visual=a609bb icon=d93629 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Magical Zone](wiki/assets/skills/5193.png) |
| **Skill id** | `5193` |
| **Kind** | active (1) |
| **Target** | self; self, ally, enemy; units: monster, player; up to 10 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Cooldown** | 16 s |
| **Visual** | skillVisual 330 `수호신장_변신스킬_05_마력지대 버프` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 4 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10232-magical-zone-increased-movement-and-attack-speed\|Magical Zone : Increased Movement and Attack Speed.]] | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/10233-magical-zone-improved-health-and-mana-regeneration\|Magical Zone : Improved Health and Mana Regeneration.]] | 100 |

**Reading:** applies [[wiki/buffs/10232-magical-zone-increased-movement-and-attack-speed|Magical Zone : Increased Movement and Attack Speed.]] (100%); applies [[wiki/buffs/10233-magical-zone-improved-health-and-mana-regeneration|Magical Zone : Improved Health and Mana Regeneration.]] (100%).
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

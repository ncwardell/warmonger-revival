---
title: "Morion Passive"
type: "skill"
id: 19962
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 19962"]
name_key: "Skill_19962"
desc_key: "SkillComment_19962"
kind: 2
kind_name: "passive"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 0.0}
cost: null
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 19962, "rate": 100}
  - {"slot": 2, "type": 302, "value": 19963, "rate": 100}
  - {"slot": 3, "type": 302, "value": 19964, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 19962, "rate": 100}, {"buff": 19963, "rate": 100}, {"buff": 19964, "rate": 100}]}
icon: {"file": "Items_20.png", "index": 28}
used_by:
  - {"hero": 6, "slot": 1}
  - {"hero": 56, "slot": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=22f201 type=86a754 id=a441a4 sources=281411 name_key=a79b0c desc_key=8e3c80 kind=da4b92 kind_name=3844d5 target=d99f6c range=77de68 area=c0807e cost=2be88c cooldown=2be88c effect_kind=356a19 effects=5de2f1 damage_or_effect=6d1c08 icon=23f487 used_by=52475e -->
|  |  |
|---|---|
|  | ![Morion Passive](wiki/assets/skills/19962.png) |
| **Skill id** | `19962` |
| **Kind** | passive (2) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 3, width/angle 0 |
| **Effect kind** | damage (physical?) (1) |
| **Icon** | `ui/icons/Items_20.png` cell 28 |

### Tooltip

> [Passive]Flaming fire : When you drop below 25% health you recover 10% of your total health over 12 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/19962-flaming-fire-120-seconds\|Flaming fire : 120 Seconds]] | 100 |
| 2 | 302 | applies buff (variant 302) | [[wiki/buffs/19963-flaming-fire\|Flaming fire]] | 100 |
| 3 | 302 | applies buff (variant 302) | [[wiki/buffs/19964-flaming-fire-health-regeneration-10-secs\|Flaming fire : Health Regeneration (10 Secs)]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/19962-flaming-fire-120-seconds|Flaming fire : 120 Seconds]] (100%); applies [[wiki/buffs/19963-flaming-fire|Flaming fire]] (100%); applies [[wiki/buffs/19964-flaming-fire-health-regeneration-10-secs|Flaming fire : Health Regeneration (10 Secs)]] (100%).

### Used by

- Hero [[wiki/heroes/6-morion|Morion]], skill 1
- Hero [[wiki/heroes/56-morion-crystal|Morion (Crystal)]], skill 1
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

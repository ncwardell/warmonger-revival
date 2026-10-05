---
title: "Blind"
type: "skill"
id: 5225
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 5225"]
name_key: "Skill_5225"
desc_key: "SkillComment_5225"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 14, "type_name": "TP", "amount": 90}
cooldown: {"ms": 10000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 324, "value": 13007, "rate": 100}
damage_or_effect: {}
visual: 358
icon: {"file": "Policy_01.png", "index": 36}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=b8d6a9 type=86a754 id=b89506 sources=9cad21 name_key=ee1f0f desc_key=14c6c8 kind=356a19 kind_name=9bc378 target=cacd0a range=3028f5 area=d82541 cost=5b2b23 cooldown=4aa5a5 effect_kind=b6589f effects=568e7e damage_or_effect=bf21a9 visual=abf749 icon=494d30 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Blind](../assets/skills/5225.png) |
| **Skill id** | `5225` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 90 TP |
| **Cooldown** | 10 s |
| **Visual** | skillVisual 358 `TP스킬_블라인드` |
| **Icon** | `ui/icons/Policy_01.png` cell 36 |

### Tooltip

> Blinds all enemies in the targeted area and slows them down.Blind disturbs the sight of your enemies.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 13,007 | 100 |

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 183): Blind · 2,500 / 120 · 1,500 / 120
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

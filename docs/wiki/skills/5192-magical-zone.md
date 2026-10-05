---
title: "Magical Zone"
type: "skill"
id: 5192
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 5192"]
name_key: "Skill_5192"
desc_key: "SkillComment_5192"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: {"type": 4, "type_name": "HP %", "amount": 3}
cooldown: {"ms": 16000, "group": 0}
delivery: {"type": 4, "field_tick": 0.1}
effect_kind: 0
effects:
  - {"slot": 1, "type": 324, "value": 405, "rate": 100}
damage_or_effect: {}
visual: 329
icon: {"file": "Skill_Boss_01.dds", "index": 4}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=324252 type=86a754 id=1d464a sources=6ab015 name_key=394f4f desc_key=22928e kind=356a19 kind_name=9bc378 target=cacd0a range=fe5dbb area=950fc9 cost=e65f66 cooldown=a93f07 delivery=8af2f4 effect_kind=b6589f effects=ef8161 damage_or_effect=bf21a9 visual=8d396f icon=d93629 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Magical Zone](../assets/skills/5192.png) |
| **Skill id** | `5192` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Cost** | 3 HP % |
| **Cooldown** | 16 s |
| **Delivery** | projectile / SFX (4), tick 0.1 |
| **Visual** | skillVisual 329 `수호신장_변신스킬_05_마력지대` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 4 |

### Tooltip

> [Active] Summon a Magical Zone for 8 seconds that increases Movement, Attack Speed, HP and Mana Regeneration for all allies inside.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 405 | 100 |
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

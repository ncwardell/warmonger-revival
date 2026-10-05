---
title: "Immortality"
type: "skill"
id: 20255
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 20255"]
name_key: "Skill_20255"
desc_key: "SkillComment_20255"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: null
cooldown: {"ms": 110000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 308, "value": 20259, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20259, "rate": 100}]}
visual: 455
icon: {"file": "Skill_Boss_01.dds", "index": 50}
used_by:
  - {"weapon_base": 75, "slot": 4, "items": [8006, 8506]}
---
<!-- generated:start -->
<!-- generated-keys: title=afcd70 type=86a754 id=9b656c sources=08834d name_key=a23d94 desc_key=893824 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=2be88c cooldown=e0e4dd effect_kind=b6589f effects=f902f6 damage_or_effect=d73c86 visual=b02b70 icon=99f337 used_by=9a5896 -->
|  |  |
|---|---|
|  | ![Immortality](../assets/skills/20255.png) |
| **Skill id** | `20255` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cooldown** | 110 s |
| **Visual** | skillVisual 455 `데스헤드_불사` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 50 |

### Tooltip

> [Active] Your HP does not fall below a certain level, and you will be immortal for 5 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 308 | applies buff (variant 308) | [[wiki/buffs/20259-immortality-your-health-does-not-fall-below-a-certain-level\|Immortality : Your health does not fall below a certain level, and you will be immortal for 5 seconds.]] | 100 |

**Reading:** applies [[wiki/buffs/20259-immortality-your-health-does-not-fall-below-a-certain-level|Immortality : Your health does not fall below a certain level, and you will be immortal for 5 seconds.]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 75: [[wiki/items/8006-king-deathhead|King Deathhead]], [[wiki/items/8506-crystal-king-deathhead|Crystal : King Deathhead]]
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

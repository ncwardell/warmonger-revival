---
title: "Water shield"
type: "skill"
id: 20153
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20153"]
name_key: "Skill_20153"
desc_key: "SkillComment_20153"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 65}
cooldown: {"ms": 5000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 308, "value": 20153, "rate": 100}
  - {"slot": 2, "type": 301, "value": 20159, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 20153, "rate": 100}, {"buff": 20159, "rate": 100}]}
visual: 422
icon: {"file": "Skill_Boss_01.dds", "index": 24}
used_by:
  - {"weapon_base": 72, "slot": 2, "items": [8003, 8503]}
---
<!-- generated:start -->
<!-- generated-keys: title=3a7f1e type=86a754 id=151704 sources=697c37 name_key=1ae1cf desc_key=e29e36 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=9fa5fb cooldown=752bf3 effect_kind=356a19 effects=c0aa4e damage_or_effect=a327b4 visual=020c48 icon=13fce1 used_by=b06368 -->
|  |  |
|---|---|
|  | ![Water shield](../assets/skills/20153.png) |
| **Skill id** | `20153` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 65 MP |
| **Cooldown** | 5 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 422 `사라스바티_물 보호막` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 24 |

### Tooltip

> [Active]When used, a shield is created, and up to 10 stacks can be nested.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 308 | applies buff (variant 308) | [[wiki/buffs/20153-water-shield-creates-a-absorvs-damage-for-10-seconds\|Water shield : Creates a absorvs damage for 10 seconds]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/20159\|Buff 20159]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/20153-water-shield-creates-a-absorvs-damage-for-10-seconds|Water shield : Creates a absorvs damage for 10 seconds]] (100%); applies [[wiki/buffs/20159|Buff 20159]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 72: [[wiki/items/8003-sarasvati|Sarasvati]], [[wiki/items/8503-crystal-sarasvati|Crystal : Sarasvati]]
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

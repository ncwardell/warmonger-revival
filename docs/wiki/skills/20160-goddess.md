---
title: "Goddess"
type: "skill"
id: 20160
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20160"]
name_key: "Skill_20160"
desc_key: "SkillComment_20160"
kind: 2
kind_name: "passive"
target: {"type": 0, "type_name": "none", "relation": [], "unit_classes": [], "max_targets": 0}
range: 0
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20157, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20157, "rate": 100}]}
icon: {"file": "Skill_Boss_01.dds", "index": 29}
used_by:
  - {"weapon_base": 72, "slot": 7, "items": [8003, 8503]}
---
<!-- generated:start -->
<!-- generated-keys: title=b39afc type=86a754 id=f5a46d sources=65ef59 name_key=cc6936 desc_key=62902a kind=da4b92 kind_name=3844d5 target=2771a9 range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=195432 damage_or_effect=e743dc icon=cd5c85 used_by=6efe88 -->
|  |  |
|---|---|
|  | ![Goddess](../assets/skills/20160.png) |
| **Skill id** | `20160` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 0 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 29 |

### Tooltip

> [Passive]The base damage is reduced by 20%.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20157-goddess-reduced-damage-by-20\|Goddess : Reduced damage by 20%]] | 100 |

**Reading:** applies [[wiki/buffs/20157-goddess-reduced-damage-by-20|Goddess : Reduced damage by 20%]] (100%).

### Used by

- Weapon skill **hero set 3** of WeaponBase 72: [[wiki/items/8003-sarasvati|Sarasvati]], [[wiki/items/8503-crystal-sarasvati|Crystal : Sarasvati]]
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

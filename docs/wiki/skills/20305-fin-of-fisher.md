---
title: "Fin of Fisher"
type: "skill"
id: 20305
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20305"]
name_key: "Skill_20305"
desc_key: "SkillComment_20305"
kind: 2
kind_name: "passive"
target: {"type": 0, "type_name": "none", "relation": [], "unit_classes": [], "max_targets": 0}
range: 0
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20304, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20304, "rate": 100}]}
icon: {"file": "Skill_Boss_01.dds", "index": 41}
used_by:
  - {"weapon_base": 76, "slot": 3, "items": [8007, 8507]}
---
<!-- generated:start -->
<!-- generated-keys: title=e83dd2 type=86a754 id=a283c7 sources=079599 name_key=f199dd desc_key=f6c447 kind=da4b92 kind_name=3844d5 target=2771a9 range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=724c6a damage_or_effect=968ed0 icon=ce91ab used_by=000388 -->
|  |  |
|---|---|
|  | ![Fin of Fisher](../assets/skills/20305.png) |
| **Skill id** | `20305` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 0 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 41 |

### Tooltip

> [Passive] It increases by 20% of your max Mana.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20304\|Buff 20304]] | 100 |

**Reading:** applies [[wiki/buffs/20304|Buff 20304]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 76: [[wiki/items/8007-tempest-fisher|Tempest Fisher]], [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]]

### Mentioned in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level (line 19): 3 · Lake of the tsunami → 122 "[Lv 3] Tsunami Lake" · Tempest Fisher → 674; 733, 1209 · Topaz 814, Blue Bloodstone 804, Rosemary 822, Jasmine 824 · Red Passi...
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

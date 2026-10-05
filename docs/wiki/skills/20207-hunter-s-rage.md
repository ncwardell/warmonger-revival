---
title: "Hunter's Rage"
type: "skill"
id: 20207
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20207"]
name_key: "Skill_20207"
desc_key: "SkillComment_20207"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 20208, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 20208, "rate": 100}]}
visual: 439
icon: {"file": "Skill_Boss_01.dds", "index": 34}
used_by:
  - {"weapon_base": 73, "slot": 4, "items": [8004, 8504]}
---
<!-- generated:start -->
<!-- generated-keys: title=21da96 type=86a754 id=2a6042 sources=30af41 name_key=79545e desc_key=89ce1c kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=9e049c cooldown=7d0c8c effect_kind=356a19 effects=9f7d8f damage_or_effect=d1ebdc visual=0fdf6a icon=056ae7 used_by=f3e92c -->
|  |  |
|---|---|
|  | ![Hunter's Rage](wiki/assets/skills/20207.png) |
| **Skill id** | `20207` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 439 `아르타모스_사냥꾼의 분노` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 34 |

### Tooltip

> [Active] Increases Attack Speed and Critical Damage

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/20208-hunter-s-rage-attack-speed-and-critical-damage-increase\|Hunter's Rage: Attack Speed and Critical Damage Increase]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/20208-hunter-s-rage-attack-speed-and-critical-damage-increase|Hunter's Rage: Attack Speed and Critical Damage Increase]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 73: [[wiki/items/8004-artamos|Artamos]], [[wiki/items/8504-crystal-artamos|Crystal : Artamos]]
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

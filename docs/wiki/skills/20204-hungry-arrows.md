---
title: "Hungry arrows"
type: "skill"
id: 20204
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20204"]
name_key: "Skill_20204"
desc_key: "SkillComment_20204"
kind: 3
kind_name: "kind 3"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 1.0}
cost: {"type": 5, "type_name": "MP", "amount": 50}
cooldown: {"ms": 2000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 20204, "rate": 100}
  - {"slot": 2, "type": 321, "value": 20204, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 20204, "rate": 100}, {"buff": 20204, "rate": 100}]}
requirements:
  - {"type": 20204, "a": 4, "b": 0}
visual: 436
icon: {"file": "Skill_Boss_01.dds", "index": 32}
used_by:
  - {"weapon_base": 73, "slot": 2, "items": [8004, 8504]}
---
<!-- generated:start -->
<!-- generated-keys: title=1de249 type=86a754 id=46e870 sources=df8aa2 name_key=c22ea4 desc_key=ed65ca kind=77de68 kind_name=78ea43 target=d99f6c range=356a19 area=394af4 cost=7e5cd4 cooldown=367d78 effect_kind=356a19 effects=e905a1 damage_or_effect=30bd04 requirements=aa72e6 visual=6c4c04 icon=6834b3 used_by=c10c58 -->
|  |  |
|---|---|
|  | ![Hungry arrows](../assets/skills/20204.png) |
| **Skill id** | `20204` |
| **Kind** | kind 3 (3) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 1, width/angle 1 |
| **Cost** | 50 MP |
| **Cooldown** | 2 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 436 `아르타모스_굶주린 화살` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 32 |

### Tooltip

> [Active] It consumes Mana per second and increases your Life Steal by 5%.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/20204-hungry-arrows-increased-life-steal\|Hungry arrows: increased Life Steal]] | 100 |
| 2 | 321 | applies buff (variant 321) | [[wiki/buffs/20204-hungry-arrows-increased-life-steal\|Hungry arrows: increased Life Steal]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/20204-hungry-arrows-increased-life-steal|Hungry arrows: increased Life Steal]] (100%); applies [[wiki/buffs/20204-hungry-arrows-increased-life-steal|Hungry arrows: increased Life Steal]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 20204 | 4 | 0 |

### Used by

- Weapon skill **W** of WeaponBase 73: [[wiki/items/8004-artamos|Artamos]], [[wiki/items/8504-crystal-artamos|Crystal : Artamos]]
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

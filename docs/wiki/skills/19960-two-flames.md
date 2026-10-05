---
title: "Two Flames"
type: "skill"
id: 19960
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 19960"]
name_key: "Skill_19960"
desc_key: "SkillComment_19960"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 10.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 110}
cooldown: {"ms": 14000, "group": 0}
delivery: {"type": 2, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 314, "value": 19958, "rate": 100}
  - {"slot": 3, "type": 330, "value": 100, "rate": 100}
  - {"slot": 4, "type": 314, "value": 19959, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 19958, "rate": 100}, {"buff": 19959, "rate": 100}], "base": 100}
visual: 410
icon: {"file": "Skill_Boss_01.dds", "index": 10}
used_by:
  - {"weapon_base": 74, "slot": 7, "items": [8005, 8505]}
---
<!-- generated:start -->
<!-- generated-keys: title=d8488b type=86a754 id=98aca3 sources=fcb73d name_key=10c2ca desc_key=1e7267 kind=356a19 kind_name=9bc378 target=c9e051 range=b1d578 area=728214 cost=060055 cooldown=5b7687 delivery=1d1859 effect_kind=356a19 effects=456ecb damage_or_effect=462b2d visual=329dc1 icon=593306 used_by=afa677 -->
|  |  |
|---|---|
|  | ![Two Flames](wiki/assets/skills/19960.png) |
| **Skill id** | `19960` |
| **Kind** | active (1) |
| **Target** | ground; ally, enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | line / rectangle?, radius 10, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 110 MP |
| **Cooldown** | 14 s |
| **Delivery** | 2 |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 410 `모리온_2개의 불` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 10 |

### Tooltip

> [Active] Casts fire in a straight line, increasing your Movement and Attack Speed when hit by ally forces, and damages enemies for 3 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/19958-two-flame-decreased-attack-speed-and-movement-speed\|Two Flame : Decreased Attack Speed and Movement Speed]] | 100 |
| 3 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 4 | 314 | applies buff (variant 314) | [[wiki/buffs/19959-two-flame-damage-over-time-for-6-seconds\|Two Flame : Damage over time for 6 seconds]] | 100 |

**Reading:** amount **100**; damage (physical?); applies [[wiki/buffs/19958-two-flame-decreased-attack-speed-and-movement-speed|Two Flame : Decreased Attack Speed and Movement Speed]] (100%); applies [[wiki/buffs/19959-two-flame-damage-over-time-for-6-seconds|Two Flame : Damage over time for 6 seconds]] (100%).

### Used by

- Weapon skill **hero set 3** of WeaponBase 74: [[wiki/items/8005-morion|Morion]], [[wiki/items/8505-crystal-morion|Crystal : Morion]]
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

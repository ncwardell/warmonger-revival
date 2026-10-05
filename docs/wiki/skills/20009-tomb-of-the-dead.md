---
title: "Tomb of the Dead"
type: "skill"
id: 20009
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 20009"]
name_key: "Skill_5186"
desc_key: "SkillComment_5186"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 5, "type_name": "MP", "amount": 640}
cooldown: {"ms": 120000, "group": 0}
delivery: {"type": 4, "field_tick": 0.1}
effect_kind: 2
effects:
  - {"slot": 1, "type": 324, "value": 14000, "rate": 100}
damage_or_effect: {}
visual: 317
icon: {"file": "Policy.png", "index": 42}
used_by:
  - {"weapon_base": 69, "slot": 8, "items": [8000, 8500]}
---
<!-- generated:start -->
<!-- generated-keys: title=25fe5b type=86a754 id=c6d459 sources=a5a532 name_key=40eafa desc_key=ad1d7b kind=356a19 kind_name=9bc378 target=cacd0a range=902ba3 area=d82541 cost=59d981 cooldown=a7242f delivery=8af2f4 effect_kind=da4b92 effects=8cd921 damage_or_effect=bf21a9 visual=f44a28 icon=5cb950 used_by=55e096 -->
|  |  |
|---|---|
|  | ![Tomb of the Dead](../assets/skills/20009.png) |
| **Skill id** | `20009` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 640 MP |
| **Cooldown** | 120 s |
| **Delivery** | projectile / SFX (4), tick 0.1 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 317 `Skeleton_King_변신스킬_06_망자의 무덤` |
| **Icon** | `ui/icons/Policy.png` cell 42 |

### Tooltip

> [Active] Summon a Tomb in the targeted area. Inflicts 7% of the enemy's current Health as damage on them for 10 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 14,000 | 100 |

### Used by

- Weapon skill **hero set 4** of WeaponBase 69: [[wiki/items/8000-dark-knight-skull|Dark knight Skull]], [[wiki/items/8500-crystal-dark-knight-skull|Crystal : Dark knight Skull]]

### Mentioned in

- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § Hero form (Dark Knight Skull) (line 53): Hero · Dark Knight Skull: the new R skill is Heaven and Earth 20006, which is weapon 69 (item 8000 "Dark knight Skull"; HeroData 1). Hero skills on that weap...
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

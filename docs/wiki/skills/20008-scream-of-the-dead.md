---
title: "Scream of the Dead"
type: "skill"
id: 20008
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20008", "client: StringAll_Eng SkillComment_5185 (tooltip value tags)"]
name_key: "Skill_5185"
desc_key: "SkillComment_5185"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 6
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 304, "value": 20006, "rate": 100}
  - {"slot": 2, "type": 314, "value": 20007, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20006, "rate": 100}, {"buff": 20007, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_R_MDAM", "value": 10}
visual: 322
icon: {"file": "Policy.png", "index": 40}
used_by:
  - {"weapon_base": 69, "slot": 6, "items": [8000, 8500]}
---
<!-- generated:start -->
<!-- generated-keys: title=a18e83 type=86a754 id=28dea5 sources=79f596 name_key=516a99 desc_key=7657d9 kind=356a19 kind_name=9bc378 target=9dc90e range=c1dfd9 area=d82541 cost=911ade cooldown=628d31 effect_kind=b6589f effects=e9f2a3 damage_or_effect=c6d100 tooltip_formula=1f41f5 visual=81110d icon=6665b9 used_by=c1aa0a -->
|  |  |
|---|---|
|  | ![Scream of the Dead](../assets/skills/20008.png) |
| **Skill id** | `20008` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 10 |
| **Range** | 6 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Visual** | skillVisual 322 `Skeleton_King_변신스킬_05_망자들의 절규` |
| **Icon** | `ui/icons/Policy.png` cell 40 |

### Tooltip

> [Active] Generates a 300`{EF_R_MDAM 10}` protective barrier around you. Reduces Armor and Magic Resistance of all surrounding enemies by 30.

Tooltip formula: **10% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 304 | applies buff (variant 304) | [[wiki/buffs/20006-scream-of-the-dead-creates-a-absorvs-damage-for-8-seconds\|Scream of the Dead : Creates a absorvs damage for 8 seconds]] | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/20007-scream-of-the-dead-reduced-armor-and-magic-resistance\|Scream of the Dead : Reduced Armor and Magic Resistance]] | 100 |

**Reading:** applies [[wiki/buffs/20006-scream-of-the-dead-creates-a-absorvs-damage-for-8-seconds|Scream of the Dead : Creates a absorvs damage for 8 seconds]] (100%); applies [[wiki/buffs/20007-scream-of-the-dead-reduced-armor-and-magic-resistance|Scream of the Dead : Reduced Armor and Magic Resistance]] (100%).

### Used by

- Weapon skill **hero set 2** of WeaponBase 69: [[wiki/items/8000-dark-knight-skull|Dark knight Skull]], [[wiki/items/8500-crystal-dark-knight-skull|Crystal : Dark knight Skull]]

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

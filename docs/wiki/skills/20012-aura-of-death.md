---
title: "Aura of Death"
type: "skill"
id: 20012
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20012", "video: [[gameplay/video-fort-war]] §1 Hero form (hero skill list; client WeaponBase 69)"]
name_key: "Skill_5189"
desc_key: "SkillComment_5189"
kind: 2
kind_name: "passive"
target: {"type": 0, "type_name": "none", "relation": [], "unit_classes": [], "max_targets": 1}
range: 0
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 303, "value": 20011, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20011, "rate": 100}]}
icon: {"file": "Policy.png", "index": 41}
used_by:
  - {"weapon_base": 69, "slot": 7, "items": [8000, 8500]}
---
<!-- generated:start -->
<!-- generated-keys: title=d266c7 type=86a754 id=9101d1 sources=8ea2f9 name_key=ba91d8 desc_key=1a11c7 kind=da4b92 kind_name=3844d5 target=6d698f range=b6589f cost=2be88c cooldown=2be88c effect_kind=b6589f effects=04f123 damage_or_effect=e67847 icon=4e653c used_by=7308d3 -->
|  |  |
|---|---|
|  | ![Aura of Death](wiki/assets/skills/20012.png) |
| **Skill id** | `20012` |
| **Kind** | passive (2) |
| **Target** | none; -; units: -; up to 1 |
| **Range** | 0 (world units) |
| **Icon** | `ui/icons/Policy.png` cell 41 |

### Tooltip

> [Passive] Restores 3% of your Health for every kill or assist.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 303 | applies buff (variant 303) | [[wiki/buffs/20011-aura-of-death-kills-and-assists-heal-you\|Aura of Death : Kills and assists heal you]] | 100 |

**Reading:** applies [[wiki/buffs/20011-aura-of-death-kills-and-assists-heal-you|Aura of Death : Kills and assists heal you]] (100%).

### Used by

- Weapon skill **hero set 3** of WeaponBase 69: [[wiki/items/8000-dark-knight-skull|Dark knight Skull]], [[wiki/items/8500-crystal-dark-knight-skull|Crystal : Dark knight Skull]]

### Mentioned in

- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § Hero form (Dark Knight Skull) (line 53): Hero · Dark Knight Skull: the new R skill is Heaven and Earth 20006, which is weapon 69 (item 8000 "Dark knight Skull"; HeroData 1). Hero skills on that weap...
<!-- generated:end -->

## Notes

- One of the Dark Knight Skull hero skills (weapon 69, item 8000), the hero used in the June 2018 fort-war video ([[gameplay/video-fort-war]] §1 Hero form). Only its R, Heaven and Earth, is shown in use. *video + client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-fort-war]] §1.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

---
title: "Morion (Crystal)"
type: "hero"
id: 56
status: "complete"
missing: []
sources: ["client: HeroData.cdb id 56", "client: Item_Base.cdb id 8505 (kind 18, option 201 = 56)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)"]
name_key: "HeroName_6"
stats: {"stat1": 1242, "stat2": 795, "hp": 10460, "mp": 3470}
skills: [19962, 19964, 19966, 19968, 19970, 19972, 19972, 19972, 19972, 19972]
transform_skill: 19999
base_hero: 6
trigger: {"item": 8505, "kind": "Innocence Crystal"}
weapon_base: 74
visual: 1005
cooldown_s: 120
durability: 1500
duration: {"durability": 1500, "drain_per_second": 5, "seconds": 300}
---
<!-- generated:start -->
<!-- generated-keys: title=6693ef type=e44582 id=54ceb9 sources=daf339 name_key=0a9330 stats=8b2051 skills=56fd06 transform_skill=7519dd base_hero=c1dfd9 trigger=c7827a weapon_base=1f1362 visual=0477d7 cooldown_s=775bc5 durability=7841fb duration=712893 -->
|  |  |
|---|---|
|  | ![Morion (Crystal)](wiki/assets/heroes/56.png) |
| **Hero id** | `56` |
| **Unlocked by** | [[wiki/items/8505-crystal-morion\|Crystal : Morion]] (Innocence Crystal, worn in the Innocence slot) |
| **Same form as** | [[wiki/heroes/6-morion\|Morion]] |
| **Transform skill** | [[wiki/skills/19999-morion-transformation\|Morion Transformation]] |
| **Level required** | none (WM 1107) |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 1,500 |
| **Visual** | CostumeDB row 1005 (WeaponBase 74 c14) |

### Description

> Devil Morion
>
> "You can use the power of fire after you transform into Morion"

### Stats

`HeroData` columns. The decoder's names are guesses: `stat1` / `stat2` look like Attack / Ability Power (the mage heroes Amaterasu and Tempest Fisher have the higher `stat2` and more MP). In the [[gameplay/video-fort-war|fort-war video]] Dark Knight Skull raised max HP/MP from 7,282 / 1,660 to 16,214 / 3,645 (×2.2), which is not base + these values; the formula is unknown. A hero also gets a share of the gear's stats: 35 % at T1+0 up to 100 % at T3+15 (WM 0628, [[gameplay/classes-and-legions|Classes]] §5).

| stat1 (Attack?) | stat2 (Ability Power?) | HP | MP |
|---|---|---|---|
| 1,242 | 795 | 10,460 | 3,470 |

### Duration

An Innocence Crystal has **1,500 durability** and loses **5 per second** while transformed, so a full crystal gives **300 s** of hero form; it has no level limit (WM 1107, [[gameplay/events-and-schedules|Events and schedules]] §9). The client row's period column holds the same 1,500.

### Skills

`HeroData` skill1–10 (repeats dropped):

1. [[wiki/skills/19962-morion-passive|Morion Passive]]
2. [[wiki/skills/19964-morion-passive|Morion Passive]]
3. [[wiki/skills/19966-morion-passive|Morion Passive]]
4. [[wiki/skills/19968-morion-passive|Morion Passive]]
5. [[wiki/skills/19970-morion-passive|Morion Passive]]
6. [[wiki/skills/19972-morion-passive|Morion Passive]]

### Weapon base

The Innocence item's WeaponBase row 74: skills [[wiki/skills/19951-fiery-anger|Fiery Anger]], [[wiki/skills/19956-flame-armor|Flame armor]], [[wiki/skills/19953-fury-of-fire|Fury of fire]], [[wiki/skills/19954-flame-area|Flame area]], [[wiki/skills/19958-push|Push]], [[wiki/skills/19959-flame-wave|Flame wave]], [[wiki/skills/19960-two-flames|Two Flames]], [[wiki/skills/19961-flame-absorbtion-shield|Flame Absorbtion Shield]].

### How to get it

- Craft [[wiki/items/8505-crystal-morion|Crystal : Morion]] from [[wiki/items/9005-piece-morion|Piece : Morion]] × 5, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 50 ([[wiki/recipes/1206-crystal-morion-recipe|Crystal : Morion recipe]])
- Innocence and pieces come from the Innocence gacha card ([[wiki/gacha/3-innocence-gacha|Innocence gacha]], [[gameplay/progression-and-economy|Progression]] §6).

See also: [[wiki/items/hero-items|Innocence items]].
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

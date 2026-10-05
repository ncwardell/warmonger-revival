---
title: "Morion"
type: "hero"
id: 6
status: "stub"
missing: ["duration"]
sources: ["client: HeroData.cdb id 6", "client: Item_Base.cdb id 8005 (kind 18, option 201 = 6)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)", "docs: [[gameplay/classes-and-legions]] §1 (hero only at level 30, guides); client string Item_Hero_LevelLimit30"]
name_key: "HeroName_6"
stats: {"stat1": 1242, "stat2": 795, "hp": 10460, "mp": 3470}
skills: [19962, 19964, 19966, 19968, 19970, 19972, 19972, 19972, 19972, 19972]
transform_skill: 19950
trigger: {"item": 8005, "kind": "Innocence"}
weapon_base: 74
visual: 1005
cooldown_s: 120
durability: 240
level_required: 30
---
<!-- generated:start -->
<!-- generated-keys: title=083c06 type=e44582 id=c1dfd9 sources=446d6f name_key=0a9330 stats=8b2051 skills=56fd06 transform_skill=00e24c trigger=291db6 weapon_base=1f1362 visual=0477d7 cooldown_s=775bc5 durability=cae91e level_required=22d200 -->
|  |  |
|---|---|
|  | ![Morion](wiki/assets/heroes/6.png) |
| **Hero id** | `6` |
| **Unlocked by** | [[wiki/items/8005-morion\|Morion]] (Innocence, worn in the Innocence slot) |
| **Crystal version** | [[wiki/heroes/56-morion-crystal\|Morion (Crystal)]] |
| **Transform skill** | [[wiki/skills/19950-morion-transformation\|Morion Transformation]] |
| **Level required** | 30 |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 240 |
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

Innocence durability was raised from 24 to **240** (WM 0402, [[gameplay/events-and-schedules|Events and schedules]] §9); how fast it drains while transformed is not known, so the duration is still open. In the fort-war video a Dark Knight Skull form lasted **at least 8.5 minutes** ([[gameplay/video-fort-war|video]]).

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

- Craft [[wiki/items/8005-morion|Morion]] from [[wiki/items/9005-piece-morion|Piece : Morion]] × 100, [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]] × 200 ([[wiki/recipes/1506-morion-recipe|Morion recipe]])
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

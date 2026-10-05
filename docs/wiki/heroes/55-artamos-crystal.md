---
title: "Artamos (Crystal)"
type: "hero"
id: 55
status: "complete"
missing: []
sources: ["client: HeroData.cdb id 55", "client: Item_Base.cdb id 8504 (kind 18, option 201 = 55)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)"]
name_key: "HeroName_5"
stats: {"stat1": 535, "stat2": 270, "hp": 6200, "mp": 4275}
skills: [20214, 20217, 20218, 20219, 20220, 20221, 20221, 20221, 20221, 20221]
transform_skill: 20249
base_hero: 5
trigger: {"item": 8504, "kind": "Innocence Crystal"}
weapon_base: 73
visual: 1004
cooldown_s: 120
durability: 1500
duration: {"durability": 1500, "drain_per_second": 5, "seconds": 300}
---
<!-- generated:start -->
<!-- generated-keys: title=324759 type=e44582 id=8effee sources=7874dd name_key=821a49 stats=6515b8 skills=3b48eb transform_skill=244de1 base_hero=ac3478 trigger=42a248 weapon_base=35e995 visual=70b8dc cooldown_s=775bc5 durability=7841fb duration=712893 -->
|  |  |
|---|---|
|  | ![Artamos (Crystal)](wiki/assets/heroes/55.png) |
| **Hero id** | `55` |
| **Unlocked by** | [[wiki/items/8504-crystal-artamos\|Crystal : Artamos]] (Innocence Crystal, worn in the Innocence slot) |
| **Same form as** | [[wiki/heroes/5-artamos\|Artamos]] |
| **Transform skill** | [[wiki/skills/20249-artamos-transformation\|Artamos Transformation]] |
| **Level required** | none (WM 1107) |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 1,500 |
| **Visual** | CostumeDB row 1004 (WeaponBase 73 c14) |

### Description

> Artamos
>
> "After converting to Artamos, you can use the power of Artamos."

### Stats

`HeroData` columns. The decoder's names are guesses: `stat1` / `stat2` look like Attack / Ability Power (the mage heroes Amaterasu and Tempest Fisher have the higher `stat2` and more MP). In the [[gameplay/video-fort-war|fort-war video]] Dark Knight Skull raised max HP/MP from 7,282 / 1,660 to 16,214 / 3,645 (×2.2), which is not base + these values; the formula is unknown. A hero also gets a share of the gear's stats: 35 % at T1+0 up to 100 % at T3+15 (WM 0628, [[gameplay/classes-and-legions|Classes]] §5).

| stat1 (Attack?) | stat2 (Ability Power?) | HP | MP |
|---|---|---|---|
| 535 | 270 | 6,200 | 4,275 |

### Duration

An Innocence Crystal has **1,500 durability** and loses **5 per second** while transformed, so a full crystal gives **300 s** of hero form; it has no level limit (WM 1107, [[gameplay/events-and-schedules|Events and schedules]] §9). The client row's period column holds the same 1,500.

### Skills

`HeroData` skill1–10 (repeats dropped):

1. [[wiki/skills/20214-fatal-skill|Fatal skill]]
2. [[wiki/skills/20217-fatal-skill|Fatal skill]]
3. [[wiki/skills/20218-fatal-skill|Fatal skill]]
4. [[wiki/skills/20219-fatal-skill|Fatal skill]]
5. [[wiki/skills/20220-fatal-skill|Fatal skill]]
6. [[wiki/skills/20221-fatal-skill|Fatal skill]]

### Weapon base

The Innocence item's WeaponBase row 73: skills [[wiki/skills/20202-covert-step|Covert Step]], [[wiki/skills/20204-hungry-arrows|Hungry arrows]], [[wiki/skills/20215-hunting-eye|Hunting Eye]], [[wiki/skills/20207-hunter-s-rage|Hunter's Rage]], [[wiki/skills/20208-capture-weakness|Capture Weakness]], [[wiki/skills/20209-invisible-prison|Invisible prison]], [[wiki/skills/20211-improved-hand|Improved Hand]], [[wiki/skills/20213-prudent-blow|Prudent blow]].

### How to get it

- Craft [[wiki/items/8504-crystal-artamos|Crystal : Artamos]] from [[wiki/items/9004-piece-artamos|Piece : Artamos]] × 5, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 50 ([[wiki/recipes/1205-crystal-artamos-recipe|Crystal : Artamos recipe]])
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

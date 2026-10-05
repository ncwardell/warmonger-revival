---
title: "Artamos"
type: "hero"
id: 5
status: "stub"
missing: ["duration"]
sources: ["client: HeroData.cdb id 5", "client: Item_Base.cdb id 8004 (kind 18, option 201 = 5)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)", "docs: [[gameplay/classes-and-legions]] §1 (hero only at level 30, guides); client string Item_Hero_LevelLimit30"]
name_key: "HeroName_5"
stats: {"stat1": 535, "stat2": 270, "hp": 6200, "mp": 4275}
skills: [20214, 20217, 20218, 20219, 20220, 20221, 20221, 20221, 20221, 20221]
transform_skill: 20201
trigger: {"item": 8004, "kind": "Innocence"}
weapon_base: 73
visual: 1004
cooldown_s: 120
durability: 240
level_required: 30
---
<!-- generated:start -->
<!-- generated-keys: title=d105b8 type=e44582 id=ac3478 sources=a5ece2 name_key=821a49 stats=6515b8 skills=3b48eb transform_skill=ff525e trigger=16a62f weapon_base=35e995 visual=70b8dc cooldown_s=775bc5 durability=cae91e level_required=22d200 -->
|  |  |
|---|---|
|  | ![Artamos](wiki/assets/heroes/5.png) |
| **Hero id** | `5` |
| **Unlocked by** | [[wiki/items/8004-artamos\|Artamos]] (Innocence, worn in the Innocence slot) |
| **Crystal version** | [[wiki/heroes/55-artamos-crystal\|Artamos (Crystal)]] |
| **Transform skill** | [[wiki/skills/20201-artamos-transformation\|Artamos Transformation]] |
| **Level required** | 30 |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 240 |
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

Innocence durability was raised from 24 to **240** (WM 0402, [[gameplay/events-and-schedules|Events and schedules]] §9); how fast it drains while transformed is not known, so the duration is still open. In the fort-war video a Dark Knight Skull form lasted **at least 8.5 minutes** ([[gameplay/video-fort-war|video]]).

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

- Craft [[wiki/items/8004-artamos|Artamos]] from [[wiki/items/9004-piece-artamos|Piece : Artamos]] × 100, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 200 ([[wiki/recipes/1505-artamos-recipe|Artamos recipe]])
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

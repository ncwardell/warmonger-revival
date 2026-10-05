---
title: "Tempest Fisher (Crystal)"
type: "hero"
id: 58
status: "complete"
missing: []
sources: ["client: HeroData.cdb id 58", "client: Item_Base.cdb id 8507 (kind 18, option 201 = 58)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)"]
name_key: "HeroName_8"
stats: {"stat1": 902, "stat2": 1101, "hp": 5400, "mp": 7205}
skills: [20311, 20312, 20313, 20314, 20315, 20316, 20316, 20316, 20316, 20316]
transform_skill: 20349
base_hero: 8
trigger: {"item": 8507, "kind": "Innocence Crystal"}
weapon_base: 76
visual: 1007
cooldown_s: 120
durability: 1500
duration: {"durability": 1500, "drain_per_second": 5, "seconds": 300}
---
<!-- generated:start -->
<!-- generated-keys: title=a26a8d type=e44582 id=667be5 sources=5f7cb2 name_key=4cab12 stats=36c21a skills=4972ce transform_skill=f84e6b base_hero=fe5dbb trigger=178165 weapon_base=d54ad0 visual=1ccace cooldown_s=775bc5 durability=7841fb duration=712893 -->
|  |  |
|---|---|
|  | ![Tempest Fisher (Crystal)](wiki/assets/heroes/58.png) |
| **Hero id** | `58` |
| **Unlocked by** | [[wiki/items/8507-crystal-tempest-fisher\|Crystal : Tempest Fisher]] (Innocence Crystal, worn in the Innocence slot) |
| **Same form as** | [[wiki/heroes/8-tempest-fisher\|Tempest Fisher]] |
| **Transform skill** | [[wiki/skills/20349-tempest-fisher-transformation\|Tempest Fisher Transformation]] |
| **Level required** | none (WM 1107) |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 1,500 |
| **Visual** | CostumeDB row 1007 (WeaponBase 76 c14) |

### Description

> Tempest Fisher
>
> "You can use Fisher's power to turn into Fisher"

### Stats

`HeroData` columns. The decoder's names are guesses: `stat1` / `stat2` look like Attack / Ability Power (the mage heroes Amaterasu and Tempest Fisher have the higher `stat2` and more MP). In the [[gameplay/video-fort-war|fort-war video]] Dark Knight Skull raised max HP/MP from 7,282 / 1,660 to 16,214 / 3,645 (×2.2), which is not base + these values; the formula is unknown. A hero also gets a share of the gear's stats: 35 % at T1+0 up to 100 % at T3+15 (WM 0628, [[gameplay/classes-and-legions|Classes]] §5).

| stat1 (Attack?) | stat2 (Ability Power?) | HP | MP |
|---|---|---|---|
| 902 | 1,101 | 5,400 | 7,205 |

### Duration

An Innocence Crystal has **1,500 durability** and loses **5 per second** while transformed, so a full crystal gives **300 s** of hero form; it has no level limit (WM 1107, [[gameplay/events-and-schedules|Events and schedules]] §9). The client row's period column holds the same 1,500.

### Skills

`HeroData` skill1–10 (repeats dropped):

1. [[wiki/skills/20311-fisher-s-essence|Fisher's essence]]
2. [[wiki/skills/20312-fisher-s-essence|Fisher's essence]]
3. [[wiki/skills/20313-fisher-s-essence|Fisher's essence]]
4. [[wiki/skills/20314-fisher-s-essence|Fisher's essence]]
5. [[wiki/skills/20315-fisher-s-essence|Fisher's essence]]
6. [[wiki/skills/20316-fisher-s-essence|Fisher's essence]]

### Weapon base

The Innocence item's WeaponBase row 76: skills [[wiki/skills/20302-water-of-deceleration|Water of deceleration]], [[wiki/skills/20303-water-column|Water column]], [[wiki/skills/20305-fin-of-fisher|Fin of Fisher]], [[wiki/skills/20306-tsunami|Tsunami]], [[wiki/skills/20307-fisher-s-protection|Fisher's Protection]], [[wiki/skills/20308-earthquake|Earthquake]], [[wiki/skills/20309-divine|Divine]], [[wiki/skills/20310-fisher-s-cries|Fisher's cries]].

### How to get it

- Craft [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]] from [[wiki/items/9007-piece-tempest-fisher|Piece : Tempest Fisher]] × 5, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50 ([[wiki/recipes/1208-crystal-tempest-fisher-recipe|Crystal : Tempest Fisher recipe]])
- Innocence and pieces come from the Innocence gacha card ([[wiki/gacha/3-innocence-gacha|Innocence gacha]], [[gameplay/progression-and-economy|Progression]] §6).

### Monster with this name

[[wiki/monsters/674-tempest-fisher|Tempest Fisher]], [[wiki/monsters/733-tempest-fisher|Tempest Fisher]], [[wiki/monsters/1209-tempest-fisher|Tempest Fisher]]

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

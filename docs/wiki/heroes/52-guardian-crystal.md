---
title: "Guardian (Crystal)"
type: "hero"
id: 52
status: "complete"
missing: []
sources: ["client: HeroData.cdb id 52", "client: Item_Base.cdb id 8501 (kind 18, option 201 = 52)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)"]
name_key: "HeroName_2"
stats: {"stat1": 1019, "stat2": 938, "hp": 8425, "mp": 2660}
skills: [20050, 20064, 20065, 20066, 20067, 20068, 20068, 20068, 20068, 20068]
transform_skill: 20099
base_hero: 2
trigger: {"item": 8501, "kind": "Innocence Crystal"}
weapon_base: 70
visual: 1001
cooldown_s: 120
durability: 1500
duration: {"durability": 1500, "drain_per_second": 5, "seconds": 300}
---
<!-- generated:start -->
<!-- generated-keys: title=23fcdc type=e44582 id=a93349 sources=4990ea name_key=6133cb stats=50fb90 skills=734319 transform_skill=d5aa4f base_hero=da4b92 trigger=02a3c1 weapon_base=b7103c visual=dd0190 cooldown_s=775bc5 durability=7841fb duration=712893 -->
|  |  |
|---|---|
|  | ![Guardian (Crystal)](wiki/assets/heroes/52.png) |
| **Hero id** | `52` |
| **Unlocked by** | [[wiki/items/8501-crystal-guardian\|Crystal : Guardian]] (Innocence Crystal, worn in the Innocence slot) |
| **Same form as** | [[wiki/heroes/2-guardian\|Guardian]] |
| **Transform skill** | [[wiki/skills/20099-guardian-transformation\|Guardian Transformation]] |
| **Level required** | none (WM 1107) |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 1,500 |
| **Visual** | CostumeDB row 1001 (WeaponBase 70 c14) |

### Description

> Guardian
>
> "I use the sacred power of the temple knight "

### Stats

`HeroData` columns. The decoder's names are guesses: `stat1` / `stat2` look like Attack / Ability Power (the mage heroes Amaterasu and Tempest Fisher have the higher `stat2` and more MP). In the [[gameplay/video-fort-war|fort-war video]] Dark Knight Skull raised max HP/MP from 7,282 / 1,660 to 16,214 / 3,645 (×2.2), which is not base + these values; the formula is unknown. A hero also gets a share of the gear's stats: 35 % at T1+0 up to 100 % at T3+15 (WM 0628, [[gameplay/classes-and-legions|Classes]] §5).

| stat1 (Attack?) | stat2 (Ability Power?) | HP | MP |
|---|---|---|---|
| 1,019 | 938 | 8,425 | 2,660 |

### Duration

An Innocence Crystal has **1,500 durability** and loses **5 per second** while transformed, so a full crystal gives **300 s** of hero form; it has no level limit (WM 1107, [[gameplay/events-and-schedules|Events and schedules]] §9). The client row's period column holds the same 1,500.

### Skills

`HeroData` skill1–10 (repeats dropped):

1. [[wiki/skills/20050-guardian-passive|Guardian Passive]]
2. [[wiki/skills/20064-guardian-passive|Guardian Passive]]
3. [[wiki/skills/20065-guardian-passive|Guardian Passive]]
4. [[wiki/skills/20066-guardian-passive|Guardian Passive]]
5. [[wiki/skills/20067-guardian-passive|Guardian Passive]]
6. [[wiki/skills/20068-guardian-passive|Guardian Passive]]

### Weapon base

The Innocence item's WeaponBase row 70: skills [[wiki/skills/20063-advent|Advent]], [[wiki/skills/20062-maximized-efficiency|Maximized Efficiency]], [[wiki/skills/20060-a-warrior-s-body|A Warrior's Body]], [[wiki/skills/20055-critical-strike|Critical Strike]], [[wiki/skills/20056-magical-zone|Magical Zone]], [[wiki/skills/20054-magical-protection|Magical Protection]], [[wiki/skills/20059-absorbing-magic|Absorbing Magic]], [[wiki/skills/20058-overload|Overload]].

### How to get it

- Craft [[wiki/items/8501-crystal-guardian|Crystal : Guardian]] from [[wiki/items/9001-piece-guardian|Piece : Guardian]] × 5, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50 ([[wiki/recipes/1202-crystal-guardian-recipe|Crystal : Guardian recipe]])
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

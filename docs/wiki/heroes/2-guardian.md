---
title: "Guardian"
type: "hero"
id: 2
status: "stub"
missing: ["duration"]
sources: ["client: HeroData.cdb id 2", "client: Item_Base.cdb id 8001 (kind 18, option 201 = 2)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)", "docs: [[gameplay/classes-and-legions]] §1 (hero only at level 30, guides); client string Item_Hero_LevelLimit30"]
name_key: "HeroName_2"
stats: {"stat1": 1019, "stat2": 938, "hp": 8425, "mp": 2660}
skills: [20050, 20064, 20065, 20066, 20067, 20068, 20068, 20068, 20068, 20068]
transform_skill: 20051
trigger: {"item": 8001, "kind": "Innocence"}
weapon_base: 70
visual: 1001
cooldown_s: 120
durability: 240
level_required: 30
---
<!-- generated:start -->
<!-- generated-keys: title=1817f8 type=e44582 id=da4b92 sources=69ca18 name_key=6133cb stats=50fb90 skills=734319 transform_skill=aed405 trigger=d47f9f weapon_base=b7103c visual=dd0190 cooldown_s=775bc5 durability=cae91e level_required=22d200 -->
|  |  |
|---|---|
|  | ![Guardian](wiki/assets/heroes/2.png) |
| **Hero id** | `2` |
| **Unlocked by** | [[wiki/items/8001-guardian\|Guardian]] (Innocence, worn in the Innocence slot) |
| **Crystal version** | [[wiki/heroes/52-guardian-crystal\|Guardian (Crystal)]] |
| **Transform skill** | [[wiki/skills/20051-guardian-transformation\|Guardian Transformation]] |
| **Level required** | 30 |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 240 |
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

Innocence durability was raised from 24 to **240** (WM 0402, [[gameplay/events-and-schedules|Events and schedules]] §9); how fast it drains while transformed is not known, so the duration is still open. In the fort-war video a Dark Knight Skull form lasted **at least 8.5 minutes** ([[gameplay/video-fort-war|video]]).

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

- Craft [[wiki/items/8001-guardian|Guardian]] from [[wiki/items/9001-piece-guardian|Piece : Guardian]] × 100, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 200 ([[wiki/recipes/1502-guardian-recipe|Guardian recipe]])
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

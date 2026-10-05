---
title: "Dark Knight Skull (Crystal)"
type: "hero"
id: 51
status: "complete"
missing: []
sources: ["client: HeroData.cdb id 51", "client: Item_Base.cdb id 8500 (kind 18, option 201 = 51)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)"]
name_key: "HeroName_1"
stats: {"stat1": 1204, "stat2": 756, "hp": 10890, "mp": 3010}
skills: [20011, 20013, 20014, 20015, 20016, 20017, 20017, 20017, 20017, 20017]
transform_skill: 20049
base_hero: 1
trigger: {"item": 8500, "kind": "Innocence Crystal"}
weapon_base: 69
visual: 1000
cooldown_s: 120
durability: 1500
duration: {"durability": 1500, "drain_per_second": 5, "seconds": 300}
---
<!-- generated:start -->
<!-- generated-keys: title=02db96 type=e44582 id=b7eb6c sources=b20b37 name_key=b6a296 stats=6967eb skills=97aa79 transform_skill=b2e9e9 base_hero=356a19 trigger=ad8b70 weapon_base=a72b20 visual=e3cbba cooldown_s=775bc5 durability=7841fb duration=712893 -->
|  |  |
|---|---|
|  | ![Dark Knight Skull (Crystal)](wiki/assets/heroes/51.png) |
| **Hero id** | `51` |
| **Unlocked by** | [[wiki/items/8500-crystal-dark-knight-skull\|Crystal : Dark knight Skull]] (Innocence Crystal, worn in the Innocence slot) |
| **Same form as** | [[wiki/heroes/1-dark-knight-skull\|Dark Knight Skull]] |
| **Transform skill** | [[wiki/skills/20049-dark-knight-skull-transformation\|Dark Knight Skull Transformation]] |
| **Level required** | none (WM 1107) |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 1,500 |
| **Visual** | CostumeDB row 1000 (WeaponBase 69 c14) |

### Description

> Dark Knight Skull
>
> "Using the Dark Knight's Dark Power"

### Stats

`HeroData` columns. The decoder's names are guesses: `stat1` / `stat2` look like Attack / Ability Power (the mage heroes Amaterasu and Tempest Fisher have the higher `stat2` and more MP). In the [[gameplay/video-fort-war|fort-war video]] Dark Knight Skull raised max HP/MP from 7,282 / 1,660 to 16,214 / 3,645 (×2.2), which is not base + these values; the formula is unknown. A hero also gets a share of the gear's stats: 35 % at T1+0 up to 100 % at T3+15 (WM 0628, [[gameplay/classes-and-legions|Classes]] §5).

| stat1 (Attack?) | stat2 (Ability Power?) | HP | MP |
|---|---|---|---|
| 1,204 | 756 | 10,890 | 3,010 |

### Duration

An Innocence Crystal has **1,500 durability** and loses **5 per second** while transformed, so a full crystal gives **300 s** of hero form; it has no level limit (WM 1107, [[gameplay/events-and-schedules|Events and schedules]] §9). The client row's period column holds the same 1,500.

### Skills

`HeroData` skill1–10 (repeats dropped):

1. [[wiki/skills/20011-guardian-avenger|Guardian Avenger]]
2. [[wiki/skills/20013-guardian-avenger|Guardian Avenger]]
3. [[wiki/skills/20014-guardian-avenger|Guardian Avenger]]
4. [[wiki/skills/20015-guardian-avenger|Guardian Avenger]]
5. [[wiki/skills/20016-guardian-avenger|Guardian Avenger]]
6. [[wiki/skills/20017-guardian-avenger|Guardian Avenger]]

### Weapon base

The Innocence item's WeaponBase row 69: skills [[wiki/skills/20004-overcharge|Overcharge]], [[wiki/skills/20005-cut|Cut]], [[wiki/skills/20000-dark-knight-skull-passive|Dark Knight Skull Passive]], [[wiki/skills/20006-heaven-and-earth|Heaven and Earth]], [[wiki/skills/20007-sweep|Sweep]], [[wiki/skills/20008-scream-of-the-dead|Scream of the Dead]], [[wiki/skills/20012-aura-of-death|Aura of Death]], [[wiki/skills/20009-tomb-of-the-dead|Tomb of the Dead]].

### How to get it

- Craft [[wiki/items/8500-crystal-dark-knight-skull|Crystal : Dark knight Skull]] from [[wiki/items/9000-piece-dark-knight-skull|Piece : Dark knight Skull]] × 5, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50 ([[wiki/recipes/1201-crystal-dark-knight-skull-recipe|Crystal : Dark knight Skull recipe]])
- Innocence and pieces come from the Innocence gacha card ([[wiki/gacha/3-innocence-gacha|Innocence gacha]], [[gameplay/progression-and-economy|Progression]] §6).

### Monster with this name

[[wiki/monsters/673-dark-knight-skull|Dark Knight Skull]], [[wiki/monsters/809-dark-knight-skull|Dark Knight Skull]], [[wiki/monsters/1205-dark-knight-skull|Dark Knight Skull]], [[wiki/monsters/1504-dark-knight-skull|Dark Knight Skull]]

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

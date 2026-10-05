---
title: "King Deathhead (Crystal)"
type: "hero"
id: 57
status: "complete"
missing: []
sources: ["client: HeroData.cdb id 57", "client: Item_Base.cdb id 8506 (kind 18, option 201 = 57)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)"]
name_key: "HeroName_7"
stats: {"stat1": 1059, "stat2": 978, "hp": 8490, "mp": 2615}
skills: [20261, 20263, 20264, 20265, 20266, 20267, 20267, 20267, 20267, 20267]
transform_skill: 20299
base_hero: 7
trigger: {"item": 8506, "kind": "Innocence Crystal"}
weapon_base: 75
visual: 1006
cooldown_s: 120
durability: 1500
duration: {"durability": 1500, "drain_per_second": 5, "seconds": 300}
---
<!-- generated:start -->
<!-- generated-keys: title=2111c0 type=e44582 id=9109c8 sources=419370 name_key=9ab802 stats=01a740 skills=8fc2ba transform_skill=07a730 base_hero=902ba3 trigger=baa7e1 weapon_base=450dde visual=8554fe cooldown_s=775bc5 durability=7841fb duration=712893 -->
|  |  |
|---|---|
|  | ![King Deathhead (Crystal)](wiki/assets/heroes/57.png) |
| **Hero id** | `57` |
| **Unlocked by** | [[wiki/items/8506-crystal-king-deathhead\|Crystal : King Deathhead]] (Innocence Crystal, worn in the Innocence slot) |
| **Same form as** | [[wiki/heroes/7-king-deathhead\|King Deathhead]] |
| **Transform skill** | [[wiki/skills/20299-king-deathhead-transformation\|King Deathhead Transformation]] |
| **Level required** | none (WM 1107) |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 1,500 |
| **Visual** | CostumeDB row 1006 (WeaponBase 75 c14) |

### Description

> King Deathhead
>
> "You can use the power of the Death Head after you turn into Death Head Knight"

### Stats

`HeroData` columns. The decoder's names are guesses: `stat1` / `stat2` look like Attack / Ability Power (the mage heroes Amaterasu and Tempest Fisher have the higher `stat2` and more MP). In the [[gameplay/video-fort-war|fort-war video]] Dark Knight Skull raised max HP/MP from 7,282 / 1,660 to 16,214 / 3,645 (×2.2), which is not base + these values; the formula is unknown. A hero also gets a share of the gear's stats: 35 % at T1+0 up to 100 % at T3+15 (WM 0628, [[gameplay/classes-and-legions|Classes]] §5).

| stat1 (Attack?) | stat2 (Ability Power?) | HP | MP |
|---|---|---|---|
| 1,059 | 978 | 8,490 | 2,615 |

### Duration

An Innocence Crystal has **1,500 durability** and loses **5 per second** while transformed, so a full crystal gives **300 s** of hero form; it has no level limit (WM 1107, [[gameplay/events-and-schedules|Events and schedules]] §9). The client row's period column holds the same 1,500.

### Skills

`HeroData` skill1–10 (repeats dropped):

1. [[wiki/skills/20261-power-of-the-ax|Power of the ax]]
2. [[wiki/skills/20263-power-of-the-ax|Power of the ax]]
3. [[wiki/skills/20264-power-of-the-ax|Power of the ax]]
4. [[wiki/skills/20265-power-of-the-ax|Power of the ax]]
5. [[wiki/skills/20266-power-of-the-ax|Power of the ax]]
6. [[wiki/skills/20267-power-of-the-ax|Power of the ax]]

### Weapon base

The Innocence item's WeaponBase row 75: skills [[wiki/skills/20252-roar|Roar]], [[wiki/skills/20253-gallop|Gallop]], [[wiki/skills/20254-bloody-anger|Bloody anger]], [[wiki/skills/20255-immortality|Immortality]], [[wiki/skills/20256-blow|Blow]], [[wiki/skills/20257-cut|Cut]], [[wiki/skills/20258-quick-attack|Quick attack]], [[wiki/skills/20260-final-blow|Final blow]].

### How to get it

- Craft [[wiki/items/8506-crystal-king-deathhead|Crystal : King Deathhead]] from [[wiki/items/9006-piece-king-deathhead|Piece : King Deathhead]] × 5, [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 50 ([[wiki/recipes/1207-crystal-king-deathhead-recipe|Crystal : King Deathhead recipe]])
- Innocence and pieces come from the Innocence gacha card ([[wiki/gacha/3-innocence-gacha|Innocence gacha]], [[gameplay/progression-and-economy|Progression]] §6).

### Monster with this name

[[wiki/monsters/672-king-deathhead|King Deathhead]], [[wiki/monsters/1501-king-deathhead|King Deathhead]]

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

---
title: "Amaterasu (Crystal)"
type: "hero"
id: 53
status: "complete"
missing: []
sources: ["client: HeroData.cdb id 53", "client: Item_Base.cdb id 8502 (kind 18, option 201 = 53)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)"]
name_key: "HeroName_3"
stats: {"stat1": 819, "stat2": 1222, "hp": 5230, "mp": 6805}
skills: [20110, 20111, 20112, 20113, 20114, 20115, 20115, 20115, 20115, 20115]
transform_skill: 20149
base_hero: 3
trigger: {"item": 8502, "kind": "Innocence Crystal"}
weapon_base: 71
visual: 1002
cooldown_s: 120
durability: 1500
duration: {"durability": 1500, "drain_per_second": 5, "seconds": 300}
---
<!-- generated:start -->
<!-- generated-keys: title=eb7080 type=e44582 id=c5b76d sources=a12a2b name_key=0daa62 stats=fbf854 skills=2719a9 transform_skill=b9228b base_hero=77de68 trigger=59f5e5 weapon_base=d02560 visual=a5b1d7 cooldown_s=775bc5 durability=7841fb duration=712893 -->
|  |  |
|---|---|
|  | ![Amaterasu (Crystal)](wiki/assets/heroes/53.png) |
| **Hero id** | `53` |
| **Unlocked by** | [[wiki/items/8502-crystal-amaterasu\|Crystal : Amaterasu]] (Innocence Crystal, worn in the Innocence slot) |
| **Same form as** | [[wiki/heroes/3-amaterasu\|Amaterasu]] |
| **Transform skill** | [[wiki/skills/20149-amaterasu-transformation\|Amaterasu Transformation]] |
| **Level required** | none (WM 1107) |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 1,500 |
| **Visual** | CostumeDB row 1002 (WeaponBase 71 c14) |

### Description

> Sun Amaterasu
>
> "You can use the power of the sun after you turn into Amaterasu"

### Stats

`HeroData` columns. The decoder's names are guesses: `stat1` / `stat2` look like Attack / Ability Power (the mage heroes Amaterasu and Tempest Fisher have the higher `stat2` and more MP). In the [[gameplay/video-fort-war|fort-war video]] Dark Knight Skull raised max HP/MP from 7,282 / 1,660 to 16,214 / 3,645 (×2.2), which is not base + these values; the formula is unknown. A hero also gets a share of the gear's stats: 35 % at T1+0 up to 100 % at T3+15 (WM 0628, [[gameplay/classes-and-legions|Classes]] §5).

| stat1 (Attack?) | stat2 (Ability Power?) | HP | MP |
|---|---|---|---|
| 819 | 1,222 | 5,230 | 6,805 |

### Duration

An Innocence Crystal has **1,500 durability** and loses **5 per second** while transformed, so a full crystal gives **300 s** of hero form; it has no level limit (WM 1107, [[gameplay/events-and-schedules|Events and schedules]] §9). The client row's period column holds the same 1,500.

### Skills

`HeroData` skill1–10 (repeats dropped):

1. [[wiki/skills/20110-the-nucleus-of-the-sun|The nucleus of the sun]]
2. [[wiki/skills/20111-the-nucleus-of-the-sun|The nucleus of the sun]]
3. [[wiki/skills/20112-the-nucleus-of-the-sun|The nucleus of the sun]]
4. [[wiki/skills/20113-the-nucleus-of-the-sun|The nucleus of the sun]]
5. [[wiki/skills/20114-the-nucleus-of-the-sun|The nucleus of the sun]]
6. [[wiki/skills/20115-the-nucleus-of-the-sun|The nucleus of the sun]]

### Weapon base

The Innocence item's WeaponBase row 71: skills [[wiki/skills/20102-explosion|Explosion]], [[wiki/skills/20103-snow-of-the-sun|Snow of the Sun]], [[wiki/skills/20104-two-suns-kra-tura|Two suns (Kra, Tura)]], [[wiki/skills/20105-a-warm-flame|A warm flame]], [[wiki/skills/20106-flame-pillar|Flame pillar]], [[wiki/skills/20107-the-source-of-the-sun|The source of the sun]], [[wiki/skills/20108-shield-of-the-sun|Shield of the Sun]], [[wiki/skills/20109-the-flame-of-the-sun|The Flame of the Sun]].

### How to get it

- Craft [[wiki/items/8502-crystal-amaterasu|Crystal : Amaterasu]] from [[wiki/items/9002-piece-amaterasu|Piece : Amaterasu]] × 5, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 50 ([[wiki/recipes/1203-crystal-amaterasu-recipe|Crystal : Amaterasu recipe]])
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

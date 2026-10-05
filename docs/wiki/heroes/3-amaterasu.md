---
title: "Amaterasu"
type: "hero"
id: 3
status: "stub"
missing: ["duration"]
sources: ["client: HeroData.cdb id 3", "client: Item_Base.cdb id 8002 (kind 18, option 201 = 3)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)", "docs: [[gameplay/classes-and-legions]] §1 (hero only at level 30, guides); client string Item_Hero_LevelLimit30"]
name_key: "HeroName_3"
stats: {"stat1": 819, "stat2": 1222, "hp": 5230, "mp": 6805}
skills: [20110, 20111, 20112, 20113, 20114, 20115, 20115, 20115, 20115, 20115]
transform_skill: 20101
trigger: {"item": 8002, "kind": "Innocence"}
weapon_base: 71
visual: 1002
cooldown_s: 120
durability: 240
level_required: 30
---
<!-- generated:start -->
<!-- generated-keys: title=3e70ae type=e44582 id=77de68 sources=39ca5b name_key=0daa62 stats=fbf854 skills=2719a9 transform_skill=007e0d trigger=41d1ff weapon_base=d02560 visual=a5b1d7 cooldown_s=775bc5 durability=cae91e level_required=22d200 -->
|  |  |
|---|---|
|  | ![Amaterasu](wiki/assets/heroes/3.png) |
| **Hero id** | `3` |
| **Unlocked by** | [[wiki/items/8002-amaterasu\|Amaterasu]] (Innocence, worn in the Innocence slot) |
| **Crystal version** | [[wiki/heroes/53-amaterasu-crystal\|Amaterasu (Crystal)]] |
| **Transform skill** | [[wiki/skills/20101-amaterasu-transformation\|Amaterasu Transformation]] |
| **Level required** | 30 |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 240 |
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

Innocence durability was raised from 24 to **240** (WM 0402, [[gameplay/events-and-schedules|Events and schedules]] §9); how fast it drains while transformed is not known, so the duration is still open. In the fort-war video a Dark Knight Skull form lasted **at least 8.5 minutes** ([[gameplay/video-fort-war|video]]).

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

- Craft [[wiki/items/8002-amaterasu|Amaterasu]] from [[wiki/items/9002-piece-amaterasu|Piece : Amaterasu]] × 100, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 200 ([[wiki/recipes/1503-amaterasu-recipe|Amaterasu recipe]])
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

---
title: "Sarasvati"
type: "hero"
id: 4
status: "stub"
missing: ["duration"]
sources: ["client: HeroData.cdb id 4", "client: Item_Base.cdb id 8003 (kind 18, option 201 = 4)", "docs: [[gameplay/events-and-schedules]] §9 (WM 0402 hero durability 24 → 240; WM 0621 transformation cooldown 120 s; WM 1107 Innocence Crystal durability 1,500, −5 per second transformed, no level limit)", "docs: [[gameplay/classes-and-legions]] §1 (hero only at level 30, guides); client string Item_Hero_LevelLimit30"]
name_key: "HeroName_4"
stats: {"stat1": 1063, "stat2": 978, "hp": 8864, "mp": 3754}
skills: [20162, 20163, 20164, 20165, 20166, 20167, 20167, 20167, 20167, 20167]
transform_skill: 20151
trigger: {"item": 8003, "kind": "Innocence"}
weapon_base: 72
visual: 1003
cooldown_s: 120
durability: 240
level_required: 30
---
<!-- generated:start -->
<!-- generated-keys: title=400bd0 type=e44582 id=1b6453 sources=f58507 name_key=fc9c05 stats=3fa987 skills=bee47c transform_skill=571985 trigger=670b15 weapon_base=c09763 visual=9f6bf8 cooldown_s=775bc5 durability=cae91e level_required=22d200 -->
|  |  |
|---|---|
|  | ![Sarasvati](wiki/assets/heroes/4.png) |
| **Hero id** | `4` |
| **Unlocked by** | [[wiki/items/8003-sarasvati\|Sarasvati]] (Innocence, worn in the Innocence slot) |
| **Crystal version** | [[wiki/heroes/54-sarasvati-crystal\|Sarasvati (Crystal)]] |
| **Transform skill** | [[wiki/skills/20151-sarasbati-transformation\|Sarasbati Transformation]] |
| **Level required** | 30 |
| **Cooldown** | 120 s after transforming back (WM 0621) |
| **Durability** | 240 |
| **Visual** | CostumeDB row 1003 (WeaponBase 72 c14) |

### Description

> The goddess of water Sarasbati
>
> You can use the power of the water after you turn into a Sarasbati.

### Stats

`HeroData` columns. The decoder's names are guesses: `stat1` / `stat2` look like Attack / Ability Power (the mage heroes Amaterasu and Tempest Fisher have the higher `stat2` and more MP). In the [[gameplay/video-fort-war|fort-war video]] Dark Knight Skull raised max HP/MP from 7,282 / 1,660 to 16,214 / 3,645 (×2.2), which is not base + these values; the formula is unknown. A hero also gets a share of the gear's stats: 35 % at T1+0 up to 100 % at T3+15 (WM 0628, [[gameplay/classes-and-legions|Classes]] §5).

| stat1 (Attack?) | stat2 (Ability Power?) | HP | MP |
|---|---|---|---|
| 1,063 | 978 | 8,864 | 3,754 |

### Duration

Innocence durability was raised from 24 to **240** (WM 0402, [[gameplay/events-and-schedules|Events and schedules]] §9); how fast it drains while transformed is not known, so the duration is still open. In the fort-war video a Dark Knight Skull form lasted **at least 8.5 minutes** ([[gameplay/video-fort-war|video]]).

### Skills

`HeroData` skill1–10 (repeats dropped):

1. [[wiki/skills/20162-the-person-who-selected-water|The person who selected water]]
2. [[wiki/skills/20163-the-person-who-selected-water|The person who selected water]]
3. [[wiki/skills/20164-the-person-who-selected-water|The person who selected water]]
4. [[wiki/skills/20165-the-person-who-selected-water|The person who selected water]]
5. [[wiki/skills/20166-the-person-who-selected-water|The person who selected water]]
6. [[wiki/skills/20167-the-person-who-selected-water|The person who selected water]]

### Weapon base

The Innocence item's WeaponBase row 72: skills [[wiki/skills/20152-aim-of-water|Aim of water]], [[wiki/skills/20153-water-shield|Water shield]], [[wiki/skills/20154-puddle|Puddle]], [[wiki/skills/20156-blessing-of-water|Blessing of water]], [[wiki/skills/20157-water-strike|Water strike]], [[wiki/skills/20158-blow-of-water|Blow of water]], [[wiki/skills/20160-goddess|Goddess]], [[wiki/skills/20161-wave-of-water|Wave of water]].

### How to get it

- Craft [[wiki/items/8003-sarasvati|Sarasvati]] from [[wiki/items/9003-piece-sarasvati|Piece : Sarasvati]] × 100, [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]] × 200 ([[wiki/recipes/1504-sarasvati-recipe|Sarasvati recipe]])
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

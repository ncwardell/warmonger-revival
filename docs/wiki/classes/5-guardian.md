---
title: "Guardian"
type: "class"
id: 5
status: "stub"
missing: ["base_stats"]
sources: ["client: Create_Char.cdb row 5", "client strings: GUI_CharCreate_Comment_Gardian, Item_ReqClass_16", "docs: [[gameplay/video-character-creation-and-tutorial]] §2 (HP 450 / MP 700 at level 1, 530/725 at 2, 610/750 at 3, no gear: +80 HP / +25 MP per level; video 2:45)", "docs: [[gameplay/classes-and-legions]] §5 (WM 0420: Magic Resist per level)"]
class_mask: 16
unit_id: 5
offered: true
starting_weapons:
  - {"item": 20001, "label": "Mace", "weapon_base": 43, "skills": [5036, 5038, 5040, 5041]}
  - {"item": 20021, "label": "Cannon", "weapon_base": 63, "skills": [5107, 5109, 5110, 5111]}
  - {"item": 20003, "weapon_base": 45, "skills": [5067, 5068, 5069, 5070]}
equippable: {"weapons": 30, "costumes": 23, "armour": 74, "accessories": 446}
portraits: 13
base_hp: 450
base_mp: 700
hp_per_level: 80
mp_per_level: 25
mr_per_level: 6
---
<!-- generated:start -->
<!-- generated-keys: title=1817f8 type=22feea id=ac3478 sources=82b6ea class_mask=1574bd unit_id=ac3478 offered=5ffe53 starting_weapons=e37d19 equippable=3c3078 portraits=bd307a base_hp=d96adb base_mp=d8e4bb hp_per_level=b888b2 mp_per_level=f6e112 mr_per_level=c1dfd9 -->
|  |  |
|---|---|
|  | ![Guardian](wiki/assets/classes/5.png) |
| **Unit id** | `5` (`UnitDB`: Warrior (Male)) |
| **Class mask** | `16` (`Item_Base` req_class bit) |
| **Offered at creation** | yes |
| **HP at level 1** | 450 |
| **MP at level 1** | 700 |
| **HP per level** | 80 |
| **MP per level** | 25 |
| **Magic Resist per level** | 6 |

### Description

> The Guardian's main weapons consist of maces
> and cannons. They are the frontline, the first
> to enter a battle and usually the last ones
> standing. 
>
>  [Difficulty : Middle]

### Starting weapons

Chosen at character creation (`Create_Char` weapon1–4). The weapon decides the skills: its `WeaponBase` row gives 4 normal skills (Q/W/E/R) and 4 hero-form skills.

|  | weapon | label | WeaponBase | skills (Q/W/E/R) | hero skills |
|---|---|---|---|---|---|
| ![](wiki/assets/items/20001.png) | [[wiki/items/20001-magical-demolition-hammer\|Magical Demolition Hammer]] | Mace | 43 | [[wiki/skills/5036-soul-infestation\|Soul Infestation]], [[wiki/skills/5038-aura-of-demise\|Aura of Demise]], [[wiki/skills/5040-severe-blow\|Severe Blow]], [[wiki/skills/5041-dark-transformation\|Dark Transformation]] | – |
| ![](wiki/assets/items/20021.png) | [[wiki/items/20021-magical-protect-cannon\|Magical Protect Cannon]] | Cannon | 63 | [[wiki/skills/5107-nimble-pursuit\|Nimble Pursuit]], [[wiki/skills/5109-firm-hand\|Firm Hand]], [[wiki/skills/5110-buckshot\|Buckshot]], [[wiki/skills/5111-explosive-mortar\|Explosive Mortar]] | – |
| ![](wiki/assets/items/20003.png) | [[wiki/items/20003-magical-crush-hammer\|Magical Crush Hammer]] | – | 45 | [[wiki/skills/5067-crushing-blow\|Crushing Blow]], [[wiki/skills/5068-head-butt\|Head Butt]], [[wiki/skills/5069-howl-of-victory\|Howl of Victory]], [[wiki/skills/5070-unyielding-will\|Unyielding Will]] | – |

### Equipment

From each item's class mask (`Item_Base` req_class@33): weapons and costumes are made per class, armour and accessories fit every class.

| what | items | list |
|---|---|---|
| Weapons | 30 | [[wiki/items/weapons-guardian\|Guardian weapons]] |
| Armour | 74 | [[wiki/items/armor-helmet\|helmets]], [[wiki/items/armor-body\|body armour]], [[wiki/items/armor-gloves\|gloves]], [[wiki/items/armor-shoes\|shoes]] |
| Accessories and runes | 446 | [[wiki/items/accessories\|accessories]], [[wiki/items/runes\|runes]] |
| Costumes | 23 | [[wiki/costumes/index\|costume sets]] |

All Guardian weapons: [[wiki/items/20001-magical-demolition-hammer|Magical Demolition Hammer]], [[wiki/items/20002-magical-dash-hammer|Magical Dash Hammer]], [[wiki/items/20003-magical-crush-hammer|Magical Crush Hammer]], [[wiki/items/20004-skeleton-king-s-magic-hammer|Skeleton King's Magic Hammer]], [[wiki/items/20005-d-knuckler-01|D-KnuckleR-01]], [[wiki/items/20006-d-knuckler-02|D-KnuckleR-02]], [[wiki/items/20007-d-knuckler-03|D-KnuckleR-03]], [[wiki/items/20008-d-knuckler-04|D-KnuckleR-04]], [[wiki/items/20009-d-knuckler-05|D-KnuckleR-05]], [[wiki/items/20011-magical-blast-cannon|Magical Blast Cannon]], [[wiki/items/20012-d-cannon-03|D-Cannon-03]], [[wiki/items/20013-d-cannon-04|D-Cannon-04]], [[wiki/items/20014-skeleton-king-s-magic-cannon|Skeleton King's Magic Cannon]], [[wiki/items/20015-magical-protect-mace|Magical Protect Mace]], [[wiki/items/20016-d-maceshd-02|D-MaceShd-02]], [[wiki/items/20017-d-maceshd-03|D-MaceShd-03]], [[wiki/items/20018-d-maceshd-04|D-MaceShd-04]], [[wiki/items/20019-d-maceshd-05|D-MaceShd-05]], [[wiki/items/20020-magical-protect-hammer|Magical Protect Hammer]], [[wiki/items/20021-magical-protect-cannon|Magical Protect Cannon]], [[wiki/items/21001-magical-demolition-hammer|Magical Demolition Hammer]], [[wiki/items/21002-magical-dash-hammer|Magical Dash Hammer]], [[wiki/items/21003-magical-crush-hammer|Magical Crush Hammer]], [[wiki/items/21011-magical-blast-cannon|Magical Blast Cannon]], [[wiki/items/21015-magical-protect-mace|Magical Protect Mace]], [[wiki/items/21020-magical-protect-hammer|Magical Protect Hammer]], [[wiki/items/21021-magical-protect-cannon|Magical Protect Cannon]], [[wiki/items/40003-magical-crush-hammer|Magical Crush Hammer]], [[wiki/items/40014-skeleton-king-s-magic-cannon|Skeleton King's Magic Cannon]], [[wiki/items/64999-magical-protect-cannon|Magical Protect Cannon]].

### HP, MP and stats

- At level 1 the Guardian has **450 HP / 700 MP**, at level 2 530/725 and at level 3 610/750, with no gear: **+80 HP and +25 MP per level** ([[gameplay/video-character-creation-and-tutorial|character creation video]] §2, 2:45). *video*
- Magic Resist per level: **+6** (the patch note says 150 at level 30) — WM 0420 ([[gameplay/classes-and-legions|Classes]] §5). *notes*
- `base_stats` (the six radar stats on the creation screen: Attack, Ability Power, Magic Resist, Movement Speed, Attack Speed, Armor) are not in the client; the creation screen shows them only as a chart (`CreatChar.Chart_02`).

### Level table

`Level_Table` is shared by every class: `exp` is the total exp that ends the level; the `hp?`/`mp?`/`atk?`/`def?` columns grow linearly (+30 HP, +20 MP per level) but are not read by any client code found and do not match the observed Guardian values (+80 / +25), so they are not used as class growth.

| level | exp | hp? | mp? | atk? | def? |
|---|---|---|---|---|---|
| 1 | 700 | 130 | 70 | 2 | 1 |
| 2 | 1,680 | 160 | 90 | 3 | 1 |
| 3 | 3,052 | 190 | 110 | 3 | 2 |
| 4 | 4,972 | 220 | 130 | 4 | 2 |
| 5 | 7,661 | 250 | 150 | 5 | 3 |
| 6 | 11,425 | 280 | 170 | 5 | 3 |
| 7 | 16,695 | 310 | 190 | 6 | 3 |
| 8 | 24,073 | 340 | 210 | 6 | 4 |
| 9 | 34,403 | 370 | 230 | 7 | 4 |
| 10 | 48,865 | 400 | 250 | 8 | 5 |
| 11 | 69,112 | 430 | 270 | 8 | 5 |
| 12 | 97,458 | 460 | 290 | 9 | 5 |
| 13 | 137,143 | 490 | 310 | 9 | 6 |
| 14 | 192,703 | 520 | 330 | 10 | 6 |
| 15 | 270,487 | 550 | 350 | 11 | 7 |
| 16 | 379,384 | 580 | 370 | 11 | 7 |
| 17 | 531,840 | 610 | 390 | 12 | 7 |
| 18 | 745,279 | 640 | 410 | 12 | 8 |
| 19 | 1,044,094 | 670 | 430 | 13 | 8 |
| 20 | 1,462,435 | 700 | 450 | 14 | 9 |
| 21 | 2,048,112 | 730 | 470 | 14 | 9 |
| 22 | 2,868,060 | 760 | 490 | 15 | 9 |
| 23 | 4,015,988 | 790 | 510 | 15 | 10 |
| 24 | 5,623,087 | 820 | 530 | 16 | 10 |
| 25 | 7,873,026 | 850 | 550 | 17 | 11 |
| 26 | 11,022,941 | 880 | 570 | 17 | 11 |
| 27 | 15,432,822 | 910 | 590 | 18 | 11 |
| 28 | 21,606,656 | 940 | 610 | 18 | 12 |
| 29 | 30,250,024 | 970 | 630 | 19 | 12 |
| 30 | 42,350,740 | 1000 | 650 | 20 | 13 |

### Masteries

Character mastery tree (`Mastery`): [[wiki/masteries/501-guardian-mastery-1|Guardian mastery 1]], [[wiki/masteries/502-guardian-mastery-2|Guardian mastery 2]], [[wiki/masteries/503-guardian-mastery-3|Guardian mastery 3]], [[wiki/masteries/504-guardian-mastery-4|Guardian mastery 4]], [[wiki/masteries/505-guardian-mastery-5|Guardian mastery 5]], [[wiki/masteries/506-guardian-mastery-6|Guardian mastery 6]], [[wiki/masteries/507-guardian-mastery-7|Guardian mastery 7]], [[wiki/masteries/508-guardian-mastery-8|Guardian mastery 8]], [[wiki/masteries/509-guardian-mastery-9|Guardian mastery 9]], [[wiki/masteries/510-guardian-mastery-10|Guardian mastery 10]], [[wiki/masteries/511-guardian-mastery-11|Guardian mastery 11]], [[wiki/masteries/512-guardian-mastery-12|Guardian mastery 12]], [[wiki/masteries/513-guardian-mastery-13|Guardian mastery 13]], [[wiki/masteries/515-guardian-mastery-15|Guardian mastery 15]], [[wiki/masteries/516-guardian-mastery-16|Guardian mastery 16]], [[wiki/masteries/517-guardian-mastery-17|Guardian mastery 17]], [[wiki/masteries/518-guardian-mastery-18|Guardian mastery 18]], [[wiki/masteries/519-guardian-mastery-19|Guardian mastery 19]], [[wiki/masteries/520-guardian-mastery-20|Guardian mastery 20]], [[wiki/masteries/521-guardian-mastery-21|Guardian mastery 21]], [[wiki/masteries/522-guardian-mastery-22|Guardian mastery 22]], [[wiki/masteries/523-guardian-mastery-23|Guardian mastery 23]], [[wiki/masteries/524-guardian-mastery-24|Guardian mastery 24]], [[wiki/masteries/525-guardian-mastery-25|Guardian mastery 25]], [[wiki/masteries/526-guardian-mastery-26|Guardian mastery 26]], [[wiki/masteries/527-guardian-mastery-27|Guardian mastery 27]].

Hero forms: see [[wiki/heroes/index|Heroes]] (any class can transform at level 30).
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

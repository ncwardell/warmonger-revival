---
title: "Saint"
type: "class"
id: 1
status: "stub"
missing: ["base_hp", "base_mp", "hp_per_level", "mp_per_level", "base_stats"]
sources: ["client: Create_Char.cdb row 1", "client strings: GUI_CharCreate_Comment_Saint, Item_ReqClass_1", "docs: [[gameplay/classes-and-legions]] §5 (WM 0420: Magic Resist per level)"]
class_mask: 1
unit_id: 1
offered: true
starting_weapons:
  - {"item": 10017, "label": "Flying Blade", "weapon_base": 18, "skills": [5022, 5023, 5024, 5025]}
  - {"item": 10011, "label": "Dual Gun", "weapon_base": 12, "skills": [5102, 5103, 5104, 5105]}
  - {"item": 10001, "label": "Wand", "weapon_base": 2, "skills": [5004, 5005, 5006, 5007]}
  - {"item": 10002, "weapon_base": 64, "skills": [5277, 5279, 5280, 5281]}
equippable: {"weapons": 29, "costumes": 23, "armour": 74, "accessories": 446}
portraits: 13
mr_per_level: 4
---
<!-- generated:start -->
<!-- generated-keys: title=52e8c4 type=22feea id=356a19 sources=8ac654 class_mask=356a19 unit_id=356a19 offered=5ffe53 starting_weapons=696f70 equippable=5162e0 portraits=bd307a mr_per_level=1b6453 -->
|  |  |
|---|---|
|  | ![Saint](wiki/assets/classes/1.png) |
| **Unit id** | `1` (`UnitDB`: Magician (Female)) |
| **Class mask** | `1` (`Item_Base` req_class bit) |
| **Offered at creation** | yes |
| **Magic Resist per level** | 4 |

### Description

> The Saint's main weapons consist of
> Flying Blades,Dual Guns and Wands.
> Their strength lies in supporting allies and
> yielding powerful magic against
> their enemies.
>
>  [Difficulty : High]

### Starting weapons

Chosen at character creation (`Create_Char` weapon1–4). The weapon decides the skills: its `WeaponBase` row gives 4 normal skills (Q/W/E/R) and 4 hero-form skills.

|  | weapon | label | WeaponBase | skills (Q/W/E/R) | hero skills |
|---|---|---|---|---|---|
| ![](wiki/assets/items/10017.png) | [[wiki/items/10017-magical-wrath-blade\|Magical Wrath Blade]] | Flying Blade | 18 | [[wiki/skills/5022-blade-storm\|Blade storm]], [[wiki/skills/5023-wings-of-fair-wind\|Wings of fair wind]], [[wiki/skills/5024-blink-like-wind\|Blink like wind]], [[wiki/skills/5025-wrath-of-the-west\|Wrath of the West]] | – |
| ![](wiki/assets/items/10011.png) | [[wiki/items/10011-magical-adapted-dual-gun\|Magical adapted Dual Gun]] | Dual Gun | 12 | [[wiki/skills/5102-ankle-aim\|Ankle Aim]], [[wiki/skills/5103-rapid-reload\|Rapid Reload]], [[wiki/skills/5104-entangling-bullet\|Entangling Bullet]], [[wiki/skills/5105-suppressing-fire\|Suppressing Fire]] | – |
| ![](wiki/assets/items/10001.png) | [[wiki/items/10001-magical-thunder-wand\|Magical Thunder Wand]] | Wand | 2 | [[wiki/skills/5004-thunderbolt\|Thunderbolt]], [[wiki/skills/5005-lightning-strike\|Lightning Strike]], [[wiki/skills/5006-ball-of-lighting\|Ball of Lighting]], [[wiki/skills/5007-might-of-thunder-god\|Might of Thunder God]] | – |
| ![](wiki/assets/items/10002.png) | [[wiki/items/10002-magical-life-wand\|Magical Life Wand]] | – | 64 | [[wiki/skills/5277-mother-nature-s-blessing\|Mother Nature's Blessing]], [[wiki/skills/5279-blessing-of-light\|Blessing of Light]], [[wiki/skills/5280-essential-blessing\|Essential Blessing]], [[wiki/skills/5281-savior-s-gift\|Savior's Gift]] | – |

### Equipment

From each item's class mask (`Item_Base` req_class@33): weapons and costumes are made per class, armour and accessories fit every class.

| what | items | list |
|---|---|---|
| Weapons | 29 | [[wiki/items/weapons-saint\|Saint weapons]] |
| Armour | 74 | [[wiki/items/armor-helmet\|helmets]], [[wiki/items/armor-body\|body armour]], [[wiki/items/armor-gloves\|gloves]], [[wiki/items/armor-shoes\|shoes]] |
| Accessories and runes | 446 | [[wiki/items/accessories\|accessories]], [[wiki/items/runes\|runes]] |
| Costumes | 23 | [[wiki/costumes/index\|costume sets]] |

All Saint weapons: [[wiki/items/10000-magical-storm-wand|Magical Storm Wand]], [[wiki/items/10001-magical-thunder-wand|Magical Thunder Wand]], [[wiki/items/10002-magical-life-wand|Magical Life Wand]], [[wiki/items/10003-magical-cystal-wand|Magical Cystal Wand]], [[wiki/items/10004-tempest-s-magical-wand|Tempest's magical wand]], [[wiki/items/10005-magical-blade-shield-flame|Magical Blade Shield : Flame]], [[wiki/items/10006-e-swordshd-02|E-SwordShd-02]], [[wiki/items/10007-e-swordshd-03|E-SwordShd-03]], [[wiki/items/10008-e-swordshd-04|E-SwordShd-04]], [[wiki/items/10009-e-swordshd-05|E-SwordShd-05]], [[wiki/items/10011-magical-adapted-dual-gun|Magical adapted Dual Gun]], [[wiki/items/10012-e-gun-03|E-Gun-03]], [[wiki/items/10013-e-gun-04|E-Gun-04]], [[wiki/items/10014-skeleton-king-s-magic-gun|Skeleton king's Magic Gun]], [[wiki/items/10015-magical-dash-blade|Magical Dash Blade]], [[wiki/items/10017-magical-wrath-blade|Magical Wrath Blade]], [[wiki/items/10018-e-knife-04|E-Knife-04]], [[wiki/items/10019-e-knife-05|E-Knife-05]], [[wiki/items/10020-magical-devil-wand|Magical Devil Wand]], [[wiki/items/11000-magical-storm-wand|Magical Storm Wand]], [[wiki/items/11001-magical-thunder-wand|Magical Thunder Wand]], [[wiki/items/11002-magical-life-wand|Magical Life Wand]], [[wiki/items/11003-magical-cystal-wand|Magical Cystal Wand]], [[wiki/items/11011-magical-adapted-dual-gun|Magical adapted Dual Gun]], [[wiki/items/11015-magical-dash-blade|Magical Dash Blade]], [[wiki/items/11017-magical-wrath-blade|Magical Wrath Blade]], [[wiki/items/11020-magical-devil-wand|Magical Devil Wand]], [[wiki/items/30002-magical-life-wand|Magical Life Wand]], [[wiki/items/30020-magical-devil-wand|Magical Devil Wand]].

### HP, MP and stats

- Base HP/MP not observed yet (no Saint video at low level).
- Magic Resist per level: **+4** (the patch note says 120 at level 30) — WM 0420 ([[gameplay/classes-and-legions|Classes]] §5). *notes*
- `base_stats` (the six radar stats on the creation screen: Attack, Ability Power, Magic Resist, Movement Speed, Attack Speed, Armor) are not in the client; the creation screen shows them only as a chart (`CreatChar.Chart_03`).

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

Character mastery tree (`Mastery`): [[wiki/masteries/101-saint-mastery-1|Saint mastery 1]], [[wiki/masteries/102-saint-mastery-2|Saint mastery 2]], [[wiki/masteries/103-saint-mastery-3|Saint mastery 3]], [[wiki/masteries/104-saint-mastery-4|Saint mastery 4]], [[wiki/masteries/105-saint-mastery-5|Saint mastery 5]], [[wiki/masteries/106-saint-mastery-6|Saint mastery 6]], [[wiki/masteries/107-saint-mastery-7|Saint mastery 7]], [[wiki/masteries/108-saint-mastery-8|Saint mastery 8]], [[wiki/masteries/109-saint-mastery-9|Saint mastery 9]], [[wiki/masteries/110-saint-mastery-10|Saint mastery 10]], [[wiki/masteries/111-saint-mastery-11|Saint mastery 11]], [[wiki/masteries/112-saint-mastery-12|Saint mastery 12]], [[wiki/masteries/113-saint-mastery-13|Saint mastery 13]], [[wiki/masteries/115-saint-mastery-15|Saint mastery 15]], [[wiki/masteries/116-saint-mastery-16|Saint mastery 16]], [[wiki/masteries/117-saint-mastery-17|Saint mastery 17]], [[wiki/masteries/118-saint-mastery-18|Saint mastery 18]], [[wiki/masteries/119-saint-mastery-19|Saint mastery 19]], [[wiki/masteries/120-saint-mastery-20|Saint mastery 20]], [[wiki/masteries/121-saint-mastery-21|Saint mastery 21]], [[wiki/masteries/122-saint-mastery-22|Saint mastery 22]], [[wiki/masteries/123-saint-mastery-23|Saint mastery 23]], [[wiki/masteries/124-saint-mastery-24|Saint mastery 24]], [[wiki/masteries/125-saint-mastery-25|Saint mastery 25]], [[wiki/masteries/126-saint-mastery-26|Saint mastery 26]], [[wiki/masteries/127-saint-mastery-27|Saint mastery 27]].

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

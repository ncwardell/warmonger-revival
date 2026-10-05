---
title: "Punisher"
type: "class"
id: 4
status: "stub"
missing: ["base_hp", "base_mp", "hp_per_level", "mp_per_level", "base_stats"]
sources: ["client: Create_Char.cdb row 4", "client strings: GUI_CharCreate_Comment_Punisher, Item_ReqClass_2", "docs: [[gameplay/classes-and-legions]] §5 (WM 0420: Magic Resist per level)", "docs: [[gameplay/video-early-quests]] (Punisher HUD HP/MP with starting and quest gear: Lv 1 420/424, Lv 3 560/472, Lv 7 970/568, Lv 20 3240–3260/1000)"]
class_mask: 2
unit_id: 4
offered: true
starting_weapons:
  - {"item": 15007, "label": "Dagger", "weapon_base": 29, "skills": [5026, 5027, 5028, 5029]}
  - {"item": 15004, "label": "Bow", "weapon_base": 26, "skills": [5112, 5113, 5114, 5115]}
equippable: {"weapons": 28, "costumes": 24, "armour": 74, "accessories": 446}
portraits: 13
mr_per_level: 3
---
<!-- generated:start -->
<!-- generated-keys: title=757b87 type=22feea id=1b6453 sources=bcc8fc class_mask=da4b92 unit_id=1b6453 offered=5ffe53 starting_weapons=0f35cf equippable=e50a7c portraits=bd307a mr_per_level=77de68 -->
|  |  |
|---|---|
|  | ![Punisher](wiki/assets/classes/4.png) |
| **Unit id** | `4` (`UnitDB`: Assasisn (Male)) |
| **Class mask** | `2` (`Item_Base` req_class bit) |
| **Offered at creation** | yes |
| **Magic Resist per level** | 3 |

### Description

> The Punisher's main weapons consist of
> Daggers and Bows. They're able to control
> the battlefield, attacking from a long distance
> or assassinating key targets with deadly close
> range attacks.
>
>  [Difficulty : Low]

### Starting weapons

Chosen at character creation (`Create_Char` weapon1–4). The weapon decides the skills: its `WeaponBase` row gives 4 normal skills (Q/W/E/R) and 4 hero-form skills.

|  | weapon | label | WeaponBase | skills (Q/W/E/R) | hero skills |
|---|---|---|---|---|---|
| ![](wiki/assets/items/15007.png) | [[wiki/items/15007-magical-judge-dagger\|Magical judge Dagger]] | Dagger | 29 | [[wiki/skills/5026-shadow-hurl\|Shadow Hurl]], [[wiki/skills/5027-shadow-walk\|Shadow Walk]], [[wiki/skills/5028-poisonous-swamp\|Poisonous Swamp]], [[wiki/skills/5029-the-dark-art\|The Dark Art]] | – |
| ![](wiki/assets/items/15004.png) | [[wiki/items/15004-magical-frost-bow\|Magical Frost Bow]] | Bow | 26 | [[wiki/skills/5112-sharp-edges\|Sharp Edges]], [[wiki/skills/5113-potential-power\|Potential Power]], [[wiki/skills/5114-hail-of-arrows\|Hail of Arrows]], [[wiki/skills/5115-spinning-whirlwind\|Spinning Whirlwind]] | – |

### Equipment

From each item's class mask (`Item_Base` req_class@33): weapons and costumes are made per class, armour and accessories fit every class.

| what | items | list |
|---|---|---|
| Weapons | 28 | [[wiki/items/weapons-punisher\|Punisher weapons]] |
| Armour | 74 | [[wiki/items/armor-helmet\|helmets]], [[wiki/items/armor-body\|body armour]], [[wiki/items/armor-gloves\|gloves]], [[wiki/items/armor-shoes\|shoes]] |
| Accessories and runes | 446 | [[wiki/items/accessories\|accessories]], [[wiki/items/runes\|runes]] |
| Costumes | 24 | [[wiki/costumes/index\|costume sets]] |

All Punisher weapons: [[wiki/items/15000-magical-shadow-bow|Magical Shadow Bow]], [[wiki/items/15001-magical-sniping-bow|Magical Sniping Bow]], [[wiki/items/15002-magical-vision-bow|Magical Vision Bow]], [[wiki/items/15004-magical-frost-bow|Magical Frost Bow]], [[wiki/items/15005-skeleton-king-s-vision-bow|Skeleton king's Vision Bow]], [[wiki/items/15006-magical-blood-dagger|Magical Blood Dagger]], [[wiki/items/15007-magical-judge-dagger|Magical judge Dagger]], [[wiki/items/15008-magical-hiding-dagger|Magical hiding Dagger]], [[wiki/items/15009-skeleton-king-s-magic-dagger|Skeleton King's Magic Dagger]], [[wiki/items/15010-m-polearm-01|M-Polearm-01]], [[wiki/items/15011-m-polearm-02|M-Polearm-02]], [[wiki/items/15012-m-polearm-03|M-Polearm-03]], [[wiki/items/15013-m-polearm-04|M-Polearm-04]], [[wiki/items/15014-m-polearm-05|M-Polearm-05]], [[wiki/items/15015-m-sword-01|M-Sword-01]], [[wiki/items/15016-m-sword-02|M-Sword-02]], [[wiki/items/15017-m-sword-03|M-Sword-03]], [[wiki/items/15018-m-sword-04|M-Sword-04]], [[wiki/items/15019-m-sword-05|M-Sword-05]], [[wiki/items/16000-magical-shadow-bow|Magical Shadow Bow]], [[wiki/items/16001-magical-sniping-bow|Magical Sniping Bow]], [[wiki/items/16002-magical-vision-bow|Magical Vision Bow]], [[wiki/items/16004-magical-frost-bow|Magical Frost Bow]], [[wiki/items/16006-magical-blood-dagger|Magical Blood Dagger]], [[wiki/items/16007-magical-judge-dagger|Magical judge Dagger]], [[wiki/items/16008-magical-hiding-dagger|Magical hiding Dagger]], [[wiki/items/35002-magical-vision-bow|Magical Vision Bow]], [[wiki/items/35009-skeleton-king-s-magic-dagger|Skeleton King's Magic Dagger]].

### HP, MP and stats

- Base HP/MP not seen without gear yet. The Punisher HUD with starting and quest gear ([[gameplay/video-early-quests|early quests video]]) showed:

| level | HP | MP |
|---|---|---|
| 1 | 420 | 424 |
| 3 | 560 | 472 |
| 7 | 970 | 568 |
| 16 | 2,795 | 924 |
| 19 | 3,005 | 996 |
| 20 | 3,240–3,260 | 1,000 |

  MP rose by 24 per level from level 1 to 7 (gear unchanged?); HP depends on gear. *video*
- Magic Resist per level: **+3** (the patch note says 90 at level 30) — WM 0420 ([[gameplay/classes-and-legions|Classes]] §5). *notes*
- `base_stats` (the six radar stats on the creation screen: Attack, Ability Power, Magic Resist, Movement Speed, Attack Speed, Armor) are not in the client; the creation screen shows them only as a chart (`CreatChar.Chart_01`).

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

Character mastery tree (`Mastery`): [[wiki/masteries/401-punisher-mastery-1|Punisher mastery 1]], [[wiki/masteries/402-punisher-mastery-2|Punisher mastery 2]], [[wiki/masteries/403-punisher-mastery-3|Punisher mastery 3]], [[wiki/masteries/404-punisher-mastery-4|Punisher mastery 4]], [[wiki/masteries/405-punisher-mastery-5|Punisher mastery 5]], [[wiki/masteries/406-punisher-mastery-6|Punisher mastery 6]], [[wiki/masteries/407-punisher-mastery-7|Punisher mastery 7]], [[wiki/masteries/408-punisher-mastery-8|Punisher mastery 8]], [[wiki/masteries/409-punisher-mastery-9|Punisher mastery 9]], [[wiki/masteries/410-punisher-mastery-10|Punisher mastery 10]], [[wiki/masteries/411-punisher-mastery-11|Punisher mastery 11]], [[wiki/masteries/412-punisher-mastery-12|Punisher mastery 12]], [[wiki/masteries/413-punisher-mastery-13|Punisher mastery 13]], [[wiki/masteries/415-punisher-mastery-15|Punisher mastery 15]], [[wiki/masteries/416-punisher-mastery-16|Punisher mastery 16]], [[wiki/masteries/417-punisher-mastery-17|Punisher mastery 17]], [[wiki/masteries/418-punisher-mastery-18|Punisher mastery 18]], [[wiki/masteries/419-punisher-mastery-19|Punisher mastery 19]], [[wiki/masteries/420-punisher-mastery-20|Punisher mastery 20]], [[wiki/masteries/421-punisher-mastery-21|Punisher mastery 21]], [[wiki/masteries/422-punisher-mastery-22|Punisher mastery 22]], [[wiki/masteries/423-punisher-mastery-23|Punisher mastery 23]], [[wiki/masteries/424-punisher-mastery-24|Punisher mastery 24]], [[wiki/masteries/425-punisher-mastery-25|Punisher mastery 25]], [[wiki/masteries/426-punisher-mastery-26|Punisher mastery 26]], [[wiki/masteries/427-punisher-mastery-27|Punisher mastery 27]].

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

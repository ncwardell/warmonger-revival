---
title: "Gear stats (Crush Online artifacts)"
---

# Gear stats (Crush Online artifacts)

Every gear piece ("artifact") in the player spreadsheet **Crush Share**, with its EP cost and stats, and how the sheet's columns work. Tags: *sheet*, *guide* (forum or Steam guide), *client*, *guess*.

> [!warning]
> This is **Crush Online (late 2016)** gear, not Warmonger (2018). The sheet was posted on the Crush Online forum in November 2016 by EddArslon ([forum thread][f-sheet]). It covers the EP/SP gear system that Warmonger later removed (see [[gameplay/pvp-and-matches|PvP]] §SP/EP). Almost none of these items exist in the final client's `Item_Base`, and the few that share a name have different stats (§4). Use the page for Crush-mode rules or as balance reference. It does not replace `Item_Base`.

Sheet: [Crush Share][sheet], tabs **Gear** ([gid 1751214606][t-gear]), **EP cost thoughts** ([gid 1453587109][t-ep]), **Armor** ([gid 0][t-armor]), **Sheet3** ([gid 420277683][t-s3]), **Ore/Herb** ([gid 504563500][t-ore]). Stat valuation and caps are in [[gameplay/stat-values|Stat values]]. Dungeon drops are in [[gameplay/dungeon-drops|Dungeon drops]].

## 1. How the Gear tab is laid out

38 columns, one row per item, about 100 filled rows out of 1,019 ([Gear][t-gear]):

| Columns | Header | Meaning |
|---|---|---|
| A | Item name / Effect on it | Item name. Some rows have no name and are labelled by their special effect instead (e.g. "8% cooldown Ring", "Armor of 15%slow"). |
| B | Slot | 1–8, in the same order as the client's `ItemKind` 50–57: helmet, armour, gloves, shoes, necklace, belt, bracelet, ring. *sheet + client* |
| C | EP Cost | EP the item takes from the wearer's EP budget (§3). *sheet* |
| D | Difference EP | = Calc EP − EP Cost. |
| E–L | Health, Attack, Armor, Armor pen, Life Steal, AIS, AP, MR | **Base stats**: what the item gives as soon as it is worn. |
| M–T | (same 8 stats) | **SP bonus**: what the item adds once all its SP levels are bought during a fight. Usually 4 × base (3.75–4.12 × after rounding). |
| U–AB | (same 8 stats) | **Full stats** = base + SP bonus, true on every row. These are the numbers the author used for builds. |
| AC–AD | Difference EP, Calc EP | Calc EP = full stats × the per-stat EP values in row 2 (HP 1, Attack 20, Armor 15, Armor pen 13.3, Life steal 125, AIS 32, AP 29.27, MR 20). |
| AE–AL | (same 8 stats) | The EP value of each full stat (stat × weight). |

How we know the middle group is the SP bonus:

- A Crush patch (27 Oct 2016) changed **Bracelet of Temptation** to **3,900 EP, 780 SP per activation, +400 HP on 3 activations and +48 MR on 2**, i.e. +1,200 HP and +96 MR in total ([patch thread][f-halloween] post 9). The sheet's SP bonus for that item is exactly **HP 1,200 / MR 96** on a base of HP 300 / MR 24. *sheet + guide*
- SP cost per activation level, from forum posts: **SP per level = EP cost ÷ 5**, 3 levels at D rank. Seen for Invincible Armor (4,000 EP → 800 SP/level, 2,400 total), Gloves of Ghost (6,100 → 1,220, 3,660), Cape of Space (1,900 → 380) and Bracelet of Temptation (3,900 → 780). *guide* ([Invincible/Ghost thread][f-inv], [Cape of Space thread][f-cape], [patch thread][f-halloween]). The ÷5 rule fits all four but is not stated by any source. *guess*
- SP is earned by killing monsters inside a zone, starts at 0 on entry and is spent on worn items ([Crush basics][g-crush] §SP, EP, TP). Fort defenders start with full SP ([general gearing guide][f-general]).
- Check against a posted build: the forum's 15,000 EP Guardian build (8 items listed in [best-in-slot thread][f-bis]) shows **Health 5,960** and **Armor pen 30**. The full-stat HP of those 8 items in the sheet adds up to 4,800, plus the 1,160 base HP the author gives = 5,960, and their Armor pen adds up to 30. So the full columns are what a fully charged character wears. *sheet + guide*

Oddities in the data: "cure all / 800 mana" has base AP 56 but full AP 123 (2.2 ×). "Absorption belt" and "16% magic pen" put Life Steal / Armor pen only in the SP bonus. "Belt of Spirit" is listed twice. The three **No Enhance** items (helmet 800, bracelet 250, ring 500 EP) get no SP bonus on Health. The ring is the "default ring from the early quest" ([best-in-slot thread][f-bis]). *sheet*

## 2. Items by slot

Stats: HP = Health, Atk = Attack, ArPen = Armor penetration, LS% = Life steal %, AIS = attack speed (the sheet's "AIS"), AP = Ability power, MR = Magic resist. **Stat value** = the sheet's own Calc EP. A negative **Value − cost** means the item's special effect (in its name) is what the extra EP pays for. All rows *sheet* ([Gear][t-gear]). The client column is explained in §4.

### Slot 1 — Helmet / earrings (`ItemKind` 50)

| Sheet name / effect | EP cost | Base stats | Full stats (base + bonus) | Stat value (EP) | Value − cost | Client item |
|---|---:|---|---|---:|---:|---|
| Helmet of Warrior | 1800 | HP 180, Armor 12 | HP 900, Armor 60 | 1,800 | 0 | – |
| Helmet of Prot | 1800 | Atk 12, Armor 8 | Atk 60, Armor 40 | 1,800 | 0 | – |
| 8% Spell vamp | 2000 | AP 5 | AP 21 | 615 | -1,385 | – |
| Steel Helmet | 2100 | Armor 28 | Armor 138 | 2,070 | -30 | – |
| Earrings of Life | 2400 | HP 240, AP 8 | HP 1200, AP 41 | 2,400 | 0 | – |
| Break free | 3500 | AP 11, MR 9 | AP 55, MR 45 | 2,510 | -990 | – |
| cure all / 800 mana | 4400 | AP 56 | AP 123 | 3,600 | -800 | – |
| No Enhance Helmet | 800 | HP 100, Atk 4, AP 3 | HP 100, Atk 19, AP 13 | 860 | +60 | – |

### Slot 2 — Armor / cape / robe (51)

| Sheet name / effect | EP cost | Base stats | Full stats (base + bonus) | Stat value (EP) | Value − cost | Client item |
|---|---:|---|---|---:|---:|---|
| Chain Armor | 900 | Armor 12 | Armor 57 | 855 | -45 | – |
| Leather Cap | 900 | MR 9 | MR 44 | 880 | -20 | – |
| Armor of P | 1200 | Armor 16 | Armor 76 | 1,140 | -60 | – |
| Cape of Dreadman | 1200 | MR 12 | MR 57 | 1,140 | -60 | – |
| Plate Armor | 1500 | HP 120, Armor 12 | HP 600, Armor 60 | 1,500 | 0 | – |
| Armor of Barrier | 1500 | Armor 20 | Armor 100 | 1,500 | 0 | – |
| Cape of Odin | 1500 | MR 15 | MR 75 | 1,500 | 0 | – |
| Thick cap 400 mana | 1700 | HP 240 | HP 1200 | 1,200 | -500 | – |
| Cape of BLINK | 1900 | Armor 8, MR 3 | Armor 40, MR 15 | 900 | -1,000 | – |
| Cape of Sun | 2250 | HP 300 | HP 1500 | 1,500 | -750 | – |
| Armor of Spirit | 2400 | HP 240, MR 12 | HP 1200, MR 60 | 2,400 | 0 | 414 / 486 "Spirit Robe" *guess* |
| Thorns Armor | 3100 | HP 180, Armor 16 | HP 900, Armor 80 | 2,100 | -1,000 | – |
| Armor of 15%slow | 3100 | Armor 16, MR 9 | Armor 80, MR 45 | 2,100 | -1,000 | – |
| Armor of 20% slow | 3400 | Armor 16, MR 12 | Armor 80, AIS 20, MR 60 | 3,040 | -360 | – |
| Armor of 25% slow Active | 3400 | HP 240, Armor 16 | HP 1200, Armor 80 | 2,400 | -1,000 | – |
| Armor of March Active | 3700 | Armor 16, MR 15 | Armor 80, MR 75 | 2,700 | -1,000 | – |
| Invincible Active | 4000 | HP 300, Armor 20 | HP 1500, Armor 100 | 3,000 | -1,000 | 2905 "Invincible" is a use item, not armour |

### Slot 3 — Gloves (52)

| Sheet name / effect | EP cost | Base stats | Full stats (base + bonus) | Stat value (EP) | Value − cost | Client item |
|---|---:|---|---|---:|---:|---|
| Gloves of Protection | 1200 | Armor 16 | Armor 76 | 1,140 | -60 | – |
| Plate Gloves | 1500 | HP 120, Armor 12 | HP 600, Armor 60 | 1,500 | 0 | – |
| Thorn Gloves | 1575 | Atk 12, ArPen 6 | Atk 60, ArPen 30 | 1,599 | +24 | – |
| Gloves of Swordsman | 1600 | Atk 16 | Atk 76 | 1,520 | -80 | – |
| White Gloves | 1600 | AP 11 | AP 51 | 1,493 | -107 | – |
| Gloves of Fighter | 1700 | HP 180, Atk 8 | HP 900, Atk 38 | 1,660 | -40 | – |
| Last Gloves | 1850 | Atk 16, ArPen 4 | Atk 79, ArPen 20 | 1,846 | -4 | – |
| Limited Gloves | 2000 | Atk 20 | Atk 100 | 2,000 | 0 | – |
| Thief | 2100 | Atk 12, MR 9 | Atk 60, MR 45 | 2,100 | 0 | – |
| Gloves of Eternity | 2400 | HP 240, Atk 12 | HP 1200, Atk 60 | 2,400 | 0 | – |
| Gloves of life | 2400 | HP 240, AP 8 | HP 1200, AP 41 | 2,400 | 0 | 403 / 479 (name) |
| Gloves of Spirit | 2400 | HP 240, MR 12 | HP 1200, MR 60 | 2,400 | 0 | 416 / 488 "Spirit Gloves" *guess* |
| Ultimate Gloves | 2625 | Atk 20, ArPen 10 | Atk 98, ArPen 50 | 2,625 | 0 | – |
| Gloves of 8% cooldown | 3600 | Atk 12 | Atk 60 | 1,200 | -2,400 | – |
| Gloves 24% crit (2%) | 3600 | Atk 20 | Atk 98 | 1,960 | -1,640 | – |
| Gloves of Ghost CSD+12 | 6100 | Atk 20 | Atk 100 | 2,000 | -4,100 | – |

### Slot 4 — Shoes / boots (53)

| Sheet name / effect | EP cost | Base stats | Full stats (base + bonus) | Stat value (EP) | Value − cost | Client item |
|---|---:|---|---|---:|---:|---|
| Shoes of Guardian | 1200 | Armor 8, AIS 4 | Armor 38, AIS 20 | 1,210 | +10 | 411 / 483 "Guardian Shoes" *guess* |
| Boots of Warrior | 1400 | Atk 8, AIS 4 | Atk 38, AIS 20 | 1,400 | 0 | – |
| Boots of Magic | 1400 | AIS 4, AP 5 | AIS 20, AP 26 | 1,401 | +1 | – |
| Boots of Knight | 1800 | AIS 8, MR 6 | AIS 40, MR 30 | 1,880 | +80 | – |
| Boots of Prot | 2100 | Armor 16, MR 9 | Armor 79, MR 45 | 2,085 | -15 | – |
| 8%cd, 199 mana | 2385 | – | – | 0 | -2,385 | – |
| Boots of Agility 19c (2%) | 2400 | AIS 8 | AIS 40 | 1,280 | -1,120 | – |
| Boots of Wizard 4%coold | 2400 | AP 8 | AP 40 | 1,171 | -1,229 | – |

### Slot 5 — Necklace / earrings / bead (54)

| Sheet name / effect | EP cost | Base stats | Full stats (base + bonus) | Stat value (EP) | Value − cost | Client item |
|---|---:|---|---|---:|---:|---|
| Ruby of Health | 600 | HP 120 | HP 600 | 600 | 0 | – |
| Bead of Spirit | 900 | HP 60, Armor 8 | HP 300, Armor 38 | 870 | -30 | – |
| 8% cooldown | 1800 | – | HP 720 | 720 | -1,080 | – |
| Necklace of Transcend | 1850 | ArPen 4, AP 11 | ArPen 20, AP 53 | 1,817 | -33 | 425 / 457 *guess* |
| Necklace 8% cd | 2300 | HP 180 | HP 900 | 900 | -1,400 | – |
| Earrings of Dawn | 2400 | HP 480 | HP 2400 | 2,400 | 0 | – |
| Bone Neck 25%c (2%) | 2400 | Atk 8 | Atk 40 | 800 | -1,600 | – |
| Necklace of Despair | 2625 | ArPen 10, AP 14 | ArPen 50, AP 68 | 2,655 | +30 | – |
| Neck of Luck 18c | 3000 | AIS 20 | AIS 98 | 3,136 | +136 | – |
| Passive aoe | 3100 | HP 240, MR 9 | HP 1200, MR 45 | 2,100 | -1,000 | – |

### Slot 6 — Belt (55)

| Sheet name / effect | EP cost | Base stats | Full stats (base + bonus) | Stat value (EP) | Value − cost | Client item |
|---|---:|---|---|---:|---:|---|
| Old Belt | 900 | HP 120, Armor 4 | HP 600, Armor 19 | 885 | -15 | – |
| Huge Belt | 1500 | HP 300 | HP 1500 | 1,500 | 0 | – |
| Primal Quiver 12c | 2600 | AIS 12 | AIS 60 | 1,920 | -680 | – |
| Belt of AoE | 3100 | HP 240, MR 9 | HP 1200, MR 45 | 2,100 | -1,000 | – |
| Absorption belt | 3200 | Atk 12 | Atk 60, LS% 16 | 3,200 | 0 | – |
| Lifesteal 16% | 3200 | Atk 12 | Atk 60 | 1,200 | -2,000 | – |
| Sash of Souls | 3200 | Atk 16, AP 11 | Atk 79, AP 55 | 3,190 | -10 | – |
| Belt of Mom | 3300 | HP 300 | HP 1500 | 1,500 | -1,800 | – |
| 2% health regen | 3300 | HP 300 | HP 1500 | 1,500 | -1,800 | – |
| Belt of Spirit | 3600 | HP 360, MR 18 | HP 1800, MR 90 | 3,600 | 0 | – |
| Belt of Spirit | 3600 | HP 360, MR 18 | HP 1800, MR 90 | 3,600 | 0 | – |
| Belt of Guard | 3780 | Armor 28, MR 21 | Armor 139, MR 105 | 4,185 | +405 | – |
| 16% magic pen | 4600 | AP 11 | ArPen 16, AP 53 | 1,764 | -2,836 | – |

### Slot 7 — Bracelet (56)

| Sheet name / effect | EP cost | Base stats | Full stats (base + bonus) | Stat value (EP) | Value − cost | Client item |
|---|---:|---|---|---:|---:|---|
| Bracelt of Rush | 1200 | Atk 12 | Atk 57 | 1,140 | -60 | – |
| Sharp Bracelet 12c | 1700 | Atk 16 | Atk 79 | 1,580 | -120 | – |
| Brac of ILL | 2000 | Atk 8, AIS 8 | Atk 38, AIS 40 | 2,040 | +40 | – |
| White Bracelet | 2000 | AP 11 | AP 51 | 1,493 | -507 | – |
| Hard Bracelet | 2100 | Armor 24, AP 8 | Armor 120, AP 41 | 3,000 | +900 | – |
| Bracelet of Rise | 2100 | AP 8, MR 18 | AP 41, MR 90 | 3,000 | +900 | 443 / 475 (name) |
| Bracelet of Spirit | 2400 | HP 240, MR 12 | HP 1200, MR 60 | 2,400 | 0 | – |
| Ancient Bracelet | 2600 | HP 120, Atk 8, Armor 16 | HP 120, Atk 38, Armor 80 | 2,080 | -520 | – |
| Bracelet of Life | 3000 | HP 600 | HP 3000 | 3,000 | 0 | 407 / 451 (name) |
| Bracelet of Barrier | 3000 | HP 300, Armor 20 | HP 1500, Armor 98 | 2,970 | -30 | 435 / 467 "Barrier Bracelet" *guess* |
| Bracelet of Slaugher | 3200 | Atk 16, AP 11 | Atk 79, AP 55 | 3,190 | -10 | – |
| Bracelet of Temptation | 3900 | HP 300, MR 24 | HP 1500, MR 120 | 3,900 | 0 | – |
| No Enhance Bracelet | 250 | HP 100, Atk 3 | HP 100, Atk 18 | 460 | +210 | – |

### Slot 8 — Ring (57)

| Sheet name / effect | EP cost | Base stats | Full stats (base + bonus) | Stat value (EP) | Value − cost | Client item |
|---|---:|---|---|---:|---:|---|
| Ring of Emission | 1200 | AP 8 | AP 38 | 1,112 | -88 | – |
| Thorns Ring | 1575 | Atk 12, ArPen 6 | Atk 60, ArPen 30 | 1,599 | +24 | – |
| Dark Red Ring | 1575 | ArPen 6, AP 8 | ArPen 30, AP 41 | 1,599 | +24 | – |
| Ring of Fighter | 1600 | Atk 16 | Atk 76 | 1,520 | -80 | – |
| Ring of Rose | 1600 | Atk 8, AP 5 | Atk 38, AP 27 | 1,550 | -50 | – |
| White Ring | 1600 | AP 11 | AP 56 | 1,639 | +39 | – |
| Ring of Swordsman | 1700 | HP 180, Atk 8 | HP 900, Atk 38 | 1,660 | -40 | – |
| Ring of Abyss | 2100 | AP 8, MR 9 | AP 41, MR 45 | 2,100 | 0 | – |
| Ring of Life | 2400 | HP 240, AP 8 | HP 1200, AP 41 | 2,400 | 0 | 408 / 452 (name) |
| Ring 16% Vamp | 3100 | AP 14 | AP 68 | 1,990 | -1,110 | – |
| 8% cooldown Ring | 3600 | AP 8 | AP 40 | 1,171 | -2,429 | – |
| 8% magic pen +Active AoE | 4100 | ArPen 8, AP 11 | ArPen 8, AP 55 | 1,716 | -2,384 | – |
| 1000 mana +5% Ad from mana | 4250 | AP 64 | Atk 80, AP 120 | 5,112 | +862 | – |
| No Enhance Ring | 500 | HP 100, Atk 8 | HP 100, Atk 38 | 860 | +360 | – |

## 3. EP budget

- **EP** (Equipment Points) is a budget: each worn item costs its EP, and the total may not exceed the character's maximum. The maximum rises with level ([Crush basics][g-crush] §SP, EP, TP), with the **Striker (ST) level** (set by the levels of your 5 equipped weapons) and with the legion mastery **Elite Warrior** ([raise-EP thread][f-ep]). *guide*
- Values reported by players *guide*:

| EP maximum | How | Source |
|---|---|---|
| 13,400–13,500 | build used on channel 5 | [channel 5 thread][f-ch5] |
| 14,000 | Channel 5 cap (weapons and gear capped at grade C there) | [channel 5 thread][f-ch5] post 7 |
| 15,000 | all 5 weapons at A-22 = Striker 6 | [channel 5 thread][f-ch5] post 7, [general gearing guide][f-general] |
| 17,000 | all 5 weapons at SS30 (max) = Striker 7 | [channel 5 thread][f-ch5] post 10 |
| +500 | legion mastery maximum ("Elite Warrior") | [channel 5 thread][f-ch5] post 7 |
| 17,500 | Striker 7 + legion bonus | [channel 5 thread][f-ch5] post 11 |

- The sheet's own valuation uses **15,000 EP** as the budget (its "Theoretical Maximum" column, see [[gameplay/stat-values|Stat values]]). *sheet*
- Cheapest piece per slot: 600 EP (Ruby of Health). Most expensive: 6,100 EP (Gloves of Ghost). Eight pieces at the plain "value = cost" rate of about 1,500–2,400 EP each fill 15,000 EP. *sheet*

## 4. Matching to the client (`Item_Base`)

- Of the ~100 sheet items, only **Gloves of Life (403 / 479), Bracelet of Life (407 / 451), Ring of Life (408 / 452)** and **Bracelet of Rise (443 / 475)** have an exact name match in `Item_Base` (T1 / T2 rows). Close matches: Necklace of Transcend → Necklace of Transcendency 425/457, Gloves of Spirit → Spirit Gloves 416/488, Bracelet of Barrier → Barrier Bracelet 435/467, Shoes of Guardian → Guardian Shoes 411/483, Armor of Spirit → Spirit Robe 414/486. *client*, matches marked *guess* in the table.
- The stats do **not** match. Example: sheet Bracelet of Life = HP 600 base / 3,000 full. Client 407 = Attack 4, Health 20, HP regen 1, then Health 20, HP regen 2, then Attack 40, Health 200, HP regen 8 (three option groups in Warmonger's own stat model). The final client keeps the 2018 Warmonger gear (sets Life, Guardian, Spirit, Honor, Mediation, Transcendency, Bandolier, Barrier, Courage, Rise, boss sets 3001–3068, Fame sets 3501–3518). Crush artifacts such as Thorns Armor, Huge Belt, Earrings of Dawn and Cape of Odin are gone. *client*
- `Item_Base` item **2905 "Invincible"** is a use item (kind 11, priced 10,000 in currency 17), not the Crush Invincible Armor. *client*
- No EP-cost or SP column has been identified in the decoded `Item_Base`. A Crush-mode server would have to add one from this sheet. *guess*

## 5. Crafting costs of the special artifacts (forum)

| Item | EP | Recipe | Active | Source |
|---|---:|---|---|---|
| Invincible Armor | 4,000 | 28 Black Crystals + C-grade Thorns Armor + 20 Amplifying spell stones (400 gold medals). Thorns Armor itself = 42 Black Crystals + 15 Worked Moonstone + Armor of Spirit. Can fail (twice: Thorns step and final step). | 5 s invulnerable and immune to CC, 90 s cooldown | [Invincible/Ghost thread][f-inv] *guide* |
| Gloves of Ghost | 6,100 | B-grade Ultimate Gloves + 53 Black Crystals + 10 Amplifying spell stones (200 gold medals). Ultimate Gloves = Last Gloves + Thorns Gloves + 3 D Reinforcement stones. Can fail. | 5 s invisible (ends if you use a skill), 80–90 s cooldown; "CSD +12" = Critical Strike Damage +12% | [Invincible/Ghost thread][f-inv] *guide* |
| Cape of Space (sheet "Cape of BLINK") | 1,900 | 14 Blue Crystals + 18 Red Crystals + 5 Worked Topaz (= 25 Topaz) | short-range teleport, passes through walls, 30 s cooldown | [Cape of Space thread][f-cape] *guide* |
| Thorns Armor | 3,100 | see above | reflects 30% of the attacker's attack damage, ignoring armour (about 100–170 damage) | [sheet thread][f-sheet] post 1 §6, [best-in-slot thread][f-bis] *guide* |

[sheet]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY
[t-gear]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY/edit#gid=1751214606
[t-ep]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY/edit#gid=1453587109
[t-armor]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY/edit#gid=0
[t-s3]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY/edit#gid=420277683
[t-ore]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY/edit#gid=504563500
[f-sheet]: https://web.archive.org/web/20161130042453/http://www.crush-game.com:80/forum/threads/google-spreadsheet-with-gear-info.528/
[f-bis]: https://web.archive.org/web/20170211150702/http://crush-game.com:80/forum/threads/best-in-slot-guardian-11-3-2016-15-000-ep.543/
[f-ch5]: https://web.archive.org/web/20161129115247/http://www.crush-game.com:80/forum/threads/channel-5-guide-to-being-notorious-how-to-twink-your-gear-ep-13500.603/
[f-inv]: https://web.archive.org/web/20161025042755/http://www.crush-game.com:80/forum/threads/invincible-armor-gloves-of-ghost-information.295/
[f-cape]: https://web.archive.org/web/20161028132643/http://www.crush-game.com:80/forum/threads/cape-of-space.389/
[f-halloween]: https://web.archive.org/web/20161030053817/http://www.crush-game.com:80/forum/threads/patch-notes-20161027-halloween-event.453/
[f-ep]: https://web.archive.org/web/20161027194122/http://www.crush-game.com:80/forum/threads/how-to-raise-ep.91/
[f-general]: https://web.archive.org/web/20170210140704/http://crush-game.com:80/forum/threads/general-guide-to-gearing-up-and-getting-started.868/
[g-crush]: https://steamcommunity.com/sharedfiles/filedetails/?id=780459080

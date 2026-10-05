---
title: "Stat values and caps"
---

# Stat values and caps

How players of **Crush Online (late 2016)** priced each stat in EP, the caps they found, the assumed armour formula and the buff consumables. This comes from the **Crush Share** spreadsheet and the forum post that came with it, checked against the final client where possible. Tags: *sheet*, *guide* (forum or Steam guide), *client*, *guess*. The per-item numbers are in [[gameplay/gear-stats|Gear stats]].

> [!note]
> These are **player estimates**, not server code. The sheet's author says so: the values are "estimates of the amount of EP it costs for these stats to be on a piece of gear" ([forum thread][f-sheet] §4). They are useful as a balance target for a Crush-mode server. The real damage formula is server-side and lost ([[spec/combat]]).

## 1. EP value of one stat point

From the **EP cost thoughts** tab ([gid 1453587109][t-ep]) *sheet*, repeated in the [forum post][f-sheet] §4 *guide*. Theoretical max = 15,000 EP ÷ EP per point, i.e. how much of the stat a full 15,000 EP budget would buy on its own.

| Stat | EP per point | Theoretical max (15,000 EP) | Gear hardcap | Talents | Enchant, one piece | Enchant, 8 pieces | Scroll | Potion | Sheet note |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|
| Health | 1 | 15,000 | | | | | | 100 | |
| Attack | 20 | 750 | | 8 | 14 | 112 | 35 | | |
| Armor | 15 | 1,000 | | 8 | 24 | 192 | | | no gain past ~450 armor (~550 if the enemy has armor pen) |
| Armor pen | 13.3 | 1,128 | 100 | | | | 16 | | weak against high-armor targets |
| AIS (attack speed) | 32 | 469 | 238 | 4 | | | 35 | | |
| AP | 29.3 | 513 | | | | | | | |
| MR | 20 | 750 | | | 15 | 120 | | | |
| Life steal | 125 | 120 | 16 | 9 | | | | 1 | |
| Health regen | 20 | 750 | | | 20 | 160 | | 8 | |
| Critical (header says "20–140") | 10 | 1,500 | | | | | 20% | | |
| Mana | 1 | 15,000 | | | | | | | |
| Mana regen | 40 | 375 | | | | | | | |
| Cooldown | 300 | 50 | 28 | 9 | | | | | |
| Thorns | 1,000 | 1 (as written) | | | | | | | asks whether armor pen beats thorns |

- In the Gear tab the AP weight is **29.268… = 1,200 ÷ 41** (Earrings of Life: 1,200 HP-worth of AP spread over 41 AP). The other weights are the round numbers above. *sheet* ([Gear][t-gear] row 2)
- **Critical**: 10 "critical value" = 1% crit chance, so 1 point = 10 EP. Its worth depends on the character's attack. *guide* ([forum][f-sheet] §4)
- **Enchant**: one enhancement roll gives Attack 14, Armor 24, MR 15 or HP regen 20. The ×8 column assumes the same roll on all 8 gear pieces. The forum confirms "armor rolls on enhancement A = 24 (192 on 8 pieces)". *sheet + guide* ([forum][f-sheet] §5). These are the Crush "additional effect" rolls. The per-roll ranges are in [[gameplay/items-and-crafting|Items and crafting]] §3.
- **Gear hardcaps** (most of a stat that gear can give): Armor pen 100, AIS 238, Life steal 16%, Cooldown 28%. **Talents**: Attack 8, Armor 8, AIS 4, Life steal 9, Cooldown 9 (units as in the sheet). *sheet*

## 2. Armor and magic-resist reduction (assumed formula)

The author assumed **damage reduction = armor ÷ (100 + armor)** and applied the same formula to MR. *guide* ([forum][f-sheet] §1, §1b). Armor tab ([gid 0][t-armor]) *sheet*:

| Armor or MR | 0 | 25 | 50 | 75 | 100 | 125 | 150 | 175 | 200 | 300 | 400 | 500 | 600 | 700 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reduction | 0% | 20.0% | 33.3% | 42.9% | 50.0% | 55.6% | 60.0% | 63.6% | 66.7% | 75.0% | 80.0% | 83.3% | 85.7% | 87.5% |

- The MR rows (25–200) come from the forum post, which also gives their EP cost at 20 EP per MR (25 MR = 500 EP … 200 MR = 4,000 EP). It calls 100 MR reachable and recommended. *guide*
- Little benefit past **450 armor** (550 when facing armor pen). Below **300** armor, enemy armor pen is very effective. *guide* ([forum][f-sheet] §2). One player who dropped from 750 to 600 armor felt no difference ([forum][f-sheet] post 2). *guide*
- We do not know if the real server used this formula. A Crush-mode server can use it as the starting point. *guess*

## 3. Armor pen vs flat attack

Flat attack that matches **100 armor pen**, by target armor ([forum][f-sheet] §5) *guide*:

| Target armor | 200 | 250 | 300 | 400 | 500 |
|---|---:|---:|---:|---:|---:|
| Attack equal to 100 armor pen | 150 | 100 | 75 | 50 | 38 |

Armor pen starts to lose value above ~250 target armor. The author treated 250 as the normal floor, because enhancement rolls alone give 192 armor.

## 4. Reference character numbers (Crush, Nov 2016)

| Value | Number | Source |
|---|---|---|
| Base HP (may vary by class) | 1,160 | [forum][f-sheet] §6 *guide* |
| Recommended HP | 4,200–5,250 | [forum][f-sheet] §6 *guide* |
| Recommended attack speed (Guardian) | 60% (bracelet + boots); 680 → 990 "speed" greatly raised damage | [forum][f-sheet] §7 *guide* |
| Thorns reflect | 30% of the attacker's attack damage, not reduced by armor (≈100–170) | [forum][f-sheet] §6 *guide* |
| Scroll bonus used in builds | +35 Attack | [best-in-slot thread][f-bis] *guide* |
| 15,000 EP Guardian, fully charged | HP 5,960, Attack 522 (+35), Armor 413, Armor pen 30, Life steal 9, AIS 981, AP 12, MR 187 | [best-in-slot thread][f-bis] *guide* |

## 5. Consumables (Sheet3 tab) vs the client

The **Sheet3** tab ([gid 420277683][t-s3]) lists the S-grade (or numbered) consumable buffs. Here it is next to the final client's buff table (`Skill_Buff` rows 2077–2132, reached through `Item_Base` 704–759) *client*. The sheet calls the crit/AoE/cooldown/attack-speed family "Tome" and the attack/AP/pen family "Scroll". The client names are the other way round.

| Sheet row | Sheet values *sheet* | Client buff at grade S *client* | Agrees? |
|---|---|---|---|
| Tome S | Crit 20%, less AoE 20%, Cooldown 12%, Attack speed 40 | Critical Strikes +20% (2100), Reduced Area Damage 20% (2096), Cooldown Reduction 12% (2092), Attack Speed +40 (2088) | **yes** |
| Scroll S | Attack 35, Ability 35, Armor pen 16, Magic pen 16 | Warrior +160 Attack (2080), Magician +120 AP (2084), Armor Pen +8 (2104), Magic Pen +8 (2108) | **no** (Crush values, or a lower grade; Warmonger rebalanced) |
| Elixir 1 | HP on hit 12, HP 200 | Vampirism: Life steal 12, HP 400 (2120) | life steal yes, HP no |
| Elixir 2 | HP on hit 12, Tenacity 40 | Tenacity: Life steal 12, Tenacity 40 (2128) | **yes** |
| Elixir 3 | HP 200, HP regen 20 | Health: HP 400, HP regen 8 (2112) | no |
| Flask 1 | MP on hit 8, MP 120 | Devour: Mana steal 8, MP 200 (2124) | steal yes, MP no |
| Flask 2 | Tenacity 40, MP on hit 8 | Tenacity: Mana steal 8, Tenacity 40 (2132) | **yes** |
| Flask 3 | MP 120, MP regen 16 | Mana: MP 200, MP regen 8 (2116) | no |

Client grades C/B/A are 1/2/3 × a step. S is 4 steps for most buffs (crit 5/10/15/20%), but 5 steps for Warrior (32/64/96/160) and Magician (24/48/72/120). All these buffs have duration field 1500 (unit not confirmed). *client*. The EP tab's "Potions" column (HP 100, Life steal 1, HP regen 8) and "Scrolls" column (Attack 35, Armor pen 16, AIS 35, Crit 20%) are the same Crush-era buffs. *sheet*

[t-gear]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY/edit#gid=1751214606
[t-ep]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY/edit#gid=1453587109
[t-armor]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY/edit#gid=0
[t-s3]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY/edit#gid=420277683
[f-sheet]: https://web.archive.org/web/20161130042453/http://www.crush-game.com:80/forum/threads/google-spreadsheet-with-gear-info.528/
[f-bis]: https://web.archive.org/web/20170211150702/http://crush-game.com:80/forum/threads/best-in-slot-guardian-11-3-2016-15-000-ep.543/

---
title: "Potion regeneration ticks"
---

# Potion regeneration ticks

How HP/MP potions actually paid out on the live Crush Online server (March 2017), measured tick by tick by a player, set against the client's potion data. Related: [[items-and-crafting]], [[stat-values]], [[server-rules]].

Sources:
- [thread] = forum thread "Potions recovering incorrect amount", crush-game.com, posts 4290–4303, 1–7 Mar 2017 ([archived](https://web.archive.org/web/20170722131713/http://crush-game.com/forum/threads/potions-recovering-incorrect-amount.932/)).
- [img] = the poster's measurement spreadsheet, [imgur mhuVgPw](http://i.imgur.com/mhuVgPw.png) (embedded in post 4290).
- *client* = `Item_Base.cdb` and `Skill_Buff.cdb` (see [[spec/data-tables]]).

## Client data: potion items and their buffs

Each potion item points at a regen buff (`Item_Base` opt1_value = `Skill_Buff` id). The buff carries a flat Health Regeneration (option 32) and/or Mana Regeneration (option 34) bonus. *client*

| Item id | Item | Buy/sell price (gold) | c40 (grade level?) | Buff id | HP regen (opt 32) | MP regen (opt 34) |
|---|---|---|---|---|---|---|
| 883 | Potion of Health [D] | 10 | 10 | 2050 | 25 | – |
| 885 | Potion of Health [C] | 72 | 20 | 2060 | 38 | – |
| 886 | Potion of Health [B] | 90 | 30 | 2061 | 50 | – |
| 887 | Potion of Health [A] | 135 | 40 | 2062 | 63 | – |
| 888 | Potion of Health [S] | 182 | 50 | 2063 | 75 | – |
| 884 | Potion of Mana [D] | 10 | 10 | 2051 | – | 6 |
| 889 | Potion of Mana [C] | 72 | 20 | 2064 | – | 9 |
| 890 | Potion of Mana [B] | 90 | 30 | 2065 | – | 13 |
| 891 | Potion of Mana [A] | 135 | 40 | 2066 | – | 16 |
| 892 | Potion of Mana [S] | 182 | 50 | 2067 | – | 19 |
| 893 | Health Mana Potion [D] | 25 | 10 | 2068 | 13 | 3 |
| 894 | Health Mana Potion [C] | 80 | 20 | 2069 | 19 | 4 |
| 895 | Health Mana Potion [B] | 100 | 30 | 2070 | 25 | 5 |
| 896 | Health Mana Potion [A] | 151 | 40 | 2071 | 31 | 6 |
| 897 | Health Mana Potion [S] | 202 | 50 | 2072 | 38 | 8 |
| 2598 | Potion of Health [Quest] | 135 | 40 | 2062 | 63 | – |

Other shared columns on all potions: opt1_type 301 (= "apply buff"), opt2_type 261 = 15, opt3_type 262 = 1 HP / 2 MP / 3 both (potion family, *guess*), bind 1, kind 11. The client buff names call the Health Mana potions "Omni Potion". *client*

The tooltip totals the poster quotes for S grade are exactly the buff value × 16 (the 16 s potion duration): HP 75 × 16 = 1,200; MP 19 × 16 ≈ 300; Omni 38 × 16 ≈ 600 HP and 8 × 16 ≈ 120 MP [thread] post 4290. So the intended rule is **regen value per second for 16 s** (*guess*, fits all four numbers). An existing guide figure, Mana [C] = 150 MP over 16 s ([[items-and-crafting]]), also fits 9 × 16 = 144.

## What the live server paid (S grade)

Tooltip promise vs. measured total [thread] post 4290, [img]:

| Potion | Tooltip | Measured | Share | Ticks boosted | Extra per tick |
|---|---|---|---|---|---|
| Mana [S] (892) | 300 MP | 180 MP | 60% | 3 | +60 MP |
| Health Mana [S] (897) | 600 HP + 120 MP | 480 HP + 96 MP | 80% | 4 | +120 HP, +24 MP |
| Health [S] (888) | 1,200 HP | 960 HP | 80% | 4 | +240 HP |

Raw tick logs from [img] (value at each regen tick; potion ticks in **bold**):

| Test | Start | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mana S #1, MP | 670 | 716 | **822** | **928** | **1034** | 1080 | | | | | |
| per tick | | 46 | 106 | 106 | 106 | 46 | | | | | |
| Mana S #2, MP | 299 | 345 | 391 | 437 | **543** | **649** | **755** | 801 | 847 | 893 | 939 |
| per tick | | 46 | 46 | 46 | 106 | 106 | 106 | 46 | 46 | 46 | 46 |
| Mana S #3, MP | 71 | 90 | 109 | 128 | 147 | 166 | **245** | **324** | **403** | 422 | 441 |
| per tick | | 19 | 19 | 19 | 19 | 19 | 79 | 79 | 79 | 19 | 19 |
| H/M S, HP | 1044 | 1074 | 1104 | **1254** | **1404** | **1554** | **1704** | 1734 | 1764 | | |
| per tick | | 30 | 30 | 150 | 150 | 150 | 150 | 30 | 30 | | |
| H/M S, MP | 582 | 601 | **644** | **687** | **730** | **773** | 792 | | | | |
| per tick | | 19 | 43 | 43 | 43 | 43 | 19 | | | | |
| HP S, HP (sheet mislabels it "Mana") | 558 | 588 | **858** | **1128** | **1398** | **1668** | 1698 | 1728 | | | |
| per tick | | 30 | 270 | 270 | 270 | 270 | 30 | 30 | | | |

Observations, all [thread] post 4290 / [img]:
- Base (no potion) regen per tick in these tests: HP 30; MP 19 or 46 (the 46 runs had an A-grade weapon with 70 mana regen plus regen buffs, a Saint).
- Potion bonus adds a flat amount on top of the base each tick; it does not scale with the base (MP +60 on both 19 and 46).
- Regen ticks timed at **about 6 s** apart (one hand measurement); potion duration **16 s**.
- Mana potions boosted 3 ticks, HP and Health Mana potions 4 ticks.
- Staff replied "Reported to developers" on 7 Mar 2017 (post 4303); no fix is recorded in the thread.

## Fitting the numbers (*guess*)

Extra per tick ÷ client buff value: HP 240/75 = 3.2, Omni HP 120/38 ≈ 3.2, MP 60/19 ≈ 3.2, Omni MP 24/8 = 3.0. So the live server paid roughly **buff value × 3.2 per tick** (16 s / 5 ticks), i.e. it was built for 5 ticks per 16 s, but only 3–4 ticks fell inside the window. The poster drew the same conclusion (5 ticks would be needed) [thread] post 4290.

For the revival server the choice is:
- **Faithful**: credit buff value × 3.2 (rounded down to the observed 240/120/60/24) at each regen tick that falls inside 16 s.
- **As advertised**: credit buff value × 16 in total over 16 s (e.g. value × 1 every second, or value × 4 on four 4 s ticks), matching the tooltip.

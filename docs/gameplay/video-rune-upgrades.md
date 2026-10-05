---
title: "Video notes: rune upgrade attempts (ZonderCoRe)"
---

# Video notes: rune upgrade attempts (ZonderCoRe)

Notes from ZonderCoRe's video "Warmonger Upgrade a Rune to +7" ([video][v], uploaded 12 Jul 2018, 23 min). He takes one **Attack Rune** from +6 down and back up until it reaches +7 at the Rune Reinforce window. He leaves the sub-material slot empty the whole time. Every attempt was counted from the rune name in the window, read at one-second steps, and checked against the SUCCESS/FAIL pop-ups. The video is from **before** the 20 Sep 2018 cost change and the 26 Jul 2018 cap raise, so compare it with the 0420 column of [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]], not with the final client table.

Tags: *video* (read off the screen) · *client* (`data/tables/`) · *guess*.

## 1. Observed success rate per level

83 attempts, 42 successes, 41 failures. *video*

| Attempt (level before → after) | Tries | Success | Fail | Observed rate |
|---|---|---|---|---|
| +2 → +3 | 1 | 1 | 0 | (1/1) |
| +3 → +4 | 9 | 8 | 1 | **89 %** |
| +4 → +5 | 28 | 20 | 8 | **71 %** |
| +5 → +6 | 32 | 12 | 20 | **38 %** |
| +6 → +7 | 13 | 1 | 12 | **8 %** |

Counts come from the whole video ([0:44][t44] to [22:25][t1345]); the per-attempt log is in section 5. The sample is small: a 95 % interval on 12/32 is roughly 21–56 %, and on 1/13 roughly 0–36 %. *video*

- **On failure the rune drops exactly one level.** All 41 failures did this, for example +3→+4 failed and left a +2 ([2:10][t130]). The rune was never destroyed and never stayed at the same level. *video*
- The window still shows a "Destruction of rune in case of reinforce failure" note next to the empty sub-material slot ([0:50][t50]). It is a client string (`StringAll_Eng`). In this footage failure only cost one level. *video + client*
- Gold and materials are spent on every try, whether it succeeds or fails. The total for all 83 tries is 7,580 Blue Crystals (computed from section 2). The video description estimates "about 7,800 Blue Crystals", which only adds up if failed tries consume materials too. *video + guess*
- After the +6→+7 success the window empties and shows a cost of 0 ([22:25][t1345]). No +7→+8 step was offered, so on 12 Jul 2018 the rune cap was probably **+7**. That sits between the +5 launch cap and the +9 cap of 26 Jul. *video + guess*

## 2. Cost per attempt (tier 1 rune, July 2018)

Read from the Rune Reinforce window: cost, material 1, material 2 ([2:20][t140], [2:07][t127], [2:02][t122], [1:57][t117], [2:50][t170]). *video*

| Step | Gold | Blue Crystal (700) | Red Passion (shard icon, probably Fragment [D] 611) | Client `JewelSocketMake`, group 1 |
|---|---|---|---|---|
| +2 → +3 | 3,000 | 40 | 20 | Blue 20, 611 ×20 |
| +3 → +4 | 4,000 | 60 | 30 | Blue 30, 611 ×30 |
| +4 → +5 | 5,000 | 80 | 40 | Blue 60, 611 ×40, Shining 854 ×1 |
| +5 → +6 | 6,000 | 100 | 50 | Blue 80, 611 ×50, Shining 854 ×1 |
| +6 → +7 | 7,000 | 120 | 60 | Blue 100, 611 ×60, Shining 854 ×1 |

- **Gold = 1,000 × (level after the upgrade).** For example, +4→+5 costs 5,000. `JewelSocketMake` has no gold column, so this rule has to come from somewhere else. This video is the source. *video*
- **The Blue Crystal counts match the 20 Apr 2018 "after" T1 column** in [[gameplay/reinforce-and-runes]] §2 (40/60/80/100/120 for levels 2–6), not the client. *video*
- **The Red Passion counts already match the client** (20/30/40/50/60). Before 20 Sep there was **no Shining Passion** at +5 and up; the window shows only two materials ([1:57][t117]). *video + client*
- The shop sells Blue Crystals at **10 gold each**: 100 cost 1,000 gold ([1:15][t75]). *video*
- Red Passion Fragments [D] are made at the Create Item window for **3,750 gold** per craft ("Need" 60 of another Red Passion item). He used Auto Create, e.g. "Proceed 4/13" ([7:01][t421]). The Red Passion Piece [D] craft shows **7,500 gold** ([15:18][t918]). *video*
- Total for the 83 tries: **462,000 gold, 7,580 Blue Crystals and 3,790 Red Passion**. His gold went from 769,777 ([1:15][t75]) to 130,277 ([22:25][t1345]), and that also covers crystal buying and crafting. *video*

## 3. Attack Rune stat per level

The window shows the stat for the current level and the next one ([2:10][t130], [1:55][t114], [5:30][t330]). *video*

| Level | Item id (`Item_Jewel`) | Attack in the video | `Item_Jewel` opt_value |
|---|---|---|---|
| +2 | 7004 | 9 | 16 |
| +3 | 7005 | 13 | 22 |
| +4 | 7006 | 17 | 30 |
| +5 | 7007 | 22 | 42 |
| +6 | 7008 | 27 | 58 |
| +7 | 7009 | 33 | 76 |

The live July 2018 curve rises by +4, +4, +5, +5, +6 per level. Continued at +6 per level, it gives +9 = 45, which is the Attack value the 12 Apr 2018 patch notes give for +9 ([[gameplay/reinforce-and-runes]] §3). The server-only `Item_Jewel` has a much steeper curve (+9 = 120). It is either a later rebalance or a different scale. *video + client + guess*

The rune tooltip lists three socket slots ("First / Second / Third slot: All"), so this rune fits any slot. *video*

## 4. What the server needs from this

- On failure the rune drops one level (never destroyed in this sample), and the materials and gold are consumed. *video*
- Gold per rune upgrade is 1,000 × the target level, at least for tier 1 runes. *video*
- The tier-1 success curve sits at about 90 % or more up to +4, then about 70 % at +4→+5, about 40 % at +5→+6 and about 10 % at +6→+7. That matches the 6 Apr 2018 note that rarity-1 runes start to drop off around level 6–7, although here the drop starts earlier. 20 Sep 2018 raised these rates, so a revival can start from these numbers and then raise them. *video + guess*

## 5. Timestamped log

Times are when the new level first shows in the window. S = success, F = failure.

| Time | Event |
|---|---|
| [0:10][t10] | Armour tooltip shows sockets with a +7 Attack, a +4 Life Steal and a +5 Armor Penetration rune |
| [0:30][t30] | Rune Set / Delete window (the socketing screen) |
| [0:44][t44] | Rune Reinforce opened with a +6 Attack Rune |
| [0:49][t49] | +6→+7 F (→+5); [0:54][t54] +5→+6 F (→+4) |
| [1:10][t70] | Shop: buys Blue Crystals in batches of 100 at 1,000 gold; the shop also lists Shining, Mysterious, Brilliant and Amplifying Passion |
| [1:55][t115] | +4→+5 S; [2:00][t120] F; [2:05][t125] F; [2:10][t130] F (→+2); the chat asks whether the odds were lowered |
| [2:32][t152] | +2→+3 S, then +3→+4 S, +4→+5 S, +5→+6 S ([2:47][t167]); [2:52][t172] +6→+7 F; [2:57][t177] +5→+6 S |
| [3:53][t233] | +6→+7 F, +5→+6 F, then +4/+5 back and forth (S, F, S, F) to [4:19][t259] |
| [5:16][t316] | +4→+5 S, F, S, +5→+6 S ([5:31][t331]); [5:36][t336] +6→+7 F |
| [6:40][t400] | Create Item: auto-crafts Red Passion Fragments [D] at 3,750 gold each ([7:01][t421]) |
| [7:16][t436] | +5→+6 F; [7:24][t444] +4→+5 S |
| [8:08][t488] | Four F/S pairs at +4/+5 up to [8:38][t518] |
| [9:56][t596] | +4→+5 F (→+3) |
| [10:38][t638] | +3→+4 S, +4→+5 S, +5→+6 S ([10:48][t648]); +6→+7 F, then F, F (→+3), then S ([11:08][t668]) |
| [12:41][t761] | +4→+5 F; then S, S, F, S, S (+6 at [13:06][t786]); [13:11][t791] +6→+7 F; [13:16][t796] S |
| [13:57][t837] | +6→+7 F, F, F (→+3); [14:13][t853] S, [14:18][t858] S |
| [15:18][t918] | Crafting Red Passion Piece [D] (7,500 gold) and more Fragments [D] ([15:51][t951]) |
| [16:07][t967] | +5→+6 S; [16:12][t972] +6→+7 F |
| [16:47][t1007] | F, F, S, S, S (+6 at [17:08][t1028]); then F, F ([17:17][t1037]) |
| [18:43][t1123] | S, S (+6); F, F; S, F, S, S (+6 at [19:18][t1158]) |
| [20:18][t1218] | +6→+7 F, F, F (→+3); S, F, S, S (+5 at [20:48][t1248]) |
| [21:41][t1301] | Crafting more Red Passion |
| [22:00][t1320] | +5→+6 S; [22:05][t1325] +6→+7 F; F; S; S ([22:20][t1340]) |
| [22:25][t1345] | **+6→+7 S**: the window empties, cost 0, gold 130,277 |

[v]: https://www.youtube.com/watch?v=dpofIAFX2wM
[t10]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=10s
[t30]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=30s
[t44]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=44s
[t49]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=49s
[t50]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=50s
[t54]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=54s
[t70]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=70s
[t75]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=75s
[t114]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=114s
[t115]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=115s
[t117]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=117s
[t120]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=120s
[t122]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=122s
[t125]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=125s
[t127]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=127s
[t130]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=130s
[t140]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=140s
[t152]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=152s
[t167]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=167s
[t170]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=170s
[t172]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=172s
[t177]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=177s
[t233]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=233s
[t259]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=259s
[t316]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=316s
[t330]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=330s
[t331]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=331s
[t336]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=336s
[t400]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=400s
[t421]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=421s
[t436]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=436s
[t444]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=444s
[t488]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=488s
[t518]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=518s
[t596]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=596s
[t638]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=638s
[t648]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=648s
[t668]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=668s
[t761]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=761s
[t786]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=786s
[t791]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=791s
[t796]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=796s
[t837]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=837s
[t853]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=853s
[t858]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=858s
[t918]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=918s
[t951]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=951s
[t967]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=967s
[t972]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=972s
[t1007]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1007s
[t1028]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1028s
[t1037]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1037s
[t1123]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1123s
[t1158]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1158s
[t1218]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1218s
[t1248]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1248s
[t1301]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1301s
[t1320]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1320s
[t1325]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1325s
[t1340]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1340s
[t1345]: https://www.youtube.com/watch?v=dpofIAFX2wM&t=1345s

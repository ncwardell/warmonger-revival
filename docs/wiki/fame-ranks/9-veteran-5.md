---
title: "Veteran [5]"
type: "fame-rank"
id: 9
status: "complete"
missing: []
sources: ["client: FameRank.cdb rank 9", "client: Level_Table.cdb row 8 fame_threshold@0c (FUN_005cde32)", "docs: [[gameplay/crush-patch-notes]] (CO rank structure: Soldier 600–55,410, Veteran 55,411–5,117,346 fame; Officer, General, Imperator, Marshal, King by ranking; WM thresholds equal the CO numbers)"]
name_key: "FameRank_9"
ui_key: "Veteran [5]"
min_fame: 5117346
next_min_fame: 15863773
requirement: {"min_fame": 5117346}
---
<!-- generated:start -->
<!-- generated-keys: title=65d27a type=41af97 id=0ade7c sources=09db13 name_key=102ed4 ui_key=65d27a min_fame=5d8dc7 next_min_fame=fbde3e requirement=88bb94 -->
|  |  |
|---|---|
| **Rank** | `9` (rec+0x656) |
| **Fame from** | 5,117,346 |
| **Next rank at** | 15,863,773 |

### How ranks work

The client counts the `Level_Table` rows whose `fame_threshold` is at most the character's fame (`FUN_005cde32`). Ten rows have a threshold (600 up to 15,863,773, ×3.1 per step), so fame alone reaches rank 10 at most. In Crush Online the top ranks (Officer to King) went by ranking and land; the thresholds are exactly the Crush numbers ([[gameplay/crush-patch-notes|Crush patch notes]]). Rank 10 *Officer [1]* has both a client threshold and the Crush ranking rule. A 2018 Warmonger character sheet shows *Officer [5]* at 81,500 fame ([[gameplay/progression-and-economy|Progression]] §1), far below that threshold, so Warmonger also gave the Officer ranks by ranking (*inferred*).

### All ranks

| rank | name | fame from | held by |
|---|---|---|---|
| 0 | [[wiki/fame-ranks/0-novice\|Novice]] | 0 |  |
| 1 | [[wiki/fame-ranks/1-soldier-1\|Soldier (1)]] | 600 |  |
| 2 | [[wiki/fame-ranks/2-soldier-2\|Soldier (2)]] | 1,860 |  |
| 3 | [[wiki/fame-ranks/3-soldier-3\|Soldier (3)]] | 5,766 |  |
| 4 | [[wiki/fame-ranks/4-soldier-4\|Soldier (4)]] | 17,875 |  |
| 5 | [[wiki/fame-ranks/5-veteran-1\|Veteran (1)]] | 55,411 |  |
| 6 | [[wiki/fame-ranks/6-veteran-2\|Veteran (2)]] | 171,775 |  |
| 7 | [[wiki/fame-ranks/7-veteran-3\|Veteran (3)]] | 532,502 |  |
| 8 | [[wiki/fame-ranks/8-veteran-4\|Veteran (4)]] | 1,650,757 |  |
| 9 | **Veteran [5]** | 5,117,346 |  |
| 10 | [[wiki/fame-ranks/10-officer-1\|Officer (1)]] | 15,863,773 | individual ranking 25–73 (Crush Online staff) |
| 11 | [[wiki/fame-ranks/11-officer-2\|Officer (2)]] | – | individual ranking 25–73 (Crush Online staff) |
| 12 | [[wiki/fame-ranks/12-officer-3\|Officer (3)]] | – | individual ranking 25–73 (Crush Online staff) |
| 13 | [[wiki/fame-ranks/13-officer-4\|Officer (4)]] | – | individual ranking 25–73 (Crush Online staff) |
| 14 | [[wiki/fame-ranks/14-officer-5\|Officer (5)]] | – | individual ranking 25–73 (Crush Online staff) |
| 15 | [[wiki/fame-ranks/15-general\|General]] | – | individual ranking 4–25 (Crush Online staff) |
| 16 | [[wiki/fame-ranks/16-imperator\|Imperator]] | – | individual ranking 1–3 (Crush Online staff) |
| 17 | [[wiki/fame-ranks/17-senator\|Senator]] | – |  |
| 18 | [[wiki/fame-ranks/18-marshal\|Marshal]] | – | 20 per nation (8 after a later council); from 15 Dec 2016 every fort owner (Crush Online staff) |
| 19 | [[wiki/fame-ranks/19-king\|King]] | – | one per nation (Crush Online staff) |

Achievements that count fame: [[wiki/achievements/22-fame-cumulative|Fame Cumulative]], [[wiki/achievements/23-achive-fame|Achive Fame]].
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

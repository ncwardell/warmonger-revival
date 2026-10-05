---
title: "Battle Arena monthly ranking rewards"
---

# Battle Arena monthly ranking rewards

Source: a Crush Online forum thread from 17 Oct 2016 ([thread][t231]) with two in-game screenshots taken in a Fortress at 13:26 on 17 Oct 2016, both opened beside the Ranking window and a system mail ([img A][imgA] reward tab, [img B][imgB] ranking tab). This was during the Crush Online launch period. Later Warmonger rules may differ: see [[events-and-schedules]] §2 and [[pvp-and-matches]] §3.

## Monthly arena reward table

Ranking window → `Arena(Monthly)`, **Reward** button ([img A][imgA]). *image*

| Final monthly rank | Reward |
|---|---|
| 1st | 20,000 jewels |
| 2nd | 10,000 jewels |
| 3rd | 5,000 jewels |
| 4th–10th | 1,000 jewels |
| 11th–50th | 200 jewels |
| 51st–100th | 100 jewels |
| 101st+ | nothing listed |

- Payment timing: the monthly reward is paid **after the last day of the month** ([img A][imgA]). *image*
- The thread does not say which jewel colour. [[events-and-schedules]] says WoW monthly ranking pays in **yellow** jewels, but that is a different ranking. *guess*

## Weekly arena payment

- A weekly payment also exists. It arrives as a **system mail**: sender `SYSTEM`, title "Weekly arena payments", and a one-line body saying the payments were delivered. The screenshot shows the mail with no attachment and money 0, so the reward had probably been collected already ([img A][imgA], [img B][imgB]). *image*
- The poster got **10 medals** from the weekly mail while ranked **51st–100th** ([thread][t231]). The client calls the medal item 1007 `Medal : Arena` (`Item_Base`). *guide* / *client*
- The thread gives no weekly amounts for the other rank bands.

## Ranking window (Arena, monthly)

Columns: **Rank · Player · Win / Lose · Point · Fluctuation**, where Fluctuation is the rank change shown with ▲/▼ n. Each page holds 15 rows, with first/prev/next/last paging ([img B][imgB]). *image*

Sample values on 17 Oct 2016 ([img B][imgB]), useful for sizing points per win. *image*

| Rank | W/L | Points |
|---|---|---|
| 1 | 6/0 | 186 |
| 2 | 6/0 | 144 |
| 3 | 12/5 | 144 |
| 4 | 6/0 | 132 |
| 5 | 6/0 | 108 |
| 6 | 5/0 | 105 |
| 7 | 9/0 | 105 |
| 8–9 | 6/0 | 102 |
| 10 | 5/0 | 95 |
| 11 | 6/0 | 90 |
| 12 | 5/0 | 85 |
| 13 | 6/0 | 84 |
| 14 | 6/0 | 78 |
| 15 | 7/0 | 72 |

- The points per match vary: 6 wins gave anywhere from 78 to 186. A reply in the thread mentions a single arena game worth **35 points** ([thread][t231]). So points are probably scaled by something such as opponent rating, kills or damage, not a flat amount per win. *guess*
- A player in the same thread had **3,252 points** a week later ([thread][t231], post of 24 Oct 2016). *guide*

## Access and timing (forum posts)

- The Battle Arena NPC stands on the top/middle of a **Fortress**. It was disabled at the time ([thread][t231], Elderwillow, 17 Oct 2016). *guide*
- One player said the arena seemed to start every day at **12:00 PT** while in a fortress. A second player tested 21:00 and 12:00 CET and got no pop-up ([thread][t231], 24 Oct 2016). The later Warmonger schedule is in [[events-and-schedules]]. *guide*

## Fortress scene details from the screenshots

- The **Warehouse Manager** NPC is named **Kaysa**. It stands near the central pillar of the Fortress plaza, north of the Mail box ([img A][imgA]). *image*
- A **Mail box** object (client unit **218** `Mail box`, `UnitDB`) stands in the same plaza. Its target frame reads **10000 / 10000 (+500)**. This is the object's HP/shield frame, **not** a mailbox item cap. `UnitDB` row 218 holds 1080 in the three i16 columns @b0–b4, so the 10000 comes from the server. *image* / *client*
- The minimap header reads `Fortress`. Coordinates cannot be read from the image.

## Client cross-reference

| What | Client id | Table |
|---|---|---|
| Battle Arena field | 140 (`SceneList` type 4) | `FieldNames` / `SceneList` |
| Battle Arena zone | ZoneDB 5 `Battle_Arena_01` (800×320 → 991×447); ZoneDB 148 `new_arena` | `ZoneDB` |
| Arena NPC (talk `Quest_Talk_Default_Arena`, profile `NPC_Instructor`) | unit 240, title `TitleName_18` | `UnitDB` |
| Battle Arena quests | 839, 843 | `Quest` |
| Medal : Arena | item 1007 | `Item_Base` |
| Battle Arena Scroll | item 910 | `Item_Base` |
| Box of the Arena Help | item 1050 | `Item_Base` |
| Mail box | unit 218; summon scroll item 923 | `UnitDB` / `Item_Base` |
| Warehouse Summon Scroll | item 921 | `Item_Base` |
| Start notices | `system_msg` 16 `Strdef_BAT_START`, 231 `Strdef_BAT_START_PreNotice` (5 min warning) | `system_msg` |

The client strings say nothing about the reward amounts. The table above is the only source for them. *client*

[t231]: http://www.crush-game.com/forum/threads/is-there-a-way-to-stop-battle-arena-weekly-monthly-reward.231/
[imgA]: http://i.imgur.com/IHj9yeD.jpg
[imgB]: http://i.imgur.com/fPJOKRS.jpg

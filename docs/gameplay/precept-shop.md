---
title: "Precept shop and precept quests"
---

# Precept shop and precept quests

A **precept** is a scroll that you buy and then use to start a random repeatable quest. The quest is named "Rank[D/C/B] Crafting" and pays out medals and Spellstones. This page covers the Crush Online era (October 2016) and checks it against the decoded Warmonger client tables.

Sources:
- A forum thread by *kawe*, 13–19 Oct 2016 ([thread][t97], [archived copy][t97a]).
- One screenshot in that thread ([img][img]). It shows the shop window, the quest log and quest detail, the quest tracker and the Fortress minimap. The player is level 30 and stands next to Freya.

Tags: *image* = read from the screenshot. *guide* = a player post. *client* = decoded client table. *guess* = our inference.

## 1. Shop prices

| Scroll | Price in the screenshot (gold) | Client item ids (`Item_Base`, kind 44 "Quest precept") | Client buy price | Starts quest id(s) (`opt1_value`) |
|---|---|---|---|---|
| Rank[D] precept | **4,650** *image* ([img][img]) | 1201, 1202, 1203, 1204 "D Rank Quest" | 10,000 | 800, 801, 802, 803 |
| Rank[C] precept | **9,300** *image* ([img][img]) | 1251–1255 "C Rank Quest" | 25,000 | 811, 812, 813, 814, 815 |
| Rank[B] precept | **18,600** *image* ([img][img]) | 1301, 1302 "B Rank Quest" | 50,000 | 0 (no quest linked) |

- In the 2016 shop the prices run 1 : 2 : 4. Each window slot sells a stack of 1 *image* ([img][img]). The later client data runs 10k : 25k : 50k *client* (`Item_Base` buy_price@20, currency 2 = gold).
- Neither ratio comes out as the other times one shop multiplier: 4,650/10,000 = 0.465, but 9,300/25,000 = 0.372. Either the base prices changed between 2016 and the later client, or the 2016 server set its own prices. *guess*. For the later fortress price multiplier, see [[progression-and-economy]].
- Client shop **289** (`Npc_Carry`) sells only 1201–1204 and 1251–1253. It sells no B precept, and 1254/1255 point to quests 814/815, which are not in `Quest.tsv`. UnitDB 200 (Oracle of Knowledge) points to shop 289 *client*. So in the client, the precept seller is **Freya** herself. *client + guess*

## 2. How the quest works

- Each precept gives a **randomly generated** quest. The type of reward depends on the rank *guide* ([post #1][p1]):

| Precept | Medals mostly paid | Medal count | Spellstone D count |
|---|---|---|---|
| D | Bronze (`Item_Base` 1000) | 1–5 | 20–150 |
| C | Silver (1001) | 1–5 | 20–150 |
| B | Gold (1002) | 1–5 | 20–150 |

Source: *guide* ([post #1][p1]). The item ids are *client*.

- If a quest's reward or objective doesn't suit you, **drop it and buy another precept** to re-roll. Boss-kill objectives are the hardest *guide* ([post #1][p1]).
- You can have **one** precept quest at a time. It shows in red in the quest log as "Rank [D/C/B] Crafting", and you must finish or drop it before you can use another scroll. Otherwise you get "You can not receive this quest anymore" *guide* ([post #4][p4], [post #2][p2]). One player suggested a workaround for a stuck state: drop the quest, relog or fully restart, then buy a fresh scroll *guide* ([post #3][p3]).
- The objective "win a territorial war" means attacking an enemy-owned land or defending your own. Taking a grey (NPC) land does **not** count *guide* ([post #6][p6]).
- In the quest log, precept quests get their own group, **"Precept"**, below "Sub" *image* ([img][img]).

## 3. Example rolled quest (screenshot)

**Rank[C] Crafting** *image* ([img][img]):

| Step | Objective | Client cross-reference |
|---|---|---|
| 1 | Kill Ghost 0/10 | `UnitDB` kill group **10029** = Black Ghost 654, Red Ghost 655 (Ghost Fortress, field **124**) *client* |
| 2 | Kill Elite Ghost 0/10 | kill group **10030** = Elite Black Ghost 656, Elite Red Ghost 657 *client* |
| 3 | Talk to Freya | `Quest_QuickText_R_FREYA` *client* |

| Reward ("Basic" row; the "Select" row is empty) | Count | Probable client id |
|---|---|---|
| Medal (a star with a red centre) | 1 | Silver medal 1001, as "C → mostly Silver" suggests *guess* |
| Spellstone [D] (a blue stone with a "D" tag) | 100 | Blue Passion Fragments [D] **601** (blue icon, `Items_26.png` #0) *guess* |

This roll is **not** in the client's `Quest.tsv`. Its kill-count objectives don't match any of the client's Rank C rows. The 2016 server generated these quests itself *guess*.

## 4. Precept quests in the client (`Quest.tsv`)

All rows below are *client*. They share title key `Quest_Title_1299` (D) or `Quest_Title_1300` (C), with kind 6, fields map1–6 = **120 (Fortress)**, next_quest? = 720, pre1 = type 4 / a = **30**, and a final step "return to Freya".

| Quest | Rank | obj1 (type, a, b) | Rewards (type 1 = item, `class flag 11`) | rew3 |
|---|---|---|---|---|
| 800 | D | 2, 5, 10 | Potion of Health [A] 887 ×25, Potion of Mana [A] 891 ×25 | type 5, 100 |
| 801 | D | 34, 0, 7 | Blue Passion Fragments [D] 601 ×50, Red Passion Fragments [D] 611 ×30 | — |
| 802 | D | 31, 3, 5 | 601 ×50, 611 ×30 | — |
| 803 | D | 1, 5, 3 | 601 ×50, 611 ×30 | — |
| 811 | C | 15, 4, 3 | 601 ×80, 611 ×40 | type 5, 100 |
| 812 | C | 15, 3, 2 | 601 ×80, 611 ×40 | type 5, 100 |
| 813 | C | 15, 2, 3 | 601 ×80, 611 ×40 | type 5, 100 |

- pre1 type 4, a = 30 is probably a **minimum level of 30**. The player in the screenshot is level 30 *guess* ([img][img]).
- rew3 type 5 = 100 is probably **fame** (`Quest.tsv` header guess) *guess*.
- In the client, D and C pay a **fixed** amount of Passion fragments and pay no medals. In 2016 they paid random medals and spellstones *client* vs *guide*. A revived server has to choose between the two (see the proposed rules below).

## 5. Freya, Oracle of Knowledge: location

- The NPC is labelled "Freya", title "‹Oracle of Knowledge›". She stands in the **Fortress** (minimap header "Fortress") on the plaza just south of the central pillar *image* ([img][img]).
- On the minimap, the player's view frame (and so Freya) sits **just below the centre** of the fort, with the **mail box** icon to the east, the **auction/gold** icon just north, and the **blue portal** icon just south. The portal sits at the top of the long tail toward the south-east *image* ([img][img]). The image gives no coordinates. The client has no NPC placement data (see the [[navmesh]] spec).
- Client: `UnitDB` units **198, 199, 200** all use name key `UnitName_200`, portrait `Oracle_of_Knowledge.dds` and talk script `Quest_Talk_Default_Oracle`. Only **200** has a shop (289) *client*. Item 2564 "Letter to Oracle of Knowledge" and quest 46 "To Oracle of knowledge" lead to her *client*.

## 6. Other numbers in the screenshot

- The tracker shows "Defensive aggression": kill **Slayer Komodo ×1**, then talk to Freya. Slayer Komodo = units 675/736/1213, and 675 is in kill group 10016 *image* ([img][img]) + *client*. This quest title is not in the client's `Quest.tsv`.
- The tracker also shows "Battle with Legion members No. 2": battle with **10** legion members, then return to **Kelsey** *image* ([img][img]). In the client this is quest **755** (obj type 23, a=2, b=1; the "10" is not in the row) *client*. Note the spelling: the screenshot says *Kelsey*, while [[maps-and-dungeons]] says *Kesley*.
- A banner reads "Attack started in **Cold Breath**", which is field **70** (`FieldNames`) *image + client*.

[t97]: http://www.crush-game.com/forum/threads/psa-precept-quest-medals-and-spellstones.97/
[t97a]: https://web.archive.org/web/20161113032247/http://www.crush-game.com:80/forum/threads/psa-precept-quest-medals-and-spellstones.97/
[img]: http://i.imgur.com/ST4OtVY.jpg
[p1]: https://web.archive.org/web/20161113032247/http://www.crush-game.com:80/forum/posts/328/permalink
[p2]: https://web.archive.org/web/20161113032247/http://www.crush-game.com:80/forum/threads/psa-precept-quest-medals-and-spellstones.97/#post-940
[p3]: https://web.archive.org/web/20161113032247/http://www.crush-game.com:80/forum/threads/psa-precept-quest-medals-and-spellstones.97/#post-949
[p4]: https://web.archive.org/web/20161113032247/http://www.crush-game.com:80/forum/threads/psa-precept-quest-medals-and-spellstones.97/#post-956
[p6]: https://web.archive.org/web/20161113032247/http://www.crush-game.com:80/forum/threads/psa-precept-quest-medals-and-spellstones.97/#post-1086

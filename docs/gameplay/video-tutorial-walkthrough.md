---
title: "Video notes: tutorial walkthrough (Bravely Forward 2)"
---

# Video notes: tutorial walkthrough (Bravely Forward 2)

Notes taken from [Warmonger is a Free-to-Play PVP MMO with MOBA-style combat](https://www.youtube.com/watch?v=CqCY2ULeVGw) (Bravely Forward 2, streamed 2018-06-20, 63:54). The streamer makes an **Arslan Guardian** and plays the starter chain from character creation to the Darkstar Fortress (about 3:20 to 33:30). Everything below is a video observation unless it is tagged *client* (read from the decoded tables in `data/tables/`). Related pages: [[gameplay/npc-locations|NPC locations]], [[gameplay/videos|Videos]], [[gameplay/progression-and-economy|Progression and economy]].

Timestamps link to the moment. They are good to about ±3 s, because frames were sampled every 5 s.

Ids: quest ids are `Quest.tsv` ids; dialogue keys are in `QuestTalk.tsv` and `StringAll_Eng.cdb`. The on-screen titles match `Quest_Title_*` strings exactly, so each step below is matched to a quest row with high confidence. Unit ids are from `UnitDB.tsv` and item ids from `Item_Base.tsv`.

## 1. Tutorial and early quest flow

> [!note] There is no separate tutorial map in this video
> After **Enter World** the new character appears straight in the **Training Ground** (field 89, the Arslan copy) next to Shaia. Field 117 "Beginner's Training Ground" (`FieldNames.tsv`) is never visited. The "tutorial" is the chain of quests 1 → 12 plus a set of `kind 2` help quests (700, 701, 704, 706, 712, 718, 719, 722) that pop up on their own and complete when the player uses the UI.

> [!important] Quest exp shown in the game is lower than the `Quest.tsv` value
> Every reward window and every "+N" exp popup in this video shows the table value **divided by 1.1 for `kind 0` (main) quests and by 1.2 for `kind 1` (side) quests**. Examples: Q1 550 → 500, Q3 3850 → 3500, Q5 2750 → 2500 (the "+2500" popup confirms it), Q7 10010 → 9100, Q9 11440 → 10400, Q100 8880 → 7400, Q101 17400 → 14500, Q102 67200 → 56000. Gold (`rew type 4`) is shown unchanged (Q100 5000, Q101 10000). The server should award the reduced figure, or store the reduced figure. *video + client*

Reward types seen (*client*, confirmed by what the windows show): `rew type 2` = exp; `type 4` = gold; `type 1` with `a = 0` = a fixed item (`b` = item, `c` = count); `type 1` with `a = 11` = one item **the player chooses** ("Choose Reward" row). Q10's Oracle Set rows use `a = 1/4/5`, which looks like a per-class pick (Guardian = 1?) *guess*.

Quest chaining (*client*): `c6@04` is the quest's place in the chain and `c4@08` is the place it follows, so the main chain is c6 = 1 → 2 → 3 → 4 → 5 → 6 → 99 → 8 → 9 → 10 → 11 (quests 1, 2, 3, 4, 5, 6/45, 7, 9, 10, 11, 12). The side quests hang off it: c4 = 99 gives 101 and 107, and c4 = 9 gives 102.

### Steps

1. **Character creation** [1:38](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=98s)–[3:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=200s). The nation is chosen first (Arslan). Then the class: Guardian, Saint, Punisher, each with a weapon picked from the class's list (Saint: Magical Life Wand, Thunder Wand and others; Guardian: Magical Demolition Hammer). Then appearance (hair, face, eyes and colours) and a name. The Guardian's skill preview shows Q Soul Infestation, W Aura of Demise, E Severe Blow, R Dark Transformation. On character select there is 1 "Available" slot and 3 "Locked" slots ([3:15](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=195s)).
2. **Spawn and Q1 "On to a promising start"** (quest **1**, `Quest_Title_630`) [3:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=200s). The character spawns in the Training Ground at about **(435.5, 3648)**, roughly 14 units south of Shaia. A quest dialogue opens on its own with the player's line "Oops, late again, Shaia will be grumbling" and a reward panel showing 500 exp. A **Tip** window then says to talk to Shaia with a right click ([3:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=220s); `Quest_HelpText_1`). Tracker: "Talk to Shaia" (`obj type 4`, unit 201). On completion the player is at level 1 with HP 450 and MP 700.
3. **Talk to Shaia (201)** [4:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=240s). The QuestTalk 630 lines play: she asks why you are always late and sends you for slime mucus for Biologist Floyd. Q1 completes and **Q2 "The Slime is mine"** (quest **2**, `Quest_Title_631`) starts: Slime mucus obtained 0/3, then bring them to Floyd. Help quest **700 "Basic Combat Lesson 1"** ("Use a basic attack", 200 exp) appears with a Tip ("attack the slime with a right click").
4. **Slimes** [4:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=295s). Killing the first Slime (604) gives **level 2** at once: 500 (Q1) + 200 (Q700) = 700 = `Level_Table` exp for level 1. Help quest **701 "Basic Combat Lesson 2"** ("Use one of your Abilities", 300 exp) follows. Each kill drops one Slime Mucus (item 2550) until 3/3. Help quest **722 "Juicy Potions"** ("Use a Health Potion [D]" on key D, "Use a Mana Potion [F]" on key F; 500 exp plus 10 of each potion 883 and 884) appears at about [5:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=340s).
5. **Floyd (239), Q2 turn-in** [7:06](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=426s). Floyd's line is QuestTalk 632. Reward: 1200 exp and Gloves of Life (403), which gives level 3 (HP 610, MP 750). She offers **Q3 "The task at hand"** (quest **3**, `Quest_Title_632`) right away [7:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=450s): "Hunt the bees and snakes around the training hill" for Bee Needle 0/5 and Cobra Leather 0/5, then bring them to Floyd. Reward shown: 3500 exp and Helmet of Life (401). Help quest **704 "Equip Gear"** ("Open your Inventory [I] and equip a Gear", 600 exp) appears.
6. **Bees (731) and Cobras (732)** [8:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=480s)–[9:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=585s). The drops show in chat as Bee Needle (2552) and Snake Leather (2551). The tracker names the second one "Cobra Leather". Level 4 at about 8:40 and levels 5–6 by 12:20.
7. **Q3 turn-in at Floyd, then Q4 "Go to Shaia"** (quest **4**, no objectives; Floyd → Shaia) [9:46](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=586s). Floyd thanks you (QuestTalk 633), and the chat shows "acquired Helmet of Life".
8. **Shaia, Q4 → Q5 "United Problem Solvers"** (quest **5**, `Quest_Title_633`) [10:07](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=607s)–[11:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=690s). The player complains about errand jobs. Shaia says he needs more training and gives him a letter to deliver to Frei. Tracker: "Talk to Frei, you can find her in the training camp." The reward is 2500 exp and Armor of Life (402) (QuestTalk 634).
9. **Training Ground → Training Camp** through the "Training Camp" portal in the south-east of the map (gate 1203) [12:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=740s).
10. **Frei (198, Oracle of Knowledge), Q5 turn-in** [12:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=770s)–[13:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=810s). This is QuestTalk 635 (`Quest_Talk_Tutorial_Speech6_*`): the player hands over the letter, Frei is surprised Shaia sent an apprentice and says she will test him first. A "+2500" exp popup appears, and the chat shows "acquired Armor of Life" and "acquired Faded Passion fragments" (1900). Help quest **28 "What does Wren do?"** (`kind 2`) appears: talk to Wren, sell a Faded Passion fragment to Wren, buy a Return Scroll from Wren. Trying to equip the gear here gives the red system message "You can't replace that weapon." ([13:35](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=815s)).
11. **Wren (238, Merchant)** [13:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=820s)–[15:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=900s). Her greeting says she is a merchant who buys and sells, and the menu has Quest / Shop / Close. In the shop the fragment sells for **315 gold**, as shown in §3. The Reinforce window was also opened by mistake ([14:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=860s)). The Return Scroll was **not** bought, so Q28 stays open for the rest of the video.
12. **Lewellyn (315, Scroll Merchant), Q100 "Hunting for Furs"** (quest **100**, `kind 1`) [15:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=910s). Floyd has vouched for the player, and Lewellyn wants Chepa fur. Objectives: White Chepa Fur 0/5, Black Chepa Fur 0/5, bring them back to Lewellyn. Reward shown: 7400 exp, 5000 gold, and a choice of Spell Necklace (397) or Necklace of Life (405).
13. **Chepas in the Training Ground** [16:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=960s)–[19:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1140s). Chepa Warriors (727) and Chepa Archers (728) live in the round clearings of the northern lobes. The drops are named "Whiter Chepa Fur" (2554) and "Black Chepa Fur" (2553), both at 100%. Level 7 at about 18:00.
14. **Q100 turn-in at Lewellyn** [19:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1170s)–[19:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1195s). Lewellyn thanks the player and offers the jewellery she made as a reward. Necklace of Life was chosen, and the player reached **level 8** with "MISSION COMPLETE: Hunting for Furs". Help quest **706 "Expand your Inventory"** appears ("Press [I] … expand it once"; 700 exp).
15. **Hint "New quests are available in the nearby area."** shown on the quest-book button [20:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1210s).
16. **Frei: quest 45 / 6 "The 1st Challenge: Chepas ahead"** [20:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1220s)–[20:35](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1235s) (QuestTalk 637). The player asks about the tests, and Frei names the first challenge: hunt down the Chepa Leaders. Accept. The tracker then reads "Talk to Shaia" (quest **45**: `obj type 4`, unit 201, from Frei 198).
17. **Shaia** [20:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1255s)–[21:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1270s). She asks whether he has finished Frei's missions, and he cannot find the leaders. She says they are in the north and wishes him luck. "Complete" turns this into **quest 7**: Hunt Chepa Warriors officer 0/1, Hunt Chepa Archers officer 0/1, Report back to Frei.
18. **Chepa Warrior Officer (710) and Chepa Archer Officer (711)** in the north-west clearing of the Training Ground, among normal Chepas [21:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1310s)–[22:15](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1335s). Each is a single kill.
19. **Frei, Q7 turn-in** [23:35](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1415s) (QuestTalk 638). He has killed the Chepas and asks what is next; Frei warns that the real test is still ahead. Reward: 9100 exp, 10× Scroll: Return (906), and a choice of Ring of Life (408, picked) or Spell Ring (400). This reaches **level 9**.
20. **Frei, Q9 "Find the missing Scout"** (quest **9**) [23:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1425s) (QuestTalk 639). A scout carrying important information is long overdue, and the Guard will explain. Objectives: Talk to the Guard, then find the Scout in Corpse incineration. Reward shown: 10400 exp and a choice of 100× Potion of Health [C] (885) or 100× Potion of Mana [C] (889).
21. **Guard (215)** at the Corpse incineration portal (gate 1503), in the south of the camp [24:02](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1442s). His idle speech bubble warns that the Abyss is a labyrinth and a PK area. His dialogue (QuestTalk 640) begins by saying the player is the one being sent into the Abyss.
22. **Portal → Corpse incineration (field 99)** [24:12](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1452s). The player arrives beside a "Training Camp" return portal (gate 1500 at 306.03, 2254.17, *client*). Mobs: Skeleton Warrior (700), Skeleton Archer (701), Elite Skeleton Warrior (702) and Elite Skeleton Archer (703). Level 10 at about 26:30.
23. **Scout (238, Trigger 9901)** [26:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1590s)–[26:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1605s) (QuestTalk 641). He is glad to be found and asks whether the Oracle sent the player. He lost a document to the skeletons, says where they are, and asks for it to be taken back to Frei. Q9 completes (`obj2 type 5` = reach the Scout trigger). **Quest 10 "Find the Secret Document"** starts: kill the Leader of the Skeleton Warriors and get the document (0/1), then give it to Frei. Side **quest 107 "Hunting Skeletons"** also appears: kill the Skeleton Warrior Leader and the Skeleton Archer Leader, then report to Frei.
24. **Skeleton Warrior Officer (704) and Skeleton Archer Officer (705)** in the south of field 99, guarded by elites [28:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1680s)–[28:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1720s). An officer's speech bubble shouts "Kill them!!". Level 11.
25. **Back to the camp** through the "Training Camp" portal [29:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1750s). The player arrives next to the Guard.
26. **Odin (335, Blue Union): quest 101 "All sorts of Fragile bones"** [29:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1770s) (accepted but not finished in the video). He needs skeleton bones. Objectives: Fragile Weak Skeleton bone 0/10 and Fragile Weak Elite Skeleton bone 0/10 (kill groups 10003 and 10004 = units 700–703), then deliver them to Odin. Reward shown: 14500 exp, 10000 gold, 10× Crystal: Blue (700), and a choice of Spell Belt (398) or Belt of Life (406). The NPC menu reads Quest / **Create** / Close (Odin is a crafter).
27. **Frei: quests 10 and 107 turned in** [29:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1790s)–[30:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1830s). The player hands over the secret document. Two "MISSION COMPLETE" banners follow. The chat lists Oracle Set (Q10 costume), Bracelet of Life (Q10 choice: 407 or Spell Bracelet 399), 20 Blue Passion Fragments [D] (601), 20 Red (611) and 10 Crystal: Blue (Q107), then Scroll: Gaia (912) and Urgent Letter (2567). Those last two are the `pre` items that start **quest 11 "An urgent message"**: "Use the Gaia Scroll in your inventory" (`obj type 13`, item 912).
28. **Wren: quest 102 "Wren's sister Wren?"** [30:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1850s). She asks whether the player is heading to the Fortress and wants a favour. Reward shown: 56000 exp, 20 Blue and 20 Red Passion Fragments [D], 10 Crystal: Blue. The tracker reads "Meet Wren in the fort", and the chat shows "acquired Hawker letter" (2563, the `pre` item of Q102).
29. **Camp → Castle (field 90)** through the north-east "Castle" portal (gate 1198) [31:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1870s). Imperial Guards (red armour, halberds) stand at the Castle entrance.
30. **Using Scroll: Gaia** [32:25](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1945s). The tooltip says "Return to Gaia". A cast bar plays, then the player lands in **Eternal River – Upper Region (field 14)**, a front-line field. An achievement "Gaia Explorer" pops up. Help quest **719 "Go to the Fortress"** appears ("Click the Nexus to get to the Fortress"; Tip "You can move to Fortress through click Nexus"), and Q11 becomes **quest 12**: "Talk to Freya".
31. **Nexus → Darkstar Fortress (field 120)** [32:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1975s). "MISSION COMPLETE: Go to the Fortress" (10000 exp, level 12). The player arrives beside Haley (217, Teleporter), whose idle bubble says she moves people around Gaia instantly.
32. **Freya (200), quest 12 turn-in** [33:05](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1985s)–[33:15](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1995s). She remarks on the journey and thanks the player for the letter. The chat shows 20 Blue and 20 Red fragments and 10 Crystal: Blue, then **level 13** (HP 1940, MP 950). New quests: help quest **712 "Take a look at the World Map"** (press M), help quest **718 "Open item reinforcement window"**, and **quest 13 "Battle preparations"** ("Talk to Cassia", unit 212) [33:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=2010s).

What the server needs to send for this flow: quest offers (an NPC with a "!" over its head, a reward panel with Basic Reward and Choose Reward rows), objective counters in the tracker, the "MISSION COMPLETE <title>" banner, "+N" exp popups, "Levelup.N" and "You acquired an X item." chat lines, and "X was destroyed." for every kill.

## 2. NPC positions

Method as in [[gameplay/npc-locations|NPC locations]] §2: the minimap camera box gives the camera centre, and the NPC name-label offset is scaled at 29.7 px/unit in x and 22.1 px/unit in y. This video is the **Arslan** copy, so no shift is needed. Error is about ±4 units. In this video the camera is often not centred on the player, so the box centre, not the player's position, is used as the reference. Zone rectangles (*client*, `ZoneDB.tsv`): Training Ground 127 = x 288–479, z 3616–3807 (192 units over 171 px); Training Camp 128 = x 288–447, z 3392–3551 (160 units).

| NPC | Unit id | Field | x | z | Sightings | Agrees with npc-locations? |
|---|---|---|---|---|---|---|
| Spawn point (new character) | – | 89 | 435.5 | 3648 | [3:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=200s) | new |
| Shaia (guide) | 201 | 89 | 433.5 | 3662 | [3:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=200s) (minimap "!" icon and label), [4:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=240s) (label); spread 1 | **No**: the table has 423.9, 3664.8, about 9 units further west. Two sightings here agree with each other. |
| Floyd (Biologist) | 239 | 89 | 371.5 | 3659 | [7:05](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=425s) | yes (370.5, 3660.6) |
| Frei (Oracle of Knowledge) | 198 | 88 | 362.6 | 3467.6 | [12:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=760s) | yes, within 4 (358.8, 3469.1) |
| Mail box | 218 | 88 | 352.8 | 3463.9 | [12:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=760s) | yes, within 5 (347.6, 3464.2) |
| Wren (Merchant) | 238 | 88 | 375.0 | 3479.3 | [12:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=760s), [20:05](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1205s) | yes (373.8, 3479.5) |
| Lewellyn (Scroll Merchant) | 315 | 88 | 380.3 | 3478.6 | same two | yes (378.9, 3478.9) |
| Odin (Blue Union) | 335 | 88 | 385.9 | 3478.8 | same two | yes (387.1, 3478.9) |
| Owen (Red Union) | 337 | 88 | 392.3 | 3475.1 | [20:05](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1205s) | within 5 (393.7, 3470.4) |
| Guard (Corpse incineration gate) | 215 | 88 | 383.2 | 3439.1 | [24:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1440s) (minimap "?" icon) | yes (385.0, 3436.4) |
| Scout | 238 | 99 | – | – | [26:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1590s) | use Trigger 9901 (465.27, 2259.45), *client* |

Not measured but seen: the Imperial Guards (189–197) at the Castle entrance gate ([31:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1870s)); Haley and Freya in the Fortress arrival plaza ([33:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1980s)); and the Nexus in Eternal River – Upper Region, east of the arrival point ([32:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1965s)).

## 3. Other facts by system

### Player stats (Arslan Guardian, Magical Demolition Hammer)

| Level | HP | MP | When | Gear note |
|---|---|---|---|---|
| 1 | 450 | 700 | [3:25](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=205s) | novice set |
| 2 | 530 | 725 | [5:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=300s) | |
| 3 | 610 | 750 | [7:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=450s) | |
| 4 | 690 | 775 | [8:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=520s) | |
| 6 | 980 | 775 | [12:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=740s) | some Life gear equipped |
| 7 | 1060 | 800 | [18:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1080s) | |
| 8 | 1140 | 825 | [20:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1200s) | |
| 9 | 1220 | 850 | [24:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1440s) | |
| 10 | 1300 | 875 | [26:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1590s) | |
| 11 | 1380 → 1780 | 900 | [28:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1720s), [29:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1790s) | +400 after equipping Necklace and Ring of Life (+200 HP each per tooltip) |
| 12 | 1860 | 925 | [33:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1980s) | |
| 13 | 1940 | 950 | [33:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1990s) | |

HP grows by **+80 per level** and MP by **+25 per level** for the Guardian. Levels 1–4 fit HP = 370 + 80·L. *inferred*. These are class values; `Level_Table`'s linear hp?/mp? columns (130 + 30/level) do not match them.

Character sheet at level 2 ([5:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=340s)): Nation Arslan, Legion –, Class Guardian, Rank Novice, Fame 0, Arena 0 P; HP 530 (regen 44), MP 725 (regen 7), Attack 89, Ability Power 79, Armor 14, Magic Resist 10, Armor/Magic penetration 0/0%, Life Steal 0%, Spell Vamp 0, Critical Strike Damage 100%, Critical Strike Chance 0.1%, Reduced Critical Damage 5%, Reduced Area Damage 0%, Toughness 0%, Cooldown Reduction 0%, Attack Speed 528, Movement Speed 530.

Hotbar: Q/W/E/R skills; X = weapon swap; D and F = potion slots (starting with 10 each of Potion of Health [D] and Potion of Mana [D]); slots 1–6. The cooldowns shown on Q, W and R were roughly 15, 22–25 and 25–60 s.

Item tooltips (*video*, in our words): Novice Helmet (equipped) gives Health Regeneration +3, Mana +50, Mana Regeneration +1 and Movement +9%; it cannot be reinforced and its buy price is 0. Helmet of Life gives Armor +10, Magic Resist +5, Mana +110 and Movement +10%; it is Bound and sells for 630. Necklace of Life and Ring of Life each give Attack +40, Health +200 and Health Regeneration +8. Spell Necklace gives Ability Power +30, Health +200 and Health Regeneration +8. All of these say "Binds when picked up".

### Monsters and damage

| Monster | Unit id | Where | Notes |
|---|---|---|---|
| Slime | 604 | Training Ground, south | drops Slime Mucus (2550) for Q2 |
| Bee / Cobra | 731 / 732 | Training Ground, middle | Bee Needle 2552 / Snake Leather 2551 for Q3; a Bee hit the player for 15 |
| Chepa Warrior / Chepa Archer | 727 / 728 | Training Ground, north clearings | furs 2554 / 2553 for Q100; they hit for 22 |
| Chepa Warrior Officer / Archer Officer | 710 / 711 | Training Ground, north-west clearing | one each for Q7 |
| Skeleton Warrior / Archer, Elite Skeleton Warrior / Archer | 700 / 701, 702 / 703 | Corpse incineration (99) | groups 10003 / 10004; they hit for about 19 |
| Skeleton Warrior Officer / Archer Officer | 704 / 705 | Corpse incineration, south | Q10 / Q107 |

The player's basic hits were 88 against Slimes, 93 against Cobras, 98–101 against Chepas, 104 against Chepa Archers and 109 against Skeletons, with occasional larger hits such as 120. No monster levels or HP numbers are shown on screen, only bars.

### Shop and economy

- **Wren (238), shop 287 at the Training Camp** ([14:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=860s)): the shop showed Potion of Health [D], Potion of Mana [D] and Scroll: Return, each at **79 gold**. `Npc_Carry` 287 also lists 945 (Auto decomposition hammer [D]), which was not shown. `Item_Base` buy prices are 10, 10 and 80, so displayed prices do not come straight from `Item_Base`. *video vs client*
- Selling 1 Faded Passion fragment gave **315 gold** (Item_Base sell price 50). The Helmet of Life tooltip says Sell Price 630 (Item_Base 100). Both are **×6.3** the table value. *video vs client*
- Gold was 0 until that sale, even though quest 5 lists `rew type 4` 500. The Q5 reward panel showed no gold either, so treat Q5's 500 as not awarded. *video*
- The Shop window has a **Repurchase** button. Selling opens a "Sell Item" box with a count spinner and the sell price.
- The inventory has two tabs, a 5-wide grid with locked expansion rows, Sort / Reinforce / Decompose / Trash buttons, and gold and a second currency at the bottom.

### UI, system and chat messages seen

- Red centre text: "You can't replace that weapon." and "Skill is not ready yet."
- System line in chat: "There is no Legion for you to join." ([6:45](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=405s)).
- Chat lines: "Levelup.N", "You acquired an <item> item.", "<monster> was destroyed." Other players' chat shows as "[name]: text"; a shout appears as "[Soldier [4]] name: …" in large orange text at the top of the screen.
- Banners: "MISSION COMPLETE" + quest title; "ACHIEVEMENTS COMPLETE" + "Gaia Explorer". A floating "HP +30 / MP +10" text appeared over the player at a level-up ([19:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1195s)).
- Each quest-tracker entry has an **Auto Move** button that paths to the objective, plus a Quest Info button. A quest-giver shows "!" over its head and a hand-in shows "?".
- NPC dialogue buttons are Quest / Shop (or Create) / Close, and Next → Accept or Complete. The reward panel appears on the right.
- World map (M) ([6:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=360s)): the Training Camp, Castle and Training Ground form an island at the top. Clicking a land shows "During the war" with defend side and attack side; at 6:00 Echo of Earth had defend Erion, attack Arslan and 39:31 remaining. An "Auto move" button is on the map.
- Keys the streamer tries ([5:30](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=330s)–[6:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=400s), from the commentary, so treat these as approximate): C = character sheet, I = inventory, M = world map; other letters open the friend list and the ranking.

### Teleports used

| From | Via | To | Time |
|---|---|---|---|
| Training Ground 89 | south-east portal "Training Camp" (gate 1203) | Training Camp 88 | [12:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=740s), [19:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1150s) |
| Training Camp 88 | south-west portal "Training Ground" (gate 1202) | Training Ground 89 | [16:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=960s) |
| Training Camp 88 | south portal "Corpse incineration" (gate 1503) | Corpse incineration 99 | [24:12](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1452s) |
| Corpse incineration 99 | "Training Camp" portal next to the arrival point (gate 1500) | Training Camp 88, at the Guard | [29:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1750s) |
| Training Camp 88 | north-east portal "Castle" (gate 1198) | Castle 90 | [31:10](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1870s) |
| Castle 90 | item Scroll: Gaia (912), "Return to Gaia", with a cast bar | Eternal River – Upper Region 14 | [32:25](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1945s) |
| Field 14 | Nexus (click) | Darkstar Fortress 120 | [32:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1975s) |

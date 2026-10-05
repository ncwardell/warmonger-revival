---
title: "Video notes: character creation and tutorial (ZonderCoRe, June 2018)"
---

# Video notes: character creation and tutorial (ZonderCoRe, June 2018)

Source: [Warmonger #1 Gameplay, primera hora de juego](https://www.youtube.com/watch?v=-DMnhYzYiC0) (ZonderCoRe, uploaded 2018-06-19, 52:27). It shows the first hour after the June 2018 relaunch on an **Erion** Guardian named ZonderCoRe, grouped with a friend (WATTXA, a Saint). The commentary is Spanish and adds nothing that the screen does not show. The game UI is English. Related pages: [[gameplay/videos|Videos]], [[gameplay/npc-locations|NPC locations]], [[gameplay/classes-and-legions|Classes and legions]], [[testing]].

Every timestamp below links to the moment. Frames were read at 720p: one every 2 s during character creation, one every 5 s for the whole video, with crops of the quest tracker, chat log, HP/MP bars and minimap. Ids come from the client tables in `data/tables/` (`Quest.tsv`, `QuestTalk.tsv`, `Create_Char.tsv`, `Item_Base.tsv`, `WeaponBase.tsv`, `Skill_Base.tsv`) and the English string table. Confidence tags: *video* = read off the screen; *client* = from a client table; *inferred* = our reading of how the two fit together.

> [!important] What a server needs from this video
> - **No tutorial map.** After *Enter World* the character loads straight into the nation's **Training Ground** (field 93 for Erion), about 30 units north-west of the gate to the Training Camp. Field 117 (`Beginner's Training Ground`) is never visited. *video*
> - **Quest 1 is offered on arrival.** The opening dialogue (QuestTalk 684, the character's own lines) pops up with a Quest Reward panel before the player does anything. *video + client*
> - **The quest chain follows `Quest.tsv` row order:** 1 → 2 → 3 → 4 → 5 → 6/7 → 9 → 10 → 11/12. "Lesson" quests (kind 2: 700, 701, 722, 704, 706, 712, 718, 713, 719, 723) run alongside it. Side quests (kind 1: 100, 101, 107, 102) are offered by camp NPCs. *video + client*
> - **The EXP shown in the reward panel is the table value ÷ 1.1:** quest 1 shows 500 (table 550) and quest 2 shows 1,200 (table 1,320). Levelling agrees with the displayed values. *video*

## 1. Character creation

The video opens on the class page. Nation choice happened before the recording starts: the top icon in the left-hand summary column is the Erion emblem, and the character list later shows "Erion". The left column fills with one icon per finished step (nation, class, hair, face, costume, weapon). *video*

| Step | Time | What the screen offers | Client match |
|---|---|---|---|
| 1. Select Class | [0:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=0s)–[0:28](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=28s) | Three class icons, left to right **Saint, Punisher, Guardian**. Each shows a short description and an "Ability" radar chart with six axes: Attack, Ability Power, Magic Resist, Movement Speed, Attack Speed, Armor. The model previews its weapons (Punisher: daggers, then a bow; Saint: flying blades). | `Create_Char` rows class 1 (Saint), 4 (Punisher) and 5 (Guardian). The fourth row, class 7 **Valkyrie**, has no weapons and **is not offered**. Description strings are `GUI_CharCreate_Comment_*`. *video + client* |
| 2. Select Appearance (1) | [0:30](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=30s)–[1:02](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=62s) | **Hair** style (a row of 3 portraits with scroll arrows), **Hair** colour (24 swatches, 6×4), **Face** (a row of 4 with scroll arrows), **Eyes** colour (24 swatches). | `face_list`, `hair_list` and `color_list` in `Create_Char` each hold 12 entries. *client* |
| 3. Select Appearance (2) | [1:04](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=64s)–[1:46](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=106s) | **Basic Costume** (2 choices), then **Part 1 / Part 2 / Part 3** colour (24 swatches each), dyeing the costume's regions independently. | Strings `GUI_CharCreate_Color_C1..C3`. *client* |
| 4. Weapon ("Selection") | [1:48](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=108s)–[2:12](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=132s) | The page is still titled "Select Class", with a "Selection" row of **three Guardian weapons**. Below it are the four skills of the selected weapon, each with its cooldown, mana cost and description. The player kept the first weapon. | See the weapon table below. *video + client* |
| 5. Name | [2:14](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=134s) | A "Character Name" box and a **Create Character** button. | — |
| 6. Select your Character | [2:18](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=138s) | Five slots: the new character ("Lv.1", "Erion", name), one **Available** and three **Locked**. Buttons: Back, Enter World, Create Character, Delete Character. | *video* |

There is no gender choice. Each class has a fixed body: Guardian male, Punisher male, Saint female (matching `UnitDB` units 5, 4 and 1). *video + client*

**Starting weapons per class** (`Create_Char` weapon columns → `Item_Base` → `WeaponBase` via option type 200). All of them are kind 31, bind-on-pickup, buy price 500, and restricted to their class. *client*

| Class | Weapon choices (item id, label) | WeaponBase id: its four skills |
|---|---|---|
| Guardian | **20001** Magical Demolition Hammer (Mace) · **20021** Magical Protect Cannon (Cannon) · **20003** Magical Crush Hammer (no label string) | 43: Soul Infestation 5036, Aura of Demise 5038, Severe Blow 5040, Dark Transformation 5041 · 63: Nimble Pursuit, Firm Hand, Buckshot, Explosive Mortar · 45: Crushing Blow, Head Butt, Howl of Victory, Unyielding Will |
| Punisher | **15007** Magical judge Dagger (Dagger) · **15004** Magical Frost Bow (Bow) | 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edges, Potential Power, Hail of Arrows, Spinning Whirlwind |
| Saint | **10017** Magical Wrath Blade (Flying Blade) · **10011** Magical adapted Dual Gun (Dual Gun) · **10001** Magical Thunder Wand (Wand) · **10002** Magical Life Wand (no label string) | 18: Blade storm… · 12: Ankle Aim… · 2: Thunderbolt… · 64: Mother Nature's Blessing… |

The Guardian screen matched this exactly: three icons in table order, with the first (20001) selected and skills 5036/5038/5040/5041 listed ([1:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=110s)). Values on screen at level 1, which the client does not hold (*video*):

| Skill | Cooldown | Mana | Effect as shown |
|---|---|---|---|
| Soul Infestation | 19 s | 135 | Basic attacks deal +10 (+0) damage and hit several enemies |
| Aura of Demise | 28 s | 180 | 45 (+0) damage to nearby enemies over 10 s, plus 1 % of own max HP per second |
| Severe Blow | 20 s | 140 | 70 (+0) damage and knock-up |
| Dark Transformation | 60 s | 340 | More HP regeneration and movement speed for 10 s |

The class descriptions on screen **end without the "[Difficulty : …]" line** that our `StringAll_Eng` strings carry. Our string table is probably from a later build. *video + client*

## 2. Starting state (level 1 Guardian)

- **HP 450 / MP 700** at level 1 ([2:45](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=165s)). Level 2: 530/725. Level 3: 610/750, still with no gear. So the Guardian gains **+80 HP and +25 MP per level** here. `Level_Table` hp/mp columns (130/70, 160/90, …) do not match these totals directly. *video*
- **Skill bar:** Q/W/E/R = the four weapon skills above, an X slot (transformation, empty), D = Potion of Health [D] ×10, F = Potion of Mana [D] ×10, and quick slots 1–6 empty. *video*
- **Gold 0** (the inventory at [8:45](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=525s) still shows 0). *video*
- The HUD has a **Help** button that opens an "Advice" list of the lessons finished so far (Basic function – Move character, Basic attack, Skill Use, QuickSlot Use; Item – Gear Wear at [6:35](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=395s)). These are the `Quest_Title_Help_<n>` strings of quests 1, 700, 701, 722 and 704. *video + client*

## 3. Tutorial and first quests, in order

"Offer" and "turn-in" dialogue ids are `QuestTalk` rows. `Quest.tsv` column `prev_quest?@20` is the **offer dialogue** and `next_quest?@34` is the **completion dialogue**. This fits every step below: quest 1 → 684/–, quest 2 → 630/632, quest 3 → 636/633, quest 4 → 789/713, quest 5 → 634/635, quest 7 → 685/638, quest 9 → 639/–, quest 10 → 641/642. Column `c18@2c` is the **turn-in NPC** (quest 2 → 239 Floyd, quest 4 → 201 Shaia, quest 5 → 198 Frei). *inferred from video + client*

In the reward panel, rewards with `rew*_a = 0` appear under **Basic Reward**, and those with `rew*_a = 11` appear under **Choose Reward** (pick one). For example, quest 100 shows 5,000 gold under Basic and a necklace pair under Choose. *video + client*

### Training Ground (field 93)

1. **[2:33](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=153s) Arrival, quest 1 "On to a promising start"** (title key 630, giver Shaia 201). Dialogue 684 opens by itself: the character is late and Shaia will grumble. The reward panel shows **500 EXP**. The objective is to talk to Shaia (`obj1_type 4`, unit 201). The quest-help tip (Help_02, "talk to Shaia with right-click") shows at [2:45](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=165s). *video + client*
2. **[2:58](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=178s) Talk to Shaia.** Dialogue 630 ("why are you always late", fetch slime mucus for Floyd) completes quest 1 ("Mission complete", [3:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=180s)) and starts two quests together:
   - **Quest 2 "The Slime is mine"** (631): kill Slime 604 for **3 Slime Mucus 2550** (100 % drop), bring them to Floyd.
   - **Lesson quest 700 "Basic Combat Lesson 1"**: use a basic attack (200 EXP). It has a tip window.
3. **[3:25](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=205s) Lesson 700 done → "Levelup.2"** (500 + 200 = 700 = `Level_Table` exp for level 1). **Lesson 701 "Basic Combat Lesson 2"** starts: use an ability; the tip shows the QWER keys (300 EXP).
4. **[3:40](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=220s) Lesson 701 done → lesson 722 "Juicy Potions":** use a Health Potion [D] and a Mana Potion [D] (keys D and F). The reward of 10 of each potion arrives at [4:15](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=255s). Level 3 comes in the same moment.
5. **[3:55](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=235s) Slime Mucus 3/3.** The tracker's "!" becomes "?".
6. **[4:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=260s) Turn in at Floyd** (Biologist, 239). Dialogue 632. The reward panel shows **1,200 EXP + Gloves of Life 403** (table: 1,320 + 403). Level 4.
7. **[4:25](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=265s) Quest 3 "The task at hand"** (632, from Floyd, offer 636) together with **lesson 704 "Equip Gear"** (open inventory and equip a piece of gear, 600 EXP). Equipping the gloves at [4:30](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=270s) completes it, and max HP rises 610 → 820.
   - Objectives: **5 Bee Needle 2552** from Bee 731 and **5 Snake Leather 2551** from Cobra 732, both 100 % drops (the tracker calls the second "Cobra Leather").
8. **[5:45](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=345s) Quest 3 complete at Floyd** (dialogue 789 hands over to the next quest). Reward: **Helmet of Life 401**, Level 5.
9. **[6:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=360s) Quest 4 "Go to Shaia"** (692, no objectives, turn-in Shaia). **[6:05](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=365s)** Dialogue 713: the character complains about gathering jobs. Quest 4 completes.
10. **[6:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=370s) Quest 5 "United Problem Solvers"** (633, offer 634: Shaia hands over a letter). The tracker reads "Talk to Frei, you can find her in the training camp." The player wandered the north of the Training Ground first (Chepa area, Level 6–7) and crossed into the **Training Camp** at about [8:15](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=495s).

### Training Camp (field 92) and back

11. **[8:30](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=510s) Turn in quest 5 at Frei** (Oracle of Knowledge, 198; dialogue 635). The chat shows **Armor of Life 402** and **Faded Passion fragments 1900**. No gold appeared, although the table lists `t4 500` for this quest. Two quests start at once:
    - **Quest 6 "The 1st Challenge: Chepas ahead"**: talk to Shaia.
    - **Quest 28 "What does Wren do?"** (kind 2; needs item 1900, which is why the fragment is handed out): talk to Wren 238, sell her a Faded Passion fragment, buy a Return Scroll.
12. **[8:40](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=520s) Wren** (Merchant): dialogue 731, then her shop. The shop sells **Potion of Health [D], Potion of Mana [D] and Scroll : Return at 79 gold each** (`Item_Base` buy prices are 10, 10 and 80, so the price on screen comes from elsewhere). *video*
13. **[8:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=530s) Lewellyn** (Scroll Merchant, 315) offers side quest **100 "Hunting for Furs"** (dialogue 644): **5 White Chepa Fur 2554** from Chepa Warrior 727 and **5 Black Chepa Fur 2553** from Chepa Archer 728. The reward panel shows 5,000 gold under Basic and Spell Necklace 397 / Necklace of Life 405 under Choose. The Necklace of Life tooltip reads Attack +40, Health +200, Health Regeneration +8 (the last three option pairs in `Item_Base`).
14. [9:05](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=545s) Owen (Red Union) has only a greeting line. **[9:25](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=565s)** The camp portal asks "Do you want to leave the area?" and leads to **Corpse incineration** (field 100). The player looked around there and came back (12:10 load).
15. **[12:35](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=755s) Back at Shaia** (Training Ground): quest 6 completes. **Quest 7** (same title, offer dialogue 685: the Chepa leaders are in the north) asks the player to kill **Chepa Warrior Officer 710 ×1** and **Chepa Archer Officer 711 ×1**, then report to Frei. Both died in the round stone arena in the north part of the Training Ground ([13:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=790s)–[13:45](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=825s)). The furs were done by [14:55](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=895s).
16. **[15:30](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=930s) Quest 7 turned in at Frei** (dialogue 638). The player chose **Ring of Life 408** (the Choose pair is Spell Ring 400 / Ring of Life 408) and also received **Scroll : Return 906**. **Quest 9 "Find the missing Scout"** follows (offer 639): talk to the Guard 215, then find the Scout in Corpse incineration.
17. **[15:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=950s) Quest 100 turned in** (Necklace of Life, 5,000 gold; Level 9) → **lesson 706 "Expand your Inventory"**. Expanding asked "Gold : 5000" ([16:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=980s)) and took the gold to 0. The lesson completed at [16:35](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=995s). Quest 28 completed at [16:40](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1000s).
18. **[15:55](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=955s) Odin** (Blue Union, 335) offers side quest **101 "All sorts of Fragile bones"** (dialogue 645): 10 Weak Skeleton bone 2571 and 10 Weak Elite Skeleton bone 2572 in Corpse incineration.
19. [16:55](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1015s) Guard talked to (dialogue 640). **[17:15](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1035s)** At the Corpse incineration portal a **"Nation support fund"** notice appears: "51,627 Gold has been paid in the country" (a nation payout). See [[gameplay/progression-and-economy]].
20. **[18:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1090s) Scout found** → quest 9 complete. The Scout (dialogue 641) starts **quest 10 "Find the Secret Document"**: kill Skeleton Warrior Officer 704 for **Secret document 2565** (100 %). With dialogue 646 he also starts side quest **107 "Hunting Skeletons"**: Skeleton Warrior Leader 704 ×1 and Skeleton Archer Leader 705 ×1, report to Frei. Both were done by [19:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1160s).
21. **[20:00](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1200s) Frei: quest 10 turned in** (dialogue 642). Rewards: **Oracle Set** (the class-specific costume row: `rew_a` = class id 1/4/5 picks 2021/2022/2023) and **Bracelet of Life 407** (chosen). Quest 107 also paid out: Blue and Red Passion Fragments [D] and Crystal : Blue. **Quest 11 "An urgent message"** follows (offer 643): the player receives **Scroll : Gaia 912** and **Urgent Letter 2567**, which are the two `pre` items quest 11 requires.
22. [20:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1220s) Wren offers side quest **102 "Wren's sister Wren?"** (dialogue 679; gives Hawker letter 2563; "Meet Wren in the fort"). [20:25](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1225s) Odin takes the bones (dialogue 649): **Belt of Life 406** and Crystal : Blue; Level 12.
23. **[21:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1270s) Use the Gaia Scroll** → load → **[21:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1280s) Cracked Earth** (field 63), standing beside a **Nexus**. Quest 11 completes. **Lesson 719 "Go to the Fortress"** (click the Nexus) and **quest 12** (talk to Freya) start. Clicking the Nexus opens the world map with a "Fortress / Owner Legion" panel ([21:35](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1295s)) and moves the player to the Fortress (field 120). The Fortress minimap is titled **"Scourge Fortress"**, which looks like the owning legion's name ([21:30](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1290s), [21:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1310s)).

### After the tutorial (Fortress, from 22:00)

The rest is outside the tutorial and is summarised from the quest tracker:

- Freya completes quest 12. Then come **lessons 712 "Take a look at the World Map" and 718 "Open item reinforcement window"** and **quest 13/14 "Battle preparations"** (talk to Cassia → go to Owen, create Health Potion [C], talk to Freya) ([22:05](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1325s)–[25:25](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1525s)), followed by **lesson 713 "Weapon Level (+) reinforcement"**.
- Next come side quests **749 "Kill monster of The land of Greed"** (50 Tow, 50 Elite Tow, return to Athan), **752 "Join & Create Legion"** (Kesley), **104 "Delivering Punishment"** (Haley) and **110 "Gear manufacturing"** (Odin), and the main quest **17 "Support the Abyss expedition"** (meet the Scout Leader). Quest 17 continues as **82** (the Guardian's copy: 10 Tow, 10 Elite Tow, Tow Chief 826; its Choose reward is the three Guardian weapons).
- Lesson **723** is titled **"How to obtain SP"** on screen ([25:55](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1555s)). Our client calls it "Automatism decomposition point recharging", although the objective text matches.
- From about 31:00 to the end, the player farms Tows in **The land of Greed** (field 109).

## 4. NPC positions (Erion copy)

Measured with the [[gameplay/npc-locations|minimap method]]. The Training Ground (ZoneDB 131) is x 544–736, z 3616–3808, at 1.1228 units per minimap pixel. The camera box here is about 38 × 29 px, and NPC offsets are taken from the name labels (29.7 px per unit across, 22.1 px per unit down). Local = world − (512, 3584). For the Arslan copy subtract 256 in x; for the Armia copy add 256. *video*

| Who | Unit | Field | World x, z | Local x, z | Time | Agreement |
|---|---|---|---|---|---|---|
| Spawn point (first frames, player not yet moving) | — | 93 | 686.3, 3652.3 | 174.3, 68.3 | [2:34](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=154s)–[2:45](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=165s) | 31 units north-west of gate 1206 (708.78, 3630.78) |
| Shaia | 201 | 93 | 680.0, 3663.5 | 168.0, 79.5 | [6:08](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=368s) | Wiki (March 2018 video): local 167.9, 80.8. A second, rougher sighting from the spawn frame gives 168.8, 78.2 |
| Floyd | 239 | 93 | 625.9, 3660.5 | 113.9, 76.5 | [4:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=260s) | Wiki: local 114.5, 76.6 |
| Chepa Warrior/Archer Officers 710/711 | — | 93 | north arena (not measured) | — | [13:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=790s) | Dialogue 685 says "in the north" |

Shaia and Floyd stand within 1.3 units of the positions measured from the March 2018 launch video, so the relaunch did not move them. Camp NPCs seen here (Frei, Wren, Lewellyn, Odin, Owen, the Mail box, the Guard) match the existing [[gameplay/npc-locations|Training Camp table]] and were not re-measured.

## 5. Other facts

- **Monsters by area:** Training Ground: Slime 604, Bee 731, Cobra 732, Chepa Warrior 727, Chepa Archer 728, Chepa officers 710/711 (the officers fight inside a group of Chepas). Corpse incineration: Skeleton Warrior/Archer, Elite variants, Skeleton officers 704/705. *video + client*
- **System messages seen in chat:** "Slime was destroyed.", "You acquired an <item> item.", "Levelup.<n>", "<name> entered the party.", "This item cannot be sold." (when trying to sell a bound reward), "<n> Gold has been paid in the country". *video*
- **Level pace:** Level 2 at 3:25, 3 at 4:15, 4 at about 4:25 (after the quest 2 turn-in), 5 at 5:45, 6–7 by 8:30, 9 by 15:50, 12 by 20:25. Exp from kills adds to the quest EXP. *video*
- **HP with gear:** 980/835 at level 6 with gloves and helmet ([6:36](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=396s)); 1,310/810 at level 7 with the Armor of Life ([8:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=530s)); 1,870/860 at level 9 ([15:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=950s)). *video*
- **Return Scroll use:** at [15:15](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=915s) the player left the Training Ground with a short load and reappeared in the Training Camp, consistent with Scroll : Return taking the player to the camp. *inferred*

## 6. Differences from other builds

- **No tutorial map:** the June 2018 relaunch starts the character in the Training Ground (field 89/93/97) with quest 1, as in the March 2018 launch video ([E-87WgbO_vo](https://www.youtube.com/watch?v=E-87WgbO_vo&t=149s)). Field 117 `Beginner's Training Ground` and Training Assistants 220–223 never appear. The repo's quest test (map 89 at the tutorial coordinates) is therefore closer to the real flow than the default map 117. A faithful server should spawn at about local (174, 68) in the nation's Training Ground. *video*
- **Quest EXP displayed = `Quest.tsv` ÷ 1.1** (500/550, 1,200/1,320). Either the relaunch scaled quest EXP down or the client shows a base value without a 10 % bonus. Check against the April 2018 videos before choosing. *video*
- **Strings differ from our client:** the class descriptions have no difficulty line, and lesson 723 is called "How to obtain SP". Our `StringAll_Eng` is from a different (probably later) build. *video + client*
- **Three classes only:** the Valkyrie row in `Create_Char` (class 7, no weapons) is not offered. *video + client*
- **Q5 reward:** the table's `t4 500` paid nothing visible, while a Faded Passion fragment 1900 (needed by quest 28) arrived. The relaunch server may have swapped this reward, or `t4` may mean something other than gold for this row. Quest 100's `t4 5000` did pay 5,000 gold. *video*

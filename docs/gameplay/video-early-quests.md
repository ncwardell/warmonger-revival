---
title: "Video notes: first session, levels 1+ (charmanmugen)"
---

# Video notes: first session, levels 1+ (charmanmugen)

Notes from [Warmonger - Steam PC Gameplay (2+ Hrs, 1080p60fps)](https://www.youtube.com/watch?v=s04CSN16w1s) (charmanmugen, recorded 2018-04-01, 2:29:34). It is one unedited session by a new **Punisher** called *Randius* of the **Arslan** nation. It runs from character creation to level 22. Quests drive levels 1–20 (0:00–1:06). After that the player grinds Land of Greed and Avenue of Spirit, joins a war in Mist Lake (about 1:47–2:02) and visits the auction house. The uploader says server staff were changing monster stats live from [1:43:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=6190s), so treat monster numbers after that point as unreliable.

Method: frames every 5 s were read with OCR (chat log, quest tracker, dialog box, reward panel, target frame, map name), and the key moments were checked by eye. Every timestamp below links to the moment (±5 s). Quest ids come from `Quest.tsv`; objective texts come from `StringAll_Eng.cdb`. Related pages: [[gameplay/npc-locations|NPC locations]], [[gameplay/progression-and-economy|Progression and economy]], [[gameplay/videos|Videos]].

> [!note] No tutorial island in this build
> After character creation ([3:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=210s)) the character spawns straight into **Training Ground** (field 89, Arslan) at level 1. Quest 1 is already active. Field 117 *Beginner's Training Ground* is never visited. Use this video to cross-check the first quests, not the tutorial map.

## 1. Map order

| Time | Map (field id) | How the player got there |
|---|---|---|
| [3:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=220s) | Training Ground (89) | spawn |
| [16:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=960s) | Training Camp (88) | walks through the gate |
| [17:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=1060s) → [21:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=1260s) | Training Ground, then back to the Camp | gates; a "Do you want to leave the area?" prompt appears at each gate |
| [24:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=1470s) | Corpse incineration (99) | Camp gate next to the Guard |
| [36:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=2165s) | Training Camp | return |
| [37:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=2260s) | Eternal River – Upper Region (14), briefly | uses *Scroll: Gaia*, then the nexus |
| [37:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=2270s) | Fortress (120) | nexus |
| [51:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=3085s) | Place for Scattered troops (103; Abyss hub) | Fortress portal or Haley "Abyss" |
| [52:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=3135s) | The land of Greed (108) | portal in the hub |
| [57:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=3445s) | Castle (90) | *Scroll: Castle* (quest 19) |
| [64:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=3845s) | Fortress | teleport |
| [81:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=4890s) | The avenue of spirit (113) | Abyss |
| [89:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=5395s) | "UG Fortress" (minimap title; the town after the war map changed) | — |
| [106:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=6360s), [107:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=6455s) | Punish Peak (13), Mist Lake (31): war | war invitation popup |

**Teleporter Haley** (Fortress, [63:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=3832s), [84:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=5077s)) offers four destinations: **Castle (10000)**, **Fortress (4000)** (shown later as "TOP Fortress (4000)"), **Gaia** and **Abyss**. The numbers in brackets are gold costs; Gaia and Abyss show no price. *video*

## 2. Quest chain in order

Rewards are given as **shown in the reward panel**, with the `Quest.tsv` value in brackets when it differs. All exp values match one pattern (see §4): kind 0 shows table ÷ 1.1, kind 1 shows table ÷ 1.2, kind 3 shows the table value. "Choose" means a pick-one reward. Class-specific choices are the Punisher's options.

### Training Ground and Camp (levels 1–11)

1. **On to a promising start** (`1`, Shaia 201). Already active at spawn, [3:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=220s). The objective is to talk to Shaia. Randius's line "Oops! I'm late again" comes first, then Shaia's "Why are you always late?" at [4:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=260s). Table reward: 550 exp. The talk links straight to quest 2. Tutorial hint quests start at the same moment: *Basic Combat Lesson 1* (`700`, basic attack), *Lesson 2* (`701`, use an ability, [4:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=295s)) and *Juicy Potions* (`722`, use a health and a mana potion; table gives 10 of each, [6:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=380s)).
2. **The Slime is mine** (`2`). Shaia sends the player to collect 3 Slime mucus from Slimes (`604`, drop 2550 at 100%). Tracker: "Slime mucus obtained (0/3) → Bring them to Floyd". Turn in to Floyd (239) at [6:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=405s). Reward: **1200 exp** [1320] + Gloves of Life (403).
3. **The task at hand** (`3`, Floyd), accepted at [7:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=420s): 5 Bee Needle from Bees (`731`) and 5 Cobra/Snake Leather from Cobras (`732`). Turn in to Floyd at [12:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=757s). Reward: **3500 exp** [3850] + Helmet of Life (401). On the way the player cleared the Chepa circle (Chepa Warrior/Archer) for exp.
4. **Go to Shaia** (`4`) from Floyd at [12:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=760s). No reward.
5. **United Problem Solvers** (`5`, Shaia), accepted at [13:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=812s): deliver a letter to Frei, the Oracle of Knowledge (198), in the Training Camp. Tracker: "Talk to Frei, you can find her in the training camp". Done at [16:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=965s). Reward: **2500 exp** [2750] + Armor of Life (402). The table also lists 500 gold, which the panel does not show.
6. **What does Wren do?** (`28`, hint quest, [16:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=995s)–23:15): talk to Wren (238), sell her a Faded Passion fragment, buy a Return Scroll. No reward.
7. **The 1st Challenge: Chepas ahead** (`6` → `7`). Frei, [16:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=997s): "hunt down the Chepa Leaders", then go and ask Shaia (`6`, talk). Shaia, [17:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=1067s): kill 1 Chepa Warriors officer (`710`) and 1 Chepa Archers officer (`711`) in the Training Ground's spiral circle (`7`). Report to Frei at [21:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=1268s). Reward: **9100 exp** [10010] + Scroll: Return ×10, then choose Spell Ring (400) or Ring of Life (408).
8. **Hunting for Furs** (`100`, Lewellyn 315, Camp), accepted at [17:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=1022s): 5 Whiter Chepa Fur (Chepa Warrior `727`) and 5 Black Chepa Fur (Chepa Archer `728`). Turn in to Lewellyn at [22:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=1322s). Reward: **7400 exp** [8880] + **5000 gold**, then choose Spell Necklace (397) or Necklace of Life (405). Her line mentions shoes, but the reward is a necklace.
9. **Find the missing Scout** (`9`, Frei), accepted at [21:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=1300s). Objectives: talk to the Guard (215) at the Corpse incineration gate ([23:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=1420s)), then find the Scout in Corpse incineration ([26:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=1575s)). Panel: **10400 exp** [11440], then choose Potion of Health [C] ×100 or Potion of Mana [C] ×100.
10. **All sorts of Fragile bones** (`101`, Odin 335, Camp), accepted at [22:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=1368s): 10 Weak Skeleton bone and 10 Weak Elite Skeleton bone from the skeleton groups (`10003`/`10004`) in Corpse incineration. Turn in to Odin at [36:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=2170s). Reward: **14500 exp** [17400] + **10000 gold** + Crystal: Blue ×10, then choose Spell Belt (398) or Belt of Life (406).
11. **Find the Secret Document** (`10`, the Scout, [26:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=1580s)): kill the Skeleton Warrior Officer (`704`) for the Secret document (2565, 100%) and give it to Frei. Done at [36:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2184s). Reward: one Oracle Set piece chosen by class (2021/2022/2023), then choose Spell Bracelet (399) or Bracelet of Life (407). No exp.
12. **Hunting Skeletons** (`107`, the Scout, [26:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=1590s)): kill the Skeleton Warrior Leader and the Skeleton Archer Leader (`704`/`705`), then report to Frei at [36:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=2196s). Reward: **10000 exp** [12000] + Blue and Red Passion Fragments [D] ×20 each + Crystal: Blue ×10.

### Fortress (levels 12–20)

13. **An urgent message** (`11` → `12`, Frei, [36:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=2205s)): "It's Gaia's scrolls. Use this and use the nexus to move to the fortress" (use Scroll: Gaia, item 912), then deliver the letter to Freya (200) in the Fortress at [38:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=2289s). Table: 44000 exp, 20/20 fragments, Crystal: Blue ×10, Armor Rune (7022). The reward panel was not captured. The player went from level 13 to 14 at 38:15.
14. **Wren's sister Wren?** (`102`, Wren 238, accepted in the Camp at [37:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=2222s)): carry the "Hawker letter" to her twin Wren (204) in the Fortress (done about 40:05). Reward: **56000 exp** [67200] + 20/20 fragments + Crystal: Blue ×10.
15. **Battle preparations** (`13` → `14`, Freya, [38:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=2312s)). `13` (talk to Cassia 212, [40:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2420s)) pays Empty Flask [C] ×100 + **30000 gold** + 15/15 fragments + Crystal: Blue ×5. `14` (talk to Owen 214 and craft 100 Potion of Health [C], [40:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=2430s)–40:50) is turned in to Freya at [41:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2482s). Reward: **50000 exp** [55000] + Shoes of Life (404) + 15/15 fragments + Auto decomposition hammer (948). The hint quest **Battle preparations** (`721`: decompose blue jewels) runs alongside.
16. **Support the Abyss expedition** (`17`, Freya, [41:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=2490s)): the Tow Chief is stirring up an uprising; meet the Scout Leader in the Abyss. Done in The land of Greed at [52:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=3137s). Reward: **180000 exp** [198000], then choose Potion of Health or Mana [C] ×100.
17. **Kill monster of The land of Greed** (`749`, Athan 207, accepted at [41:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=2515s)): 50 Tow (`10001`) and 50 Elite Tow (`10002`), then return to Athan. Turned in at [2:22:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=8547s). Reward: **50000 exp + 50000 gold** + 50/50 fragments + Crystal: Blue ×20 (shown = table). Athan then offers the ghost version, 70000 exp + 70000 gold + 60/60 + Crystal: Yellow ([2:22:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=8552s); `750`/`1102` share these rewards).
18. **Delivering Punishment** (`104`, Haley 217, [42:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=2532s)): "Because of the Lizards we lack important supplies". Kill 10 Lizard (`10005`) and 10 Elite Lizard (`10006`) in Place for Scattered troops (fields 103/105/107). Turn in at [56:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=3397s). Reward: **170000 exp** [204000] + **20000 gold** + 40/40 fragments.
19. **Gear manufacturing** (`110`, Odin 213, [42:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=2555s)): craft a piece of gear at Odin. Done at [46:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=2787s). Reward: **10000 exp** [12000] + **30000 gold**. The panel shows no rune choice, although the table lists Attack/Ability Power runes. Hint quests that run alongside: *Weapon Level (+) reinforcement* (`713`, 39:15–59:25), *Gear Level (+) reinforcement* (`720`, 45:00–61:25), *Item – Level (+) reinforcement* (`1512`).
20. **Join & Create Legion** (`752`, Kesley 210, [47:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=2832s)): reward Medal: Bronze (1000). Never completed. *Join the Legion* (`753`) appears at 75:40.
21. **Support the Abyss expedition** (`81`, the Punisher row of `80`/`81`/`82`; Scout Leader, [52:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=3147s)): kill 10 Tow, 10 Elite Tow and the **Tow's Chief** (`826`), then talk to Freya. Done at [89:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=5377s). Reward: **200000 exp** [220000], then choose Magical judge Dagger (15007) or Magical Frost Bow (15004).
22. **Meeting Freya** (`19`, Freya, [56:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=3417s)): "Meet with Bernice on the plaza first". Use the Castle Scroll, then go to Bernice (224) in the Castle at [57:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=3477s). Reward: **200000 exp** [220000]. Bernice offers to let a disaffected player change nation.
23. **Talk to Freya** (`20`, Patrick 199, the Castle's Oracle of Knowledge, [58:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=3502s)): carry the "Letter to Oracle of Knowledge" to Freya, done at [64:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=3897s). Reward: **300000 exp** [330000], then choose one ×5 of Scroll of the Warrior [A], Tome of Attack SPD [A], Scroll of the Magician [A] or Tome of Cooldown [A]. Freya then shows the cash-item features. Krister (219), the Stocks Manager, explains legion stocks at [58:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=3530s); quest `106` was not taken.
24. **[Group] Ancient Ghosts** (`21`, Freya, [65:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=3920s)): obtain the essence of Darkness ×3 (Ancient Ghost `827`, 70%) in The avenue of spirit (113). Panel: **900000 exp** [990000] + Dimensional energy, then choose potions [C] ×100. Still open at the end of the video.
25. **Hunting Ghosts (Spirit Avenue)** (`108`, Owen 214, [66:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=3962s)): 10 Ghost and 10 Elite Ghost (`10007`/`10008`). Panel: **500000 exp** [600000] + 50/50 fragments. The video does not show it being completed.
26. Hint quests later on: *A new weapon* (`708`, equip a secondary weapon, 89:45) and *Two sets of weapons* (`709`, Space to swap, 92:55). After 66:00 the player grinds and does not finish another story quest, so levels 20→22 took 77 minutes.

## 3. NPCs

Positions come from the minimap camera box (see [[gameplay/npc-locations]] §2). An NPC position is the player position plus the name-label offset (Δx/29.7, −Δy/22.1). Error is about ±3 units unless stated. **Bold** rows are new; the others are checks against existing values.

| NPC | Unit | Map (field) | x | z | Local x, z | Source | Note |
|---|---|---|---|---|---|---|---|
| Shaia | 201 | Training Ground (89) | 433.8 | 3662 | 177.8, 78 | [4:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=260s), [13:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=785s), [17:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=1075s) | 3 sightings agree within 2 units, but the wiki has (423.9, 3664.8), about 10 units further west. Shaia is a hovering fairy |
| Floyd | 239 | Training Ground (89) | 371.1 | 3660.1 | 115.1, 76.1 | [6:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=410s) | matches the wiki (370.5, 3660.6) |
| Lewellyn / Wren | 315 / 238 | Training Camp (88) | 378.7 / 374.5 | 3477.4 / 3477.0 | — | [17:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=1020s), [23:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=1380s) | player position while talking; matches the wiki within 2 units |
| Hadrian | 211 | Fortress (120, Arslan copy) | 1842.2 | 1709.2 | 50.2, 173.2 | [48:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=2880s) | Fortress Administrator ("Fort Information", "Civil war application"); confirms the wiki's guess (1841, 1712) |
| Bell Thain | 208 | Fortress | 1917.2 | 1745.4 | 125.2, 209.4 | [49:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=2990s) | Training Officer ("Mock Battle"); confirms the wiki's guess (1917, 1746) |
| **Bernice** | 224 | Castle (90) | 493.8 | 4285.8 | 237.8, 189.8 | [58:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=3480s) | Oracle of Judgment, on the plaza by the big gate; ±4 |
| **Patrick** | 199 | Castle (90) | 486.1 | 4292.5 | 230.1, 196.5 | [58:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=3480s) | Oracle of Knowledge (Castle); ±5 |
| **Krister** | 219 | Castle (90) | 489.7 | 4139.6 | 233.7, 43.6 | [59:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=3541s) | Stock Administrator; ±4 |
| **Kesley** | 210 (318?) | Castle (90) | 480.8 | 4146.2 | 224.8, 50.2 | [59:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=3541s) | Legion Administrator; a second Kesley besides the Fortress one; ±5 |
| **Bell Thain** | 208 | Castle (90) | ~482 | ~4122 | ~226, ~26 | [59:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=3541s) | Training Officer, at the edge of the screen; ±8 |
| Imperial Guards | 189–197 | Castle (90) | around 470–490 | 4285–4300 | — | [58:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=3480s) | four or more stand on the plaza near Bernice |
| Scout Leader | 241 | The land of Greed (108) | 452.4 | 2758.8 | — | [52:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=3135s) | within 6 units of `Trigger` 10803 (448.84, 2753.87); confirms the trigger row and the ZoneDB 113 minimap mapping |

Other NPCs seen without measurement, all in the Fortress: Cassia (212, "Material Merchant": go to Odin or Owen to craft), Owen (214, Create), Odin (213, Create: Life gear cost 0 gold, Honor/Rise gear 15,000 gold), Athan (207, quests and shop), Haley (217, Teleport), Cathy (303, auction, [48:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2900s)), Kaysa (300, warehouse, [48:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=2920s)), Casta (324, rune socketing, [49:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2960s)), Paraman (322, "named weapon with boss material only", [50:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=3005s)), Lewellyn (205, scrolls). In the Training Camp: Guard (215), Odin (335), Owen (337), Frei (198). In Corpse incineration: the Scout (Trigger 9901).

## 4. Levelling

The bottom-left badge and the chat line "Levelup.N" give these times:

| Level | Time | | Level | Time |
|---|---|---|---|---|
| 2 | [4:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=295s) | | 12 | [36:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=2175s) (quest turn-ins) |
| 3 | [6:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=400s) | | 13, 14 | [38:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=2295s) (two levels together: urgent message + Wren's letter) |
| 4 | [6:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=415s) | | 15 | [38:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=2320s) |
| 5 | [10:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=635s) | | 16 | [47:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=2825s) |
| 6 | [12:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=760s) | | 17 | [52:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=3145s) |
| 7 | [16:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=995s) | | 18 | [56:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=3415s) |
| 8 | [19:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=1195s) | | 19 | [58:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=3510s) |
| 9 | [21:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=1295s) | | 20 | [65:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=3940s) |
| 10 | [24:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=1445s) | | 21 | [86:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=5210s) |
| 11 | [27:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=1625s) | | 22 | [2:22:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=8575s) |

- **Displayed quest exp versus `Quest.tsv`.** Every reward panel checked shows the table value divided by **1.1 for kind 0** (main story: 1320→1200, 3850→3500, 2750→2500, 10010→9100, 11440→10400, 55000→50000, 198000→180000, 220000→200000, 330000→300000, 990000→900000). It shows the table divided by **1.2 for kind 1** (side quests: 8880→7400, 17400→14500, 12000→10000, 67200→56000, 204000→170000, 600000→500000). For **kind 3** (repeatable Athan kill quests) it shows the table value unchanged (50000, 70000). Gold and item counts always equal the table. The table probably stores exp with a 10%/20% bonus already applied, or the client divides it for display. The video cannot show which amount was actually granted, because the HUD has no numeric exp readout. *video + client*
- Monster kills give most of the exp in the first ten minutes: level 2 came from Slimes before any quest was handed in. The client `Level_Table` needs 700 exp for level 2. *client*
- HP and MP on the HUD, with starting and quest gear (not base stats): Lv 1 420/424, Lv 3 560/472, Lv 7 970/568, Lv 16 2795/924, Lv 19 3005/996, Lv 20 3240–3260/1000. *video*
- Gold: 0 at the start; **38,736** at Lv 16 ([46:05](https://www.youtube.com/watch?v=s04CSN16w1s&t=2765s)), almost all of it from quests. *video*

## 5. Monsters seen

Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warrior/Archer Officer → Skeleton Warrior/Archer → Elite Skeleton Warrior/Archer → Skeleton Warrior/Archer Officer (Corpse incineration) → Fragile (Elite) Lizard Swordsman/Lancer (Place for Scattered troops) → Fragile (Elite) Tow Warrior/Sorcerer and the Tow Chief (Land of Greed) → Fragile (Elite) Red/Black Ghost (Avenue of Spirit) → Tough Elite Black Skeleton Warrior/Archer and a Troll (Mist Lake war map, after 1:43, so unreliable).

Maximum HP read from the target frame. The number in brackets is regeneration and is always 2% of the maximum:

| Monster | HP | Regen | Time |
|---|---|---|---|
| Elite Skeleton Warrior | 600 | +12 | [31:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=1910s) |
| Skeleton Warrior Officer (quest boss) | 2000 | +0 | [35:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2120s) |
| Fragile Lizard Swordsman | 600 | — | [53:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=3220s) |
| Tow Chief (`826`) | 5000 | +100 | [70:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=4200s), [88:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=5300s) |
| Fragile Elite Tow Sorcerer / Warrior | 1400 | +28 | [87:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=5255s) |
| Fragile Black / Red Ghost | 1500 | +30 | [81:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=4900s) |
| Fragile Elite Red / Black Ghost | 2000 | +40 | [83:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=4995s) |
| "Bot: Guardian" (war bot) | 3600 | +180 | [1:48:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=6520s), unreliable |

Shaia's target frame reads 30000/30000 (+500) ([4:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=260s)).

## 6. Drops, shop, other numbers

- **Quest items drop at the table rate:** every kill of a matching monster gave Slime Mucus, Bee Needle/Snake Leather, Chepa furs or Weak Skeleton bones (rate 100 in `Quest.tsv`). Faded Passion fragments and Blue/Red Passion Fragments [D] drop constantly; Gem Stone: Blue drops in Place for Scattered troops and the Land of Greed. *video*
- **Wren, Training Camp (238)** at [16:54](https://www.youtube.com/watch?v=s04CSN16w1s&t=1014s): Potion of Health [D] **79**, Potion of Mana [D] **79** ("regenerates mana for 16 seconds"), Scroll: Return **79**, and Scroll of Transform [Golem], [Demon] and [Slime] at **7,920** each. That is 7.92 × the `Item_Base` buy price (10 and 1000), the same multiplier the Fortress shop uses (see [[gameplay/progression-and-economy]] §4), so it is not a fort tax. This stock does **not** match `Npc_Carry` shop 287 (883, 884, 906, 945): the transform scrolls 760–762 are missing there and the hammer is absent in the video. At 79 the Return scroll must have a base price of 10, so it is not item 906 (base 80). *video + client*
- Potion of Health [C] tooltip: regenerates for 16 s, 600 HP in total ([21:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=1300s)).
- Item tooltips: Ring of Spell/Life gives Attack +40, Health +200, Health Regen +40; Necklace of Spell gives Ability Power +30, Health +200, Health Regen +40; Helmet of Honor gives Armor +40, Magic Resist +20, Mana +85, Movement +13%. All are marked "Binds when picked up". *video*
- System messages seen: "Attack started in <land>", "<land> was invaded", "There is no legion for you to join", "The war began in <land>. Do you want to participate?", "Do you want to leave the area?" (at every gate), "You can't replace that weapon", "There is no space in your inventory", "Skill is not ready yet". *video*

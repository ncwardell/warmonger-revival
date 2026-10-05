---
title: "Video notes: fortress war series (ZonderCoRe)"
---

# Video notes: fortress war series (ZonderCoRe)

Notes from the four-part series "Warmonger Fortress War #1" by ZonderCoRe (uploaded 24 June 2018, Spanish voice-over, 1280×720 at 60 fps):

| Part | Video | Length | What it shows |
|---|---|---|---|
| 1/4 "Entrando en su mapa principal" | [XoSM3RbZon0](https://www.youtube.com/watch?v=XoSM3RbZon0) | 4:12 | Joining a land war in Eternal River – Upper Region, towers and jungle |
| 2/4 "Hero Form" | [6_z6CUpZj30](https://www.youtube.com/watch?v=6_z6CUpZj30) | 4:32 | Transforming into a hero, fight at the defenders' nexus |
| 3/4 "Hero Combo Wombo" | [7f7QwwUyYBg](https://www.youtube.com/watch?v=7f7QwwUyYBg) | 4:18 | Hero fight at the nexus until it nearly falls |
| 4/4 "Core Room" | [JPd7TCu-44o](https://www.youtube.com/watch?v=JPd7TCu-44o) | 8:04 | The siege that follows: Room of Core, cores, Heart of Magic, defeat screen |

The four parts are one continuous session. The streamer is on **Erion** (attacking side), legion tag `<Scourge>`. Parts 1–3 are a normal land war; the "fortress" part is only part 4. The player never reaches the guardian's room (field 131), so **Crusader Cherubim, the guardian and core HP do not appear on screen.**

Method: the 360p stream was sampled every 4 s for the whole series, and the first 40–60 s of each part was also read at 720p (the 720p download was cut off by YouTube). Positions use the minimap method of [[gameplay/npc-locations]] §2 (minimap texture = `ZoneDB` rectangle). Timestamps are good to about ±4 s. Tags: *video* (read off the screen), *client* (decoded tables), *guess*. Related pages: [[gameplay/pvp-and-matches]], [[gameplay/classes-and-legions]], [[gameplay/crush-mechanics]], [[gameplay/server-rules]].

## 1. Numbers

### War and siege timers

| Item | Value | Source | Tag |
|---|---|---|---|
| Land war timer when the player joins | 39:39 left (40:00 war) | [P1 0:12](https://www.youtube.com/watch?v=XoSM3RbZon0&t=12s) | video |
| Land war won (defenders' nexus destroyed) | at about 27:05 left, about 13 min into the war | [P3 3:56](https://www.youtube.com/watch?v=7f7QwwUyYBg&t=236s), [P4 0:02](https://www.youtube.com/watch?v=JPd7TCu-44o&t=2s) | video |
| Siege timer on arrival in the Room of Core | **40:00** (39:52 shown 5 s in) | [P4 0:05](https://www.youtube.com/watch?v=JPd7TCu-44o&t=5s) | video |
| Siege lost | at about 32:05 left (7 min 55 s after it began) | [P4 7:52](https://www.youtube.com/watch?v=JPd7TCu-44o&t=472s) | video |
| Respawn delay in the siege | about **14 s** (death at 38:17, back at the Nexus at 38:03) | [P4 1:40](https://www.youtube.com/watch?v=JPd7TCu-44o&t=100s)–[1:54](https://www.youtube.com/watch?v=JPd7TCu-44o&t=114s) | video |
| Jungle respawn | "The Jungle monsters have returned" at 35:03; the Giant Bear camp was cleared at about 39:03, so about **4 min** | [P1 0:52](https://www.youtube.com/watch?v=XoSM3RbZon0&t=52s), [P2 0:36](https://www.youtube.com/watch?v=6_z6CUpZj30&t=36s) | video + guess |
| Lords of the Land window | "Remaining time: 86 min" during the war | [P1 2:20](https://www.youtube.com/watch?v=XoSM3RbZon0&t=140s) | video |

### TP

| Event | TP change | Source | Tag |
|---|---|---|---|
| Pool at the start of the land war and of the siege | 0 / 10,000 (resets for the siege) | [P1 0:12](https://www.youtube.com/watch?v=XoSM3RbZon0&t=12s), [P4 0:05](https://www.youtube.com/watch?v=JPd7TCu-44o&t=5s) | video |
| Small gains | +30 (39:38), +100 (39:22), +30 (38:53) | [P1 0:15](https://www.youtube.com/watch?v=XoSM3RbZon0&t=15s), [0:31](https://www.youtube.com/watch?v=XoSM3RbZon0&t=31s), [1:00](https://www.youtube.com/watch?v=XoSM3RbZon0&t=60s) | video |
| Gain after the tower area is taken | **+2,500** (30 → 2,530 at 39:34) | [P1 0:19](https://www.youtube.com/watch?v=XoSM3RbZon0&t=19s) | video; cause is a guess |
| Gain as the Giant Bear jungle camp dies | **+1,500** (2,630 → 4,130 at 39:06) | [P1 0:47](https://www.youtube.com/watch?v=XoSM3RbZon0&t=47s) | video; cause is a guess |
| Siege Minion placed | −1,000 (5,550 → 4,550, 37:43) | [P1 2:08](https://www.youtube.com/watch?v=XoSM3RbZon0&t=128s) | video, matches `Skill_TP` 1,000 |
| Remote Bomb | −1,500 (3,050 → 1,550, 37:19) | [P1 2:32](https://www.youtube.com/watch?v=XoSM3RbZon0&t=152s) | video, matches `Skill_TP` 1,500 |
| Nexus Remote Bomb ("WinterGold set a Nexus Remote Bomb") | −2,500 (2,780 → 280, 32:39 → 32:35) | [P2 2:56](https://www.youtube.com/watch?v=6_z6CUpZj30&t=176s)–[3:04](https://www.youtube.com/watch?v=6_z6CUpZj30&t=184s) | video at 360p; the client lists Nexus Remote Bomb at 2,000 and Powerful Remote Bomb at 2,500, so check |

TP is one pool for the side: it drops when any ally uses a TP skill. Other TP skills used by name: Shield recovery, Siege Minion, Remote Bomb, Nexus Remote Bomb ([P2 2:08](https://www.youtube.com/watch?v=6_z6CUpZj30&t=128s), [P3 0:00](https://www.youtube.com/watch?v=7f7QwwUyYBg&t=0s)). *video*

### Hero form (Dark Knight Skull)

| Item | Value | Source | Tag |
|---|---|---|---|
| Key | X (the slot shows the hero's skull portrait) | [P2 0:05](https://www.youtube.com/watch?v=6_z6CUpZj30&t=5s) | video |
| Hero | **Dark Knight Skull**: the new R skill is Heaven and Earth 20006, which is weapon 69 (item 8000 "Dark knight Skull"; `HeroData` 1). Hero skills on that weapon: Overcharge 20004, Cut 20005, passive 20000, Heaven and Earth 20006, Sweep 20007, Scream of the Dead 20008, Aura of Death 20012, Tomb of the Dead 20009 | `WeaponBase` 69, `Skill_Base` | client |
| Max HP / MP before | 7,282 / 1,660 | [P2 0:05](https://www.youtube.com/watch?v=6_z6CUpZj30&t=5s) | video |
| Max HP / MP in hero form | **16,214 / 3,645** (×2.23 and ×2.20) | [P2 0:07](https://www.youtube.com/watch?v=6_z6CUpZj30&t=7s) | video |
| HP and MP right after transforming | HP 8,107 (exactly **50 %** of the new max; it was 39 % before); MP 911 (25 %) | [P2 0:07](https://www.youtube.com/watch?v=6_z6CUpZj30&t=7s) | video |
| Client values for Dark Knight Skull | `HeroData` stat1 1,204, stat2 756, hp 10,890, mp 3,010. The observed max is not base + these values (7,282 + 10,890 ≠ 16,214), so the formula is still unknown | `HeroData.tsv` | client |
| X cooldown after transforming | counts down from about 10 s (9 s two seconds after) | [P2 0:07](https://www.youtube.com/watch?v=6_z6CUpZj30&t=7s)–[0:15](https://www.youtube.com/watch?v=6_z6CUpZj30&t=15s) | video |
| Heaven and Earth (R) | cooldown 80 s, mana 440; "deals 110 (+3,499) damage to all enemies, stunning them for 3 seconds" | [P3 0:02](https://www.youtube.com/watch?v=7f7QwwUyYBg&t=2s); `Skill_Base` 20006 (80,000 ms, cost 440) | video + client |
| Duration | at least **8.5 min**: still 16,214 max HP from 35:33 to 27:12 on the war timer, through heavy fighting. Gone (7,282 max) by the siege | [P2 0:07](https://www.youtube.com/watch?v=6_z6CUpZj30&t=7s) → [P3 3:56](https://www.youtube.com/watch?v=7f7QwwUyYBg&t=236s), [P4 0:02](https://www.youtube.com/watch?v=JPd7TCu-44o&t=2s) | video |

### Structures

| Unit | Reading | Source | Tag |
|---|---|---|---|
| Defenders' **Reinforced Nexus** (land war, field 14) | about 9,403, then 3,486, of "120,000 (+6,000)" max. The 360p text is blurred, so the max could be misread | [P3 3:52](https://www.youtube.com/watch?v=7f7QwwUyYBg&t=232s)–[3:56](https://www.youtube.com/watch?v=7f7QwwUyYBg&t=236s) | video (low confidence) |
| Room of Core cores, Heart of Magic, guardian, Crusader Cherubim | **no HP readable**: cores are captured by standing on the platform, and the Heart was never targeted on screen | P4 | — |

### Siege result screen (defeat)

| Field | Value | Source | Tag |
|---|---|---|---|
| Banner | LOSE / "DEFEAT" | [P4 7:52](https://www.youtube.com/watch?v=JPd7TCu-44o&t=472s) | video |
| Medal (three medal types) | 0 / 0 / 0 | same | video |
| Fame | **−100** | same | video |
| Legion Contribution | **20** | same | video |
| Acquired Gold | 0 | same | video |
| After Close | loading screen, then the player is in their own legion's fort ("Scourge Fortress", field 120) | [P4 7:56](https://www.youtube.com/watch?v=JPd7TCu-44o&t=476s)–[8:00](https://www.youtube.com/watch?v=JPd7TCu-44o&t=480s) | video |

The panel also has six achievement icons, all grey. *video*

## 2. Positions

### Room of Core (field 130 "Room of Core", ZoneDB 138 `코어실`, rectangle x 256–511, z 3840–4095)

The video minimap lines up exactly with `minimap_z138_00.dds` (checked by overlaying three 720p frames). The map is a **ring of six hexagonal rooms** around a closed centre room, plus three outer rooms in the south-west and one detached room in the north-east. Centres below are read off the texture (±5 units); `x = 256 + px/2`, `z = 4096 − py/2`.

| Room | World x, z (centre) | What is there | Source | Tag |
|---|---|---|---|---|
| Outer south room | 376, 3869 | **Attackers' Nexus**: arrival point and respawn point (blue marker on the minimap) | [P4 0:05](https://www.youtube.com/watch?v=JPd7TCu-44o&t=5s), [1:54](https://www.youtube.com/watch?v=JPd7TCu-44o&t=114s) | video |
| Ring, south-west | 364, 3934 | **Entry Core** (UnitDB 1047), the first capture ("Our allies has captured Entry"). Gate 1300 (362.79, 3947.06) is in this room | [P4 0:48](https://www.youtube.com/watch?v=JPd7TCu-44o&t=48s); `Teleport_List` | video + client |
| Ring, north-west | 361, 3996 | Core (element core; captured next, 39:00) | [P4 0:56](https://www.youtube.com/watch?v=JPd7TCu-44o&t=56s) | video |
| Ring, north | 426, 4031 | Core | minimap icon | video |
| Ring, north-east | 476, 4001 | **Invasion Core** (1048), captured at 38:05; gate 1306 (480.01, 4008.33) is here | [P4 1:52](https://www.youtube.com/watch?v=JPd7TCu-44o&t=112s); `Teleport_List` | video + client |
| Ring, south-east | 471, 3941 | Core; **Anti-Aircraft Defence Equipment** (1036) destroyed here at 37:33 | [P4 2:24](https://www.youtube.com/watch?v=JPd7TCu-44o&t=144s) | video (room is ±1 room) |
| Ring, south | 419, 3909 | Core | minimap icon | video |
| Centre room | 421, 3971 | **Heart of Magic** (1049): the minimap hover list names it here; destroyed at 37:53 | [P4 2:00](https://www.youtube.com/watch?v=JPd7TCu-44o&t=120s)–[2:04](https://www.youtube.com/watch?v=JPd7TCu-44o&t=124s) | video |
| Detached north-east room | 476, 4044 | Pink star marker all through the siege. Gates 1302 (473.31, 4058.3) ↔ 1303 (459.92, 4048.72) are here | minimap; `Teleport_List` | video + client; purpose is a guess (exit to the guardian?) |
| Outer west room | 314, 3954 | A white glow appears here right after the air defence falls ("It's possible to move to the room of the guardian") | [P4 2:28](https://www.youtube.com/watch?v=JPd7TCu-44o&t=148s) | video; that it is the portal is a guess |
| Outer south-west room | 311, 3904 | Second blue marker (ally) | minimap | video |

So the six ring rooms hold the six cores named in `UnitDB` 1043–1048 (Water, Wind, Earth, Fire, Entry, Invasion); only Entry and Invasion could be tied to a room by name. Small yellow markers sit on three ring corridors (north-west→north, north-east→centre, south-east→south). They may be gates or "equipment" units; this was not checked. *video*

The **Room of the Fortress Keeper** (field 131, ZoneDB 139 `신장실`, x 512–767, z 3840–4095; gates 1301 at (546.46, 3867.4), 1304/1305/1307 near (664–678, 4028–4046)) is not visited in this series. *client*

### Eternal River – Upper Region (field 14, ZoneDB 39, rectangle x 3616–3775, z 544–703)

| Point | World x, z | Source | Tag |
|---|---|---|---|
| Entry from Eternal Lake (gate 941 → field 84) | 3760.31, 673.16 | `Teleport_List` | client |
| Tower area being captured ("Capture the Tower areas") | about 3724, 677 | [P1 0:12](https://www.youtube.com/watch?v=XoSM3RbZon0&t=12s) | video (player position beside it) |
| Giant Bear jungle camp | about 3748, 636 | [P1 0:35](https://www.youtube.com/watch?v=XoSM3RbZon0&t=35s)–[0:47](https://www.youtube.com/watch?v=XoSM3RbZon0&t=47s) | video |
| Defenders' nexus; clicking it after the land war opens the siege | about 3693, 625 | [P4 0:02](https://www.youtube.com/watch?v=JPd7TCu-44o&t=2s) | video (player next to it, ±5) |

## 3. Entry flow (land war → siege)

1. The world map shows the land at war: "Eternal Lake", *During the war*, Defend side Arslan, Attack side Erion, Remaining Time 39:39 ([P1 0:00](https://www.youtube.com/watch?v=XoSM3RbZon0&t=0s)). *video*
2. Walking into the war field brings up a confirm box: "If you enter the area, you will participate in a war against another nation" ([P1 0:08](https://www.youtube.com/watch?v=XoSM3RbZon0&t=8s)). The war HUD then shows kills/assists, TP 0/10,000 and the timer. *video*
3. The attackers win the land war by destroying the Reinforced Nexus (part 3). The banner "A **Siege** was declared on Eternal River – Upper Region. Click on the nexus to join the battle for the fortress." appears. Clicking the nexus asks "If you enter the area, you will participate in a siege warfare against another nation" ([P4 0:02](https://www.youtube.com/watch?v=JPd7TCu-44o&t=2s)). *video*
4. On OK the player lands beside the attackers' Nexus in the Room of Core with a new 40:00 timer and TP 0/10,000 ([P4 0:05](https://www.youtube.com/watch?v=JPd7TCu-44o&t=5s)). *video*
5. Inside: capture Entry, then the ring cores, then Invasion. Destroy the Heart of Magic: "**Divine Guard will not be summoned, The guardian does not recover.**" Destroy the Air defence equipment: "It's possible to move to the **room of the guardian**". *video*
6. Either side can retake cores ("Enemy has captured Core"). Chat just before the defeat: "we need 2 minutes", then "nexus … help … come back" ([P4 7:28](https://www.youtube.com/watch?v=JPd7TCu-44o&t=448s)). The siege ended in a defeat at 32:05 left, so the attackers most likely lost because their Nexus was destroyed (*guess*).

## 4. Timestamped log

| Video time | War timer | Moment |
|---|---|---|
| [P1 0:00](https://www.youtube.com/watch?v=XoSM3RbZon0&t=0s) | 39:39 | World map war panel for Eternal Lake (Arslan defends, Erion attacks) |
| [P1 0:12](https://www.youtube.com/watch?v=XoSM3RbZon0&t=12s) | 39:41 | "Capture the Tower areas"; TP 0 |
| [P1 0:19](https://www.youtube.com/watch?v=XoSM3RbZon0&t=19s) | 39:34 | TP +2,500 |
| [P1 0:24](https://www.youtube.com/watch?v=XoSM3RbZon0&t=24s)–[0:52](https://www.youtube.com/watch?v=XoSM3RbZon0&t=52s) | 39:27–39:03 | Group kills the Giant Bear jungle mob next to a tower; TP +1,500 at 39:06 |
| [P1 1:00](https://www.youtube.com/watch?v=XoSM3RbZon0&t=60s)–[1:20](https://www.youtube.com/watch?v=XoSM3RbZon0&t=80s) | 38:51–38:35 | Second jungle camp (Ogre) |
| [P1 1:40](https://www.youtube.com/watch?v=XoSM3RbZon0&t=100s) | 38:11 | Match Info: attack 7 kills / 26 assists, defence 3 / 6; player dead with a resurrection countdown |
| [P1 2:20](https://www.youtube.com/watch?v=XoSM3RbZon0&t=140s) | 37:31 | Lords of the Land window (buff tiers, six reward boxes, 86 min left) |
| [P1 2:30](https://www.youtube.com/watch?v=XoSM3RbZon0&t=150s)–[4:12](https://www.youtube.com/watch?v=XoSM3RbZon0&t=252s) | 37:20–35:43 | Push onto the defenders' nexus |
| [P2 0:06](https://www.youtube.com/watch?v=6_z6CUpZj30&t=6s) | 35:33 | **Hero form**: HP 2,874/7,282 → 8,107/16,214 |
| [P2 0:36](https://www.youtube.com/watch?v=6_z6CUpZj30&t=36s) | 35:03 | "The Jungle monsters have returned" |
| [P2 1:00](https://www.youtube.com/watch?v=6_z6CUpZj30&t=60s) | 34:23 | "Ariel use a Nexus Remote Bomb" |
| [P2 1:36](https://www.youtube.com/watch?v=6_z6CUpZj30&t=96s) | 34:03 | "MISZA set a Siege Minion" |
| [P2 2:08](https://www.youtube.com/watch?v=6_z6CUpZj30&t=128s) | 33:31 | "Zpike set a Shield recovery" |
| [P2 3:04](https://www.youtube.com/watch?v=6_z6CUpZj30&t=184s) | 32:35 | "WinterGold set a Nexus Remote Bomb"; TP 2,780 → 280 |
| [P3 0:02](https://www.youtube.com/watch?v=7f7QwwUyYBg&t=2s) | 31:06 | Heaven and Earth tooltip |
| [P3 2:04](https://www.youtube.com/watch?v=7f7QwwUyYBg&t=124s) | 29:32 | "Zpike use a Nexus Remote Bomb" |
| [P3 3:52](https://www.youtube.com/watch?v=7f7QwwUyYBg&t=232s) | 27:16 | Reinforced Nexus at about 9,403 HP, then 3,486 at 27:12 |
| [P4 0:02](https://www.youtube.com/watch?v=JPd7TCu-44o&t=2s) | — | Siege declared; join prompt at the nexus |
| [P4 0:05](https://www.youtube.com/watch?v=JPd7TCu-44o&t=5s) | 39:52 | Room of Core, beside the attackers' Nexus |
| [P4 0:48](https://www.youtube.com/watch?v=JPd7TCu-44o&t=48s) | 39:08 | "Our allies has captured Entry" |
| [P4 0:56](https://www.youtube.com/watch?v=JPd7TCu-44o&t=56s)–[1:04](https://www.youtube.com/watch?v=JPd7TCu-44o&t=64s) | 39:00–38:53 | Three "captured Core" messages |
| [P4 1:40](https://www.youtube.com/watch?v=JPd7TCu-44o&t=100s) | 38:17 | Player dies; respawns at the Nexus about 14 s later |
| [P4 1:52](https://www.youtube.com/watch?v=JPd7TCu-44o&t=112s) | 38:05 | "Our allies has captured Invasion" |
| [P4 2:04](https://www.youtube.com/watch?v=JPd7TCu-44o&t=124s) | 37:53 | "The Heart of Magic has destroyed. Divine Guard will not be summoned, The guardian does not recover." |
| [P4 2:24](https://www.youtube.com/watch?v=JPd7TCu-44o&t=144s) | 37:33 | "The Air defence equipment was destroyed. It's possible to move to the room of the guardian" |
| [P4 2:56](https://www.youtube.com/watch?v=JPd7TCu-44o&t=176s) | 37:01 | "Enemy has captured Core" (cores change hands both ways from here on) |
| [P4 4:32](https://www.youtube.com/watch?v=JPd7TCu-44o&t=272s) | 35:25 | Enemy retakes a core |
| [P4 6:12](https://www.youtube.com/watch?v=JPd7TCu-44o&t=372s) | 33:45 | Allies retake a core |
| [P4 7:48](https://www.youtube.com/watch?v=JPd7TCu-44o&t=468s) | 32:09 | Allies retake Entry; the enemy takes a core |
| [P4 7:52](https://www.youtube.com/watch?v=JPd7TCu-44o&t=472s) | ~32:05 | **DEFEAT**: Fame −100, Legion Contribution 20, Gold 0, Medals 0 |
| [P4 8:00](https://www.youtube.com/watch?v=JPd7TCu-44o&t=480s) | — | Back in Scourge Fortress |

## 5. Still open

- Guardian, Crusader Cherubim, core and Heart of Magic HP. Neither this series nor the client gives them. [2umwpYlKAvg](https://www.youtube.com/watch?v=2umwpYlKAvg) (Crush Online) is the next place to look.
- The layout of the guardian's room (field 131) and what the north-east pink-star room is for.
- Why the siege was lost at 7:55 (nexus HP or a core count?), and what the reward screen shows after a win.
- Hero form duration and its stat formula: the observed max HP 16,214 does not follow from `HeroData` in any obvious way.

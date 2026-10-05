---
title: "Video notes: Nas Village dungeon run (ZonderCoRe)"
---

# Video notes: Nas Village dungeon run (ZonderCoRe)

Numbers and positions from two videos:

- **[Warmonger Nas Village Run 3 guys Party][v]** (ZonderCoRe, 28 June 2018, 11:44). Three players (ZonderCoRe, Uraniel, Maaac) farm the event dungeon *Nas Village Entrance* in Hard Mode. The only copy online is 640×360.
- **[Crush Online - How to farm material in dungeons][w]** (Jonathan Silverblood, 24 Nov 2016, 3:47). One player gathers Moonstone in *[Lv 5] Fortress of Ghost* (client field 124).

Positions are world (x, z), measured with the minimap method in [[gameplay/npc-locations]] §2. The panel was rescaled to 360p (x 551.65–637.15, y 266.15–351.65), and the white camera box was tracked once per second. Background for this page: [[gameplay/maps-and-dungeons]] §2–3, [[gameplay/dungeon-drops]], [[gameplay/sources]].

Tags: *client* (read from a table), *video* (measured or read off the video), *guess*.

> [!note]
> **The Nas run has no boss and shows no EXP or gold.** The party clears the same six packs over and over until "Dungeon finished / Exiting the dungeon initiated" appears at 11:29 ([v &t=689s][v689]). No EXP bar, gold change, monster level or HP number can be read at 360p. Monster labels are red text that cannot be read. Monster identities below come from `UnitDB` (*client*).

## 1. Field id and map

| Item | Value | Source | Tag |
|---|---|---|---|
| Name on the minimap and in the entry dialog | "Nas Village Entrance", **Hard Mode** | [v &t=6s][v6], [&t=30s][v30] | video |
| Client field | **133 "Sinking Nest (Crystal)"**. `DungeonAdmission` row 133 advertises Crystal Blue/Yellow/Red (700–702) and Gem Stone Blue/Yellow/Red (693–695), which is exactly what Nas drops. 134/135 are taken (see §6) | `DungeonAdmission`, `FieldNames` | client + guess |
| Map geometry | **ZoneDB 126** (`전장 튜토리얼`, map Battlefield_Tutorial_01), rect x 1312–1503, z 2848–2975, segment ZP05_11. Its minimap `minimap_z126` is the only texture with a diagonal chain of six round chambers, the shape on the in-game minimap | `ZoneDB`, minimap textures; [v &t=300s][v300] | client + video |
| Entry / exit point | **(1332.13, 2866.99)**, `Teleport_List` gate 1200 of field **119 "Sinking Nest"**. The blue portal icon on the in-game minimap measures (1332, 2868) | `Teleport_List`; [v &t=20s][v20] | client + video |
| Minimap scale for this zone | The texture covers a **192×192** square centred on the 192×128 rect: x = 1312 + u·192, z = 3008 − v·192 (u, v = 0..1 across the panel). The portal icon lands within 2 units of gate 1200. The same centring fits field 124 (§5) | measured | video + client |
| Entry cost (client) | 4 Dimensional Energy (item 688) normal, 4 hard. The guides say 5 / 10 (see [[gameplay/maps-and-dungeons]] §2). The video does not show the cost | `DungeonAdmission` | client |
| Entered from | Field **57 Raging Wind** (ZoneDB 74, x 4384–4543, z 1056–1215). The player stands on a stone portal ring at about **(4452, 1070)** when the "Connected World" dialog opens | [v &t=6s][v6] | video (±5) |
| Party | 3 players, all in the dungeon from 0:16 ("… entered the area") | [v &t=16s][v16] | video |

## 2. Pack positions (field 133)

These are the spots where the party stops and fights on every lap. The minimap chain runs from the portal (south-west) to a dead end (north-east). It is about 160 units long and has no side branches.

| # | Position (x, z) | Note | Example time |
|---|---|---|---|
| 0 | 1332, 2867 | Portal / entry point (gate 1200) | [v &t=20s][v20] |
| 1 | 1352–1372, 2884–2890 | First chamber. The party also waits here for respawns (§3) | [v &t=24s][v24], [&t=190s][v190] |
| 2 | 1377–1388, 2890–2897 | Second chamber | [v &t=325s][v325], [&t=430s][v430] |
| 3 | 1408–1419, 2908–2915 | Third chamber | [v &t=130s][v130], [&t=550s][v550] |
| 4 | 1449–1458, 2929–2935 | Fourth chamber (long fights) | [v &t=51s][v51], [&t=668s][v668] |
| 5 | 1460–1467, 2938–2942 | Fifth chamber | [v &t=62s][v62], [&t=145s][v145] |
| 6 | 1478–1482, 2951–2958 | Dead end, the last pack | [v &t=69s][v69], [&t=581s][v581] |

All *video*, about ±4 units (360p).

- **Pack size:** about **5–7** monsters are on screen at each stop ([v &t=40s][v40], [&t=141s][v141]). *video*. With six stops, that is about 30–40 monsters per lap (*guess*).
- **Monster types:** humanoid warriors with shields and bow archers ([v &t=51s][v51]). The client has exactly these for Nas: **688 Nas Warrior, 689 Nas Archer, 690 Elite Nas Warrior, 691 Elite Nas Archer, 1219 Superior Nas Warrior, 1220 Superior Nas Archer**. The archers carry a projectile id (1240, or 662 for the Superior one). *client*; which ids spawn in this run is a *guess*.
- **Damage taken by monsters:** hits of about 2,180–2,400 (one recurring number is **2180**). Most monsters die after a few hits ([v &t=24s][v24], [&t=72s][v72]). The HP cannot be measured at this resolution. *video*

## 3. Respawn and timing (3-player party, Hard)

| Measurement | Value | Source | Tag |
|---|---|---|---|
| Time for one lap (portal side → dead end → back to chamber 1) | **≈ 95–105 s** | camera-box track, laps start at 0:24, 1:48, 3:30, 5:12, 7:00, 8:33, 10:15 | video |
| Gap between pulls of chamber 1 | 84, 102, 102, 108, 93, 102 s | same | video |
| Idle wait at chamber 1 for the respawn | 2:51–3:30 (39 s), 4:36–5:12 (36 s), 8:15–8:33 (18 s), 9:51–10:15 (24 s). No loot comes in while they wait | [v &t=171s][v171], [&t=276s][v276], [&t=495s][v495], [&t=591s][v591] | video |
| So: a cleared pack is back after about | **90–100 s** (first refill: under ~80 s after the first clear) | derived | video |
| "Dungeon finished" | 11:29, about **11 min 13 s** after entry, while fighting at the dead end. No timer is on screen, so the cause is unknown (an event window ending is a *guess*) | [v &t=689s][v689] | video |

This fits the guides' "respawn only with a party … then about every minute" ([[gameplay/maps-and-dungeons]] §2), at the slow end.

## 4. Loot popups (what one player picked up)

Every kill sends one or two lines ("You acquired …") to the loot log. Every quantity seen:

| Item (`Item_Base` id) | Quantities seen | NPC sell price (gold, client) | Frequency |
|---|---|---|---|
| Faded Passion fragments (1900) | ×1, ×3, ×10, ×20 | 50 each | most kills |
| Faded Passion Piece (1901) | ×10, ×20 | 100 each | often, together with Yellow crystals |
| Faded Passion Pattern (1902) | ×10, ×20 | 200 each | often, together with Red or Black crystals |
| Crystal : Blue (700) | ×1–×5 | – | common |
| Crystal : Yellow (701) | ×1–×6 | – | common |
| Crystal : Red (702) | ×1–×6 | – | common |
| Crystal : Black (703) | ×1–×6 | – | less common, from about 2:36 |
| Medal : Bronze (1000) | ×1 | 5 | once ([v &t=30s][v30]) |

Sources: the loot log throughout, for example [v &t=54s][v54], [&t=111s][v111], [&t=216s][v216], [&t=327s][v327], [&t=360s][v360], [&t=465s][v465], [&t=555s][v555], [&t=660s][v660]. Item ids and sell prices are *client*, the rest *video*.

- Drops go straight into the bag. No loot window or ground bag appears. *video*
- Each drop line is **one stack of a single item**, and the quantities cluster at 1/3/10/20 (passion) and 1–6 (crystals). The server could roll an item, then a count from a short list. *guess*
- No gear, no essence, no horn and no sealed weapon drops in 11 minutes. *video*
- Gold value: one Pattern ×20 drop sells for **4,000 gold**, which is why the guides call Nas the gold farm (sell price *client*).
- A snapshot of ZonderCoRe's bag at 2:50 shows **759,955 gold** and stacks of 47/67/51/9 Blue/Yellow/Red/Black crystals ([v &t=170s][v170]). It is not taken again later, so the gold gained cannot be measured. *video*

## 5. Gathering in a dungeon (Crush Online, field 124)

The second video shows a quick material farm: enter, walk to the nearest nodes, gather, leave by the exit gate, re-enter. The "Do you want to leave the area?" dialog is opened at the gate and left open while gathering ([w &t=72s][w72], [&t=84s][w84]).

| Item | Value | Source | Tag |
|---|---|---|---|
| Dungeon | "[Lv 5] Fortress of Ghost" (Crush numbering) = client field **124** "[Lv 6] Ghost Fortress", ZoneDB 140 (x 1824–2015, z 1792–2047) | [w &t=72s][w72] | video + client |
| Instance timer | Counts down from **20:00** (19:40 about 20 s after entry), next to Kill / Death / Assist and **TP 0 / 10000** | [w &t=72s][w72], [&t=147s][w147] | video |
| Gather cast | About **3 s**. The bar starts at about 87.5 s and "You acquired Moonstone" appears at 90.5 s. Being hit by a Black Ghost did not stop it | [w &t=87s][w87] | video |
| Nodes gathered | Moonstone at **(1902, 2009)** and **(1880, 1923)** = `Trigger` 12401 (1902.95, 2007.71) and 12404 (1881.23, 1924.38). After re-entering, 12401 can be gathered again (a fresh instance) | [w &t=90s][w90], [&t=114s][w114], [&t=147s][w147] | video + client |
| Monsters near the entrance | Red Ghost, Black Ghost | [w &t=84s][w84] | video |

**Minimap check of `Trigger.tsv`.** Every icon on the Crush minimap matches a `Trigger` row of field 124 within about 5 units. The minimap texture covers a **256×256** square centred on the 192×256 zone (x 1792–2048, z 1792–2048):

| Minimap icon | Measured (x, z) | `Trigger` / `Teleport_List` row |
|---|---|---|
| White crystal | 1904, 2013 | 12401 Moonstone (1902.95, 2007.71) |
| White crystal | 1880, 1925 | 12404 Moonstone (1881.23, 1924.38) |
| Green leaf | 1916, 2015 | 12402 Lavender (1916.33, 2010.64) |
| Green leaf | 1861, 1950 | 12403 Peppermint (1864.49, 1948.80) |
| Green leaf | 1966, 1971 | 12408 Peppermint (1964.14, 1969.35) |
| Green leaf | 2011, 1973 | 12407 Lavender (2006.81, 1970.48) |
| Green leaf | 1918, 1882 | 12405 Lavender (1919.07, 1884.46) |
| Green leaf | 1918, 1863 | 12406 Peppermint (1918.40, 1866.64) |
| Yellow cross | 1975, 1890 | 12410 type 10 "Ghost soldier" (1976.00, 1894.89) |
| Pink dot ×2 | 2007, 2000 / 1866, 1864 | FiledPortal 1238 (1997.81, 1991.80) / 1237 (1875.62, 1865.92) |
| Blue glow | 1841, 1994 | Entry gate 1236 (1852.28, 1991.14) |

Source: [w &t=76s][w76]. Measurements *video*, rows *client*. The Moonstone nodes 12411 and 12413 and the Peppermint nodes 12412 and 12414 (south-east) are not drawn on the minimap at that moment.

What this adds: the **2016 Crush node layout is the same as the final client's `Trigger.tsv`**, so a server can spawn gathering nodes straight from that table. It also confirms the rule for non-square zones: the minimap is the square of the long side, centred.

## 6. Event dungeon list (world map, Dungeon tab)

At 0:03 the world map's *Event Dungeon* list shows five entries, each with a coloured dot and a number ([v &t=3s][v3]):

| Entry | Number shown | `Event_Dungeon` row with that value (`hour?` column) |
|---|---|---|
| Hill of Gollam | 12 | target 115, 180 min |
| Nas Village Entrance | 12 | target 132 or 133, 180 min |
| Siren Lake | 12 | target 132 or 133, 180 min |
| Place for Scattered troops | 21 | target **134**, 80 min |
| The avenue of spirit | 24 | target **135**, 80 min |

The numbers are exactly the `Event_Dungeon` values 12/12/12/21/24 (*client + video*). So **134 = Place for Scattered Troops** and **135 = The Avenue of Spirit**. Their `DungeonAdmission` cost of 5 normal / 15 hard also fits the guides' "5 normal". Nas takes 133 (crystal rewards, §1), which leaves **132 = Siren Lake** (*guess*). What the number and the dot colour mean (an hour, a level, the host nation) is not known. The list's header also shows counters 56 (gold icon), 25 / 23 / 8 (red / blue / dark icons). *video*

## 7. Timestamped log

| Time | What happens |
|---|---|
| [0:00][v0] | World map, Dungeon tab. The Event Dungeon list has five entries (§6). |
| [0:04][v4] | At the stone portal ring in field 57 Raging Wind: "Connected World" dialog, Nas Village Entrance, Hard Mode, *Entrance*. |
| [0:12][v12] | Loading screen (Wanderer of Time artwork). |
| [0:16][v16] | Inside at the portal (1332, 2867). Uraniel and Maaac enter the area. |
| [0:24][v24] | First pack in chamber 1. Damage numbers of about 2,180–2,400. |
| [0:30][v30] | First loot: Faded Passion fragments, Crystal Yellow ×3, Medal Bronze, Crystal Red. |
| [1:09][v69] | Reaches the dead end (1482, 2956), then turns back. |
| [1:48][v108] | Lap 2 starts at chamber 1: the packs have respawned. |
| [2:36][v156] | First Crystal Black drop at the dead end. |
| [2:50][v170] | Inventory opened: 759,955 gold, crystal stacks. |
| [2:51–3:30][v171] | Idle at chamber 1, waiting for the respawn. |
| [3:36][v216] | Faded Passion fragments ×10 and Crystal Blue ×4 come in quick succession. |
| [5:27][v327] | Faded Passion Piece ×20 with Crystal Yellow. |
| [6:27–6:54][v387] | Back near the portal, few drops. |
| [9:15][v555] | Crystal Red ×6 and Blue ×5. |
| [10:15][v615] | Last lap starts. |
| [11:29][v689] | "Dungeon finished. Exiting the dungeon initiated." Back in Raging Wind at 11:35. |

[v]: https://www.youtube.com/watch?v=eL5hx5C9iZw
[w]: https://www.youtube.com/watch?v=Tz9LI5N6nQk
[v0]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=0s
[v3]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=3s
[v4]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=4s
[v6]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=6s
[v12]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=12s
[v16]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=16s
[v20]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=20s
[v24]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=24s
[v30]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=30s
[v40]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=40s
[v51]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=51s
[v54]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=54s
[v62]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=62s
[v69]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=69s
[v72]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=72s
[v108]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=108s
[v111]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=111s
[v130]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=130s
[v141]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=141s
[v145]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=145s
[v156]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=156s
[v170]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=170s
[v171]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=171s
[v190]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=190s
[v216]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=216s
[v276]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=276s
[v300]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=300s
[v325]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=325s
[v327]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=327s
[v360]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=360s
[v387]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=387s
[v430]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=430s
[v465]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=465s
[v495]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=495s
[v550]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=550s
[v555]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=555s
[v581]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=581s
[v591]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=591s
[v615]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=615s
[v660]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=660s
[v668]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=668s
[v689]: https://www.youtube.com/watch?v=eL5hx5C9iZw&t=689s
[w72]: https://www.youtube.com/watch?v=Tz9LI5N6nQk&t=72s
[w76]: https://www.youtube.com/watch?v=Tz9LI5N6nQk&t=76s
[w84]: https://www.youtube.com/watch?v=Tz9LI5N6nQk&t=84s
[w87]: https://www.youtube.com/watch?v=Tz9LI5N6nQk&t=87s
[w90]: https://www.youtube.com/watch?v=Tz9LI5N6nQk&t=90s
[w114]: https://www.youtube.com/watch?v=Tz9LI5N6nQk&t=114s
[w147]: https://www.youtube.com/watch?v=Tz9LI5N6nQk&t=147s

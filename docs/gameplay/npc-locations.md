---
title: "NPC and point-of-interest locations"
---

# NPC and point-of-interest locations

Where the server has to place town NPCs, portals and field-quest NPCs. Positions are world (x, z) in the client's units: 256 units per terrain segment `ZPxx_zz`, x to the east, z to the north (see [[spec/navmesh|Navmesh]]). Related pages: [[gameplay/maps-and-dungeons|Maps and dungeons]], [[spec/monsters|Monsters]], [[spec/world|World]].

Confidence tags: *client* = read from a client table; *video* = measured from gameplay video (about ±3 units); *image* = read off a guide screenshot's minimap (about ±3 units); *guide* = a guide's text; *guess*.

## 1. What the client data contains (and what it does not)

- **Town NPCs are not placed anywhere in the client.** `map.jpk` holds only the terrain (`.zp`), navmesh (`.nav`), minimap textures and fog. The `.zp` files contain no object or NPC list. `map/bookmarks.txt` is a list of editor camera bookmarks, not NPC positions. No table holds an NPC spawn point. Town NPCs were spawned by the server (0x803), so their positions have to be recovered from screenshots and video. *client*
- **The client does place these:**
  - **Teleport gates and arrival points:** `Teleport_List.tsv` (gateId, field, x, z, linked gate and field). This includes the Village start point (field 87 at 2688.83, 382.86). *client*
  - **Field-quest NPCs, dungeon and abyss NPCs, and gathering nodes:** `Trigger.tsv` (`field`, `x`, `z`, `name_key`). There are 123 rows: 19 NPC-type rows (table below) and 104 herb or ore nodes inside dungeons 121–129 and 142. *client*
  - **Which field each quest NPC stands in:** `Quest.tsv` (`start_npc`, `obj*_type 4` = talk to unit `a`, with the `map1..3` fields giving the Arslan/Erion/Armia field ids). This gives the field but not the position. *client*
  - **Minimap icon set:** `ui/Default.guimat` `MiniMap.Icon_*` on `WorldMap_Icon.png`, for example Store (bag), Mark (anvil), Guild (red banner), Guild_01 (castle), Oracle_01 (book), Transfer (green star), Warehouse (chest), Auction (coins), Mail (envelope), WeaponJewel (diamond), Training (crossed axes), Potal (blue swirl). The table that maps an NPC to its icon was not found in the client data. The identities below come from the video. *client*

## 2. How coordinates were derived

1. **Minimap texture = ZoneDB rectangle.** `map/minimap/minimap_z<zone>_00.dds` covers exactly the `ZoneDB.tsv` rectangle `x0..x1+1, z0..z1+1`, with x to the right and **z up**: `x = x0 + px·W/512`, `z = (z1+1) − py·W/512`. This was checked by rendering the navmesh of segment (7,6) against `minimap_z103` (same shape), and by drawing the four `Teleport_List` gates of field 88 onto `minimap_z128` (each lands at the end of one arm). *client*
2. **In-game minimap panel (1280×720 video).** The texture is stretched over screen pixels x 1103.3–1274.3 and y 532.3–703.3, and the panel always shows the whole zone. The white camera box is centred on the player. The box was detected automatically in each frame, and its centre gives the player's world position. Calibration check: in Corpse incineration (field 100), the player who is talking to the Scout measures within about 6 units of Trigger row 10001 (558.98, 2257.79). *video*
3. **NPC position from a dialog frame.** NPC = player position + (Δx/29.7, −Δy/22.1), where Δ is the screen offset from the player's name label (at about 640, 280) to the NPC's name label. The scale comes from the camera box size and agrees with repeated sightings of Odin (spread ≤ 2.3 units). *video*
4. **Guide screenshots.** The minimap crop was scaled and shifted onto the texture so the outlines matched (residual ≤ 2 units), then each icon was read off a world grid. *image*
5. **Three copies per nation.** Every home map exists three times with identical meshes; the navmesh vertex and face counts match. Positions are given in the copy listed under each table and also as **local** coordinates (world − segment origin). Add the copy's segment origin to get the other nations' positions.

| Map | Field ids (Arslan / Erion / Armia) | Segment origins (x, z) for the three copies |
|---|---|---|
| Fortress (`A/B/C_요새`, ZoneDB 103–105) | 120 (one id) | (1792, 1536), (2048, 1536), (2304, 1536) |
| Village (`마을A/B/C`, same mesh as the Fortress) | 87 / 91 / 95 | (2560, 256), (3840, 256), (5120, 256) |
| Training Camp (ZoneDB 128–130) | 88 / 92 / 96 | (256, 3328), (512, 3328), (768, 3328) |
| Training Ground (ZoneDB 127, 131, 132) | 89 / 93 / 97 | (256, 3584), (512, 3584), (768, 3584) |
| Castle (`A/B/C대도시`, ZoneDB 144–146) | 90 / 94 / 98 | (256, 4096), (512, 4096), (768, 4096) |

The Village's segments (10,1), (15,1) and (20,1) use **the same navmesh as the Fortress** (segment 7,6). The Village is the old copy of the town map, and its start point (2688.83, 382.86) is local (128.8, 126.9), at the centre of the Fortress plaza. In the 2018 game players moved from the Training Camp to the Castle and then the Fortress, and the camp's Village gate had no portal icon ([video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=845s)). *client + video*

## 3. Fortress (field 120)

Absolute positions are for the copy at origin (1792, 1536). The video player's nation is unknown, but all three copies share one layout.

| NPC | Unit id | Role | x | z | local x, z | Source | Confidence |
|---|---|---|---|---|---|---|---|
| Wren | 204 | Merchant (shop 281: potions, scrolls, Dimensional Energy) | 1983.2 | 1709.8 | 191.2, 173.8 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=1897s), [&t=2089s](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2089s); guide "upper stairs, right" ([guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573)) | video |
| Cassia | 212 | Material merchant (shop 286) | 1990.7 | 1716.1 | 198.7, 180.1 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=1971s); "NE in Fortress" ([guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1354427871)) | video |
| Lewellyn | 205 | Scroll merchant (shop 282) | 1987.0 | 1712.4 | 195.0, 176.4 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2085s), [&t=2469s](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2469s) | video |
| Odin | 213 | Blue Union crafting (armour) | 1991.9 | 1703.6 | 199.9, 167.6 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2713s), [&t=2807s](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2807s) | video |
| Owen | 214 | Red Union crafting (potions, powders) | 1998.9 | 1709.0 | 206.9, 173.0 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=1979s), [&t=2623s](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2623s) | video |
| Paraman | 322 | Legendary blacksmith | 1959.5 | 1699.5 | 167.5, 163.5 | [video minimap](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2071s) | video |
| Alan | 323 | Rune maker | 1939.0 | 1704.9 | 147.0, 168.9 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2049s); diamond icon (1945, 1702.5) ([guide image](https://steamcommunity.com/sharedfiles/filedetails/?id=1459898274)) | video + image |
| Casta | 324 | Rune manager | 1942.8 | 1704.1 | 150.8, 168.1 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2057s) | video |
| Ashley | 206 | Merits costume merchant (shop 284) | 1888.5 | 1704.5 | 96.5, 168.5 | [video minimap](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2229s) | video |
| Kesley | 210 | Legion administrator | 1879.9 | 1679.4 | 87.9, 143.4 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2247s); red banner icon | video + image |
| Athan | 207 | Merits / medal merchant (shop 283) | 1910.6 | 1666.7 | 118.6, 130.7 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2281s) | video |
| Cathy | 303 | Auction house (coins icon) | 1924.8 | 1666.7 | 132.8, 130.7 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2269s) | video |
| Kaysa | 300 | Warehouse (chest icon) | 1924.8 | 1657.0 | 132.8, 121.0 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2263s) | video |
| Mail box | 218 | Mail (envelope icon) | 1928 | 1642 | 136, 106 | [video minimap](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2071s) | image |
| Freya | 200 | Oracle of Knowledge, quests (shop 289; book icon) | 1906.6 | 1641.0 | 114.6, 105.0 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=1927s) (4 sightings, spread ≤ 3) | video |
| Haley | 217 | Teleporter (green star icon) | 1927.6 | 1616.4 | 135.6, 80.4 | [video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2691s); star icon (1929, 1614.5) ([image](https://steamcommunity.com/sharedfiles/filedetails/?id=1459898274)) | video + image |
| Fortress Portal | 311 | Level-matched dungeon portal (bottom-right circle) | 1981 | 1561 | 189, 25 | portal icon; "portal bottom-right" ([guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1345368744)) | image + guide |
| Hadrian? | 211 | Fortress administrator (castle icon, west arm) | 1841 | 1712 | 49, 176 | castle icon; "top-left corner of the map" ([Turkish guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1460533609)) | image + guess |
| Bell Thain? | 208 | Training officer (crossed-axes icon, north lobe) | 1917 | 1746 | 125, 210 | `Training` icon | image + guess |
| (anvil icon) | 237 Farrell / 304 Fergus? | Blacksmith or decomposer, next to Ashley | 1892 | 1708 | 100, 172 | anvil icon ([video minimap](https://www.youtube.com/watch?v=cqYz3j59MFI&t=2071s)) | image + guess |

The east-arm group (Wren, Cassia, Lewellyn, Odin, Owen) also carries one or two more anvil icons. One guide puts Farrell, the blacksmith, "next to Odin", with the runes to the left of them ([strategy guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1460486971)). A server can place Farrell (237/317) at about (1995, 1700). *guide + guess*

## 4. Training Camp (fields 88 / 92 / 96)

Measured in the Erion copy (field 92) and shifted by −256 in x to the Arslan copy (field 88, origin 256, 3328).

| NPC | Unit id | Role | x | z | local x, z | Source | Confidence |
|---|---|---|---|---|---|---|---|
| Wren | 238 | Merchant (shop 287) | 373.8 | 3479.5 | 117.8, 151.5 | [video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=553s), [&t=1115s](https://www.youtube.com/watch?v=E-87WgbO_vo&t=1115s) | video |
| Lewellyn | 315 | Scroll merchant, quests | 378.9 | 3478.9 | 122.9, 150.9 | [video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=845s) (4 sightings) | video |
| Odin | 335 | Blue Union (shop 6) | 387.1 | 3478.9 | 131.1, 150.9 | [video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=1109s) | video |
| Owen | 337 | Red Union (shop 8) | 393.7 | 3470.4 | 137.7, 142.4 | [video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=553s) | video |
| Frei | 198 | Oracle of Knowledge, quests | 358.8 | 3469.1 | 102.8, 141.1 | [video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=1125s) | video |
| Mail box | 218 | Mail | 347.6 | 3464.2 | 91.6, 136.2 | [video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=1125s) | video |
| Guard | 215 | Quest NPC at the Corpse incineration gate | 385.0 | 3436.4 | 129.0, 108.4 | [video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=1155s) | video |

Implementation check (2026-10-05): Frei's measured point (358.8, 3469.1) is not
walkable in the owned client's ZP01_13 navmesh. The Python test server uses the
nearby walkable point (360.8, 3466.1), with 2.06 units of mesh-edge clearance.
This is a placement adjustment for testing, not a more precise video measurement.
Shaia and Floyd's estimates below pass the same check. See [[testing]].

Gates (from `Teleport_List`; each portal icon is drawn about 10–15 units further out, at the tip of the arm). *client*

| Gate | x | z | Goes to |
|---|---|---|---|
| 1198 | 403.96 | 3492.28 | Castle 90 |
| 1201 | 356.65 | 3502.59 | Village 87 (no portal shown in 2018) |
| 1202 | 325.80 | 3438.90 | Training Ground 89 |
| 1503 | 391.21 | 3436.26 | Corpse incineration 99 |

Erion and Armia copies: gates 1196/1204/1205/1504 and 1194/1207/1208/1505 respectively.

## 5. Training Ground (fields 89 / 93 / 97)

| NPC | Unit id | Role | x | z | local x, z | Source | Confidence |
|---|---|---|---|---|---|---|---|
| Shaia | 201 | Guide, gives the first quest (`Quest` 1, field 89/93/97) | 423.9 | 3664.8 | 167.9, 80.8 | [video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=149s) | video |
| Floyd | 239 | Biologist, quests | 370.5 | 3660.6 | 114.5, 76.6 | [video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=262s) | video |

Gates (field 89): 1203 at (451.64, 3629.45) goes to the Camp; the field portals 1406 (341.41, 3784.99) and 1407 (448.52, 3776.57) link the two top circles. *client*

## 6. Village (87/91/95), Castle (90/94/98), tutorial (117)

- **Village:** the only gate rows are 0 (2688.83, 382.86), 1 (3963.73, 322.41) and 2 (5245.8, 337.38). Each links to itself, so these are spawn points. No video shows NPCs here. *client*
- **Castle:** gates 1199 (318.07, 4135.37) and 1410 (315.24, 4140.56) in field 90 (Erion: 1197, 1420; Armia: 1195, 1430). Quests place Krister (219, Stock Administrator), Aenes (327, Oracle of Protection) and the event NPC Corpse Bride (2001) here. One video walks from the camp gate through the Castle to a **portal that offers "move to Fortress"** ([video](https://www.youtube.com/watch?v=cqYz3j59MFI&t=1876s)), but no NPC positions were measured. *client + video*
- **Tutorial (field 117, ZoneDB 2 `튜토리얼맵_01`):** no table places anything here (see [[spec/navmesh|Navmesh]]). Candidate units: Training Assistants 220/222/223 and Training Officer 221. A safe spawn point is (1427, 429). *client*

## 7. Field-quest NPCs placed by the client (`Trigger.tsv`)

| Trigger id | Field | x | z | NPC (name key) | Model |
|---|---|---|---|---|---|
| 9901 / 10001 / 10101 | 99 / 100 / 101 | 465.27 / 558.98 / 979.52 | 2259.45 / 2257.79 / 2098.32 | Scout (UnitName_238) | 178 |
| 10803 / 10904 / 11105 | 108 / 109 / 111 | 448.84 / 575.82 / 1216.22 | 2753.87 / 2629.17 / 2753.61 | Scout Leader (UnitName_241) | 187 |
| 11406–11408 | 114 | 315.92, 305.42, 451.65 | 3273.45, 3127.78, 3130.35 | Knightage's Leader | 187 |
| 12409, 12410 | 124 Ghost Fortress | 1861.5, 1976.0 | 1999.0, 1894.89 | Ghost soldier | 274 |
| 12511, 12512 | 125 Tow Canyon | 2087.03, 2200.23 | 1985.81, 1999.02 | Dispatch Knight | 88 |
| 12213, 12214 | 122 Tsunami Lake | 1366.02, 1430.97 | 1823.75, 2002.75 | A Doubtful character | 89 |
| 12316, 12317 | 123 Swamps | 1602.55, 1627.73 | 2004.82, 1905.95 | A Doubtful character | 391 |
| 12215 | 122 | 1469.48 | 1990.67 | Tsunami Lake flower | 4056 |
| 12318 | 123 | 1623.19 | 1867.09 | Swamp mushroom | 2049 |

The remaining 104 rows are herb and ore gathering nodes (type 0, shape 5; `item_or_quest` = material item, 8 to 14 per dungeon). The server should load them straight from `Trigger.cdb`. The video confirms row 10001: the player who is talking to the Scout stands within about 6 units of it ([video](https://www.youtube.com/watch?v=E-87WgbO_vo&t=1215s)). *client + video*

## 8. Still unplaced

From `Quest.tsv` and `UnitDB.tsv` (field from the quests; *client*): Bernice 224 (Oracle of Judgment), Krister 219 (Castle), Aenes 327/328, Raon 242 (Fortress or Castle), Arion/Arkin 241/243, Plida 312 (channel teleporter), Fergus 304, Lars 216 (castle teleporter), Joel 325, Truestone 321, ladi 320 (Prison, field 110), Abyss Portal 301, Fortress Guards 186–188 and Imperial Guards 189–197. The video [cqYz3j59MFI](https://www.youtube.com/watch?v=cqYz3j59MFI) still has unmeasured Fortress footage (about 1880–2960 s), and the same frame method would place these.

---
title: "Abyss map and portal graph"
---

# Abyss map and portal graph

What a server needs to rebuild the **Abyss**: which client fields it is made of, where every portal is, where each portal leads, and how players get in and out. The base source is a player-made image that puts the minimaps of all Abyss fields side by side and draws a coloured line between every pair of connected portals ([img][abyss-img]). It was posted to r/crushgame on 2016-12-18 with no text and no comments ([post][abyss-post]). The matching forum thread (`full-map-of-abyss.719`) was never archived. For the rest of the game's maps see [[maps-and-dungeons]].

Every gate that the client's `Teleport_List` table lists for the Abyss matches a line drawn in the image (18 of 18). The image then fills in the gates that the table leaves out.

Tags: *client* = decoded client table, *image* = read off the stitched map, *guess* = inferred.

## How the image was read

- **Minimap orientation:** screen right is +x and screen up is +z (north up, no rotation). This was checked against all 18 gates in the client table. *client + image*
- **Scale:** a minimap shows about 175 world units around the centre of its ZoneDB rectangle. The image scale is about **1.53 px per unit** for the 192-unit fields and **1.87 px per unit** for The avenue of spirit, which is a smaller field (160 units). Known gates land within about ±5 units of where the image puts them, so positions marked ≈ below carry the same error. *image* ([img][abyss-img])
- **What the marks mean:** a white star is a portal. The white square with an orange arrow is the player (the screenshot was taken standing next to that portal). Coloured lines join two portals that lead to each other. Large filled dots come in matched colours (blue, red and green), but the source never says what they mean (see [Open questions](#open-questions)).

## Fields and layout

Every Abyss field fills one 256-unit world segment, laid out on a grid from x = 256 and z = 2048. Level = the tier in the ZoneDB zone name (`어비스_LV<n>_<field>`), and *Map texture* is ZoneDB's `map` column.

| Level | Field id | In-game name (FieldNames) | ZoneDB id | ZoneDB rect x0–x1 / z0–z1 | Segment (x,z) | Map texture | In image |
|---|---|---|---|---|---|---|---|
| 1 | 99 | Corpse incineration | 108 | 288–479 / 2080–2271 | 1,8 | Abyss_Lv01 | top row, 2nd |
| 1 | 100 | Corpse incineration | 110 | 544–735 / 2080–2271 | 2,8 | Abyss_Lv01 | top row, far right |
| 1 | 101 | Corpse incineration | 111 | 800–991 / 2080–2271 | 3,8 | Abyss_Lv01 | top row, 1st |
| 2 | 102 | Death's Rest (labelled "Place for Scattered troops" on the minimap) | 112 | 288–479 / 2336–2527 | 1,9 | Abyss_Lv02 | 2nd row, 2nd |
| 2 | 103 | Place for Scattered troops | 117 | 544–735 / 2336–2527 | 2,9 | Abyss_Lv02 | 2nd row, 4th |
| 2 | 104 | Place for Scattered troops | 118 | 800–991 / 2336–2527 | 3,9 | Abyss_Lv02 | 2nd row, 6th |
| 2 | 105 | Place for Scattered troops | 119 | 1056–1247 / 2336–2527 | 4,9 | Abyss_Lv02 | 2nd row, 3rd |
| 2 | 106 | Place for Scattered troops | 120 | 1312–1503 / 2336–2527 | 5,9 | Abyss_Lv02 | 2nd row, 1st |
| 2 | 107 | Place for Scattered troops | 121 | 1568–1759 / 2336–2527 | 6,9 | Abyss_Lv02 | 2nd row, 5th |
| 3 | 108 | The land of Greed | 113 | 288–479 / 2592–2783 | 1,10 | Abyss_Lv03 | 3rd row, right |
| 3 | 109 | The land of Greed | 114 | 544–735 / 2592–2783 | 2,10 | Abyss_Lv03 | 3rd row, left |
| 3 | 110 | Prison | 115 | 800–991 / 2592–2783 | 3,10 | Abyss_Lv03 | not shown |
| 3 | 111 | The land of Greed | 116 | 1056–1247 / 2592–2783 | 4,10 | Abyss_Lv03 | 3rd row, middle |
| 4 | 112 | Death's Rest | 122 | 288–479 / 2848–3039 | 1,11 | Abyss_Lv04 | not shown |
| 4 | 113 | The avenue of spirit | 123 | 544–703 / 2880–3039 | 2,11 | 113 | 4th row |
| 5 | 114 | The way go to devildom | 124 | 288–479 / 3104–3295 | 1,12 | Abyss_Lv05 | bottom |

Sources: field names `FieldNames.tsv`, rectangles `ZoneDB.tsv` *client*; match between image tiles and field ids by the portal-line method below *client + image* ([img][abyss-img]). FieldNames 116 is a second "The avenue of spirit" with no ZoneDB rectangle *client*.

How the tiles were matched to field ids: the three Lv 1 tiles were told apart by the position of their exit gate (1500 at top-left = 99, 1501 at bottom-left = 100, 1502 at top-right = 101). Every other tile was then fixed by following lines from a gate whose position the client gives. For example, gate 1114 in field 109 is linked to gate 1126 in field 106 in the client table, and the image draws a line from that corner to the 1st Lv 2 tile, so that tile is 106. *client + image*

## Ways in and out

| From | Gate | Position (x, z) | To | Gate there | Confidence |
|---|---|---|---|---|---|
| Training Camp 88 | 1503 | 391.21, 3436.26 | Corpse incineration 99 | 1500 | *client* |
| Training Camp 92 | 1504 | 647.43, 3436.47 | Corpse incineration 100 | 1501 | *client* |
| Training Camp 96 | 1505 | 903.36, 3436.17 | Corpse incineration 101 | 1502 | *client* |
| Corpse incineration 99 | 1500 | 306.03, 2254.17 | Training Camp 88 | (1503) | *client*; the image shows a "Training Camp" tooltip on this portal ([img][abyss-img]) *image* |
| Corpse incineration 100 | 1501 | 567.98, 2100.77 | Training Camp 92 | (1504) | *client* |
| Corpse incineration 101 | 1502 | 973.31, 2254.92 | Training Camp 96 | (1505) | *client* |
| Fortress 120 (teleporter) | 1901 / 1902 / 1903 | none in the table | Place for Scattered troops 103 / 105 / 107 | none | *client* (`Teleport_List`, label "Land") |

- There is one Abyss entrance per nation: each nation's Training Camp (fields 88, 92 and 96, the ZoneDB camping sites A, B and C) leads to its own Corpse incineration. *client*
- The fortress teleporter's free "Abyss" option ([[maps-and-dungeons]]) is presumably what rows 1901–1903 describe. It lands in field 103, 105 or 107, which are the only three Lv 2 fields with a third portal that has no line in the image. *guess*, built on *client* + *image*

## Portal table

Corner = where the portal sits on that field's minimap (TL top-left, TR top-right, BL bottom-left, BR bottom-right). Positions with a gate id are the client's own. Positions marked ≈ are measured off the image (±5 units).

| Field | Corner | Position (x, z) | Gate id | Leads to (field, corner) | Confidence |
|---|---|---|---|---|---|
| 99 | TL | 306.03, 2254.17 | 1500 | Training Camp 88 | *client* |
| 99 | BL | 312.96, 2102.09 | 1106 | 102 TL (gate 1100) | *client*; line drawn *image* |
| 100 | BL | 567.98, 2100.77 | 1501 | Training Camp 92 | *client* |
| 100 | BR | ≈ 718, 2104 | – | 104 TR | *image* |
| 101 | TR | 973.31, 2254.92 | 1502 | Training Camp 96 | *client* |
| 101 | BL | ≈ 823, 2103 | – | 106 TL | *image* |
| 102 | TL | ≈ 309, 2497 | 1100 (named by 1106; not a row of its own) | 99 BL | *client* link, *image* position |
| 102 | BR | ≈ 451, 2365 | – | 109 TL | *image* |
| 103 | TL | 566.51, 2496.40 | 1122 | 108 TR (1109) | *client* + *image* |
| 103 | BL | ≈ 569, 2361 | – | 111 TL | *image* |
| 103 | TR | ≈ 695, 2491 | – | no line; red dot (fortress arrival? *guess*) | *image* |
| 104 | TR | ≈ 962, 2499 | – | 100 BR | *image* |
| 104 | BL | ≈ 828, 2361 | – | 111 BR | *image* |
| 105 | BL | 1084.75, 2361.27 | 1131 | 109 BL (1125) | *client* + *image* |
| 105 | BR | ≈ 1217, 2365 | – | 108 TL | *image* |
| 105 | TL | ≈ 1079, 2497 | – | no line; blue dot (fortress arrival? *guess*) | *image* |
| 106 | TL | ≈ 1330, 2494 | – | 101 BL | *image* |
| 106 | BR | ≈ 1476, 2362 | 1126 (named by 1114; not a row of its own) | 109 BR (1114) | *client* link + *image* |
| 107 | BR | 1732.58, 2362.85 | 1124 | 111 TR (1107) | *client* + *image* |
| 107 | BL | ≈ 1593, 2362 | – | 108 BR | *image* |
| 107 | TR | ≈ 1727, 2501 | – | no line; green dot (fortress arrival? *guess*) | *image* |
| 108 | TR | 456.63, 2761.09 | 1109 | 103 TL (1122) | *client* + *image* |
| 108 | BL | 308.96, 2619.52 | 1140 | 113 TL (1134) | *client* + *image* |
| 108 | TL | ≈ 318, 2755 | – | 105 BR | *image* |
| 108 | BR | ≈ 445, 2621 | – | 107 BL | *image* |
| 109 | TL | ≈ 574, 2758 | – | 102 BR | *image* |
| 109 | TR | 711.35, 2760.44 | 1135 | 113 BL (1138) | *client* + *image* |
| 109 | BL | 567.67, 2620.55 | 1125 | 105 BL (1131) | *client* + *image* |
| 109 | BR | 701.93, 2624.07 | 1114 | 106 BR (1126) | *client* + *image* |
| 111 | TR | 1225.76, 2761.94 | 1107 | 107 BR (1124) | *client* + *image* |
| 111 | BL | 1080.11, 2620.79 | 1137 | 113 TR (1142) | *client* + *image* |
| 111 | TL | ≈ 1080, 2757 | – | 103 BL | *image* |
| 111 | BR | ≈ 1215, 2623 | – | 104 BL | *image* |
| 113 | TL | 558.93, 3004.09 | 1134 | 108 BL (1140) | *client* + *image* |
| 113 | TR | 688.29, 3008.59 | 1142 | 111 BL (1137) | *client* + *image* |
| 113 | BL | 562.83, 2896.42 | 1138 | 109 TR (1135) | *client* + *image* |
| 113 | BR | 664.27, 2890.44 | 1139 | 114 TR (1136) | *client* + *image* (black line) |
| 114 | TR | 455.13, 3271.86 | 1136 | 113 BR (1139) | *client* + *image*; the only portal shown in 114 |

Source for every *image* row: [img][abyss-img]. Source for every *client* row: `Teleport_List.tsv` (columns gateId, fieldId, x, z, linkGate, linkField).

- **Portals sit at four standard spots in each segment.** Measured from the segment origin (segX·256, segZ·256), the known gates sit near (55–60, 52–61) for BL, (50–57, 192–206) for TL, (190–196, 58–64) for BR and (199–205, 200–207) for TR. Gates 1106 (field 99) and 1122 (field 103) have nearly the same offsets in their segments, so a server can place the ≈ portals on these spots with confidence. *client* (pattern), *guess* (applies to the missing ones)
- **The gates missing from the client table** fall between 1100 and 1142, a range the table uses with gaps: 1100, 1126 and about 15 more (one per ≈ row above). The real ids for those portals were probably in the server's data. *guess*

## Routes

Each Lv 1 field (one per nation) leads to its own Lv 2 field. All routes then meet at The avenue of spirit (113), and from there one portal leads to The way go to devildom (114). *image + client* ([img][abyss-img])

| Start (nation camp) | Path to the bottom | Jumps |
|---|---|---|
| 88 → 99 | 99 → 102 → 109 → 113 → 114 | 4 |
| 92 → 100 | 100 → 104 → 111 → 113 → 114 | 4 |
| 96 → 101 | 101 → 106 → 109 → 113 → 114 | 4 |
| Fortress → 103 | 103 → 108 or 111 → 113 → 114 | 3 |
| Fortress → 105 | 105 → 108 or 109 → 113 → 114 | 3 |
| Fortress → 107 | 107 → 108 or 111 → 113 → 114 | 3 |

- The Lv 3 fields connect the three nations' Lv 2 fields to one another: 108 links 103, 105 and 107; 109 links 102, 105 and 106; 111 links 103, 104 and 107. Players of different nations therefore meet in the Land of Greed. *image* ([img][abyss-img])
- Fields 110 (Prison) and 112 (Death's Rest) are not in the image, and no gate in the client table touches them. They may be closed areas or ones that a trigger or quest sends players into. *guess*

## Markers inside fields

| Field | What | Position (x, z) ≈ | Confidence |
|---|---|---|---|
| 108 | 7 open clearings (lighter circles) at ≈ (390,2738), (362,2713), (332,2683), (385,2689), (432,2693), (404,2668), (376,2637) | see list | *image* |
| 108 | The centre clearing (385, 2689) holds a red multi-dot icon, probably a boss or elite group | 385, 2689 | *image*; meaning *guess* |
| 108 | The other clearings show red dots (monsters?) at 362,2713 · 432,2693 · 376,2637, and blue dots (other players or NPCs?) in most clearings | – | *image*; meaning *guess* |
| 108 | A red crystal formation on the south edge (decoration) | ≈ 385, 2600 | *image* |
| 111 | One clearing with a blue dot | 1103, 2686 | *image* |
| 111 | A large red crystal north of the centre (landmark) | ≈ 1140, 2740 | *image* |
| 106 | A large blue crystal or object in the middle (landmark; the source does not mark it as a boss) | ≈ 1440, 2425 | *image* |
| 113 | A white rectangle in the centre of the minimap (probably the camera frame, not a marker) | – | *image* |

Source: [img][abyss-img]. The image has **no NPC names, no level numbers and no monster names**. Those have to come from other sources. Leads: the forum threads "make-abyss-great-again.338" (archived 2016-10-24) and "stay-afk-in-abyss-this-game-is-so-good.686" (archived 2017–2018) in the Wayback CDX. The ES guide's claim that Abyss loot stops at level 30 is already on [[maps-and-dungeons]].

## Open questions

- **The coloured dots.** Blue dots sit on 105 TL and next to 109 BL. Red dots sit on 103 TR and 111 TL. Green dots sit on 107 TR and 108 BR. Each pair matches one nation-coloured line family, and the unlinked portal of 103, 105 and 107 always carries one. A plausible reading: "the fortress drops you here", with the paired dot marking that nation's way down. *guess*
- **Line colours** (blue, red, green, plus black for the last jump) may only be there to keep the lines apart, or they may mark nations. The source does not say. *image*
- **Name of field 102.** FieldNames gives "Death's Rest", but its minimap reads "Place for Scattered troops". The minimap title may come from a different string table. *client* vs *image*

[abyss-img]: https://i.imgur.com/GULFN0G.jpg
[abyss-post]: https://www.reddit.com/r/crushgame/comments/5j0s94/

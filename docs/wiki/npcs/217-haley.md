---
title: "Haley"
type: "npc"
id: 217
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 217", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3", "video: [[gameplay/video-early-quests]] §1 (Haley menu at 63:50 and 84:35): Castle 10000, Fortress 4000 ('TOP Fortress'), Gaia and Abyss with no price", "image: [[gameplay/maps-and-dungeons]] §1 and [[gameplay/progression-and-economy]] §4 Teleporter (noob guide): Castle 10,000, Fortress 6,000, Gaia and Abyss free", "client + guess: [[gameplay/abyss-map]] Teleport_List 1901–1903 ('Land' rows of field 120) put the free Abyss option in fields 103/105/107", "guess: Castle destination = the player's nation copy 90/94/98 ([[gameplay/npc-locations]] §2)"]
manual: ["teleport_to"]
name_key: "TitleName_13"
title_key: "UnitName_217"
npc_title: "Teleporter"
category: 50
class_mask: 2
model: 33
scale: 1.5
functions:
  - {"code": 4, "function": "teleport", "label": "Teleport"}
role: "Teleporter"
talk_key: "Quest_Talk_Default_Teleport"
portrait: "ui/NPCProfile/Quest_Teleport.dds"
quests: {"gives": [104], "receives": [104]}
quest_fields: [120]
map: 120
x: 1927.6
z: 1616.4
positions:
  - {"field": 120, "x": 1927.6, "z": 1616.4, "source": "gameplay/npc-locations §3", "confidence": "video + image"}
  - {"field": 120, "x": 2183.6, "z": 1616.4, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2439.6, "z": 1616.4, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
teleport_to: [{"name": "Castle", "fields": [90, 94, 98], "cost_gold": 10000}, {"name": "Fortress", "fields": [120], "cost_gold": 4000}, {"name": "Gaia", "cost_gold": 0}, {"name": "Abyss", "fields": [103, 105, 107], "gates": [1901, 1902, 1903], "cost_gold": 0}]
---
<!-- generated:start -->
<!-- generated-keys: title=7a24d5 type=3664ce id=49e3d0 sources=fa23dc name_key=18c717 title_key=b900c8 npc_title=aa4174 category=e1822d class_mask=da4b92 model=b6692e scale=aa8f28 functions=b85d7e role=aa4174 talk_key=9b525c portrait=a9b793 quests=360a3c quest_fields=6c3da9 map=775bc5 x=f7f372 z=d916ec positions=621db8 teleport_to=2be88c -->
|  |  |
|---|---|
|  | ![Haley](../assets/npcs/217.png) |
| **Unit id** | `217` |
| **Title** | Teleporter |
| **Category** | NPC (category 50) |
| **Menu** | Teleport (`4`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1927.6, 1616.4) |
| **Model** | ObjectList `33`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Quest_Teleport.dds` |

### Greeting

> Hello there, where shall I send you?

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1927.6 | 1616.4 | video + image | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2183.6 | 1616.4 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2439.6 | 1616.4 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Quests

- **Gives:** [[wiki/quests/104-delivering-punishment|Delivering Punishment]]
- **Takes the turn-in of:** [[wiki/quests/104-delivering-punishment|Delivering Punishment]]

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] (9. Other timers and limits)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (1. The world (Gaia); 5. Fortress layout (town))
- [[gameplay/patch-history|Patch notes and other sources]] (Economy and timeline)
- [[gameplay/server-rules|Server rules checklist]] (Economy and misc)
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] (After the tutorial (Fortress, from 22:00))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 42:10, 48:20, 48:40, 49:20, 50:05, 51:25, 63:50, 84:35 (1. Map order; Fortress (levels 12–20); 3. NPCs)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 32:45, 33:00 (Steps; 2. NPC positions)
<!-- generated:end -->

## Notes

- Haley is the Fortress teleporter. A character who takes the Nexus to the Fortress arrives right beside her, and her idle bubble says she can move people around Gaia instantly ([[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough]] step 31, [32:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1975s)). She stands on the arrival plaza near Freya ([[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough]] §2, [33:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1980s)).
- Her menu has four destinations. In the April 2018 video they are Castle (10,000 gold), Fortress (4,000 gold, later shown as "TOP Fortress (4000)"), Gaia and Abyss, and the last two show no price ([[gameplay/video-early-quests|Video notes: first session]] §1, [1:03:52](https://www.youtube.com/watch?v=s04CSN16w1s&t=3832s), [1:24:37](https://www.youtube.com/watch?v=s04CSN16w1s&t=5077s)). A guide screenshot gives Castle 10,000, Fortress 6,000, Gaia and Abyss free ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1, [[gameplay/progression-and-economy|Progression and economy]] §4). *video / image*
- The free Abyss option probably lands in Place for Scattered troops (field 103, 105 or 107 by nation): `Teleport_List` rows 1901–1903 belong to field 120 and have no gate of their own ([[gameplay/abyss-map|Abyss map]]). *client + guess*. The video player did reach field 103 straight from the Fortress ([[gameplay/video-early-quests|Video notes: first session]] §1, [51:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=3085s)).
- From the January 2019 patch (WM 0110), teleporting through Haley costs 20 yellow jewels. In Gaia the cash-shop Teleport Scroll (913) does the same job ([[gameplay/events-and-schedules|Events and schedules]] §9, [[gameplay/patch-history|Patch history]]). *notes*
- Fort masteries gate several fort services, the teleporter among them ([[gameplay/server-rules|Server rules]], Legions, forts, events). *guide + client*

## Behaviour

- Gives quest 104 "Delivering Punishment": kill 10 Lizard and 10 Elite Lizard in Place for Scattered troops. The reward panel showed 170,000 exp (table 204,000), 20,000 gold and 40/40 passion fragments ([[gameplay/video-early-quests|Video notes: first session]] §2 step 18, [42:12](https://www.youtube.com/watch?v=s04CSN16w1s&t=2532s)). *video*

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough]]
- [[gameplay/video-early-quests|Video notes: first session]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/progression-and-economy|Progression and economy]]
- [[gameplay/abyss-map|Abyss map]]
- [[gameplay/events-and-schedules|Events and schedules]]
- [[gameplay/patch-history|Patch history]]
- [[gameplay/server-rules|Server rules]]

## Open questions

- Fortress price: 4,000 gold in the April 2018 video ([[gameplay/video-early-quests|Video notes: first session]] §1) or 6,000 gold in the guide screenshot ([[gameplay/maps-and-dungeons|Maps and dungeons]] §1)? Both are Warmonger 2018. The page uses the video value, because it was seen twice. The price may also have changed with the fort or tax.
- "TOP Fortress" suggests the Fortress option goes to one particular fortress (the top legion's?), not the player's own. Which field and point it lands on is unknown.
- Which field the free "Gaia" option lands in is not recorded anywhere.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

---
title: "Hadrian"
type: "npc"
id: 211
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 211", "gameplay/npc-locations §3", "gameplay/video-early-quests §3"]
name_key: "TitleName_14"
title_key: "UnitName_211"
npc_title: "Fortress Administrator"
category: 50
class_mask: 2
model: 45
scale: 1.5
functions:
  - {"code": 16, "function": "fort_info", "label": "Fortress Information"}
  - {"code": 29, "function": "guild_war_request", "label": "Civil war application"}
  - {"code": 12, "function": "fort_donate", "label": "Donate"}
role: "Fortress Administrator"
talk_key: "Quest_Talk_Default_Fort"
portrait: "ui/NPCProfile/Oracle_Hadrian_Illust.dds"
map: 120
x: 1841.0
z: 1712.0
positions:
  - {"field": 120, "x": 1841.0, "z": 1712.0, "source": "gameplay/npc-locations §3", "confidence": "image + guess"}
  - {"field": 120, "x": 1842.2, "z": 1709.2, "source": "gameplay/video-early-quests §3", "confidence": "video", "seen": ["48:00"]}
  - {"field": 120, "x": 2097.0, "z": 1712.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2353.0, "z": 1712.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=0c76e4 type=3664ce id=1b4a36 sources=4062e0 name_key=10e07a title_key=b5edf8 npc_title=334169 category=e1822d class_mask=da4b92 model=fb6443 scale=aa8f28 functions=dddd43 role=334169 talk_key=697300 portrait=755aef map=775bc5 x=8b12a4 z=926a77 positions=7296f3 -->
|  |  |
|---|---|
|  | ![Hadrian](../assets/npcs/211.png) |
| **Unit id** | `211` |
| **Title** | Fortress Administrator |
| **Category** | NPC (category 50) |
| **Menu** | Fortress Information (`16`), Civil war application (`29`), Donate (`12`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1841.0, 1712.0) |
| **Model** | ObjectList `45`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Oracle_Hadrian_Illust.dds` |

### Greeting

> Did you know? The Legion Master that owns the fortress can use the Holy Things to gain 
> various advantages.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1841.0 | 1712.0 | image + guess | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 1842.2 | 1709.2 | video | [[gameplay/video-early-quests\|video-early-quests]] §3 at 48:00 |
| [[wiki/fields/120-fortress\|Fortress]] | 2097.0 | 1712.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2353.0 | 1712.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/classes-and-legions|Classes, nations and legions]] (4. Forts (castles))
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (5. Fortress layout (town))
- [[gameplay/server-rules|Server rules checklist]] (Legions, forts, events)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 48:00 (3. NPCs)
- [[gameplay/warmonger-forum|Warmonger forum (2018)]] (5. Legions and forts)
<!-- generated:end -->

## Notes

- Fortress Administrator in the top-left (west arm) of the Fortress, with the menu "Fort Information" and "Civil war application". The April 2018 video measures (1842.2, 1709.2), which confirms the minimap guess (1841, 1712) ([[gameplay/video-early-quests|Video notes: first session]] §3, [48:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=2880s)). *video*
- Any player can donate gold here to raise the fort's EXP ([[gameplay/classes-and-legions|Classes and legions]] §4, [[gameplay/server-rules|Server rules]]). Crafted cores (28 kinds) are installed at Hadrian ([[gameplay/warmonger-forum|Warmonger forum]] §5). *guide / forum*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/video-early-quests|Video notes: first session]]
- [[gameplay/classes-and-legions|Classes and legions]]
- [[gameplay/server-rules|Server rules]]
- [[gameplay/warmonger-forum|Warmonger forum]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

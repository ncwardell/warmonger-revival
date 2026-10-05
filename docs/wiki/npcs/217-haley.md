---
title: "Haley"
type: "npc"
id: 217
status: "stub"
missing: ["teleport_to"]
sources: ["client: UnitDB.cdb id 217", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
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
teleport_to: null
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

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

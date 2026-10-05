---
title: "Krister"
type: "npc"
id: 219
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 219", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/video-early-quests §3"]
name_key: "TitleName_16"
title_key: "UnitName_219"
npc_title: "Stock Administrator"
category: 50
class_mask: 2
model: 237
scale: 1.7
functions:
  - {"code": 11, "function": "legion_stock", "label": "Legion Stock"}
role: "Stock Administrator"
talk_key: "Quest_Talk_Default_Stock"
portrait: "ui/NPCProfile/NPC_Shares.dds"
quests: {"gives": [106], "talk_objective": [106]}
quest_fields: [90, 94, 98]
map: 90
x: 489.7
z: 4139.6
positions:
  - {"field": 90, "x": 489.7, "z": 4139.6, "source": "gameplay/video-early-quests §3", "confidence": "video", "seen": ["59:00"]}
  - {"field": 94, "x": 745.7, "z": 4139.6, "source": "derived: gameplay/video-early-quests §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 98, "x": 1001.7, "z": 4139.6, "source": "derived: gameplay/video-early-quests §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=3c9146 type=3664ce id=c0ba17 sources=622e8d name_key=8fc47f title_key=c11b05 npc_title=b29ca0 category=e1822d class_mask=da4b92 model=3c3316 scale=58e6d3 functions=cf1117 role=b29ca0 talk_key=678323 portrait=bad4e3 quests=9961ab quest_fields=18e60d map=2d0c8a x=51a422 z=324963 positions=6dc95f -->
|  |  |
|---|---|
|  | ![Krister](wiki/assets/npcs/219.png) |
| **Unit id** | `219` |
| **Title** | Stock Administrator |
| **Category** | NPC (category 50) |
| **Menu** | Legion Stock (`11`) |
| **Stands in** | [[wiki/fields/90-castle\|Castle]] at (489.7, 4139.6) |
| **Model** | ObjectList `237`, scale 1.7 |
| **Portrait** | `ui/NPCProfile/NPC_Shares.dds` |

### Greeting

> Nice to meet you. I'm overseeing the Legion stocks.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/90-castle\|Castle]] | 489.7 | 4139.6 | video | [[gameplay/video-early-quests\|video-early-quests]] §3 at 59:00 |
| [[wiki/fields/94-castle\|Castle]] | 745.7 | 4139.6 | derived | derived: gameplay/video-early-quests §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/98-castle\|Castle]] | 1001.7 | 4139.6 | derived | derived: gameplay/video-early-quests §3 + copy origin (gameplay/npc-locations §2) |

### Quests

- **Gives:** [[wiki/quests/106-talk-to-krister|Talk to Krister]]
- **Must be talked to in:** [[wiki/quests/106-talk-to-krister|Talk to Krister]]

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (6. Village (87/91/95), Castle (90/94/98), tutorial (117); 8. Still unplaced)
- [[gameplay/sources|Sources and gaps]] (9. What is still missing)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 58:50, 59:00 (Fortress (levels 12–20); 3. NPCs)
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

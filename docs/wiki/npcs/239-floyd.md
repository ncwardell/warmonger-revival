---
title: "Floyd"
type: "npc"
id: 239
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 239", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §5", "gameplay/video-character-creation-and-tutorial §4", "gameplay/video-early-quests §3", "gameplay/video-tutorial-walkthrough §2"]
name_key: "TitleName_22"
title_key: "UnitName_239"
npc_title: "Biologist"
category: 50
class_mask: 2
model: 297
scale: 1.5
functions:
  - {"code": 71, "function": "none"}
role: "Biologist"
quests: {"gives": [3, 4], "receives": [2, 3]}
quest_fields: [89, 93, 97]
map: 89
x: 370.5
z: 3660.6
positions:
  - {"field": 89, "x": 370.5, "z": 3660.6, "source": "gameplay/npc-locations §5", "confidence": "video"}
  - {"field": 93, "x": 625.9, "z": 3660.5, "source": "gameplay/video-character-creation-and-tutorial §4", "confidence": "video", "seen": ["4:20"]}
  - {"field": 89, "x": 371.1, "z": 3660.1, "source": "gameplay/video-early-quests §3", "confidence": "video", "seen": ["6:50"]}
  - {"field": 89, "x": 371.5, "z": 3659.0, "source": "gameplay/video-tutorial-walkthrough §2", "confidence": "video", "seen": ["7:05"]}
  - {"field": 93, "x": 626.5, "z": 3660.6, "source": "derived: gameplay/npc-locations §5 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 97, "x": 882.5, "z": 3660.6, "source": "derived: gameplay/npc-locations §5 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=d8843d type=3664ce id=584130 sources=806020 name_key=93f346 title_key=506468 npc_title=4aa619 category=e1822d class_mask=da4b92 model=dd500e scale=aa8f28 functions=40bee7 role=4aa619 quests=cf01e9 quest_fields=6e2020 map=16b06b x=a82d3f z=9082fe positions=6848ce -->
|  |  |
|---|---|
|  | ![Floyd](wiki/assets/npcs/239.png) |
| **Unit id** | `239` |
| **Title** | Biologist |
| **Category** | NPC (category 50) |
| **Menu** | no menu entry (code `71`) |
| **Stands in** | [[wiki/fields/89-training-ground\|Training Ground]] at (370.5, 3660.6) |
| **Model** | ObjectList `297`, scale 1.5 |

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/89-training-ground\|Training Ground]] | 370.5 | 3660.6 | video | [[gameplay/npc-locations\|npc-locations]] §5 |
| [[wiki/fields/93-training-ground\|Training Ground]] | 625.9 | 3660.5 | video | [[gameplay/video-character-creation-and-tutorial\|video-character-creation-and-tutorial]] §4 at 4:20 |
| [[wiki/fields/89-training-ground\|Training Ground]] | 371.1 | 3660.1 | video | [[gameplay/video-early-quests\|video-early-quests]] §3 at 6:50 |
| [[wiki/fields/89-training-ground\|Training Ground]] | 371.5 | 3659.0 | video | [[gameplay/video-tutorial-walkthrough\|video-tutorial-walkthrough]] §2 at 7:05 |
| [[wiki/fields/93-training-ground\|Training Ground]] | 626.5 | 3660.6 | derived | derived: gameplay/npc-locations §5 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/97-training-ground\|Training Ground]] | 882.5 | 3660.6 | derived | derived: gameplay/npc-locations §5 + copy origin (gameplay/npc-locations §2) |

Current server: `server/world.py` spawns this NPC (listed in `NPCS`).

### Quests

- **Gives:** [[wiki/quests/3-the-task-at-hand|The task at hand]], [[wiki/quests/4-go-to-shaia|Go to Shaia]]
- **Takes the turn-in of:** [[wiki/quests/2-the-slime-is-mine|The Slime is mine]], [[wiki/quests/3-the-task-at-hand|The task at hand]]

Dialogue rows (`QuestTalk`; full text on the quest pages):

| quest | QuestTalk | speaker | first line |
|---|---|---|---|
| [[wiki/quests/3-the-task-at-hand\|The task at hand]] | 632 | Floyd : Biologist | There you are, I already thought about sending out a rescue party! But I'm glad you finally made it and brought me the s |

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/334-floyd|Floyd (334)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (5. Training Ground (fields 89 / 93 / 97))
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] at 4:20 (3. Tutorial and first quests, in order; Training Ground (field 93); 4. NPC positions (Erion copy))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 6:45, 6:50 (Training Ground and Camp (levels 1–11); 3. NPCs)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 7:05, 7:06, 7:30 (Steps; 2. NPC positions)
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

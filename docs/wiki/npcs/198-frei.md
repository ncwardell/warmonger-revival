---
title: "Frei"
type: "npc"
id: 198
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 198", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §4", "gameplay/video-tutorial-walkthrough §2"]
name_key: "TitleName_24"
title_key: "UnitName_200"
npc_title: "Oracle of Knowledge"
category: 50
class_mask: 2
model: 53
scale: 1.5
functions:
  - {"code": 71, "function": "none"}
role: "Oracle of Knowledge"
talk_key: "Quest_Talk_Default_Oracle"
portrait: "ui/NPCProfile/Oracle_of_Knowledge.dds"
quests: {"gives": [9, 11, 45], "receives": [5, 7, 10, 107], "talk_objective": [6]}
quest_fields: [88, 92, 96]
map: 88
x: 358.8
z: 3469.1
positions:
  - {"field": 88, "x": 358.8, "z": 3469.1, "source": "gameplay/npc-locations §4", "confidence": "video"}
  - {"field": 88, "x": 362.6, "z": 3467.6, "source": "gameplay/video-tutorial-walkthrough §2", "confidence": "video", "seen": ["12:40"]}
  - {"field": 92, "x": 614.8, "z": 3469.1, "source": "derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 96, "x": 870.8, "z": 3469.1, "source": "derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=53d874 type=3664ce id=c83730 sources=16f101 name_key=6f3b2e title_key=21d171 npc_title=955057 category=e1822d class_mask=da4b92 model=c5b76d scale=aa8f28 functions=40bee7 role=955057 talk_key=7b5881 portrait=263ce3 quests=e8bd47 quest_fields=46bf0f map=b37f6d x=1bd63a z=3bff14 positions=d40e9b -->
|  |  |
|---|---|
|  | ![Frei](../assets/npcs/198.png) |
| **Unit id** | `198` |
| **Title** | Oracle of Knowledge |
| **Category** | NPC (category 50) |
| **Menu** | no menu entry (code `71`) |
| **Stands in** | [[wiki/fields/88-training-camp\|Training Camp]] at (358.8, 3469.1) |
| **Model** | ObjectList `53`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Oracle_of_Knowledge.dds` |

### Greeting

> Is you mission going well? Find me if you are looking for work

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/88-training-camp\|Training Camp]] | 358.8 | 3469.1 | video | [[gameplay/npc-locations\|npc-locations]] §4 |
| [[wiki/fields/88-training-camp\|Training Camp]] | 362.6 | 3467.6 | video | [[gameplay/video-tutorial-walkthrough\|video-tutorial-walkthrough]] §2 at 12:40 |
| [[wiki/fields/92-training-camp\|Training Camp]] | 614.8 | 3469.1 | derived | derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/96-training-camp\|Training Camp]] | 870.8 | 3469.1 | derived | derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2) |

Current server: `server/world.py` spawns this NPC (placed at (360.8, 3466.1) in map 88).

### Quests

- **Gives:** [[wiki/quests/9-find-the-missing-scout|Find the missing Scout]], [[wiki/quests/11-an-urgent-message|An urgent message]], [[wiki/quests/45-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]
- **Takes the turn-in of:** [[wiki/quests/5-united-problem-solvers|United Problem Solvers]], [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]], [[wiki/quests/10-find-the-secret-document|Find the Secret Document]], [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]
- **Must be talked to in:** [[wiki/quests/6-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]

Dialogue rows (`QuestTalk`; full text on the quest pages):

| quest | QuestTalk | speaker | first line |
|---|---|---|---|
| [[wiki/quests/9-find-the-missing-scout\|Find the missing Scout]] | 635 | Frei : Oracle of Knowledge | Are you Frei? Shaia has sent me to deliver this letter to you. |
| [[wiki/quests/11-an-urgent-message\|An urgent message]] | 639 | Frei : Oracle of Knowledge | I'm awaiting the arrival of one of our scouts, but he is long overdue. He carries important information. |
| [[wiki/quests/107-hunting-skeletons\|Hunting Skeletons]] | 665 | Freya : Oracle of Knowledge | You done already? Great! |

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (4. Training Camp (fields 88 / 92 / 96))
- [[gameplay/sources|Sources and gaps]] (3. Player screenshots (image sets that still load))
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] at 8:15, 8:30, 15:30, 20:00 (3. Tutorial and first quests, in order; Training Ground (field 93); Training Camp (field 92) and back)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 13:30, 16:35, 21:05, 21:35, 26:20, 26:30, 36:35, 36:45 (Training Ground and Camp (levels 1–11); Fortress (levels 12–20); 3. NPCs)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 12:40, 12:50, 13:30, 20:20, 20:35, 23:35, 23:45, 29:50 … (Steps; 2. NPC positions)
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

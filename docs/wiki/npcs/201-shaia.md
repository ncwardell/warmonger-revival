---
title: "Shaia"
type: "npc"
id: 201
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 201", "gameplay/npc-locations §5 (role)", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §5", "gameplay/video-character-creation-and-tutorial §4", "gameplay/video-early-quests §3", "gameplay/video-tutorial-walkthrough §2"]
name_key: "UnitName_201"
category: 50
class_mask: 2
model: 275
scale: 3.0
role: "Guide"
quests: {"gives": [1, 2, 5, 7], "receives": [4], "talk_objective": [1, 45, 1501]}
quest_fields: [89, 93, 97]
map: 89
x: 423.9
z: 3664.8
positions:
  - {"field": 89, "x": 423.9, "z": 3664.8, "source": "gameplay/npc-locations §5", "confidence": "video"}
  - {"field": 93, "x": 680.0, "z": 3663.5, "source": "gameplay/video-character-creation-and-tutorial §4", "confidence": "video", "seen": ["6:08"]}
  - {"field": 89, "x": 433.8, "z": 3662.0, "source": "gameplay/video-early-quests §3", "confidence": "video", "seen": ["4:20", "13:05", "17:55"]}
  - {"field": 89, "x": 433.5, "z": 3662.0, "source": "gameplay/video-tutorial-walkthrough §2", "confidence": "video", "seen": ["3:20", "4:00"]}
  - {"field": 93, "x": 679.9, "z": 3664.8, "source": "derived: gameplay/npc-locations §5 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 97, "x": 935.9, "z": 3664.8, "source": "derived: gameplay/npc-locations §5 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=1a4861 type=3664ce id=7f03f3 sources=b5034a name_key=ed8141 category=e1822d class_mask=da4b92 model=df518c scale=bdc140 role=875cc6 quests=68cb74 quest_fields=6e2020 map=16b06b x=7df2da z=b78ecc positions=a6af5e -->
|  |  |
|---|---|
|  | ![Shaia](../assets/npcs/201.png) |
| **Unit id** | `201` |
| **Role** | Guide |
| **Category** | NPC (category 50) |
| **Stands in** | [[wiki/fields/89-training-ground\|Training Ground]] at (423.9, 3664.8) |
| **Model** | ObjectList `275`, scale 3.0 |

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/89-training-ground\|Training Ground]] | 423.9 | 3664.8 | video | [[gameplay/npc-locations\|npc-locations]] §5 |
| [[wiki/fields/93-training-ground\|Training Ground]] | 680.0 | 3663.5 | video | [[gameplay/video-character-creation-and-tutorial\|video-character-creation-and-tutorial]] §4 at 6:08 |
| [[wiki/fields/89-training-ground\|Training Ground]] | 433.8 | 3662.0 | video | [[gameplay/video-early-quests\|video-early-quests]] §3 at 4:20, 13:05, 17:55 |
| [[wiki/fields/89-training-ground\|Training Ground]] | 433.5 | 3662.0 | video | [[gameplay/video-tutorial-walkthrough\|video-tutorial-walkthrough]] §2 at 3:20, 4:00 |
| [[wiki/fields/93-training-ground\|Training Ground]] | 679.9 | 3664.8 | derived | derived: gameplay/npc-locations §5 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/97-training-ground\|Training Ground]] | 935.9 | 3664.8 | derived | derived: gameplay/npc-locations §5 + copy origin (gameplay/npc-locations §2) |

Current server: `server/world.py` spawns this NPC (listed in `NPCS`).

### Quests

- **Gives:** [[wiki/quests/1-on-to-a-promising-start|On to a promising start]], [[wiki/quests/2-the-slime-is-mine|The Slime is mine]], [[wiki/quests/5-united-problem-solvers|United Problem Solvers]], [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]
- **Takes the turn-in of:** [[wiki/quests/4-go-to-shaia|Go to Shaia]]
- **Must be talked to in:** [[wiki/quests/1-on-to-a-promising-start|On to a promising start]], [[wiki/quests/45-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]], [[wiki/quests/1501-basic-function-move-character|Basic function - Move character]]

Dialogue rows (`QuestTalk`; full text on the quest pages):

| quest | QuestTalk | speaker | first line |
|---|---|---|---|
| [[wiki/quests/1-on-to-a-promising-start\|On to a promising start]] | 630 | Shaia | Why are you always late? |
| [[wiki/quests/7-the-1st-challenge-chepas-ahead\|The 1st Challenge: Chepas ahead]] | 634 | Shaia | Do you have any important missions for a  real warrior? |
| [[wiki/quests/45-the-1st-challenge-chepas-ahead\|The 1st Challenge: Chepas ahead]] | 634 | Shaia | Do you have any important missions for a  real warrior? |
| [[wiki/quests/1501-basic-function-move-character\|Basic function - Move character]] | 630 | Shaia | Why are you always late? |

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/202-shaia|Shaia (202)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (5. Training Ground (fields 89 / 93 / 97))
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] at 2:33, 2:45, 6:08 (3. Tutorial and first quests, in order; Training Ground (field 93); 4. NPC positions (Erion copy))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 4:20, 13:05, 17:55 (Training Ground and Camp (levels 1–11); 3. NPCs)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 3:20, 3:40, 4:00 (Steps; 2. NPC positions)
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

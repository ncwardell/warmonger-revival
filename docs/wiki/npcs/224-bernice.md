---
title: "Bernice"
type: "npc"
id: 224
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 224", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/video-early-quests §3"]
name_key: "TitleName_17"
title_key: "UnitName_224"
npc_title: "Oracle of Judgment"
category: 50
class_mask: 2
model: 45
scale: 1.5
functions:
  - {"code": 14, "function": "change_nation", "label": "Change Nation"}
role: "Oracle of Judgment"
talk_key: "Quest_Talk_Default_Judgement"
portrait: "ui/NPCProfile/Oracle of Judgment.dds"
quests: {"receives": [19]}
quest_fields: [90, 94, 98]
map: 90
x: 493.8
z: 4285.8
positions:
  - {"field": 90, "x": 493.8, "z": 4285.8, "source": "gameplay/video-early-quests §3", "confidence": "video", "seen": ["58:00"]}
  - {"field": 94, "x": 749.8, "z": 4285.8, "source": "derived: gameplay/video-early-quests §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 98, "x": 1005.8, "z": 4285.8, "source": "derived: gameplay/video-early-quests §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=7f3a06 type=3664ce id=bc15c7 sources=114acf name_key=3a09e3 title_key=b24321 npc_title=aaa7ff category=e1822d class_mask=da4b92 model=fb6443 scale=aa8f28 functions=cc0051 role=aaa7ff talk_key=fa2d23 portrait=76267c quests=09ca2b quest_fields=18e60d map=2d0c8a x=2bd327 z=6875bc positions=56d66c -->
|  |  |
|---|---|
|  | ![Bernice](wiki/assets/npcs/224.png) |
| **Unit id** | `224` |
| **Title** | Oracle of Judgment |
| **Category** | NPC (category 50) |
| **Menu** | Change Nation (`14`) |
| **Stands in** | [[wiki/fields/90-castle\|Castle]] at (493.8, 4285.8) |
| **Model** | ObjectList `45`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Oracle of Judgment.dds` |

### Greeting

> The current leaders are only interested in profits and personal gain,
> there are endless conflicts and disputes because of that.
> This nation should be led by the likes of you. 
>  If you ever get sick of the policies in your home country make sure to come back to me,
> you can affiliate yourself with another nation here.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/90-castle\|Castle]] | 493.8 | 4285.8 | video | [[gameplay/video-early-quests\|video-early-quests]] §3 at 58:00 |
| [[wiki/fields/94-castle\|Castle]] | 749.8 | 4285.8 | derived | derived: gameplay/video-early-quests §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/98-castle\|Castle]] | 1005.8 | 4285.8 | derived | derived: gameplay/video-early-quests §3 + copy origin (gameplay/npc-locations §2) |

### Quests

- **Takes the turn-in of:** [[wiki/quests/19-meeting-freya|Meeting Freya]]

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (8. Still unplaced)
- [[gameplay/sources|Sources and gaps]] (9. What is still missing)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 56:55, 57:55, 58:00 (Fortress (levels 12–20); 3. NPCs)
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

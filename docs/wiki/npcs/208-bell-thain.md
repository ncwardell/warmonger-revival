---
title: "Bell Thain"
type: "npc"
id: 208
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 208", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_2"
title_key: "UnitName_208"
npc_title: "Training Officer"
category: 50
class_mask: 2
model: 34
scale: 1.5
functions:
  - {"code": 2, "function": "mock_battle", "label": "Mock Battle"}
role: "Training Officer"
talk_key: "Quest_Talk_Default_Trainer"
portrait: "ui/NPCProfile/NPC_Instructor.dds"
quests: {"gives": [48, 49, 50, 51, 53], "receives": [51, 53, 501]}
quest_fields: [120]
map: 120
x: 1917.0
z: 1746.0
positions:
  - {"field": 120, "x": 1917.0, "z": 1746.0, "source": "gameplay/npc-locations §3", "confidence": "image + guess"}
  - {"field": 120, "x": 2173.0, "z": 1746.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2429.0, "z": 1746.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=c06b8b type=3664ce id=baab34 sources=06edb1 name_key=5bfd4f title_key=75b8d8 npc_title=43ef83 category=e1822d class_mask=da4b92 model=f1f836 scale=aa8f28 functions=da9a7c role=43ef83 talk_key=fb5861 portrait=6aa998 quests=95ab0e quest_fields=6c3da9 map=775bc5 x=658c52 z=212b7c positions=d2b96d -->
|  |  |
|---|---|
|  | ![Bell Thain](../assets/npcs/208.png) |
| **Unit id** | `208` |
| **Title** | Training Officer |
| **Category** | NPC (category 50) |
| **Menu** | Mock Battle (`2`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1917.0, 1746.0) |
| **Model** | ObjectList `34`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/NPC_Instructor.dds` |

### Greeting

> Training!! Training!! Training is necessary to improve.
>  Test your combat power in virtual battles.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1917.0 | 1746.0 | image + guess | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2173.0 | 1746.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2429.0 | 1746.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Quests

- **Gives:** [[wiki/quests/48-doping-create|Doping Create]], [[wiki/quests/49-war-objects|War - Objects]], [[wiki/quests/50-war-winning-means|War - Winning means]], [[wiki/quests/51-war-winning-means|War - Winning means]], [[wiki/quests/53-safety-factor-management|Safety factor Management]]
- **Takes the turn-in of:** [[wiki/quests/51-war-winning-means|War - Winning means]], [[wiki/quests/53-safety-factor-management|Safety factor Management]], [[wiki/quests/501-return-player|Return Player]]

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 49:50, 59:00 (3. NPCs)
<!-- generated:end -->

## Notes

- Training Officer with the "Mock Battle" menu. The April 2018 video measures him at (1917.2, 1745.4) in the Fortress, which confirms the minimap-icon guess (1917, 1746) ([[gameplay/video-early-quests|Video notes: first session]] §3, [49:50](https://www.youtube.com/watch?v=s04CSN16w1s&t=2990s)). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/video-early-quests|Video notes: first session]]

## Open questions

- The same video sees a "Bell Thain" at the edge of the screen in the Castle, at about (482, 4122) ±8 ([[gameplay/video-early-quests|Video notes: first session]] §3, [59:01](https://www.youtube.com/watch?v=s04CSN16w1s&t=3541s)). Whether that is this unit or another Training Officer row (for example 221) is unknown.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

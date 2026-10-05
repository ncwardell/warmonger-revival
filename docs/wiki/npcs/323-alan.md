---
title: "Alan"
type: "npc"
id: 323
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 323", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_31"
title_key: "UnitName_323"
npc_title: "Rune Maker"
category: 50
class_mask: 2
model: 238
scale: 1.5
functions:
  - {"code": 34, "function": "craft", "label": "Create"}
role: "Rune Maker"
talk_key: "Quest_Talk_Default_Black_Jewel"
portrait: "ui/NPCProfile/Quest_Reinforce.dds"
quests: {"gives": [121], "receives": [121], "talk_objective": [697]}
quest_fields: [120]
map: 120
x: 1939.0
z: 1704.9
positions:
  - {"field": 120, "x": 1939.0, "z": 1704.9, "source": "gameplay/npc-locations §3", "confidence": "video + image"}
  - {"field": 120, "x": 2195.0, "z": 1704.9, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2451.0, "z": 1704.9, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=de3bbd type=3664ce id=cb4dd5 sources=b826f2 name_key=11f507 title_key=20ef62 npc_title=43af3a category=e1822d class_mask=da4b92 model=5b7d26 scale=aa8f28 functions=f6eab2 role=43af3a talk_key=c52c82 portrait=d2d345 quests=62380e quest_fields=6c3da9 map=775bc5 x=6d20a2 z=37b117 positions=827710 -->
|  |  |
|---|---|
|  | ![Alan](wiki/assets/npcs/323.png) |
| **Unit id** | `323` |
| **Title** | Rune Maker |
| **Category** | NPC (category 50) |
| **Menu** | Create (`34`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1939.0, 1704.9) |
| **Model** | ObjectList `238`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Quest_Reinforce.dds` |

### Greeting

> Have you tried to make a glitter Jewel Stone?

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1939.0 | 1704.9 | video + image | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2195.0 | 1704.9 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2451.0 | 1704.9 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Quests

- **Gives:** [[wiki/quests/121-create-rune|Create Rune]]
- **Takes the turn-in of:** [[wiki/quests/121-create-rune|Create Rune]]
- **Must be talked to in:** [[wiki/quests/697-create-rune|Create Rune]]

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] (2017-03-02 ([t934]))
- [[gameplay/items-and-crafting|Items, upgrades and crafting]] (2. Sockets and runes; 3. Crafting)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (5. Fortress layout (town))
- [[gameplay/sources|Sources and gaps]] (4. Blog and guides)
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

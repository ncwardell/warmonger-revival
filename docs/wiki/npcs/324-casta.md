---
title: "Casta"
type: "npc"
id: 324
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 324", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_32"
title_key: "UnitName_324"
npc_title: "Rune Manager"
category: 50
class_mask: 2
model: 297
scale: 1.5
functions:
  - {"code": 35, "function": "rune_socket", "label": "Rune Reinforcement"}
  - {"code": 36, "function": "rune_bind", "label": "Rune Set / Delete"}
role: "Rune Manager"
talk_key: "Quest_Talk_Default_Black_Jewel_NPC"
portrait: "ui/NPCProfile/Quest_RedFlames.dds"
quests: {"gives": [122, 123], "receives": [123], "talk_objective": [122, 698, 699, 1516]}
quest_fields: [120]
map: 120
x: 1942.8
z: 1704.1
positions:
  - {"field": 120, "x": 1942.8, "z": 1704.1, "source": "gameplay/npc-locations §3", "confidence": "video"}
  - {"field": 120, "x": 2198.8, "z": 1704.1, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2454.8, "z": 1704.1, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=253605 type=3664ce id=914127 sources=40a8bb name_key=10348e title_key=d752cf npc_title=e49f92 category=e1822d class_mask=da4b92 model=dd500e scale=aa8f28 functions=cc5591 role=e49f92 talk_key=d48d90 portrait=7348e7 quests=757f04 quest_fields=6c3da9 map=775bc5 x=5ae5fb z=af5569 positions=45c2a9 -->
|  |  |
|---|---|
|  | ![Casta](wiki/assets/npcs/324.png) |
| **Unit id** | `324` |
| **Title** | Rune Manager |
| **Category** | NPC (category 50) |
| **Menu** | Rune Reinforcement (`35`), Rune Set / Delete (`36`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1942.8, 1704.1) |
| **Model** | ObjectList `297`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Quest_RedFlames.dds` |

### Greeting

> Only I can handle setting Jewel Stones.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1942.8 | 1704.1 | video | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2198.8 | 1704.1 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2454.8 | 1704.1 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Quests

- **Gives:** [[wiki/quests/122-rune-equipment|Rune Equipment.]], [[wiki/quests/123-rune-reinforcement|Rune Reinforcement]]
- **Takes the turn-in of:** [[wiki/quests/123-rune-reinforcement|Rune Reinforcement]]
- **Must be talked to in:** [[wiki/quests/122-rune-equipment|Rune Equipment.]], [[wiki/quests/698-rune-equipment|Rune Equipment.]], [[wiki/quests/699-rune-reinforcement|Rune Reinforcement]], [[wiki/quests/1516-item-equip-or-release-rune|Item - Equip or release Rune]]

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] (2017-03-02 ([t934]))
- [[gameplay/items-and-crafting|Items, upgrades and crafting]] (2. Sockets and runes)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (5. Fortress layout (town))
- [[gameplay/sources|Sources and gaps]] (4. Blog and guides)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 48:20, 48:40, 49:20, 50:05 (3. NPCs)
<!-- generated:end -->

## Notes

- Rune manager next to Alan. She upgrades, sets and removes runes ([[gameplay/items-and-crafting|Items and crafting]] §2; [[gameplay/maps-and-dungeons|Maps and dungeons]] §5); the April 2018 video shows rune socketing here ([[gameplay/video-early-quests|Video notes: first session]] §3, [49:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2960s)). *guide + video*
- In Crush Online she opened weapon sockets and inserted or removed jewel stones. A failed socket opening could destroy the weapon, and removing a stone destroyed it ([[gameplay/crush-patch-notes|Crush patch notes]] 2017-03-02). *staff*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/items-and-crafting|Items and crafting]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/video-early-quests|Video notes: first session]]
- [[gameplay/crush-patch-notes|Crush patch notes]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

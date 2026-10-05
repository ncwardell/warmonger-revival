---
title: "Cathy"
type: "npc"
id: 303
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 303", "gameplay/npc-locations §3"]
name_key: "TitleName_6"
title_key: "UnitName_303"
npc_title: "Auction House Manager"
category: 50
class_mask: 2
model: 185
scale: 1.5
functions:
  - {"code": 17, "function": "auction", "label": "Auction House"}
role: "Auction House Manager"
talk_key: "Quest_Talk_Default_Auction"
portrait: "ui/NPCProfile/NPC_Action.dds"
map: 120
x: 1924.8
z: 1666.7
positions:
  - {"field": 120, "x": 1924.8, "z": 1666.7, "source": "gameplay/npc-locations §3", "confidence": "video"}
  - {"field": 120, "x": 2180.8, "z": 1666.7, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2436.8, "z": 1666.7, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=b37e47 type=3664ce id=bbcbb1 sources=5286d1 name_key=d1ae66 title_key=8a975e npc_title=8ad434 category=e1822d class_mask=da4b92 model=cfa2ed scale=aa8f28 functions=3ee449 role=8ad434 talk_key=19cfbb portrait=742d9e map=775bc5 x=f31179 z=f4f2e4 positions=c2b7eb -->
|  |  |
|---|---|
|  | ![Cathy](../assets/npcs/303.png) |
| **Unit id** | `303` |
| **Title** | Auction House Manager |
| **Category** | NPC (category 50) |
| **Menu** | Auction House (`17`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1924.8, 1666.7) |
| **Model** | ObjectList `185`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/NPC_Action.dds` |

### Greeting

> Hello, I handle all auctions in Gaia.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1924.8 | 1666.7 | video | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2180.8 | 1666.7 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2436.8 | 1666.7 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] (10. Economy, VIP, cash shop)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (5. Fortress layout (town))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 48:20, 48:40, 49:20, 50:05 (3. NPCs)
- [[gameplay/warmonger-forum|Warmonger forum (2018)]] (8. VIP and account)
<!-- generated:end -->

## Notes

- Auction House manager (coins icon) in the Fortress ([[gameplay/npc-locations|NPC locations]] §3; [[gameplay/maps-and-dungeons|Maps and dungeons]] §5). The auction house charges a 5% commission when an item is listed, and listings last 6 days ([[gameplay/progression-and-economy|Progression and economy]] §5). *guide + image*
- She sold the VIP ticket: 6,000,000 gold or 2,000 jewels; with gold only VIP 1 is reachable ([[gameplay/warmonger-forum|Warmonger forum]] §8). In Crush Online the 30-day ticket went from 6 M to 9 M, then 12.5 M gold, then jewels only ([[gameplay/crush-mechanics|Crush Online mechanics]] §10). *staff / forum*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/npc-locations|NPC locations]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/progression-and-economy|Progression and economy]]
- [[gameplay/warmonger-forum|Warmonger forum]]
- [[gameplay/crush-mechanics|Crush Online mechanics]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

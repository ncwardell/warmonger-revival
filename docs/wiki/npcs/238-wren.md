---
title: "Wren"
type: "npc"
id: 238
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 238", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §4", "gameplay/video-tutorial-walkthrough §2"]
name_key: "TitleName_3"
title_key: "UnitName_204"
npc_title: "Merchant"
category: 50
class_mask: 2
model: 40
scale: 1.5
functions:
  - {"code": 1, "function": "shop", "label": "Shop"}
role: "Merchant"
shop: 287
talk_key: "Quest_Talk_Default_Hawker"
portrait: "ui/NPCProfile/Hawker.dds"
quests: {"gives": [102], "talk_objective": [28]}
quest_fields: [88, 92, 96]
map: 88
x: 373.8
z: 3479.5
positions:
  - {"field": 88, "x": 373.8, "z": 3479.5, "source": "gameplay/npc-locations §4", "confidence": "video"}
  - {"field": 88, "x": 375.0, "z": 3479.3, "source": "gameplay/video-tutorial-walkthrough §2", "confidence": "video", "seen": ["12:40", "20:05"]}
  - {"field": 92, "x": 629.8, "z": 3479.5, "source": "derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 96, "x": 885.8, "z": 3479.5, "source": "derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=60ea71 type=3664ce id=5b7d26 sources=7a37ae name_key=7d155d title_key=ee2258 npc_title=b0845f category=e1822d class_mask=da4b92 model=af3e13 scale=aa8f28 functions=7dac55 role=b0845f shop=f0a4ac talk_key=2634be portrait=399d90 quests=eb3550 quest_fields=46bf0f map=b37f6d x=a006aa z=b38514 positions=5f0d50 -->
|  |  |
|---|---|
|  | ![Wren](wiki/assets/npcs/238.png) |
| **Unit id** | `238` |
| **Title** | Merchant |
| **Category** | NPC (category 50) |
| **Menu** | Shop (`1`) |
| **Shop** | [[wiki/shops/287-wren-s-shop-merchant-287\|Wren's shop (Merchant) 287]] |
| **Stands in** | [[wiki/fields/88-training-camp\|Training Camp]] at (373.8, 3479.5) |
| **Model** | ObjectList `40`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Hawker.dds` |

### Greeting

> Welcome back friend!  Is there anything you need?

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/88-training-camp\|Training Camp]] | 373.8 | 3479.5 | video | [[gameplay/npc-locations\|npc-locations]] §4 |
| [[wiki/fields/88-training-camp\|Training Camp]] | 375.0 | 3479.3 | video | [[gameplay/video-tutorial-walkthrough\|video-tutorial-walkthrough]] §2 at 12:40, 20:05 |
| [[wiki/fields/92-training-camp\|Training Camp]] | 629.8 | 3479.5 | derived | derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/96-training-camp\|Training Camp]] | 885.8 | 3479.5 | derived | derived: gameplay/npc-locations §4 + copy origin (gameplay/npc-locations §2) |

### Shop

Sells 4 items (`Npc_Carry` row 287; full list on [[wiki/shops/287-wren-s-shop-merchant-287|Wren's shop (Merchant) 287]]): [[wiki/items/883-potion-of-health-d|Potion of Health (D)]], [[wiki/items/884-potion-of-mana-d|Potion of Mana (D)]], [[wiki/items/906-scroll-return|Scroll : Return]], [[wiki/items/945-auto-decomposition-hammer-d|Auto decomposition hammer (D)]].

### Quests

- **Gives:** [[wiki/quests/102-wren-s-sister-wren|Wren's sister Wren?]]
- **Must be talked to in:** [[wiki/quests/28-what-does-wren-do|What does Wren do?]]

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/204-wren|Wren (204)]], [[wiki/npcs/319-wren|Wren (319)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (4. Training Camp (fields 88 / 92 / 96))
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] (Training Camp (field 92) and back)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 16:35, 16:54, 17:00, 23:00, 37:00 (Training Ground and Camp (levels 1–11); Fortress (levels 12–20); 3. NPCs)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 12:40, 13:40, 14:20, 15:00, 20:05 (Steps; 2. NPC positions; Shop and economy)
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

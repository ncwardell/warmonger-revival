---
title: "Cassia"
type: "npc"
id: 212
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 212", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_15"
title_key: "UnitName_212"
npc_title: "Material Merchant"
category: 50
class_mask: 2
model: 40
scale: 1.5
functions:
  - {"code": 1, "function": "shop", "label": "Shop"}
role: "Material Merchant"
shop: 286
talk_key: "Quest_Talk_Default_Mart"
portrait: "ui/NPCProfile/Hawker.dds"
quests: {"talk_objective": [13]}
map: 120
x: 1990.7
z: 1716.1
positions:
  - {"field": 120, "x": 1990.7, "z": 1716.1, "source": "gameplay/npc-locations §3", "confidence": "video"}
  - {"field": 120, "x": 2246.7, "z": 1716.1, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2502.7, "z": 1716.1, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=e66368 type=3664ce id=e2154f sources=ea0eb8 name_key=2ddde4 title_key=91ed68 npc_title=7d4d37 category=e1822d class_mask=da4b92 model=af3e13 scale=aa8f28 functions=7dac55 role=7d4d37 shop=7edab1 talk_key=78ded7 portrait=399d90 quests=24cbc3 map=775bc5 x=b0441f z=cf8cd8 positions=a340d5 -->
|  |  |
|---|---|
|  | ![Cassia](wiki/assets/npcs/212.png) |
| **Unit id** | `212` |
| **Title** | Material Merchant |
| **Category** | NPC (category 50) |
| **Menu** | Shop (`1`) |
| **Shop** | [[wiki/shops/286-cassia-s-shop-material-merchant\|Cassia's shop (Material Merchant)]] |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1990.7, 1716.1) |
| **Model** | ObjectList `40`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Hawker.dds` |

### Greeting

> Hello! Is there anything you need?

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1990.7 | 1716.1 | video | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2246.7 | 1716.1 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2502.7 | 1716.1 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Shop

Sells 9 items (`Npc_Carry` row 286; full list on [[wiki/shops/286-cassia-s-shop-material-merchant|Cassia's shop (Material Merchant)]]): [[wiki/items/830-empty-scroll-c|Empty Scroll (C)]], [[wiki/items/831-empty-scroll-b|Empty Scroll (B)]], [[wiki/items/832-empty-scroll-a|Empty Scroll (A)]], [[wiki/items/833-empty-scroll-s|Empty Scroll (S)]], [[wiki/items/834-empty-flask-c|Empty Flask (C)]], [[wiki/items/835-empty-flask-b|Empty Flask (B)]], [[wiki/items/836-empty-flask-a|Empty Flask (A)]], [[wiki/items/837-empty-flask-s|Empty Flask (S)]], [[wiki/items/846-worked-oil|Worked oil]].

### Quests

- **Must be talked to in:** [[wiki/quests/13-battle-preparations|Battle preparations]]

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/consumables|Consumables and clickables]] (5. Where the inputs come from)
- [[gameplay/items-and-crafting|Items, upgrades and crafting]] (3. Crafting; 4. Alchemy (consumables))
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (5. Fortress layout (town))
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] at 22:05, 25:25 (After the tutorial (Fortress, from 22:00))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 38:30, 40:20, 40:30, 41:20, 48:20, 48:40, 49:20, 50:05 (Fortress (levels 12–20); 3. NPCs)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 33:30 (Steps)
<!-- generated:end -->

## Notes

- Material merchant in the north-east of the Fortress (shop 286) ([[gameplay/npc-locations|NPC locations]] §3). She sells Empty Scroll [C]–[S] (830–833; 50 / 60 / 80 / 100 base), Empty Flask [C]–[S] (834–837; 80 / 100 / 150 / 200) and Worked oil (846, 100) ([[gameplay/consumables|Consumables]] §5; [[gameplay/maps-and-dungeons|Maps and dungeons]] §5). *client + guide*
- Her dialogue sends the player to Odin or Owen to craft ([[gameplay/video-early-quests|Video notes: first session]] §3). *video*

## Behaviour

- Quest 13 "Battle preparations" (talk to Cassia) pays 100 Empty Flask [C], 30,000 gold, 15/15 fragments and 5 Crystal: Blue, then leads to quest 14 at Owen ([[gameplay/video-early-quests|Video notes: first session]] §2 step 15, [40:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2420s)). *video*

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/npc-locations|NPC locations]]
- [[gameplay/consumables|Consumables]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/video-early-quests|Video notes: first session]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->

---
title: "Kesley"
type: "npc"
id: 210
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 210", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_5"
title_key: "UnitName_210"
npc_title: "Legion Administrator"
category: 50
class_mask: 2
model: 235
scale: 1.7
functions:
  - {"code": 6, "function": "legion_create", "label": "Legion Create"}
  - {"code": 28, "function": "legion_warehouse", "label": "Warehouse"}
role: "Legion Administrator"
talk_key: "Quest_Talk_Default_Guild"
portrait: "ui/NPCProfile/NPC_Guild.dds"
quests: {"gives": [29, 105, 117, 732, 745, 748, 752, 753, 754, 755, 763, 764, 765, 766, 767, 774, 775, 776], "receives": [29, 732, 745, 748, 752, 753, 754, 755, 774, 775, 776, 1016], "talk_objective": [117, 763, 764, 765, 1016]}
quest_fields: [120]
map: 120
x: 1879.9
z: 1679.4
positions:
  - {"field": 120, "x": 1879.9, "z": 1679.4, "source": "gameplay/npc-locations §3", "confidence": "video + image"}
  - {"field": 120, "x": 2135.9, "z": 1679.4, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2391.9, "z": 1679.4, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=f6e385 type=3664ce id=135deb sources=7e2e39 name_key=ca5d69 title_key=7696fa npc_title=63326e category=e1822d class_mask=da4b92 model=0b7f5a scale=58e6d3 functions=13674d role=63326e talk_key=9314f1 portrait=69c286 quests=019ece quest_fields=6c3da9 map=775bc5 x=cfe290 z=97fb8c positions=e8b540 -->
|  |  |
|---|---|
|  | ![Kesley](wiki/assets/npcs/210.png) |
| **Unit id** | `210` |
| **Title** | Legion Administrator |
| **Category** | NPC (category 50) |
| **Menu** | Legion Create (`6`), Warehouse (`28`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1879.9, 1679.4) |
| **Model** | ObjectList `235`, scale 1.7 |
| **Portrait** | `ui/NPCProfile/NPC_Guild.dds` |

### Greeting

> Do you want to create your own Legion? I'm the person that will make that happen.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1879.9 | 1679.4 | video + image | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2135.9 | 1679.4 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2391.9 | 1679.4 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Quests

- **Gives:** [[wiki/quests/29-kesley-s-disgrace|Kesley's Disgrace]], [[wiki/quests/105-kesley-s-disgrace|Kesley's Disgrace]], [[wiki/quests/117-lords-of-the-land|Lords of the Land]], [[wiki/quests/732-fisher-s-scales|Fisher's scales]], [[wiki/quests/745-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/748-ore-and-plant-collection|Ore and plant collection]], [[wiki/quests/752-join-create-legion|Join & Create Legion]], [[wiki/quests/753-join-the-legion|Join the Legion]], [[wiki/quests/754-battle-with-legion-members-no-1|Battle with Legion members No. 1]], [[wiki/quests/755-battle-with-legion-members-no-2|Battle with Legion members No. 2]], [[wiki/quests/763-no2-lords-of-the-land|No2. Lords of the Land]], [[wiki/quests/764-no3-lords-of-the-land|No3. Lords of the Land]], [[wiki/quests/765-no4-lords-of-the-land|No4. Lords of the Land]], [[wiki/quests/766-sell-ether|Sell Ether]], [[wiki/quests/767-buy-ether|Buy Ether]], [[wiki/quests/774-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/775-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/776-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]]
- **Takes the turn-in of:** [[wiki/quests/29-kesley-s-disgrace|Kesley's Disgrace]], [[wiki/quests/732-fisher-s-scales|Fisher's scales]], [[wiki/quests/745-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/748-ore-and-plant-collection|Ore and plant collection]], [[wiki/quests/752-join-create-legion|Join & Create Legion]], [[wiki/quests/753-join-the-legion|Join the Legion]], [[wiki/quests/754-battle-with-legion-members-no-1|Battle with Legion members No. 1]], [[wiki/quests/755-battle-with-legion-members-no-2|Battle with Legion members No. 2]], [[wiki/quests/774-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/775-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/776-highly-concentrated-bomb-create|Highly Concentrated Bomb Create]], [[wiki/quests/1016-tsunami-lake-hunting|Tsunami Lake : Hunting]]
- **Must be talked to in:** [[wiki/quests/117-lords-of-the-land|Lords of the Land]], [[wiki/quests/763-no2-lords-of-the-land|No2. Lords of the Land]], [[wiki/quests/764-no3-lords-of-the-land|No3. Lords of the Land]], [[wiki/quests/765-no4-lords-of-the-land|No4. Lords of the Land]], [[wiki/quests/1016-tsunami-lake-hunting|Tsunami Lake : Hunting]]

Dialogue rows (`QuestTalk`; full text on the quest pages):

| quest | QuestTalk | speaker | first line |
|---|---|---|---|
| [[wiki/quests/752-join-create-legion\|Join & Create Legion]] | 743 | Kesley : Legion Manager | All members can gain fame for their legion.  Spread the word friend! |
| [[wiki/quests/753-join-the-legion\|Join the Legion]] | 744 | Kesley : Legion Manager | Joining a legion will make it easier for you to defeat tough opponents. You can just ask the other members for help. |
| [[wiki/quests/754-battle-with-legion-members-no-1\|Battle with Legion members No. 1]] | 745 | Kesley : Legion Manager | When you fight along side your legion members, you will receive more rewards. Let's do that. |
| [[wiki/quests/755-battle-with-legion-members-no-2\|Battle with Legion members No. 2]] | 746 | Kesley : Legion Manager | Did you get a reward? Join the fight together with your legion again. |
| [[wiki/quests/767-buy-ether\|Buy Ether]] | 767 | Kesley : Legion Manager | The war is tough, and it's really hard to save materials. Can you help me out? |

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/318-kesley|Kesley (318)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 47:10, 59:00 (Fortress (levels 12–20); 3. NPCs)
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

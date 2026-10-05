---
title: "Freya"
type: "npc"
id: 200
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 200", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_1"
title_key: "UnitName_200"
npc_title: "Oracle of Knowledge"
category: 50
class_mask: 2
model: 53
scale: 1.5
functions:
  - {"code": 71, "function": "none"}
role: "Oracle of Knowledge"
shop: 289
talk_key: "Quest_Talk_Default_Oracle"
portrait: "ui/NPCProfile/Oracle_of_Knowledge.dds"
quests: {"gives": [13, 14, 15, 17, 21, 22, 23, 24, 25, 30, 32, 33, 34, 35, 36, 37, 41, 44, 47, 109, 692, 756, 757, 758, 759, 760, 768, 769, 770, 771, 772, 773, 781, 783, 787], "receives": [14, 15, 20, 21, 22, 23, 24, 25, 30, 32, 33, 34, 35, 36, 46, 47, 80, 81, 82, 109, 756, 757, 758, 759, 760, 768, 769, 770, 771, 772, 773, 782, 784, 800, 801, 802, 803, 811, 812, 813, 814, 815, 1003, 1008, 1013, 1018, 1023, 1029, 1034, 1039, 1043, 1301, 1302, 1303, 1304, 1351, 1352, 1353], "talk_objective": [12, 39, 1003, 1008, 1013, 1018, 1023, 1029, 1034, 1039, 1043, 1301, 1302, 1303, 1304, 1351, 1352, 1353]}
quest_fields: [120]
map: 120
x: 1906.6
z: 1641.0
positions:
  - {"field": 120, "x": 1906.6, "z": 1641.0, "source": "gameplay/npc-locations §3", "confidence": "video"}
  - {"field": 120, "x": 2162.6, "z": 1641.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2418.6, "z": 1641.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=29ae4f type=3664ce id=9f9af0 sources=9af3c4 name_key=750efc title_key=21d171 npc_title=955057 category=e1822d class_mask=da4b92 model=c5b76d scale=aa8f28 functions=40bee7 role=955057 shop=6b0f4d talk_key=7b5881 portrait=263ce3 quests=b3aacc quest_fields=6c3da9 map=775bc5 x=cb5ff3 z=a915dd positions=5abb25 -->
|  |  |
|---|---|
|  | ![Freya](wiki/assets/npcs/200.png) |
| **Unit id** | `200` |
| **Title** | Oracle of Knowledge |
| **Category** | NPC (category 50) |
| **Menu** | no menu entry (code `71`) |
| **Shop** | [[wiki/shops/289-freya-s-shop-oracle-of-knowledge\|Freya's shop (Oracle of Knowledge)]] |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1906.6, 1641.0) |
| **Model** | ObjectList `53`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Oracle_of_Knowledge.dds` |

### Greeting

> Is you mission going well? Find me if you are looking for work

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1906.6 | 1641.0 | video | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2162.6 | 1641.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2418.6 | 1641.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Shop

Sells 7 items (`Npc_Carry` row 289; full list on [[wiki/shops/289-freya-s-shop-oracle-of-knowledge|Freya's shop (Oracle of Knowledge)]]): [[wiki/items/1201-d-rank-quest|D Rank Quest]], [[wiki/items/1202-d-rank-quest|D Rank Quest]], [[wiki/items/1203-d-rank-quest|D Rank Quest]], [[wiki/items/1204-d-rank-quest|D Rank Quest]], [[wiki/items/1251-c-rank-quest|C Rank Quest]], [[wiki/items/1252-c-rank-quest|C Rank Quest]], [[wiki/items/1253-c-rank-quest|C Rank Quest]].

### Quests

- **Gives:** [[wiki/quests/13-battle-preparations|Battle preparations]], [[wiki/quests/14-battle-preparations|Battle preparations]], [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]], [[wiki/quests/17-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/21-group-ancient-ghosts|(Group) Ancient Ghosts]], [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]], [[wiki/quests/23-stepping-up-your-game|Stepping up your game]], [[wiki/quests/24-stepping-up-your-game|Stepping up your game]], [[wiki/quests/25-stepping-up-your-game|Stepping up your game]], [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]], [[wiki/quests/33-ghost-fortress|Ghost Fortress]], [[wiki/quests/34-tow-canyon|Tow Canyon]], [[wiki/quests/35-demon-hell|Demon Hell]], [[wiki/quests/36-thorn-s-hell|Thorn's Hell]], [[wiki/quests/37-call-tempest|Call Tempest]], [[wiki/quests/41-innocence-s-recovery-operation|Innocence's recovery operation]], [[wiki/quests/44-innocence-report|Innocence report]], [[wiki/quests/47-create-potion|Create Potion]], [[wiki/quests/109-for-the-honor|For the honor]], [[wiki/quests/692-innocence-crystal|Innocence Crystal]], [[wiki/quests/756-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/757-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/758-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/759-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/760-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/768-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/769-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/770-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/771-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/772-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/773-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/781-tsunami-lake|Tsunami Lake]], [[wiki/quests/783-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]], [[wiki/quests/787-open-the-questboard|Open The QuestBoard]]
- **Takes the turn-in of:** [[wiki/quests/14-battle-preparations|Battle preparations]], [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]], [[wiki/quests/20-talk-to-freya|Talk to Freya]], [[wiki/quests/21-group-ancient-ghosts|(Group) Ancient Ghosts]], [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]], [[wiki/quests/23-stepping-up-your-game|Stepping up your game]], [[wiki/quests/24-stepping-up-your-game|Stepping up your game]], [[wiki/quests/25-stepping-up-your-game|Stepping up your game]], [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]], [[wiki/quests/33-ghost-fortress|Ghost Fortress]], [[wiki/quests/34-tow-canyon|Tow Canyon]], [[wiki/quests/35-demon-hell|Demon Hell]], [[wiki/quests/36-thorn-s-hell|Thorn's Hell]], [[wiki/quests/46-to-oracle-of-knowledge|To Oracle of knowledge]], [[wiki/quests/47-create-potion|Create Potion]], [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/109-for-the-honor|For the honor]], [[wiki/quests/756-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/757-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/758-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/759-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/760-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/768-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/769-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/770-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/771-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/772-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/773-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/782-tsunami-lake|Tsunami Lake]], [[wiki/quests/784-swamps-of-the-snake-warrior|Swamps of the Snake Warrior]], [[wiki/quests/800-rank-d-crafting|Rank(D) Crafting]], [[wiki/quests/801-rank-d-crafting|Rank(D) Crafting]], [[wiki/quests/802-rank-d-crafting|Rank(D) Crafting]], [[wiki/quests/803-rank-d-crafting|Rank(D) Crafting]], [[wiki/quests/811-rank-c-crafting|Rank(C) Crafting]], [[wiki/quests/812-rank-c-crafting|Rank(C) Crafting]], [[wiki/quests/813-rank-c-crafting|Rank(C) Crafting]], [[wiki/quests/814-chepa-village-hunting|Chepa Village : Hunting]], [[wiki/quests/815-chepa-village-hunting|Chepa Village : Hunting]], [[wiki/quests/1003-chepa-village-boss-hunting|Chepa Village : Boss Hunting]], [[wiki/quests/1008-skull-temple-boss-hunting|Skull Temple : Boss Hunting]], [[wiki/quests/1013-skull-cemetery-boss-hunting|Skull Cemetery : Boss Hunting]], [[wiki/quests/1018-tsunami-lake-boss-hunting|Tsunami Lake : Boss Hunting]], [[wiki/quests/1023-swamps-of-the-snake-warrior-boss-hunting|Swamps of the Snake Warrior : Boss Hunting]], [[wiki/quests/1029-ghost-fortress-boss-hunting|Ghost Fortress : Boss Hunting]], [[wiki/quests/1034-tow-canyon-boss-hunting|Tow Canyon : Boss Hunting]], [[wiki/quests/1039-demon-hell-boss-hunting|Demon Hell : Boss Hunting]], [[wiki/quests/1043-thorn-s-hell-boss-hunting|Thorn's Hell : Boss Hunting]], [[wiki/quests/1301-soldier-rank-kill-player|(Soldier Rank) Kill Player]], [[wiki/quests/1302-soldier-rank-create-dimension-gate|(Soldier Rank) Create Dimension Gate]], [[wiki/quests/1303-soldier-rank-imprint|(Soldier Rank) Imprint]], [[wiki/quests/1304-soldier-rank-nexus-destruction|(Soldier Rank) Nexus Destruction]], [[wiki/quests/1351-veteran-rank-monster-invasion-area|(Veteran Rank) Monster Invasion Area]], [[wiki/quests/1352-veteran-rank-monster-area|(Veteran Rank) Monster area]], [[wiki/quests/1353-veteran-rank-enemy-territory|(Veteran Rank) Enemy territory]]
- **Must be talked to in:** [[wiki/quests/12-an-urgent-message|An urgent message]], [[wiki/quests/39-innocence-s-recovery-operation|Innocence's recovery operation]], [[wiki/quests/1003-chepa-village-boss-hunting|Chepa Village : Boss Hunting]], [[wiki/quests/1008-skull-temple-boss-hunting|Skull Temple : Boss Hunting]], [[wiki/quests/1013-skull-cemetery-boss-hunting|Skull Cemetery : Boss Hunting]], [[wiki/quests/1018-tsunami-lake-boss-hunting|Tsunami Lake : Boss Hunting]], [[wiki/quests/1023-swamps-of-the-snake-warrior-boss-hunting|Swamps of the Snake Warrior : Boss Hunting]], [[wiki/quests/1029-ghost-fortress-boss-hunting|Ghost Fortress : Boss Hunting]], [[wiki/quests/1034-tow-canyon-boss-hunting|Tow Canyon : Boss Hunting]], [[wiki/quests/1039-demon-hell-boss-hunting|Demon Hell : Boss Hunting]], [[wiki/quests/1043-thorn-s-hell-boss-hunting|Thorn's Hell : Boss Hunting]], [[wiki/quests/1301-soldier-rank-kill-player|(Soldier Rank) Kill Player]], [[wiki/quests/1302-soldier-rank-create-dimension-gate|(Soldier Rank) Create Dimension Gate]], [[wiki/quests/1303-soldier-rank-imprint|(Soldier Rank) Imprint]], [[wiki/quests/1304-soldier-rank-nexus-destruction|(Soldier Rank) Nexus Destruction]], [[wiki/quests/1351-veteran-rank-monster-invasion-area|(Veteran Rank) Monster Invasion Area]], [[wiki/quests/1352-veteran-rank-monster-area|(Veteran Rank) Monster area]], [[wiki/quests/1353-veteran-rank-enemy-territory|(Veteran Rank) Enemy territory]]

Dialogue rows (`QuestTalk`; full text on the quest pages):

| quest | QuestTalk | speaker | first line |
|---|---|---|---|
| [[wiki/quests/12-an-urgent-message\|An urgent message]] | 639 | Frei : Oracle of Knowledge | I'm awaiting the arrival of one of our scouts, but he is long overdue. He carries important information. |
| [[wiki/quests/30-chepa-village\|Chepa Village]] | 654 | Freya : Oracle of Knowledge | I'm back and I finished the mission! |
| [[wiki/quests/756-group-border-area-hard-mode\|Group - Border Area Hard Mode]] | 749 | Freya : Oracle of Knowledge | The monster king lives in the border area. Can you go and kill him? |
| [[wiki/quests/757-group-border-area-hard-mode\|Group - Border Area Hard Mode]] | 750 | Freya : Oracle of Knowledge | Thank you so much. The village is safe again. |

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] (1. Levels and quests)
- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]] (5. Other numbers on the screenshots)
- [[gameplay/maps-and-dungeons|Maps and dungeons]] (5. Fortress layout (town))
- [[gameplay/precept-shop|Precept shop and precept quests]] (Precept shop and precept quests; 1. Shop prices; 3. Example rolled quest (screenshot))
- [[gameplay/progression-and-economy|Progression and economy]] (1. Levels and experience)
- [[gameplay/server-rules|Server rules checklist]] (Added from the source hunt (see [[gameplay/sources|Sources and gaps]]))
- [[gameplay/sources|Sources and gaps]] (3. Player screenshots (image sets that still load))
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] at 22:05, 25:25 (Training Camp (field 92) and back; After the tutorial (Fortress, from 22:00))
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 38:05, 38:30, 40:20, 40:30, 41:20, 41:25, 52:25, 56:55 … (Fortress (levels 12–20))
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] at 32:45, 33:00, 33:05, 33:15 (Steps; 2. NPC positions)
- [[gameplay/warmonger-forum|Warmonger forum (2018)]] (4. Levelling and medals)
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

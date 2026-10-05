---
title: "Owen"
type: "npc"
id: 214
status: "complete"
missing: []
sources: ["client: UnitDB.cdb id 214", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "gameplay/npc-locations §3"]
name_key: "TitleName_11"
title_key: "UnitName_214"
npc_title: "Member of Red Union"
category: 50
class_mask: 2
model: 297
scale: 1.5
functions:
  - {"code": 21, "function": "craft", "label": "Create"}
role: "Member of Red Union"
talk_key: "Quest_Talk_Default_Red"
portrait: "ui/NPCProfile/Quest_RedFlames.dds"
quests: {"gives": [108, 725, 729, 731, 735, 736, 738, 742, 744, 747], "receives": [725, 729, 731, 735, 736, 738, 742, 744, 747, 1001, 1002, 1007, 1012, 1017, 1022, 1028, 1038, 1042], "talk_objective": [14, 47, 48, 1001, 1002, 1007, 1012, 1017, 1022, 1028, 1038, 1042]}
quest_fields: [120]
map: 120
x: 1998.9
z: 1709.0
positions:
  - {"field": 120, "x": 1998.9, "z": 1709.0, "source": "gameplay/npc-locations §3", "confidence": "video"}
  - {"field": 120, "x": 2254.9, "z": 1709.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
  - {"field": 120, "x": 2510.9, "z": 1709.0, "source": "derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2)", "confidence": "derived"}
---
<!-- generated:start -->
<!-- generated-keys: title=2a0552 type=3664ce id=9a15f4 sources=7d6cc3 name_key=47bcc5 title_key=9f8371 npc_title=1bd231 category=e1822d class_mask=da4b92 model=dd500e scale=aa8f28 functions=21a907 role=1bd231 talk_key=12d6a8 portrait=7348e7 quests=1156d2 quest_fields=6c3da9 map=775bc5 x=9761d9 z=cdcdb3 positions=d0d569 -->
|  |  |
|---|---|
|  | ![Owen](../assets/npcs/214.png) |
| **Unit id** | `214` |
| **Title** | Member of Red Union |
| **Category** | NPC (category 50) |
| **Menu** | Create (`21`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] at (1998.9, 1709.0) |
| **Model** | ObjectList `297`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Quest_RedFlames.dds` |

### Greeting

> Hello. Do you need anything? Take your time and look around.

### Where it stands

Town NPC positions are not in the client data; these were measured from video and guide screenshots (see [[gameplay/npc-locations|NPC locations]] §2 for the method). Rows marked *derived* place the same spot in the other nations' copies of the map.

| field | x | z | confidence | source |
|---|---|---|---|---|
| [[wiki/fields/120-fortress\|Fortress]] | 1998.9 | 1709.0 | video | [[gameplay/npc-locations\|npc-locations]] §3 |
| [[wiki/fields/120-fortress\|Fortress]] | 2254.9 | 1709.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |
| [[wiki/fields/120-fortress\|Fortress]] | 2510.9 | 1709.0 | derived | derived: gameplay/npc-locations §3 + copy origin (gameplay/npc-locations §2) |

### Quests

- **Gives:** [[wiki/quests/108-hunting-ghosts-spirit-avenue|Hunting Ghosts (Spirit Avenue)]], [[wiki/quests/725-collecting-material|Collecting material]], [[wiki/quests/729-collecting-material|Collecting material]], [[wiki/quests/731-collecting-material|Collecting material]], [[wiki/quests/735-collecting-material|Collecting material]], [[wiki/quests/736-hunting-for-furs|Hunting for Furs]], [[wiki/quests/738-collecting-material|Collecting material]], [[wiki/quests/742-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/744-acquire-materials|Acquire materials]], [[wiki/quests/747-acquire-materials|Acquire materials]]
- **Takes the turn-in of:** [[wiki/quests/725-collecting-material|Collecting material]], [[wiki/quests/729-collecting-material|Collecting material]], [[wiki/quests/731-collecting-material|Collecting material]], [[wiki/quests/735-collecting-material|Collecting material]], [[wiki/quests/736-hunting-for-furs|Hunting for Furs]], [[wiki/quests/738-collecting-material|Collecting material]], [[wiki/quests/742-gathering-plant-and-ore|Gathering plant and ore]], [[wiki/quests/744-acquire-materials|Acquire materials]], [[wiki/quests/747-acquire-materials|Acquire materials]], [[wiki/quests/1001-chepa-village-hunting|Chepa Village : Hunting]], [[wiki/quests/1002-chepa-village-collecting-material|Chepa Village : Collecting material]], [[wiki/quests/1007-skull-temple-collecting-material|Skull Temple : Collecting material]], [[wiki/quests/1012-skull-cemetery-collecting-material|Skull Cemetery : Collecting material]], [[wiki/quests/1017-tsunami-lake-collecting-material|Tsunami Lake : Collecting material]], [[wiki/quests/1022-swamps-of-the-snake-warrior-collecting-material|Swamps of the Snake Warrior : Collecting material]], [[wiki/quests/1028-ghost-fortress-collecting-material|Ghost Fortress : Collecting material]], [[wiki/quests/1038-demon-hell-collecting-material|Demon Hell : Collecting material]], [[wiki/quests/1042-thorn-s-hell-collecting-material|Thorn's Hell : Collecting material]]
- **Must be talked to in:** [[wiki/quests/14-battle-preparations|Battle preparations]], [[wiki/quests/47-create-potion|Create Potion]], [[wiki/quests/48-doping-create|Doping Create]], [[wiki/quests/1001-chepa-village-hunting|Chepa Village : Hunting]], [[wiki/quests/1002-chepa-village-collecting-material|Chepa Village : Collecting material]], [[wiki/quests/1007-skull-temple-collecting-material|Skull Temple : Collecting material]], [[wiki/quests/1012-skull-cemetery-collecting-material|Skull Cemetery : Collecting material]], [[wiki/quests/1017-tsunami-lake-collecting-material|Tsunami Lake : Collecting material]], [[wiki/quests/1022-swamps-of-the-snake-warrior-collecting-material|Swamps of the Snake Warrior : Collecting material]], [[wiki/quests/1028-ghost-fortress-collecting-material|Ghost Fortress : Collecting material]], [[wiki/quests/1038-demon-hell-collecting-material|Demon Hell : Collecting material]], [[wiki/quests/1042-thorn-s-hell-collecting-material|Thorn's Hell : Collecting material]]

Dialogue rows (`QuestTalk`; full text on the quest pages):

| quest | QuestTalk | speaker | first line |
|---|---|---|---|
| [[wiki/quests/725-collecting-material\|Collecting material]] | 698 | Owen : Red Union | The war is tough, and it's really hard to save materials. Can you help me out? |
| [[wiki/quests/731-collecting-material\|Collecting material]] | 680 | Owen : Red Union | What brought you here? |
| [[wiki/quests/744-acquire-materials\|Acquire materials]] | 761 | Owen : Red Union | The war is tough, and it's really hard to save materials. Can you help me out? |

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/314-owen|Owen (314)]], [[wiki/npcs/337-owen|Owen (337)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
- [[gameplay/consumables|Consumables and clickables]] (4. Recipes (Owen, Red Union); 5. Where the inputs come from)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] at 38:30, 40:20, 40:30, 41:20, 48:20, 48:40, 49:20, 50:05 … (Fortress (levels 12–20); 3. NPCs)
<!-- generated:end -->

## Notes

- Red Union alchemist in the Fortress. Every buff clickable is crafted here; this Owen has the full `Item_Make` category 1 list ([[gameplay/consumables|Consumables]] §4). His tabs are Potion, Scroll, Tome, Elixir, Flask, Dye, Ore and Plants ([[gameplay/items-and-crafting|Items and crafting]] §4). *client + image*
- 1 raw gem or herb makes 10 powder for 50 gold base; 5 raw make 1 Worked gem or Extracted herb for 3,000 gold ([[gameplay/consumables|Consumables]] §4.3). A and S grades need the fort's A / S Grade Alchemy mastery ([[gameplay/consumables|Consumables]] §1). Craft gold is the `Item_Make` value × the fort rate (×1.5 seen) ([[gameplay/server-rules|Server rules]], round 2). *client + image*

## Behaviour

- Quest 14 "Battle preparations": craft 100 Potion of Health [C] here ([[gameplay/video-early-quests|Video notes: first session]] §2 step 15, [40:30](https://www.youtube.com/watch?v=s04CSN16w1s&t=2430s)).
- Quest 108 "Hunting Ghosts (Spirit Avenue)": 10 Ghost and 10 Elite Ghost; the panel shows 500,000 exp (table 600,000) and 50/50 fragments ([[gameplay/video-early-quests|Video notes: first session]] §2 step 25, [1:06:02](https://www.youtube.com/watch?v=s04CSN16w1s&t=3962s)). *video*

## Sources

Facts above come from these gameplay pages (each fact carries its own link and confidence):

- [[gameplay/consumables|Consumables]]
- [[gameplay/items-and-crafting|Items and crafting]]
- [[gameplay/server-rules|Server rules]]
- [[gameplay/video-early-quests|Video notes: first session]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
